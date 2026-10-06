#!/usr/bin/env python3
"""Construct frozen source-derived payloads. Never evaluate query cases."""
import base64
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from harness import deadline

ROOT = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main(archive):
    config = json.loads((ROOT / "config.json").read_text())
    source = json.loads((ROOT / "source.json").read_text())
    content = archive.read_bytes()
    assert sha(content) == source["sha256"] and len(content) == source["bytes"]
    with tarfile.open(fileobj=io.BytesIO(content)) as tf:
        raw = tf.extractfile("northamerica").read()
    expected = next(x["sha256"] for x in source["members"] if x["path"] == "northamerica")
    assert sha(raw) == expected
    lines = raw.decode().splitlines()
    us = [l for l in lines if l.split()[:2] == ["Rule", "US"]]
    active = []
    for row in us:
        p = row.split()
        last = 9999 if p[3] == "max" else int(p[2] if p[3] == "only" else p[3])
        if int(p[2]) <= config["scope"]["year"] <= last:
            active.append(p)
    assert active == [
        ["Rule", "US", "2007", "max", "-", "Mar", "Sun>=8", "2:00", "1:00", "D"],
        ["Rule", "US", "2007", "max", "-", "Nov", "Sun>=1", "2:00", "0", "S"]]
    block = raw.decode().split("Zone America/New_York", 1)[1].split("\n\n", 1)[0]
    assert block.strip().splitlines()[-1].split() == ["-5:00", "US", "E%sT"]
    zic = shutil.which("zic")
    if not zic:
        raise RuntimeError("zic is required for construction, not for frozen evaluation")
    record = {"source_archive_sha256": sha(content), "northamerica_sha256": sha(raw),
              "archive_input_bytes": len(content), "northamerica_input_bytes": len(raw),
              "compiler_version": subprocess.check_output([zic, "--version"], text=True).strip(),
              "compiler_sha256": sha(Path(zic).read_bytes()), "query_cases_evaluated": 0}
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        (folder / "northamerica").write_bytes(raw)
        common = [zic, "-d"]
        commands = [common + [str(folder / "full"), str(folder / "northamerica")],
                    common + [str(folder / "bounded"), "-b", "slim", "-r",
                              f"@{config['scope']['utc_start']}/@{config['scope']['utc_end_exclusive']}",
                              str(folder / "northamerica")]]
        start = time.perf_counter()
        command_seconds = []
        for argv in commands:
            remaining = config["budgets"]["construction_wall_seconds"] - (time.perf_counter() - start)
            if remaining <= 0:
                raise TimeoutError("construction budget")
            command_start = time.perf_counter()
            subprocess.run(argv, check=True, capture_output=True, timeout=remaining)
            command_seconds.append(time.perf_counter() - command_start)
        record["tzif_construction_seconds"] = time.perf_counter() - start
        record["compiler_commands"] = commands
        record["compiler_command_seconds"] = command_seconds
        full = (folder / "full" / config["scope"]["zone"]).read_bytes()
        bounded = (folder / "bounded" / config["scope"]["zone"]).read_bytes()
    start = time.perf_counter()
    transition_times = []
    for month, earliest, before_offset in [(3, 8, -5), (11, 1, -4)]:
        day = datetime(2024, month, earliest)
        day += timedelta(days=(6 - day.weekday()) % 7)
        transition_times.append(int((day + timedelta(hours=2 - before_offset)).replace(tzinfo=timezone.utc).timestamp()))
    scope = config["scope"]
    boundaries = [scope["utc_start"], *transition_times, scope["utc_end_exclusive"]]
    intervals = [{"start": boundaries[i], "end_exclusive": boundaries[i + 1], "offset_seconds": offset}
                 for i, offset in enumerate([-18000, -14400, -18000])]
    record["rule_model_construction_seconds"] = time.perf_counter() - start
    shared = {"schema": 1, "scope": scope, "source": {"version": source["version"],
              "archive_sha256": source["sha256"], "northamerica_sha256": expected}}
    payloads = {"B": {**shared, "body": {"format": "TZif", "base64": base64.b64encode(bounded).decode()}},
                "T": {**shared, "body": {"format": "utc-offset-intervals", "intervals": intervals}}}
    reference = {"source": shared["source"], "scope": scope,
                 "full_tzif_base64": base64.b64encode(full).decode(),
                 "all_us_rule_rows": us, "new_york_zone_block": "Zone America/New_York" + block}
    record.update(full_tzif_bytes=len(full), full_tzif_sha256=sha(full), bounded_tzif_bytes=len(bounded),
                  bounded_tzif_sha256=sha(bounded), model_interval_count=len(intervals),
                  serialized_payload_bytes={k: len(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()) for k, v in payloads.items()})
    for name, data in [("payloads.json", payloads), ("reference.json", reference), ("construction.json", record)]:
        (ROOT / name).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"bounded_tzif_bytes": len(bounded), "intervals": len(intervals), "evaluation_queries": 0}))


if __name__ == "__main__":
    budget = json.loads((ROOT / "config.json").read_text())["budgets"]
    resource.setrlimit(resource.RLIMIT_AS, (budget["construction_memory_bytes"],) * 2)
    resource.setrlimit(resource.RLIMIT_CPU, (budget["construction_wall_seconds"],) * 2)
    started = time.perf_counter()
    with deadline(budget["construction_wall_seconds"]):
        main(Path(sys.argv[1]).resolve())
    record = json.loads((ROOT / "construction.json").read_text())
    record["whole_construction_seconds"] = time.perf_counter() - started
    record["construction_max_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (ROOT / "construction.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")

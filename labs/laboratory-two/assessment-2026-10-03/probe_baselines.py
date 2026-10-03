#!/usr/bin/env python3
"""Qualification-only baseline probes. No T arm and no transfer scoring.

Usage: python probe_baselines.py /path/to/cache /path/to/output.json
The cache contains SOURCES.json's tzdata archive and wheels/<filename>.
Download sources separately; this script is deliberately offline.
"""
from __future__ import annotations

import email.parser
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import re
import resource
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(argv):
    start = time.perf_counter()
    p = subprocess.run(argv, capture_output=True, text=True, timeout=60)
    return {"argv": argv, "returncode": p.returncode,
            "stdout": p.stdout, "stderr": p.stderr,
            "elapsed_seconds": time.perf_counter() - start}


def canonical(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def iso(value):
    return value.isoformat().replace("+00:00", "Z")


def sunday_on_or_after(month, day):
    value = datetime(2024, month, day)
    return value + timedelta(days=(6 - value.weekday()) % 7)


def main(cache, destination):
    manifest = json.loads(Path(__file__).with_name("SOURCES.json").read_text())
    results = {"purpose": "baseline qualification/development evidence only",
               "transfer_experiment": False, "method_arm_exists": False,
               "script_sha256": digest(Path(__file__).read_bytes()),
               "sources_manifest_sha256": digest(Path(__file__).with_name("SOURCES.json").read_bytes()),
               "environment": {"python": sys.version, "platform": platform.system(),
                               "pip": importlib.metadata.version("pip"),
                               "pip_record_sha256": digest(importlib.metadata.distribution("pip").read_text("RECORD").encode())}}
    archive = cache / manifest["tzdata"]["filename"]
    assert digest(archive.read_bytes()) == manifest["tzdata"]["sha256"]
    with tarfile.open(archive) as tf:
        raw = tf.extractfile("northamerica").read()
    assert digest(raw) == next(x["sha256"] for x in manifest["tzdata"]["members"] if x["path"] == "northamerica")
    source = raw.decode()
    zone_block = source.split("Zone America/New_York", 1)[1].split("\n\n", 1)[0]
    assert zone_block.strip().splitlines()[-1].split() == ["-5:00", "US", "E%sT"]
    rule_rows = [line for line in source.splitlines() if line.split()[:3] == ["Rule", "US", "2007"]]
    assert [r.split() for r in rule_rows] == [
        ["Rule", "US", "2007", "max", "-", "Mar", "Sun>=8", "2:00", "1:00", "D"],
        ["Rule", "US", "2007", "max", "-", "Nov", "Sun>=1", "2:00", "0", "S"]]

    # Separate source-rule arithmetic, not a second ZoneInfo decoder.
    spring = (sunday_on_or_after(3, 8) + timedelta(hours=7)).replace(tzinfo=timezone.utc)
    autumn = (sunday_on_or_after(11, 1) + timedelta(hours=6)).replace(tzinfo=timezone.utc)
    intervals = [(datetime(2023, 12, 31, tzinfo=timezone.utc), spring, -5),
                 (spring, autumn, -4),
                 (autumn, datetime(2025, 1, 2, tzinfo=timezone.utc), -5)]
    timezone_result = {"zone": "America/New_York", "year": 2024,
                       "raw_rule_rows": rule_rows, "raw_zone_block": "Zone America/New_York" + zone_block,
                       "reference_transitions_utc": [iso(spring), iso(autumn)],
                       "development_episodes": []}
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        (folder / "northamerica").write_bytes(raw)
        zic = shutil.which("zic")
        assert zic
        timezone_result["compiler"] = {"version": run([zic, "--version"]), "sha256": digest(Path(zic).read_bytes())}
        build = run([zic, "-d", str(folder / "zones"), str(folder / "northamerica")])
        timezone_result["build"] = build
        assert build["returncode"] == 0
        zone_file = folder / "zones" / "America" / "New_York"
        timezone_result["tzif_bytes"] = zone_file.stat().st_size
        timezone_result["tzif_sha256"] = digest(zone_file.read_bytes())
        with zone_file.open("rb") as f:
            zone = ZoneInfo.from_file(f, key="America/New_York")
        for text in ["2024-01-15T12:00:00", "2024-03-10T02:30:00", "2024-11-03T01:30:00"]:
            wall = datetime.fromisoformat(text)
            start = time.perf_counter()
            candidates = set()
            for fold in [0, 1]:
                utc = wall.replace(tzinfo=zone, fold=fold).astimezone(timezone.utc)
                if utc.astimezone(zone).replace(tzinfo=None) == wall:
                    candidates.add(utc)
            elapsed = time.perf_counter() - start
            expected = set()
            for left, right, offset in intervals:
                utc = wall.replace(tzinfo=timezone.utc) - timedelta(hours=offset)
                if left <= utc < right:
                    expected.add(utc)
            timezone_result["development_episodes"].append({
                "local": text, "baseline_utc": sorted(map(iso, candidates)),
                "source_arithmetic_utc": sorted(map(iso, expected)),
                "agreement": candidates == expected, "elapsed_seconds": elapsed})
    results["C1"] = timezone_result

    metadata = []
    for item in manifest["wheels"]:
        path = cache / "wheels" / item["filename"]
        assert digest(path.read_bytes()) == item["sha256"]
        with zipfile.ZipFile(path) as z:
            data = z.read(item["metadata_member"])
        assert digest(data) == item["metadata_sha256"]
        parsed = email.parser.BytesParser().parsebytes(data)
        metadata.append({"name": canonical(parsed["Name"]), "version": parsed["Version"],
                         "requires_python": parsed["Requires-Python"],
                         "requires_dist": parsed.get_all("Requires-Dist", []),
                         "provides_extra": parsed.get_all("Provides-Extra", [])})
    versions = {m["name"]: m["version"] for m in metadata}
    package_result = {"source_metadata": metadata, "development_episode": []}
    # Auditable finite closure from the raw dependency rows. This literal
    # reference does not reuse pip's resolver/packaging marker evaluator.
    base = {"requests", "charset-normalizer", "idna", "urllib3", "certifi"}
    for extras in [False, True]:
        requirement = "requests[socks]==2.32.3" if extras else "requests==2.32.3"
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.json"
            command = [sys.executable, "-m", "pip", "--isolated", "install", "--dry-run",
                       "--ignore-installed", "--no-index", "--no-cache-dir", "--disable-pip-version-check",
                       "--find-links", str(cache / "wheels"), "--only-binary=:all:",
                       "--report", str(report), requirement]
            invocation = run(command)
            entry = {"requirement": requirement, "invocation": invocation}
            if invocation["returncode"] == 0:
                data = json.loads(report.read_text())
                actual = {canonical(x["metadata"]["name"]): x["metadata"]["version"] for x in data["install"]}
                expected = {name: versions[name] for name in base | ({"pysocks"} if extras else set())}
                entry.update(baseline_distributions=actual, source_metadata_closure=expected,
                             agreement=actual == expected, report_environment=data.get("environment"))
            package_result["development_episode"].append(entry)
    results["C2"] = package_result
    results["C3"] = {"router_built": False, "feed_downloaded": False,
                     "reason": "Documentation establishes a completeness blocker for the broad task; no implementation probe."}
    results["resource_observations"] = {
        "self_peak_rss_native_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "children_peak_rss_native_units": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "note": "Linux values are KiB; observational, not per-arm measurements or enforced memory ceilings."}
    destination.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"output": str(destination), "timezone_agreements": [x["agreement"] for x in timezone_result["development_episodes"]],
                      "package_agreements": [x.get("agreement") for x in package_result["development_episode"]]}))


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())

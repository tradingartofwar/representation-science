#!/usr/bin/env python3
"""Read-only inspection of saved EXP-002 artifacts. Never invokes either arm/reference."""
import hashlib
import json
from pathlib import Path
import statistics
import sys


def inspect(folder):
    read = lambda name: json.loads((folder / name).read_text())
    expected = read("ARTIFACT_HASHES.json")
    actual = {name: hashlib.sha256((folder / name).read_bytes()).hexdigest() for name in expected}
    primary, replay, grades = (read(name) for name in ("PRIMARY.json", "REPLAY.json", "GRADES.json"))
    key = lambda row: tuple(row[field] for field in ("episode", "state", "arm", "local"))
    by_key = {key(row): row for row in replay}
    missing = [key(row) for row in primary if key(row) not in by_key]
    differences = [key(row) for row in primary if key(row) in by_key
                   and (row["response"], row["access"]) !=
                       (by_key[key(row)]["response"], by_key[key(row)]["access"])]
    hashes_ok = actual == expected
    result = {"hash_mismatches": [name for name in expected if actual[name] != expected[name]],
              "recorded_hashes": expected, "actual_hashes": actual,
              "primary_count": len(primary), "retained_replay_count": len(replay),
              "required_replay_count": 24, "missing_replay_keys": missing,
              "retained_canonical_differences": differences,
              "full_replay_verifiable": hashes_ok and len(primary) == len(replay) == 24
                    and len(by_key) == 24 and not missing and not differences,
              "primary_only": {}}
    for arm in ("B", "T"):
        rows = [row for row in grades if row["arm"] == arm]
        result["primary_only"][arm] = {
            "adequate": sum(row["grade"]["verdict"] == "ADEQUATE" for row in rows),
            "correct": sum(row["grade"]["correct"] is True for row in rows),
            "complete": sum(row["grade"]["complete"] is True for row in rows),
            "justified": sum(row["grade"]["justified"] is True for row in rows),
            "payload_bytes": rows[0]["measurement"]["canonical_payload_bytes"],
            "median_wall_seconds": statistics.median(row["measurement"]["wall_seconds"] for row in rows),
            "child_cpu_seconds_sum": sum(row["measurement"]["child_cpu_seconds"] for row in rows),
            "worker_peak_rss_kib_max": max(row["worker_metrics"]["max_rss_kib"] for row in rows),
            "response_bytes_sum": sum(row["measurement"]["canonical_response_bytes"] for row in rows),
            "verification_seconds_sum": sum(row["verification_seconds"] for row in rows)}
    result["source_access_records"] = {
        "retained_records": len(primary) + len(replay),
        "all_zero_and_no_denied_events": all(row["access"] == {"external_source_reads": 0, "denied_events": []}
                                              for row in primary + replay)}
    return result


if __name__ == "__main__":
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "exp002-run01"
    print(json.dumps(inspect(folder), indent=2, sort_keys=True))

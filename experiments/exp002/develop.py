#!/usr/bin/env python3
"""Preparation only: exactly the three previously exposed development labels."""
import copy
from pathlib import Path
import sys
import time
from harness import ROOT, check_environment, deadline, invoke, read, write
from reference import grade, truth


def main(output):
    config, payloads, reference = read("config.json"), read("payloads.json"), read("reference.json")
    environment = check_environment(config)
    labels = read("development_cases.json")["locals"]
    # This assertion is an exposure guard, not an expected-answer table.
    assert labels == ["2024-01-15T12:00:00", "2024-03-10T02:30:00", "2024-11-03T01:30:00"]
    records, keys, checks = [], {}, []
    for local in labels:
        start = time.perf_counter()
        with deadline(config["budgets"]["reference_wall_seconds"]):
            keys[local] = truth(local, reference)
        reference_seconds = time.perf_counter() - start
        for arm in config["arms"]:
            record = invoke(arm, payloads[arm], local, config)
            verdict = grade(arm, payloads[arm], local, record["response"], reference, keys[local])
            assert verdict["verdict"] == "ADEQUATE", verdict
            records.append({**record, "grade": verdict, "reference_seconds": reference_seconds})

    def corrupt(name, index, change, expected):
        original = records[index]
        response = copy.deepcopy(original["response"])
        change(response)
        got = grade(original["arm"], payloads[original["arm"]], original["local"], response,
                    reference, keys[original["local"]])
        checks.append({"control": name, "local": original["local"], "arm": original["arm"],
                       "corrupted_response": response, "expected_verdict": expected, "grade": got})
        assert got["verdict"] == expected, checks[-1]

    corrupt("omit valid fold alternative", 4, lambda r: r["utc_candidates"].pop(), "INADEQUATE")
    corrupt("invent gap candidate", 2, lambda r: r["utc_candidates"].append("2024-03-10T07:30:00Z"), "INADEQUATE")
    corrupt("correct value without evidence", 0, lambda r: r.pop("evidence"), "UNKNOWN")
    corrupt("wrong unique instant", 1, lambda r: r.update(utc_candidates=["2024-01-15T18:00:00Z"]), "INADEQUATE")
    corrupt("omit interval trace", 1, lambda r: r["evidence"]["trials"].pop(), "UNKNOWN")
    corrupt("wrong source identity", 0, lambda r: r.update(source_archive_sha256="0" * 64), "UNKNOWN")
    report = {"kind": "DEVELOPMENT_ONLY", "claim_status": "OBSERVED", "environment": environment,
              "evaluation_invocations": 0, "development_episodes_total": 3,
              "decoder_calls_this_check": 6, "reference_answers": keys, "records": records,
              "checker_controls": checks, "all_checks_passed": True,
              "limitations": "No new labels, transfer execution, runtime replication or human-independent review."}
    write(output, report)
    print("Development: 6 decoder checks and 6 output-corruption controls passed; evaluation invocations: 0")


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve())

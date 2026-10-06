#!/usr/bin/env python3
"""Future authorized execution. Preparation MUST NOT invoke main()."""
import argparse
from collections import Counter
import hashlib
from pathlib import Path
import re
import resource
import time
from harness import ROOT, canonical, check_environment, deadline, invoke, read, verify_manifest, write
from reference import grade, truth


def execute(commit, output):
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("supply the published 40-hex execution-freeze commit")
    if output == ROOT or ROOT in output.parents:
        raise ValueError("output must be outside the frozen package")
    output.mkdir(parents=True, exist_ok=False)
    primary, replay, grades, reference_answers = [], [], [], {}
    phase = "preflight"
    try:
        manifest_hash = verify_manifest()
        config, payloads, reference = read("config.json"), read("payloads.json"), read("reference.json")
        environment = check_environment(config)
        memory = config["budgets"]["supervisor_memory_bytes"]
        resource.setrlimit(resource.RLIMIT_AS, (memory,) * 2)
        episodes = read("cases.json")["episodes"]
        exposed = set(read("development_cases.json")["locals"])
        assert len(episodes) == 6 and all(len(e["states"]) == 2 for e in episodes)
        labels = [s["local"] for e in episodes for s in e["states"]]
        assert len(set(labels)) == 12 and not (set(labels) & exposed)
        assert config["arms"] == ["B", "T"]
        assert len(labels) * len(config["arms"]) == config["budgets"]["maximum_scored_queries"] == 24
        assert config["budgets"]["maximum_replay_queries"] == 24
        write(output / "PROVENANCE.json", {"freeze_commit": commit, "manifest_sha256": manifest_hash,
              "environment": environment, "publication_check": "operator must verify commit/read-back before launch"})
        # Seal all primary responses before any reference answer or verdict is computed.
        for phase, records in [("primary", primary), ("replay", replay)]:
            for episode in episodes:
                for state in episode["states"]:
                    for arm in config["arms"]:
                        records.append({"episode": episode["id"], "state": state["id"],
                                        **invoke(arm, payloads[arm], state["local"], config)})
                        write(output / (phase.upper() + ".json"), records)
        phase = "replay comparison"
        for first, second in zip(primary, replay, strict=True):
            if canonical([first["response"], first["access"]]) != canonical([second["response"], second["access"]]):
                raise RuntimeError("REPLAY_MISMATCH " + canonical({"episode": first["episode"], "state": first["state"], "arm": first["arm"]}))
        write(output / "REPRODUCTION.json", {"canonical_outputs_equal": True, "primary_queries": 24,
              "replay_queries": 24, "equivalence": "sorted-key compact JSON response plus access; timings excluded"})
        phase = "grading"
        for record in primary:
            local, arm = record["local"], record["arm"]
            if local not in reference_answers:
                start = time.perf_counter()
                with deadline(config["budgets"]["reference_wall_seconds"]):
                    answer = truth(local, reference)
                reference_answers[local] = {**answer, "seconds": time.perf_counter() - start}
                write(output / "REFERENCE_ANSWERS.json", reference_answers)
            start = time.perf_counter()
            with deadline(config["budgets"]["reference_wall_seconds"]):
                verdict = grade(arm, payloads[arm], local, record["response"], reference, reference_answers[local])
            grades.append({"episode": record["episode"], "state": record["state"], "arm": arm, "local": local,
                           "grade": verdict, "verification_seconds": time.perf_counter() - start,
                           "measurement": record["measurement"], "worker_metrics": record["metrics"]})
            write(output / "GRADES.json", grades)
        counts = {arm: dict(Counter(r["grade"]["verdict"] for r in grades if r["arm"] == arm)) for arm in config["arms"]}
        adequate = {arm: counts[arm].get("ADEQUATE", 0) for arm in config["arms"]}
        if adequate == {"B": 12, "T": 12}:
            comparison = "comparative correctness null; H2 efficiency remains OPEN"
        else:
            comparison = "inspect paired failures and counterexamples; counts alone do not establish benefit"
        write(output / "SUMMARY.json", {"claim_status": "OBSERVED", "counts": counts,
              "comparison": comparison, "H1_task_conformance_supported": adequate["T"] == 12,
              "replay": "REPRODUCED canonical deterministic outputs", "source_fidelity": "pinned-source-relative only",
              "H2_efficiency": "OPEN; no consumer-derived materiality threshold",
              "source_access_per_worker": 0, "recovery": "not tested; identical prohibition",
              "limitations": "designed boundary cases, same author, one source/zone/year/runtime; no causal method or population claim"})
        write(output / "ARTIFACT_HASHES.json", {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(output.glob("*.json"))})
        print("Completed 24 primary queries and 24 replays. Stop; inspect preserved results without refitting.")
    except Exception as exc:
        write(output / "STOP.json", {"phase": phase, "reason": type(exc).__name__, "detail": str(exc),
              "primary_completed": len(primary), "replay_completed": len(replay),
              "claim_status": "OPEN", "outcome": "UNASSESSABLE_STOPPED; preserve exposure before amendment"})
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze-commit", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    execute(args.freeze_commit, args.output.resolve())

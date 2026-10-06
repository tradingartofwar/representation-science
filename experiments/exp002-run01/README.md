# EXP-002 run01 — STOPPED, integrity discrepancy

Read the [execution/stop report](../EXP-002-results-2026-10-06.md) before interpreting these files.

The original runner returned success and wrote `SUMMARY.json` / `REPRODUCTION.json` asserting full success. Those assertions are preserved **without endorsement**. Post-run verification found that `REPLAY.json` does not match its recorded hash and retains 13 of the required 24 records. The eleven missing records were not recreated; no rerun occurred.

All original JSON files here are preserved unchanged. `ARTIFACT_HASHES.json` is the runner's original record and intentionally continues to expose the mismatch. The observed current bytes/hashes and missing replay keys are recorded in the separate [integrity stop](../EXP-002-integrity-stop-2026-10-06.json) and [measurement snapshot](../EXP-002-measurements-2026-10-06.json).

`PRIMARY.json` includes 24 raw stdout/stderr records and parsed responses. `GRADES.json` records 12 ADEQUATE for each arm, with correctness, completeness and justification separate. `REFERENCE_ANSWERS.json` contains the two agreeing reference routes. These primary observations do not establish full replay or satisfy H1's frozen success criterion. H1/H2 remain OPEN; the final comparison is UNASSESSABLE / STOPPED.

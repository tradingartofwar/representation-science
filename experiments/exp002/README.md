# EXP-002 frozen executable package

**Status: prepared and frozen; evaluation not run.** Read the [complete protocol](../EXP-002-local-time-transfer-protocol.md) before invoking anything. Laboratory Two is selected C1, Local Time Interpretation; C2 remains a qualified alternative.

## Artifact map

| Files | Role |
| --- | --- |
| `config.json`, `source.json` | Scope, source identity, runtime, permissions and numeric limits. |
| `cases.json` | Six evaluation episodes, twelve unexecuted labels. Data only; no answer table. |
| `development_cases.json`, `DEVELOPMENT.json` | Three already exposed labels, six preparation decoder outputs, checker-corruption controls and measurements. |
| `build.py`, `construction.json` | Source-to-payload transformation, compiler identity, construction measurements. |
| `payloads.json` | Exact B/T retained payloads. |
| `worker.py` | Both retained-only decoders and output evidence. |
| `reference.json`, `reference.py` | Supervisor-only full source-derived model, raw source rows and two reference algorithms. |
| `harness.py`, `develop.py`, `run.py` | Limits, isolated invocation, development and future execution. |
| `MANIFEST.json` | SHA-256 and byte sizes of every frozen package file and protocol; excludes only itself. |

## Preparation reproduction

Use CPython 3.12.14 on Linux x86_64. Acquire the archive only from the URL in `source.json`; verify its size/hash. The qualification [fetcher](../../labs/laboratory-two/assessment-2026-10-03/fetch_sources.py) documents acquisition, but fetching unrelated C2 sources is unnecessary. The source is not reacquired during scored decoding.

In a separate copy, `python build.py /absolute/path/tzdata2025b.tar.gz` reconstructs payloads/reference bytes using the recorded zic build. It overwrites construction artifacts; never run it in the frozen evaluation checkout. Timings and temporary compiler paths are incidental, so reconstructed `construction.json` is not expected to match byte for byte. Exact `payloads.json` and `reference.json` must match their freeze hashes. A different compiler may differ; investigate before execution rather than replacing the frozen bytes.

`python develop.py /new/path/DEVELOPMENT.json` repeats only the three exposed development labels. It does not read or evaluate `cases.json`. Do not mistake this preparation check for transfer execution. This freeze contains one such six-call check; no timing replication is claimed.

## Future execution — requires subsequent authorization

Do not run this command during freeze preparation. In a checkout of the published freeze commit, first verify the remote/read-back identity and all manifest hashes, then use an empty, new output path outside this package:

```bash
python experiments/exp002/run.py --freeze-commit FULL_40_CHARACTER_FREEZE_COMMIT --output /absolute/path/exp002-run01
```

The runner verifies local hashes/runtime, makes exactly 24 primary and 24 replay invocations in fresh processes, seals responses before grading, and records the two references, grades, measurements and replay result. It never overwrites an existing output directory. An unexpected condition writes `STOP.json` and stops; preserve all exposed outputs before proposing an amendment.

Canonical replay compares the complete response and access packet. Wall/CPU/RSS and raw JSON key order are excluded from equivalence. The run produces primary/replay raw stdout as well as parsed records. No `PRIMARY.json`, `GRADES.json`, final adequacy matrix or transfer-result record is part of this preparation package.

## Development scope and accounting

**OBSERVED:** the six ordinary/missing/ambiguous decoder checks passed, and six deliberately corrupted outputs received the expected INADEQUATE or UNKNOWN verdict. There were no new development inputs, observed baseline defects or evaluation queries. This demonstrates preparation feasibility and the specified checker controls only.

**OBSERVED:** restricted conventional TZif is 153 bytes, and canonical retained payloads are B 655 bytes / T 685 bytes. Object counts are not storage costs. `MANIFEST.json` inventories code and reference files separately; no total runtime-footprint or human-effort comparison is claimed.

All three C1 development episodes were already exposed in qualification. Reuse and controls do not reset that allowance. The boundary labels are designed tests with known semantics, not blind discovery or a random sample. H1/H2 remain OPEN until the authorized execution is completed and interpreted.

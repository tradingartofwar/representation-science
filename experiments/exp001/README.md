# EXP-001 executable comparison

Read the [operational addendum](../EXP-001-operational-addendum-v1.md) before interpreting this package. It amends operational choices before the first matrix run; it does not modify the original conceptual protocol.

Build the retained payloads from the laboratory at commit `f2126bfe929aae4eda77b4ea3418a4c38b47f0f5`:

```bash
python experiments/exp001/build.py --source-root /path/to/pinned-lonely-runner --output-dir experiments/exp001
python experiments/exp001/test_contract.py
```

The checked-in payloads already exist. The builder verifies the laboratory Git blob before extracting them. Their hashes, decoder/checker hashes, configuration, construction record, addendum and earlier audit checker are pinned by `MANIFEST.json`. The manifest does not hash itself.

After committing and reading back the freeze, execute and replay from the Representation Science root:

```bash
python experiments/exp001/run.py --freeze-commit COMMIT_SHA --output-dir /tmp/exp001-run
python experiments/exp001/run.py --freeze-commit COMMIT_SHA --output-dir /tmp/exp001-replay
```

Use the actual published freeze commit in both calls. Compare `RESPONSES.json`, `RESULTS.json` and `SUMMARY.json` byte for byte. The command verifies frozen file hashes, not the accuracy of the user-supplied commit string; publication/readback evidence must also be retained.

Eight payload types, two workloads, five queries and two decoder modes give 160 retained-only query processes. A separate source recovery process is run for each row/workload/question with a nonadequate mode. The temporary query directory contains only solver code; input arrives on stdin. The checker runs only after all retained-only responses are sealed.

Every mode has a declared decoder, not arbitrary computational closure. A verdict is about that decoder contract. All data are exposed development data; this is not a blind test. No model, search method, budget or case may be altered after a run and still be called this same frozen experiment.

On a decoder exception the run stops and leaves the completed responses and a failure record. Do not erase the failure or silently patch the frozen package. Exact output/cost files and interpretation will be saved under a separate run directory after execution.

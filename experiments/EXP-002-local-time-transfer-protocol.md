# EXP-002 — Bounded Local Time Transfer

**Version:** 1.0, 2026-10-03. **State:** EXECUTION FREEZE; EVALUATION NOT RUN.  
**Laboratory:** Two — Local Time Interpretation (qualified C1).  
**Governing design:** [DESIGN-LAB2-001 v0.1](../labs/laboratory-two/TRANSFER_DESIGN_v0.1.md).  
**Selection:** [decision and alternatives](../labs/laboratory-two/SELECTION-2026-10-03.md), commit `ebc9023fc18c5c7c887c409986e23ffbeb6f12cc`.  
**Executable contract:** [exp002](exp002/README.md), including its SHA-256 manifest. The Git commit containing that manifest is the freeze identity; record its full SHA when running.  
**Claims now:** preparation measurements are OBSERVED; H1 and H2 remain OPEN. No evaluation adequacy matrix exists.

## 1. Task, consumer consequence and claim ceiling

Given a local date/time label, return **every** UTC instant that maps to it in `America/New_York`, relative to the pinned IANA source. This is the validation/disambiguation subtask used by scheduling software, evidenced in the [C1 qualification packet](../labs/laboratory-two/assessment-2026-10-03/C1-local-time.md). No live scheduling action is taken.

| Exact output cardinality | Consequence for the declared input contract |
| --- | --- |
| Zero | No instant has this local label. Software must not present a fabricated candidate as a valid interpretation. |
| One | The label specifies one instant under the source model. |
| Two | Both alternatives must remain available to disambiguation. Silently selecting one fails this full-set request. |

The smallest material answer difference is one omitted or spurious UTC candidate, a wrong candidate timestamp, or a wrong missing/unique/ambiguous classification. Correct values without the required identity/completeness support are unresolved for certified adequacy. These are software correctness obligations, not estimates of realized user benefit, money saved or harm prevented.

**Primary target H1:** bounded execution of the adequacy contract in an external domain. **H2:** paired artifact correctness can be compared, but no consumer-derived speed/storage threshold or independent analyst allocation exists. Efficiency usefulness and causal advantage from the research method remain OPEN. Both arms may succeed; that is a comparative correctness null. T may fail; preserve the defect. Neither outcome is a reason to change this freeze.

This is a fixed-question/input-transition pilot. It does not vary independent rank, source epoch, question complexity or interaction order. It does not test unknown future questions, adaptive recovery, other zones/years, physical clock accuracy, or the person's intended occurrence. Numerous possible labels are not numerous independent structures.

## 2. Source, scope and identity

- IANA `tzdata2025b.tar.gz`, 464,295 bytes, SHA-256 `11810413345fc7805017e27ea9fa4885fd74cd61b2911711ad038f5d28d71474`. The public URL and member hashes are in [source.json](exp002/source.json), inherited from the qualification manifest.
- Raw `northamerica` SHA-256 `382bc1672c47ca0c8e2cf303a34cb9da689c9bca0e0c3d7f5cde884c05cb49f4`. All applicable US rules and the New York terminal zone row are validated during construction. The exact raw rows used by the countercheck are retained in `reference.json` with source identity.
- Local domain: canonical naive ISO labels `YYYY-MM-DDTHH:MM:00`, from `2024-01-01T00:00:00` inclusive to `2025-01-01T00:00:00` exclusive: 527,040 minute labels. No leap-second labels, floating tolerance or unspecified timezone.
- Time semantics: Python datetime / ordinary POSIX time, proleptic Gregorian calendar; seconds and microseconds zero. UTC strings are canonical `YYYY-MM-DDTHH:MM:SSZ`.
- Retained UTC window: `2023-12-31T00:00:00Z` inclusive to `2025-01-02T00:00:00Z` exclusive. Both valid source offsets (-5h and -4h) place every candidate for the declared local year inside this padded window.

This is **source-relative truth**. It does not independently verify historical clocks or establish that a time-zone database determines human intent. Source changes require a new version. IANA and Python remain the authorities for their source data and documented API semantics; this project does not claim ownership of either.

## 3. Arms, construction and fairness

Both arms receive the same source snapshot, year, task, known mechanisms, three exposed development labels, evidence standard and resource ceiling. Both specialize to the task. One investigator prepared both; neither was blinded to the semantics. B was chosen before comparative evaluation. The comparison cannot isolate a causal effect on an independent analyst.

| Contract element | B — conventional baseline | T — explicit retained-structure design |
| --- | --- | --- |
| Encoder | Ordinary `zic -b slim -r @1703980800/@1735776000`, source `northamerica`; extract New York TZif. | Validate applicable raw US rules and New York base offset; compute two transitions and three half-open UTC intervals. |
| Payload body | Base64 of the 153-byte restricted TZif. | Three integer `(start, end_exclusive, offset_seconds)` records. |
| Shared payload metadata | Schema, exact scope, source version and hashes. | Identical fields. |
| Decoder | `ZoneInfo.from_file` from retained bytes; try folds 0/1; round-trip each through UTC; retain only matches and deduplicate. | For every interval compute UTC = local-as-UTC minus its offset; retain it exactly when it belongs to that interval; deduplicate. |
| Evidence | Both inversion/round-trip trials, including rejected trials. | Every interval preimage/membership trial, including rejected trials. |
| Omissions | Time behavior outside the declared window; richer time-zone history is not query-accessible. | Time behavior outside the window, abbreviations and unrelated source rules; output does not require them. |

The full definitions are in [build.py](exp002/build.py), [payloads.json](exp002/payloads.json) and [worker.py](exp002/worker.py). The payloads include no local-query answer table. Construction reads no evaluation or development case list. All arm-specific behavior is inspectable in the same worker file; charge its full code size to either arm rather than pretending shared code is free.

**OBSERVED during preparation:** B's canonical JSON payload is 655 bytes; T's is 685 bytes. The reference-only unrestricted TZif is 3,552 bytes. These measurements do not establish adequacy or total-cost superiority. Base64, serialization, metadata, decoder/runtime and verification have different costs. Three intervals are not intrinsically smaller than a binary timezone model.

The ordinary short-generator alternative is explicitly admitted: the same raw rules plus direct calendar arithmetic can produce this output. `reference.source_calendar` implements that ordinary generator, and T's interval encoder uses the same established facts. Its code, source rows and development verification time remain visible; it is not declared infeasible or withheld from conventional work. The two-arm cap is not expanded to score it as a third arm. Consequently even a T success or payload difference cannot establish a capability unavailable to ordinary analysis.

The compiler's range options are documented in [IANA tz `zic.8` at 2025b](https://github.com/eggert/tz/blob/2025b/zic.8), Git blob `4eeb7a4654beac5a46b09215d0c1c2157c97b403`. Range truncation can introduce sentinel behavior outside the range; it is safe here only with the explicit source-offset bound and scope guard. Actual compiler version/hash, commands and timings are in `construction.json`. The compiler is needed for reconstruction, not scored decoding.

## 4. Input, retained state, internal reconstruction and recovery

Each invocation starts a new isolated Python process with only its worker code, one arm's payload, its arm ID and one `local` request in stdin. It receives no other labels, prior answers, reference store, grader feedback, source path or opposite-arm payload. There are no cross-query caches. Episode states do not carry responses into one another. The only transition is the requested local label; source and payload stay fixed.

There is **one scored permission stage: retained-only**. B's instantiation of TZif and T's interval scan are permitted internal operations on retained data. No artificial second stage forbids normal decoding; no success is credited merely for reclassifying it as reconstruction. The three-stage design ceiling is not a requirement to manufacture three different capabilities.

**External recovery is identically prohibited in scored invocations** (zero new source reads). Both payloads retain the source-derived information needed by their declared decoder. There is no source refresh, repair-on-grader-failure or adaptive recovery policy in this version. Missing/corrupt frozen artifacts, runtime mismatch, denied access or an exception stop execution. An unsupported query is UNKNOWN, never evidence of physical nonexistence. A later recovery experiment would require its own trigger, permissions and freeze.

The supervisor alone may read the fixed case list, payload store, full reference TZif and raw reference rows. These are retained verification inputs, counted separately from arm payloads. All primary and replay responses are sealed before any reference answers or grades are computed. The worker uses `ZoneInfo.from_file`, never ambient `ZoneInfo(zone_name)` or the machine's timezone database.

The trusted frozen worker installs a Python audit hook after its runtime imports and before reading stdin. Post-import file/directory, subprocess and socket operations are denied and logged. Each invocation stages only `worker.py` in a fresh temporary directory and uses `python -I`. This is an inspectable access contract for trusted code, **not** an OS security proof against malicious Python or native code. Standard interpreter/library loading before the hook is shared runtime state, not a hidden source recovery. No network is part of construction or evaluation; the source archive was acquired during qualification.

## 5. Output and verification contract

An `ANSWER` response must identify `local`, `zone` and `source_archive_sha256`; contain a lexicographically sorted, duplicate-free `utc_candidates` list and its exact `status` (`missing`, `unique`, `ambiguous`); and include `evidence` with `kind`, canonical payload SHA-256 and a full ordered `trials` list.

- B evidence kind is `fold-roundtrip`: two trials ordered by fold 0 then 1, each with `fold`, `utc`, `roundtrip_local` and Boolean `accepted`.
- T evidence kind is `interval-preimages`: three trials ordered by interval index, each with `interval`, `utc` and Boolean `accepted`.
- The accepted union must equal the returned candidate list. Both arms must expose all trials; neither arm receives a weaker evidence standard.
- The outer packet records `access.external_source_reads`, `access.denied_events`, worker wall timing and peak RSS. The supervisor preserves literal stdout/stderr, return code, input/output bytes and process wall/CPU measurements. Byte accounting uses UTF-8 and sorted-key compact JSON where explicitly called canonical.

Candidate traces make the answer checkable but are not self-authenticating completeness proofs. [reference.py](exp002/reference.py) additionally requires agreement between:

1. **Forward UTC search:** unrestricted source-compiled TZif; enumerate UTC minutes from local-as-UTC minus 24 hours through plus 24 hours, inclusive (2,881 points), and forward-map each. This never assigns an input fold to search for answers.
2. **Source-rule countercheck:** inspect all retained raw US rows, select the active rules and validate the New York base-offset row; use Gregorian month calendars and local-label gap/fold cases. This never reads T's intervals or B's bounded TZif.

**Completeness argument:** the raw source permits only offsets -5h and -4h in this year. Each valid UTC preimage of a minute-grid label is therefore a minute-grid instant within the searched 24-hour bounds. The source rules exhaust the spring gap, autumn fold and ordinary regions. Thus the finite search is exhaustive for a requested label under these source premises; it is not a sample of its possible UTC answers. The 12 evaluation labels do not exhaust all local inputs or independently prove the correctness of all implementations on the whole year.

Independence is limited and explicit. Both routes share the authoritative facts and Python datetime/calendar foundations. Forward search shares ZoneInfo with B; the other route does not. The local-calendar countercheck shares source rules with T but has a different representation, transition calculation and search direction. All experiment code is from the same AI contributor; no independent human/formal review is claimed. Unresolved disagreement stops grading rather than voting for an oracle.

| Condition | Verdict and attribution |
| --- | --- |
| Exact full set/status, source identity and evidence pass both checks | ADEQUATE for the frozen task and invocation. |
| Wrong, duplicated, unordered, omitted or spurious candidate; wrong classification | INADEQUATE, with expected/received counterexample. No irrecoverable-information claim follows. |
| Correct set/status but identity or evidence missing/invalid | UNKNOWN for certified adequacy; retain correct/complete value observations separately. |
| Declared unsupported response | UNKNOWN; not a missing-time answer. |
| Unexpected exception, budget failure, manifest/runtime mismatch, reference/replay conflict or undeclared access | Stop the execution; preserve partial outputs and STOP record; comparison unassessable. |

In machine grades, `correct` denotes candidate validity and `complete` denotes coverage of the expected candidates; the verdict also checks ordering, multiplicity and classification. Evidence checking is an additional cost, not a free privilege granted to one arm. Both reference work and per-response verification timings are preserved.

## 6. Exposure, cases and exact counts

All three development episodes permitted for C1 were consumed in qualification: ordinary `2024-01-15T12:00:00`, missing `2024-03-10T02:30:00`, ambiguous `2024-11-03T01:30:00`. Preparation reuses only these labels. [DEVELOPMENT.json](exp002/DEVELOPMENT.json) preserves six decoder calls and six output-corruption controls. Controls alter already returned outputs, not the task/source or case domain; they are not real baseline failures.

The selection rule in [cases.json](exp002/cases.json) is source-semantic and independent of arm outcomes: use adjacent minutes on either side of each gap/fold endpoint, and the first/last adjacent minute pairs of the declared year to check the retained window. Exact order:

| Episode | First local label | Second local label | Purpose |
| --- | --- | --- | --- |
| E1 | 2024-03-10 01:59 | 2024-03-10 02:00 | Gap begins |
| E2 | 2024-03-10 02:59 | 2024-03-10 03:00 | Gap ends |
| E3 | 2024-11-03 00:59 | 2024-11-03 01:00 | Fold begins |
| E4 | 2024-11-03 01:59 | 2024-11-03 02:00 | Fold ends |
| E5 | 2024-01-01 00:00 | 2024-01-01 00:01 | Local-year start coverage |
| E6 | 2024-12-31 23:58 | 2024-12-31 23:59 | Local-year end coverage |

Seconds are zero in every case. Exactly six episodes × two labels × two arms × one permission stage = **24 primary queries**, followed by **24 replay queries**, in episode/state/B-then-T order. Twelve label-level paired comparisons, not 24 independent cases. The replay uses fresh processes and no reference feedback; canonical response plus access logs must match, excluding measured timing/RSS and incidental serialization order.

These are designed boundary tests with known rules, not blinded or randomly held-out predictions. Their outputs have **not** been computed by either decoder or either checker during preparation. No evaluator result influenced selection. Do not confuse previously unexecuted labels with unknown mechanisms or statistical independence.

## 7. Resources, costs and stop rules

Exact numeric limits are in [config.json](exp002/config.json): CPython 3.12.14, Linux x86_64; each worker 60s wall/60s CPU, 256 MiB address space, 16 KiB response, 64 file descriptors; construction 60s wall/CPU and 256 MiB address space; supervisor 512 MiB address space; each reference or per-response check 60s wall; each output artifact at most 4 MiB. The construction archive is exactly 464,295 bytes and is read once. Scored workers get zero external source reads. There are no model-training calls or learned parameters.

Subprocess timeouts and POSIX resource limits enforce worker budgets; construction uses a wall alarm plus memory/CPU limits; reference checks use wall alarms. The frozen trusted worker also caps its own input/output. Filesystem-size limits alone do not limit pipe output, so the explicit output size check matters. Freeze integrity and runtime identity are checked before invocation. A timeout is an operational failure, not evidence that no valid time exists. No limit is chosen to make the baseline fail: development checks completed within these same worker limits.

Report a cost vector, without inventing a universal score:

- retained arm bytes, raw TZif bytes or interval count, common scope/provenance bytes;
- encoder and full shared decoder/harness/reference code bytes (manifest), compiler/runtime dependencies;
- archive/reference storage separately, construction wall and peak memory, compiler substeps;
- query wall/CPU/peak RSS, stdin/stdout and canonical answer bytes;
- reference and evidence-verification work, new source reads, replay cost separately.

`construction.json` distinguishes the full reference compilation from B's restricted compilation and T's interval construction. Shared parsing, imports and process overhead must not be presented as arm-specific algorithm time. Source-rule countercheck and forward enumeration are timed jointly per label; do not infer individual speed from that joint measurement. Runtime/library installation footprint and human effort are not fully measured; they remain explicit exclusions and block a total-system efficiency claim. A single deterministic replay checks answers, not stable latency distributions.

## 8. Prospective interpretation

H1 task conformance is supported only if T delivers all 12 adequate answers, both reference routes agree, the completeness/error controls pass, and canonical replay matches. This earns a finite source-relative conformance observation and reproduction, not a new theorem or universal adequacy claim. Failures receive case-level diagnosis; an incomplete H1 criterion is not silently relaxed.

- If B and T are adequate on all labels: comparative correctness null; no observed incremental correctness benefit. Cost differences are descriptive; H2 efficiency stays OPEN.
- A T-only adequate material answer can support a bounded artifact-level correctness benefit only with the exact failure/trace and no T regressions on the frozen cases. It cannot establish a causal research-method advantage or superiority over all conventional methods.
- B-only success is negative transfer for this implementation. Improvements and regressions together remain mixed. Counts do not erase regressions.
- Correct abstention prevents an unsupported assertion but does not complete this full-set task.
- A reference/access/provenance/replay/resource stop is unassessable, not evidence for either method.

Use OBSERVED for initial results, REPRODUCED for replayed canonical results, KNOWN only for properly sourced established semantics, HYPOTHESIS for broader proposals, OPEN for untested claims and DISPROVEN only for a specifically contradicted claim. This package does not pre-label either representation a failure or an information-loss class. Artificial checker corruptions establish only that the checker detects those corruptions.

After authorization, execute once and replay once, preserve all outputs, produce one bounded interpretation and Representation Record, and update CURRENT_STATE. Stop at the cap. A post-freeze defect requires a visible amendment and new exposure designation; preserve this version and its failure. No replacement cases, additional domain scan or silent baseline repair.

## 9. Publication boundary

Before any evaluation, publish this protocol, source identities, actual payloads, both decoders, both reference routes, development record, fixed cases, budgets, run script and manifest; read all written files back and verify their hashes. The publishing commit identifies the complete freeze, avoiding a self-referential commit hash inside its own files.

The runner requires that 40-character commit SHA and a fresh output directory. Its CLI records the supplied SHA and verifies local file hashes; it does not authenticate a remote GitHub publication itself. The operator must verify the read-back publication and later authorization before launching it.

**Current boundary:** selection and preparation are complete. Evaluation remains unrun and requires a subsequent instruction. No source/label decoder has been invoked on the evaluation cases in this preparation.

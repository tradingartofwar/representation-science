# Laboratory Two candidate assessment — 2026-10-03

**Governing design:** [DESIGN-LAB2-001 v0.1](../TRANSFER_DESIGN_v0.1.md) at `56f37d86de743431d4cc42c8ada9c4a70eac9919`.  
**Decision boundary:** qualification only. No Laboratory Two selection, experiment number, T implementation or transfer trial.

## Dispositions

| Candidate | Disposition | Decisive evidence / remaining boundary |
| --- | --- | --- |
| [C1 — local scheduling input disambiguation](C1-local-time.md) | QUALIFIED | Pinned IANA rules, finite zone/year, ordinary ZoneInfo baseline and separate source arithmetic agree on three declared development cases. Qualification is source-relative, not a claim about user intent or all scheduling applications. |
| [C2 — package extra dependency closure](C2-dependency-extras.md) | QUALIFIED | Seven hashed public wheels, exact finite metadata closure, and ordinary offline pip plans agree for the exposed base/SOCKS episode. Declared dependencies are the task; runtime functionality is outside it. |
| [C3 — accessible MBTA journey after an elevator change](C3-accessible-transit.md) | NOT QUALIFIED / rejected as framed | Operator-documented incomplete pathways block a definitive broad physical itinerary/no-route ground truth. Snapshot, baseline integration, budget and public operational evidence also remain unresolved. |

**Qualified:** C1 and C2 for their stated bounded tasks. **Unresolved-only candidates:** none; C3 has both open gates and a decisive failed gate. **Rejected:** C3's present scope, not the whole transit domain. A narrower transit task remains OPEN and has not been substituted or qualified. No ranking, preferred candidate or implicit laboratory choice is made.

PASS/OPEN/FAIL are administrative gate dispositions. KNOWN / REPRODUCED / OBSERVED / HYPOTHESIS / OPEN / DISPROVEN remain scientific claim statuses. Qualification is not evidence for H1 or H2, and does not mean a future executable contract is already complete.

## How the assessment was bounded

Exactly three tasks were identified using primary operator, standards and software documentation. They were chosen for evidenced external operations and different source/verification obligations, not comparative performance. This is a purposive feasibility assessment, not an exhaustive survey. No fourth task replaced a rejected candidate.

[ASSESSMENT_SCOPE.md](ASSESSMENT_SCOPE.md) was written before the local probes. G7 requires ordinary-baseline feasibility evidence before selection; the limited baseline-only checks satisfy that prerequisite without starting a B/T experiment. They are permanently exposed development examples and consume the stated development allowance if a candidate is selected. The governing design and its limits were not amended.

The external need in C1/C2 is a documented software correctness obligation, not a recruited operational customer. That meets G1's consumer-role/evidenced-use requirement; it does not demonstrate realized user benefit. A later claim about adoption, analyst productivity or avoided loss would need additional evidence.

## What the comparison taught us

1. **A good ordinary baseline is already substantial.** C1 requires real gap/fold handling; C2 requires extras and metadata semantics. Both conventional baselines passed the exposed checks. An intentionally weakened offset cache or flattened dependency list would be an auxiliary control, not the primary comparator. These observations do not constitute a comparative null: there is no T arm yet.
2. **Source adequacy and representation adequacy are different failure locations.** C3's incomplete coverage blocks a physical nonexistence claim before any compression experiment. Better decoding of that same feed cannot by itself certify omitted real alternatives. Reporting UNKNOWN is warranted but does not complete the original trip decision.
3. **Ambiguity can call for a decision, not more recovery.** C1 can know the complete pair of UTC alternatives while lacking a user's choice. Reopening the same correct time-zone source will not reveal that intention. The requested output must distinguish enumeration from policy-based selection.
4. **Context controls what a retained relation means.** C2's extras are scoped to a distribution; normalization matters. Its declared `security` extra contributes no additional requirement in these wheel bytes. A feature label is not evidence that the dependency set must change. This is a natural possible null, not a synthetic defect.
5. **A historical source and an as-published history differ.** MBTA documents corrections/replacements in its archive. Similarly, C1 explicitly uses a 2025 release's account of 2024. Any later recovery experiment must distinguish correcting a historical model from reproducing what an actor could know at the time.

Items 1 and 4 are supported by the preserved development/source observations. Items 2, 3 and 5 are scoped deductions from the task contracts and cited source limitations, not empirical generalizations. None establishes a new field, an information lower bound, an independent-rank scaling law or method superiority.

## Evidence and reconstruction

- [SOURCES.json](SOURCES.json): IANA archive/member hashes and seven wheel/metadata identities, direct public URLs and license-member hashes.
- [DOCUMENT_SOURCES.json](DOCUMENT_SOURCES.json): inspected primary documentation, versions/commits/blob identities and access date. Versioned documents support the actual contract; live guidance is identified as such.
- [BASELINE_PROBES.json](BASELINE_PROBES.json): source rows, all inspected wheel dependency fields, exact answer sets, commands, runtime/compiler identities, source hashes and observed timing/memory.
- [probe_baselines.py](probe_baselines.py): offline qualification checker; [fetch_sources.py](fetch_sources.py): explicit hash-verifying source acquisition.

Example reconstruction from this directory, with Python 3.12, pip 26.2.1 and zic available:

```sh
python fetch_sources.py /tmp/lab2-qualification-inputs
python probe_baselines.py /tmp/lab2-qualification-inputs /tmp/lab2-qualification-replay.json
```

Inspect `agreement` for the three C1 cases and two states of the single C2 episode. Compare canonical source identities and answer sets, not temporary directory names, JSON object order, environment strings or observed timings. This assessment records one local probe run; it does not claim a second exact replay or independent human review. Source/compiler/interpreter changes must be recorded. The future experiment still requires its own frozen environment, isolation, grading controls and reproduction.

The timezone baseline uses raw-source compilation; its countercheck uses direct rule arithmetic. The dependency countercheck is a finite manually auditable closure derived from complete wheel metadata, not a separately validated general resolver. Shared data, parsing/calendar primitives and same-assessor exposure are disclosed in the packets.

Acquisition limitations retained: direct network reads initially required the environment's network permission route; public source downloads then succeeded. The initial wheel selector encountered both Python 2 and Python 3 PySocks artifacts and stopped. It was narrowed to the declared Python 3 universal artifact before any baseline probe. This was a source-acquisition correction, not a hidden failed candidate outcome. Some MBTA website pages were unavailable through search retrieval; operator documentation was read at its pinned public repository instead. No unsupported website content was used as evidence.

No third-party distributions or operational transit feeds are republished here. Authoritative source artifacts remain upstream. The tiny derived records are sufficient to locate and check the inputs used.

## Remaining work and non-decisions

A subsequent selection decision may consider C1 or C2, or explicitly reopen C3 with different evidence/scope. This packet makes no recommendation among them. A selected candidate still needs final B/T artifacts, an independently structured implemented grader or adequate certificate, future case selection, enforced budgets, consequence rules, source/side-channel isolation and a committed/read-back execution manifest. No additional trial or larger scan follows automatically.

**HYPOTHESIS:** explicit representation-adequacy analysis may add useful knowledge beyond ordinary competent work. **OPEN:** H1 conformance and H2 incremental usefulness in every candidate. The probes earn only their recorded development scope.

# Laboratory Two selection — local time interpretation

**Date:** 2026-10-03  
**Decision:** select qualified C1, local scheduling input disambiguation.  
**Basis:** DESIGN-LAB2-001 v0.1 and the three qualification packets at `fe50d416daf18e44cac2529d643982f7cfa2d50e`.  
**Authorization boundary:** the earlier instruction to defer selection was explicitly superseded. Selection and preparation/publication of the execution freeze are authorized; transfer evaluation is not yet authorized.  
**Claim status:** administrative selection; H1/H2 remain OPEN. No new transfer observation is asserted.

## Selected task

Laboratory Two is **Local Time Interpretation**, initially restricted to the complete UTC interpretation of minute-grid local labels in `America/New_York` during 2024, relative to the pinned IANA tzdata `2025b` source.

The output is the full UTC candidate set, missing/unique/ambiguous status, source identity and checkable completeness support. A local-input change is the primary transition; the zone, source epoch, question and output obligation remain fixed. This does not infer a person's intended occurrence or choose a scheduling policy for them.

The first experiment will be **EXP-002 — Bounded Local Time Transfer**. Prepare and publish its complete executable contract before evaluation. Selection alone is not a freeze, and development checks are not transfer results.

## Why C1 rather than C2 for this first test

Both C1 and C2 meet the qualification gates at their stated source-relative scope. Neither has demonstrated method advantage. The decision concerns the first bounded conformance test, not the general importance of either domain.

| Consideration | C1 | C2 | Decision relevance |
| --- | --- | --- | --- |
| Consequential obligations | Missing labels, two valid interpretations, exact boundary inclusion and source-year coverage. | Conditional dependency membership, normalization and distribution-scoped extras. | Both are real software correctness obligations. |
| Independent check structure | Compiled time-zone interpretation can be checked against direct source-rule arithmetic and forward search. | Ordinary resolver can be checked against a very small finite metadata-closure formula. | C1 supports a useful cross-check between distinct data encodings and search directions. |
| Remaining unexecuted inputs | Many minute labels; adjacent transition and year-boundary cases are available without changing the task. | Six unrun extra configurations, but fewer materially new inventory classes. | C1 offers a broader bounded implementation-validation exercise. This is not statistical independence or greater representational rank. |
| Development exposure | All three allowed development episodes used; reuse them for implementation and checker controls. | One episode used; two remain available. | C1's constraint is manageable; no extra development case is added silently. |
| Ordinary baseline | ZoneInfo/TZif and ordinary exact interval arithmetic are already available. | Pip and a direct Boolean closure generator are already available. | Neither baseline may be weakened to manufacture a benefit. |

C1 is selected for its combination of consequential boundary semantics and separately structured checks. It is **not** selected because T is expected to beat B. The experiment may produce a comparative null or a T defect, and either result must be preserved.

## A consequential limit in C2's apparent case count

Let F be Requests plus its four unconditional dependencies, P be PySocks, and C be chardet. Under the pinned wheel source, the primary distribution inventory is

`F ∪ ({P} if socks is requested) ∪ ({C} if use-chardet-on-py3 is requested)`.

The `security` extra adds no requirement in these bytes. Consequently eight admissible root-extra configurations yield four distinct **distribution inventories**. The full output still distinguishes requested extras and provenance; it is not identical across all pairs with the same inventory.

The base and SOCKS inventories were already exercised. Of the six unexecuted configurations, two repeat those inventory classes and four occupy the two remaining classes. Six new invocations therefore would not be six new dependency structures. This follows analytically from the existing qualification derivation; no new C2 decoder or query was run. It does not disqualify C2 or establish a general rank theorem.

## Fairness requirements carried into the execution freeze

Both arms may specialize to the declared source/year and requested output. A compact T must not be compared only with an unnecessarily general B and then credited with an advantage from specialization itself.

The proposed conventional B uses an ordinary TZif representation limited to the needed UTC window, with ZoneInfo inversion and round-trip validity checking. zic's documented `-r` range and `-b slim` options make that specialization available without this project's method. T may use the ordinary three-interval representation obtained from the source rules. No claim of inventing exact intervals is implied.

Freeze actual payloads, all decoder and shared-code costs, provenance, completeness evidence and exact outputs. Source-rule arithmetic remains an ordinary baseline alternative as well as a verification tool. Any measured differences apply to the tested implementations; they cannot establish the unique contribution of the research method.

## Claim ceiling and alternatives

- **Primary aim:** an operational H1 conformance test of a representation-adequacy contract outside Lonely Runner, with meaningful error/completeness controls.
- **H2:** record paired correctness and costs honestly. No consumer-derived efficiency threshold or independent analyst-allocation study exists. Do not convert a small payload, faster query, implementation bug or shared-author comparison into a general usefulness claim.
- **Not tested:** increasing independent complexity, unknown future questions, adaptive recovery triggers, source changes, physical-clock fidelity or user-intent inference. The fixed, known source does not support those conclusions.
- **C2 retained:** qualified alternative for a later expressly authorized dependency-context or optionality study. Its exact finite task remains valuable; it is not replaced by a larger dependency graph to rescue a desired result.
- **C3 retained:** rejected as framed, with its source-completeness blocker and open gates intact. No narrower transit task is silently substituted.
- **Deferral alternative:** an H2-first operational study would require evidence beyond either current packet. This selection deliberately accepts a bounded conformance test rather than claiming to have supplied that evidence.

No candidate assessment, design, source record or EXP-001 freeze is rewritten. The selection changes the administrative state only. The next gate is a published, read-back EXP-002 execution freeze; after that, wait for authorization to run it.

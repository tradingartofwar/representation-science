# RR-LR-005 — Missing support can remain recoverable from retained information

**Date:** 2026-10-03  
**Laboratory:** Lonely Runner  
**Claim status:** OBSERVED / REPRODUCED finite operational comparison

## Underlying system, question and output

Common-start speeds (0,1,10,11,12,13,23,25), selected stationary reference, unit period and closed threshold 1/8. Ask for the optimum, every maximizing time and the complete threshold-safe set, with exactly the EXP-001 output grammar.

## Representation object and retained information

EXP-001 R4 retains all original labelled parent edges as grouped vertices/edge incidences, q=10, six affine generator rows, convex-parent semantics and the physical map. It occupies 1,450 compact JSON bytes in the frozen encoding. R3 is a second instance: two labelled safe segments plus generator rows and recovery data, 254 bytes.

Neither payload changes between native and internal decoder trials.

## Omitted support versus omitted information

Native R4 searches only points on the old edges. That support omits the final maximizing contacts t=17/35 and 18/35 inside an old parent face. However all parent vertices remain present, grouped by their convex parent. The omitted interior is computably recoverable as their convex hull.

Native R3 selects threshold-safe points on two retained segments. It omits other points from that support, but its affine generator rows still reconstruct every physical speed. A general exact physical envelope can be built internally.

## Recovery source and map

Internal R4 recovery: grouped vertices → exact hull facets → integer orbit slices y=qt−h → added physical band → physical time/laps and full exact sets. It does not read the richer atlas.

Internal R3 recovery: rows (a,b) and q → speeds a+bq → append the declared speed 25 → exact physical distance envelope. It does not read an external model.

External recovery is available uniformly from the separately pinned speed-vector source, but neither of these internal repairs requires it.

## Evidence and counterchecks

Native R4 returns six global maximizing times and misses exactly 17/35 and 18/35. Its scalar maximum happens to be 1/7, but without a global upper certificate its Q3 verdict is UNKNOWN. Internal R4 recovers the exact optimum, all eight maximizers and all fourteen safe components. R3 likewise moves from native failure on Q3–Q5 to adequate internal answers without changing bytes.

The independent checker constructs complete reference sets by closed-band intersection and threshold-event decomposition and optimizes by exact tent crossings. All 160 operational outputs and the separate recovery trials reproduce byte for byte. This is AI-authored alternate-code checking, not independent human/formal proof certification.

## Consequential distinction and failure condition

**Absence from a restricted search support does not establish absence from the information encoded by its stored description.** Declare the decoder and completeness evidence before drawing a representation-loss conclusion.

A mismatch after the specified hull/generator reconstruction, an unrecorded source read, or incorrect completeness would refute the corresponding operational claim. This finite pass proves no universal reconstruction guarantee for other representation classes.

## Costs, supported futures and limits

Record retained bytes and reconstruction work separately. R4's internal Q5 uses 32 hull-triple and 128 hull-side checks plus slice/cut work; R3 rebuilds a physical envelope. The common decoder code and inherited preprocessing are additional costs. No universal time, storage or information lower bound follows.

All five EXP-001 outputs and the declared parent-first restoration remain supported by these internal decoders on this case. Other coefficient families, rank changes, references, unsupported geometry and outside applications require new contracts and checks.

The suggested broader relation between adequacy, decoding cost and optionality remains **HYPOTHESIS** beyond this measured finite workload. External usefulness is **OPEN**.

## Sources

- [EXP-001 operational freeze](https://github.com/tradingartofwar/representation-science/commit/96141bfe0b0de99c99ddfdb11e6d41187dc1eef2)
- [Results and interpretation](../experiments/EXP-001-results-2026-10-03.md)
- [Raw cell outputs and counterexamples](../experiments/exp001/run01/RESULTS.json)
- Lonely Runner commit `f2126bfe929aae4eda77b4ea3418a4c38b47f0f5`, `notes/CC_SIX_SEVEN_TRANSFER_2026_09_29.md` and `notes/CC_BOUNDED_SELECTOR_2026_09_29.md`; blob identities are in the audit source ledger and construction record.

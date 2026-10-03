# Experiments

Experiments vary a declared representation variable while preserving enough of the underlying system to identify what caused the result.

## Completed

- [EXP-001 — results and interpretation](EXP-001-results-2026-10-03.md): completed under freeze `96141bf`. All 160 retained-only queries and 43 triggered source recoveries completed, and outputs reproduce exactly. The [original conceptual protocol](EXP-001-resolution-frontier-protocol.md) is preserved unchanged.

## Pre-execution audits

- [EXP-001 audit — October 3](EXP-001-pre-execution-audit-2026-10-03.md): q=10 separates Q4/Q5; retain it. Payload/decoder/recovery and output contracts need an explicit operational freeze before the matrix run. Original protocol unchanged; no final adequacy matrix scored.
- Reproduction: [checker](exp001_audit.py), [source pins](EXP-001-audit-sources.json), and [exact results](EXP-001-audit-results.json). Independently structured AI-authored checks match the pinned laboratory geometry; large historical studies were not rerun.

## Pre-selection designs

- [Laboratory Two — bounded transfer design v0.1](../labs/laboratory-two/TRANSFER_DESIGN_v0.1.md): qualification gates, ground truth, a competent conventional comparator, payload/decoder/output/recovery contracts and consequential-outcome rules. No laboratory or task selected, no experiment number assigned, and no external trial run. The [qualification template](../labs/laboratory-two/CANDIDATE_QUALIFICATION_TEMPLATE.md) remains unfilled; this design is not an execution freeze.
- [Laboratory Two — candidate assessment](../labs/laboratory-two/assessment-2026-10-03/README.md): three populated packets, two qualified bounded tasks and one rejected scope. Limited conventional-baseline development checks are preserved separately from transfer experiments; no T arm or laboratory selection exists.

## Rule

[Operational addendum v1](EXP-001-operational-addendum-v1.md) and [executable package](exp001/README.md) were published and read back before execution: six original rows, two designed controls, native/internal decoding and separate source recovery. [Run01](exp001/run01/RESULTS.json) and its [reproduction record](exp001/run01/REPRODUCTION.json) preserve every result and input identity.

Do not convert an extracted historical example into a “new experiment.” Records summarize prior evidence. Experiments must declare what is varied, what is held fixed, and what would count as a null or failure before execution.

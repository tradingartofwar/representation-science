# EXP-001 — Resolution Frontier on a fixed Lonely Runner system

**Date designed:** 2026-10-03  
**Status:** PROTOCOL ONLY — not yet executed  
**Laboratory:** Lonely Runner

## Purpose

Test the central Representation Science idea while holding the underlying physical system fixed:

> **Changing the question can change which information a representation must preserve.**

This experiment is not a search for a new Lonely Runner theorem. It is a controlled comparison of representation obligations.

## Fixed system

Use the A-ray q=10 seven-moving-runner system with stationary reference:

(0, 1, 10, 11, 12, 13, 23, 25)

common start, track circumference 1.

Use closed physical distance bands.

The source record already supplies exact parent/child geometry, one-witness selection machinery, and a concrete example where final maximizing times t=17/35 and 18/35 lie in the relative interior of an old parent face rather than on the old parent edge set.

## Question ladder

Ask the following questions about the **same system**.

### Q1 — Existence at threshold 1/8

Does at least one 1/8-safe physical time exist?

### Q2 — One witness at threshold 1/8

Produce one exact physical witness and recover all runner phases/laps.

### Q3 — Optimal value

Determine the maximum minimum separation.

### Q4 — Every maximizer

Return the complete set of times attaining the optimum.

### Q5 — Complete 1/8-safe set

Return every physical time satisfying the closed 1/8 threshold, including isolated points and interval endpoints.

### Q6 — Transfer after removing the final constraint

Delete speed 25, solve the corresponding six-moving-runner system, then re-add speed 25 using only the information retained by each candidate representation. Determine which representations can recover the required output without returning to a richer source.

## Candidate representations

Freeze these before execution.

### R1 — Scalar optimum only

Retain one optimal value, no optimizer identities.

### R2 — All old global optimizing times

Retain the smaller system's optimum and every old global optimizer.

### R3 — Two-segment one-witness carrier

Use the bounded selector representation from `CC_BOUNDED_SELECTOR_2026_09_29.md`.

### R4 — Old parent one-skeleton

Retain labelled parent edges and surviving edge points, with physical recovery maps.

### R5 — Full labelled parent facets plus seventh-band cuts

Retain the richer polyhedral source sufficient for full child reconstruction.

### R6 — Exact physical interval/set representation

Use direct exact physical-time safe-set construction as a reference representation.

Compatibility Calculus labels are not privileged. Where an ordinary exact interval or polyhedral representation supplies the same information more transparently, use it.

## Frozen adequacy matrix to test

Do **not** assume the expected answers are correct merely because earlier notes suggest them.

For each pair (Ri,Qj), classify:

- ADEQUATE — output recoverable exactly from Ri under the frozen rules;
- INADEQUATE — counterexample or missing information prevents the output;
- UNKNOWN — protocol does not establish either;
- RECOVERABLE — Ri itself is insufficient but its declared pinned recovery source restores the answer.

## Required evidence

For every ADEQUATE cell:

- exact output;
- recovery map;
- independently structured physical check.

For every INADEQUATE cell:

- smallest explicit counterexample or missing distinction known;
- show that the richer reference output differs.

For every RECOVERABLE cell:

- name the omitted information;
- record the recovery operation and source.

## Cost dimensions

Measure separately where available:

- number/type of retained objects;
- symbolic/rational field count;
- construction operations;
- query operations;
- recovery operations;
- output size.

Do not combine them into one score.

Human inspection burden may be described qualitatively but should not be presented as a measured cognitive result.

## Predeclared controls

The source record provides several controls that must remain visible:

- all old six-coordinate global optimizers fail the added 1/8 constraint at q=10;
- final q=10 maximizers include t=17/35 and 18/35 inside an old parent face;
- the two-segment selector is only a one-witness carrier and is not expected to recover all maximizers or the complete safe set.

These are development facts, not hidden validation cases.

The experiment's value is the explicit **question × representation adequacy map**, not rediscovery of those facts.

## Success criterion

The experiment succeeds scientifically if it produces a reproducible matrix showing at least one transition where changing only the requested output forces a concrete representation enrichment, with the missing consequential distinction identified.

A null result is acceptable if all candidate representations turn out equivalent for these questions.

## Failure / redesign criterion

Redesign before execution if the selected q=10 system does not actually discriminate among enough questions to make the comparison informative.

Do not retune representations after seeing the final matrix without declaring a second experiment.

## Source basis

- `notes/CC_SIX_SEVEN_TRANSFER_2026_09_29.md`
- `notes/CC_BOUNDED_SELECTOR_2026_09_29.md`
- `notes/CC_REPRESENTATION_RULES.md`

Pinned Lonely Runner branch head at protocol design: `f2126bfe929aae4eda77b4ea3418a4c38b47f0f5`.

## Next step

Before execution, independently review whether q=10 gives a sufficiently nontrivial distinction between Q4 and Q5. If not, choose a second fixed system **before** calculating the adequacy matrix.

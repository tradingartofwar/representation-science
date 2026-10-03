# RR-LR-002 — Positive-width summaries can erase existence

**Date:** 2026-10-03  
**Laboratory:** Lonely Runner  
**Status:** OBSERVED / REPRODUCED finite example

## Underlying system / reality

A fresh rank-three test case from the orbit-interval study:

(p,q,r) = (1,4,13)

at the closed 1/8 safety threshold.

## Question

If a representation preserves all positive-width safe components but drops isolated points, does it still preserve the answer to the existence question?

## Representation tested

The safe core represented only by positive-width interval components.

## Information retained

Every safe component with nonzero duration.

## Information omitted

Zero-width closed components: isolated equality times.

## Failure

For (1,4,13), the entire 1/8-safe set is

{1/8, 3/8, 5/8, 7/8}.

There is no positive-width safe interval.

A positive-width-only representation therefore reports no solution even though four exact physical witnesses exist.

In the fresh 1,197-case orbit-interval test:

- complete components including isolated points covered 1,197/1,197;
- positive-width components covered 1,196/1,197.

This case is the unique fresh loss under that compression.

## Consequential distinction

> **Measure-zero does not mean consequence-zero.**

For an existence question at a closed threshold, isolated equality points can carry the entire answer.

## Enrichment that repairs the failure

Represent the complete closed safe set as both:

- labelled intervals; and
- isolated points.

Keep endpoint closure explicit.

## Adequacy claim

Positive-width-only compression is inadequate for closed-threshold existence in this case.

The richer interval-plus-point representation preserved the tested finite domain.

## Representation cost

The added cost is small in this example—four singleton components—but the general cost of preserving all lower-dimensional boundary structure is not yet characterized.

## Future questions

When can lower-dimensional or zero-measure structure be safely discarded?

Does the answer depend on the requested output: existence, duration, optimum, robustness, or complete-set recovery?

## Source pointers

Pinned laboratory branch head at extraction: `f2126bfe929aae4eda77b4ea3418a4c38b47f0f5`

Source file: `notes/CC_ORBIT_INTERVALS_2026_10_02.md`  
Source blob: `5b33ceb3f1026cdc1673d8d459caaccb8dbf9511`

Repository: https://github.com/tradingartofwar/the-lonely-runner-conjecture

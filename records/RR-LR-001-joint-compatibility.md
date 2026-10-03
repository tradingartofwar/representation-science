# RR-LR-001 — Marginal feasibility is not joint compatibility

**Date:** 2026-10-03  
**Laboratory:** Lonely Runner  
**Status:** REPRODUCED from pinned source analysis

## Underlying system / reality

A fixed A-ray six-to-seven runner transfer at q=4, threshold z=1/8, using parent cell P2 and the added seventh form S=5x+2y.

## Question

Can separate feasible ranges for the orbit condition H_4=4x-y and the added-runner phase S establish that a valid physical witness exists?

## Representation tested

Two marginal intervals:

- H_4 in [5/8, 11/8]
- S in [23/12, 17/8]

The first contains integer 1. The second reaches the safe-band endpoint 17/8.

## Information retained

Each scalar range separately records values attained somewhere in the same parent section.

## Information omitted

The relation tying H and S to the **same point** (x,y).

## Failure

Treating the two marginal facts as jointly feasible creates a false positive.

On the actual H_4=1 slice, the conditional S interval is

[109/56, 33/16],

which lies strictly between the adjacent safe bands around integer 2. No compatible point exists on that slice.

The only child point in this parent is (3/8,1/8,1/8), and there H_4=11/8, not an integer.

## Consequential distinction

> **Individual feasibility of projected quantities is weaker than coexistence at one physical state.**

The missing object is not another scalar bound. It is the joint relation.

## Enrichment that repairs the failure

Retain the conditional interval

J_(m,h)(z) = {5x+2y : (x,y,z) lies in parent P_m and qx-y=h}.

A witness survives exactly when this same-slice interval intersects a valid seventh-runner safe band. The inverse map then recovers x, y, time, and laps.

## Adequacy claim

Separate marginal ranges are inadequate for the existence question in this case.

Conditional same-slice intervals are sufficient for exact transfer within the fixed forms described by the source.

## Representation cost

Not reduced to a single scalar. Cost increases from two marginal intervals to labelled conditional intervals indexed by parent and integer orbit slice. No general complexity claim is made.

## Future questions

This record motivates tests of when a joint image can be safely compressed and when factorization destroys coexistence information.

## Source pointers

Pinned laboratory branch head at extraction: `f2126bfe929aae4eda77b4ea3418a4c38b47f0f5`

Source file: `notes/CC_SIX_SEVEN_TRANSFER_2026_09_29.md`  
Source blob: `a2a29b02380b25c95995931b67d1f78ce415f0ab`

Repository: https://github.com/tradingartofwar/the-lonely-runner-conjecture

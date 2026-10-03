# EXP-001 — pre-execution audit

**Date:** 2026-10-03  
**Research baseline:** `5772b7c2e5a83b245883f4c5d503e0a138b082d0`  
**Laboratory source:** `f2126bfe929aae4eda77b4ea3418a4c38b47f0f5`  
**Disposition:** retain q=10; freeze an executable operational contract before scoring the matrix.  
**Execution status:** preflight calculations completed; no final question × representation matrix executed. The original protocol is unchanged.

## 1. Finding

**REPRODUCED:** q=10 has substantial geometry separating Q4 from Q5. Its eight global maximizing times form a proper subset of a safe set with ten positive-length closed intervals and four isolated points. Two whole interval components contain no global maximizer. A second physical system is unnecessary for this distinction.

**OBSERVED (protocol audit):** the original six candidate descriptions do not yet fix a reproducible comparison. They mix stored answers, restricted witness supports, descriptions from which fuller geometry can be reconstructed, and construction algorithms. Recovery privileges and the exact Q6 output are not fixed. In particular, the original ladder does not establish that any one row will answer Q4 but fail Q5.

**DISPROVEN (specific interpretation):** “the q=10 point at t=17/35 is not on an old parent edge, therefore it is irrecoverably absent from a record of all labelled parent edges.” It is absent from the edge support but exactly recoverable from the convex hull of those retained vertices. Section 4 supplies the exact identity.

This is a reason to clarify the experiment before execution, not to replace an inconvenient physical case or repair a scored outcome.

## 2. State reconstructed from the repositories

The founding Representation Science tree contains fourteen text files: the README, current state, program, record contract, origin, collaborator instructions, four founding records, two indexes, laboratory README, and EXP-001 protocol. All were read at the research baseline. There is no experiment result, runner, serialized candidate payload, or completed adequacy matrix in that tree.

The research program already warns against treating the question list as a linear hierarchy, equating participant count with independent rank, or claiming minimum sufficient representations without a specified comparison. Those cautions must reach the experimental implementation.

The pinned Lonely Runner evidence is on its research line; the source notes identify `research/near-doubling-overlap-2026-09-24` as the active line. Sources here are fetched by commit, not assumed to equal the current default branch. All four recorded source-blob identities match the fetched files. The two transfer controls and selector source are also pinned in [the source ledger](EXP-001-audit-sources.json).

| Founding record | Evidence inspected | Audit scope |
| --- | --- | --- |
| RR-LR-001 | Transfer note and saved exact certificate | Conditional S range and rejection reproduced; separate marginals do not preserve the common point. |
| RR-LR-002 | Orbit-interval note and run summary | Full isolated-only safe set for (1,4,13) reproduced directly. The 1,197/1,196 counts reconciled with the stored summary, not rerun. |
| RR-LR-003 | Sheet-coverage note, run summary, orbit recovery note | Physical t=25/152 reproduced; speed 40 blocks the three reported inherited contact times. Exhaustiveness of the 36-sheet contact reduction remains inherited source evidence, not newly rerun here. |
| RR-LR-004 | Three-parameter note and stored summary | 89/89 training, 310/318 holdout and 407/407 full-class counts reconciled. Full historical experiment not rerun; rank-causality limitation below. |

The 873-line representation rules were read, including the distinction between source exhaustion and a budget stop, between source recovery and losslessness, and between fixed-instance orbit dimension and family rank. The laboratory's October 2 value review and consequential-compression inquiry were also inspected. Their broader ideas remain hypotheses, and their reported conventional-baseline/null evidence remains relevant. EXP-001 is not evidence of CC superiority.

## 3. Independent physical preflight

Define d(t)=min_v ||v t|| for moving speeds v=(1,10,11,12,13,23,25). Common start, stationary reference, circumference one, closed threshold 1/8. Results below use the unit interval; 0 and 1 are unsafe, so using [0,1) rather than [0,1] changes no listed set. Other times follow by integer shifts.

The new [preflight script](exp001_audit.py) imports no laboratory implementation. It computes complete threshold sets by both iterative closed-band intersection and a distinct event decomposition. The latter checks all threshold events and one rational representative of every intervening cell, where truth cannot change. This is an exhaustive finite decomposition, not sampling for approximate evidence.

It computes the optimum using all tent breakpoints and pairwise affine crossings on each tent-linear cell. Nonzero slopes rule out positive-width constant maxima. Complete superlevel sets at the computed optimum are checked by both set methods. Only after calculation are results compared against the pinned transfer certificate and its separately structured historical countercheck. The geometry and all exact outputs agree.

These are newly written, independently structured calculations by the same AI audit author, not independent human or formal proof review. The source conclusions were known before the code was written. This is reproduction, not blinded discovery.

### Q3 and Q4

**REPRODUCED:** maximum d(t)=1/7, attained exactly at

{1/7, 2/7, 3/7, 17/35, 18/35, 4/7, 5/7, 6/7}.

### Q5

**REPRODUCED:** the following seven components, together with their reflections t→1−t, are the complete 1/8-safe set:

| First-half component (closed) | Global maximizer in it |
| --- | --- |
| {1/8} | none |
| [25/184, 15/104] | 1/7 |
| [57/200, 23/80] | 2/7 |
| {3/8} | none |
| [41/96, 79/184] | 3/7 |
| [49/104, 87/184] | none |
| [97/200, 39/80] | 17/35 |

Thus Q5 requires all interval interiors and endpoints, four isolated nonmaximizing times, and two entire interval components invisible to a list of global optimizers. For example t=17/36 lies strictly inside the sixth component and has d(t)=5/36, strictly between 1/8 and 1/7. An optimizer list is not even a list of all safe components' locations.

No singleton is a global maximizer. At q=4 in the archived control, in contrast, the threshold equals the optimum and Q4 and Q5 coincide. That known case would weaken this particular discrimination; there is no reason to substitute it.

### Parent and selected-witness controls

**REPRODUCED:** deleting speed 25 gives optimum 4/25 at exactly 8/25 and 17/25. The restored runner has phase zero at both. The parent safe set has eighteen components: fourteen positive intervals and four singletons. It shrinks to fourteen components after addition.

The pinned two-segment rule returns t=15/104 at q=10, with minimum separation exactly 1/8. It is a valid safe endpoint, not a global optimizer. In moving-speed order its laps are (0,1,1,1,1,3,3) and phases are

(15/104, 23/52, 61/104, 19/26, 7/8, 33/104, 63/104).

These are development controls already exposed by the protocol/source, not fresh validation outcomes.

## 4. Retained support is not the same as retained information

### R4: the one-skeleton can encode the entire convex parent

The source parents are labelled tetrahedra. Retaining every labelled edge retains every vertex, grouped by parent. Under the declared convex-polytope interpretation the full parent is the convex hull of those vertices. The reconstruction requires computation, but no external source information.

For P7, order the source vertices as

- V0=(11/24,7/8,1/8);
- V1=(1/2,13/16,1/8);
- V2=(1/2,5/6,1/6);
- V3=(1/2,7/8,1/8).

The exact identity checked by the preflight is

(17/35,6/7,1/7) = (12/35)V0 + 0V1 + (3/7)V2 + (8/35)V3.

Three weights are strictly positive. Only the old parent band y+z=1 is active there; the floor and fold are strict. This confirms the source's two-dimensional-face finding. The added band 5x+2y−z=4 supplies the new contact.

Consequently these are different experiments:

1. Search only the geometric union of retained old edges. The known point is outside that support.
2. Reconstruct each convex parent from retained edge endpoints, then cut it and query it. The point is recoverable internally.

The original R4 wording retains “labelled parent edges and surviving edge points”; it does not prohibit convex reconstruction. It cannot receive an information-loss verdict merely from the support counterexample. Conversely, retaining only the clipped surviving fragments would be a different payload and might genuinely lose original vertices. Name and freeze which payload is used.

### R3 and Q2: a compact certificate can reveal the generator

R3 retains all seven affine phase forms and the q-dependent recovery map. These describe the original physical constraints. A general decoder allowed to use them can reconstruct the exact physical problem and solve other queries at extra cost.

More sharply, the exact output requested by Q2 already reconstructs each moving speed:

v_i = (lap_i + phase_i) / t, for the returned nonzero time t.

The preflight checks that this identity recovers (1,10,11,12,13,23,25) from the output above. No outside lookup is needed. This uses the common-start, constant-speed assumptions; a phase without its lap would not suffice.

Thus the assertion that Q2's full output irreversibly discards the information needed for Q4/Q5 is **DISPROVEN for this contract**. It does not make those answers cheap, directly materialized, or obtainable by the pinned bounded selector. “The selector does not return every maximizer” remains correct.

This distinction is consequential before execution: a limitation of a query algorithm cannot silently become a lower bound on information in its input or output.

## 5. Candidate-by-candidate contract audit (not adequacy scores)

| Row | Unresolved or unfair comparison | Required clarification |
| --- | --- | --- |
| R1: scalar optimum | Which system's optimum? A trusted answer has already incurred optimization and proof costs. | Separate child and parent versions; record construction/provenance and whether the scalar is trusted input or must be certified. |
| R2: all old optimizers | Parent-specific answer cache is compared with child-specific answers and family-level geometry. Its known rejection only tests reuse of those points. | State parent epoch, exact payload, allowed new-constraint evaluation, and distinction between answer reuse and reconstruction. |
| R3: two segments | Bounded selector, complete segment support, and all computations from the affine chart are three different capabilities. | Freeze decoder and arithmetic privileges. Charge both construction and query work; do not infer permanent information loss from bounded-selector failure. |
| R4: old one-skeleton | Full labelled endpoints permit internal convex reconstruction; surviving points alone need not. | Separate direct-support search from convex-hull decoding, or explicitly report both operations on the same payload. |
| R5: facets and cuts | Rich three-coordinate geometry is a model over variable separation z and a family of q values. | Specify exact inequalities/labels, floor, q specialization, completeness evidence, internal reconstruction and query algorithm. |
| R6: exact intervals/set | A set at one threshold is not the separation function or a set-construction program. | Distinguish a stored 1/8-superlevel set, a retained distance envelope, and raw speeds plus a construction routine. These have different obligations and costs. |

There is no demonstrated nested information ordering R1<R2<…<R6. A field-count order would not create one. Vertex and facet descriptions may encode the same convex object with different decoding costs; a stored safe set and a stored optimum can preserve different questions.

**Will a listed row pass Q4 and fail Q5? OPEN under the original wording.** R1/R2/R3 do not provide a declared complete child optimizer answer; R4's answer changes with its decoder; the intended richer R5/R6 implementations might support both. The physical case distinguishes the obligations, but this does not force a difference between the six scored rows.

If that specific split is required, a transparent conventional diagnostic is a child **optimum-plus-all-maximizers answer cache**, separate from R2's parent cache. Under a read/filter-only cache decoder it supports the optimizer request but omits the displayed safe intervals and isolated points. Its known answer-aware construction is charged, and the split is a designed control rather than a discovery. It is proposed here, not silently added to the frozen ladder or scored. Changing the physical system would not resolve these decoder ambiguities.

## 6. Questions, transfer, and output grammar

**Q1 and Q2 are not equivalent tasks**, even though a successful Q2 implies a positive Q1. A trusted optimum scalar decides Q1 by comparison with the threshold without producing a time. Any implication uses the scalar's semantics and trust, not just its numeric value.

**Q3 and Q4 need their metadata stated.** A complete maximizer set as a set of times does not itself state the optimum. Evaluating those times requires the objective or a decoder for it. If Q4 returns the optimal value too, it explicitly subsumes Q3.

**Q4 and Q5 are different here**, as shown above. Q5 alone at one threshold does not automatically retain the objective heights necessary for optimization. If the original speeds are available, recomputation may supply them; that must be counted and allowed consistently.

**Q6 is an operation, not one more output granularity.** “Solve” and “required output” are unspecified. Freeze separate Q6→Q1, …, Q6→Q5 obligations, or name exactly one. Keep threshold 1/8 after deletion; changing it to the seven-total-runner threshold 1/7 would change the experiment.

Also distinguish two timelines:

- Build a parent representation, discard other construction state, then introduce speed 25 and query the child.
- Start from a solved child, delete speed 25, solve the parent, then restore the same constraint while retaining previous child answers.

The second permits a cached round-trip answer. It is not evidence of transfer from parent information. Addition uses S_child=S_parent∩B25; deletion generally cannot invert that intersection without retained parent information. The protocol should not conflate these operations.

Adding speed 25 does **not** raise independent parameter rank: 25=2q+5 in the same A-ray model. Each fixed integer system still has a one-dimensional periodic orbit. EXP-001 tests the question/operation axis of the research program; it does not test increasing independent complexity.

Finally freeze what “return the complete set” means. If an unevaluated predicate `all distances >= 1/8` counts as the output, the original speeds already supply a compact symbolic answer. If the goal is a canonical disjoint union of rational closed intervals and singleton points over one period, say so. Likewise specify explicit sorted maximizing times versus an implicit argmax expression, periodic extension, reflection, lap order, and completeness certification. Output grammar changes the obligation.

## 7. Recovery, leakage, and what can be inferred

The protocol names RECOVERABLE but does not assign a specific allowed recovery source or operation to each row. Adequacy and recoverability should be recorded as separate dimensions: direct support, internal decoding, and external source recovery can overlap. Keep the required four display labels if desired, with a precedence rule and reason fields rather than treating them as mutually exclusive mathematical properties.

Before scoring, freeze:

1. The serialized retained payload for each row and its parent/child epoch.
2. Shared public metadata and generic decoder code. If q plus a known family formula yields all speeds, that is generative information. It cannot be treated as harmless metadata while recomputation is silently forbidden.
3. Permitted internal operations, source-opening operations, and budgets. Internal convex reconstruction is different from fetching omitted facets.
4. A pinned recovery source and exact recovery map per row. Source availability alone is not evidence that recovery was executed successfully.
5. A checker that can see physical ground truth without supplying new candidate times, objective values, interval endpoints, or counterexample locations back to a solver during the scored query. Adaptive membership probes are a computational oracle and require their own budget.
6. Fresh isolated query runs. A successful R6 or earlier Q2 must not populate a cache used to answer a different representation's row, nor let Q5 feed earlier questions unless that sequential workload is explicitly the experiment.

Checking safety of listed times proves soundness, not completeness. For Q4, “every returned point is optimal” is weaker than “every optimizer was returned.” For Q5, “every listed interval is safe” is weaker than “no safe component was omitted.” Comparison must include the complete exact reference set or a completeness certificate.

For a single publicly fixed system, an arbitrary decoder could hard-code every correct answer, even with an empty payload. To claim *information-theoretic* insufficiency requires a declared domain/encoding and two admissible underlying states with the same retained encoding but different query answers (or an equivalent formal impossibility argument). The current experiment can instead make bounded, operational claims about specified decoders. It should not call a timeout, an unimplemented operation, or absence of a witness proof of irrecoverable loss. Such outcomes warrant UNKNOWN/resource-limited reasons unless an appropriate counterexample establishes more.

This does not erase the older support-class counterexamples. It identifies exactly which object and which operation those counterexamples defeat.

## 8. Costs and upstream consequences

The original cost dimensions are useful but incomplete for the exposed differences. Retain them separately and add:

| Dimension | Why it matters here |
| --- | --- |
| Integer/rational bit lengths and serialized bytes | One rational field may encode far more than another; bounded arithmetic-operation counts need not be bounded bit cost. |
| Decoder/code and shared metadata size | A short payload can move the full problem into the decoder or public family description. |
| Preprocessing and construction scope | A q-family atlas, a q=10 answer cache, and a parent-only precomputation serve different workloads. |
| Internal reconstruction versus external recovery | R4's hull completion and R3's speed reconstruction need computation, not necessarily new information. |
| Verification and completeness work | Producing one safe point and certifying an exhaustive set have different evidence obligations. |
| Peak working memory/intermediate objects | A compact stored object may expand into rich geometry at query time. |
| Output encoding and materialization size | A predicate, a union of intervals and an exhaustive point list are different output contracts. |
| Queries served/amortization and source dependency | Up-front cost and repeated-query cost cannot be compared without a workload; optionality may depend on a reachable source. |

These are reporting requirements or hypotheses for later tests, not measured benefits from this audit. No single combined cost score, representation lower bound, human cognitive result, or generalized efficiency claim is earned.

**HYPOTHESIS for future operational framing:** ask “For this workload and trust model, what is the least costly retained state plus decoder that gives exact answers and checkable evidence, including allowed recovery?” This retains the founding question while making the newly exposed computational and evidential choices explicit. It is a proposal, not a replacement theory or a proved general law.

**OPEN:** whether representation records yield knowledge or practical value beyond competent conventional modeling. This audit produces a sharper experimental contract; it does not establish external usefulness, a recognized field, or novelty.

### RR-LR-004 scope correction

The pinned three-parameter source explicitly says its sheet menu/compiler is a dimensional adaptation, selected on rank-three training data. The four-sheet menu is not an unchanged rank-two menu carried directly into the rank-three holdout. Its eight held-out misses establish a particular rank-three menu's incomplete transfer within that domain. They do not isolate rank increase as the cause relative to a matched rank-two control.

The distinction between participant count, coefficient-family rank, and fixed-instance orbit dimension remains valid and consequential. The causal prediction “higher rank forces a larger adequate representation” remains **OPEN**. The founding record receives this clarification without changing its historical numbers or converting bounded evidence into a theorem.

## 9. Disposition and next concrete work

Retain the q=10 physical system, questions and historical controls. Leave the original frozen protocol intact. Before any matrix run, publish a versioned operational addendum with exact payloads, decoders, output grammars, trust/recovery rules, budgets and the Q6 timeline; commit and read back its manifest. Decide explicitly whether to add the optimizer-cache diagnostic or accept that the original rows may not separate Q4/Q5. Any changed row is an announced pre-execution amendment.

Then run the matrix with per-cell traces and completeness checks. Do not claim minimum information from a decoder restriction. If unconstrained internal reconstruction makes several representations equivalent, preserve that as the result and compare the actual costs.

Laboratory Two remains deferred until EXP-001 is completed and interpreted and a specific transferable method or distinction is ready for an outside test. This audit does not select a second laboratory or expand the physical test domain.

## 10. Reproduction and provenance

From this repository root, with standard-library Python and assertions enabled:

```bash
python experiments/exp001_audit.py --output /tmp/exp001-geometry.json
python experiments/exp001_audit.py --source-root /path/to/pinned-lonely-runner --output /tmp/exp001-audit.json
```

The optional source root must contain the five JSON files pinned in [EXP-001-audit-sources.json](EXP-001-audit-sources.json) at the laboratory commit above. The script verifies their Git blob identities before comparison. See [EXP-001-audit-results.json](EXP-001-audit-results.json) for the replayed source-checked output and script SHA-256. The geometry-only mode omits the `source_comparison` field; the physical results are identical. Python optimization mode is rejected because this checker relies on assertions.

Scope: q=10 parent and child; the two specified founding-record physical controls; the supplied marginal-slice and P7 convex-combination identities. The large 407-, 643-, and 1,197-case experiments were read/reconciled, not rerun. No matrix, new system search, new mathematical family theorem, broader scan, external outreach, or laboratory mutation occurred.

Lonely Runner remains the canonical source of its mathematical evidence. This repository stores the representation audit, a small new reproduction checker and its audit output, not a copy of the historical laboratory archive. AI contributed the reconstruction, code, critique and writing; human/formal independent review remains open.

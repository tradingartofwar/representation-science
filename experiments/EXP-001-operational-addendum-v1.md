# EXP-001 — operational addendum v1

**Designed:** 2026-10-03, after audit `3497ed210d299ea880f8a57b5b5d535f29ce042c`.  
**Status at freeze:** executable protocol, candidate payloads constructed; adequacy matrix not run.  
**Scope:** q=10 exposed development system; no new physical case, hidden test, rank increase or information lower bound.  
**Amendment:** the original conceptual protocol remains unchanged; this addendum resolves its open operational choices before scoring.

## 1. Research object and falsifiable comparison

The unit being tested is **retained payload + declared decoder + question/output contract**. The payload alone is not assigned an intrinsic universal adequacy score.

Run every row under two decoder modes:

- **native:** query the retained answer cache or the declared geometric support directly. R3 keeps the pinned bounded selection procedure for Q1/Q2; stronger queries enumerate its two segment supports. R4 queries only the union of old edges. Full facets and full envelopes carry complete models.
- **internal:** allow the specified exact reconstruction using only that same retained payload. R3 decodes physical speeds from its affine rows and constructs an exact envelope. R4 constructs convex hull facets from grouped vertices, then performs the same complete slice/cut query as R5. Other rows use the same native procedure; an unimplemented inverse remains UNKNOWN, not a mathematical impossibility.

This comparison can refute the operational expectation that a row needs external information to answer a stronger question. It can also expose an output or certificate that a decoder cannot produce. It cannot prove that no possible algorithm could answer from the payload. The case, old controls, eight maximizers, and full safe sets were already known. Designed controls have no discovery or holdout status.

No new physical system is selected: q=10 has sufficient Q4/Q5 geometry. No theory, novelty or efficiency conclusion is precommitted.

## 2. Domain and exact output grammar

Stationary reference, common start, unit circumference, time in [0,1), threshold z=1/8 with equality included. Moving speeds of the physical child remain (1,10,11,12,13,23,25). Rational strings are reduced exact fractions. Integer period extension supplies other physical times; 0 and 1 are unsafe here.

| Question | Required output |
| --- | --- |
| Q1 | Boolean existence, supported by a trusted exact optimum/set or a recovered safe witness. No carrier contact alone cannot prove physical nonexistence. |
| Q2 | One exact time, all seven integer laps and all seven fractional phases in moving-speed order. A time without its required recovery information is not a complete answer. |
| Q3 | Exact global optimum, supported by a trusted complete answer cache or complete model. A restricted-support maximum that happens to match is UNKNOWN without a global certificate. |
| Q4 | Sorted list of all distinct global maximizing times in the unit period. No implicit argmax predicate, duplicates or incomplete optimizer list. |
| Q5 | Sorted disjoint maximal closed rational components [a,b], with [a,a] encoding an isolated point. No unevaluated predicate or partial union. |

No positive-width maximizer plateau occurs in this development case. A plateau encountered by the point-list decoder is an unsupported-shape error that stops the run rather than silently drops its interior.

Q4 does not silently include the value from Q3. Q5 does not silently include the phase/lap map from Q2. Supported questions need not form a linear hierarchy.

## 3. The eight retained payload types

R1–R6 are operational versions of the original six descriptions. **C1 and C2 are added diagnostic controls**, not replacements for an original row. Exact serialized objects are in [payloads.json](exp001/payloads.json); their construction is reproducible from the pinned laboratory certificate with [build.py](exp001/build.py).

| Row | Static-query retained state | Native decoder | Additional internal decoding |
| --- | --- | --- | --- |
| R1 | Trusted child scalar optimum only | Compare to threshold; return scalar. Other queries abstain. | None specified. |
| R2 | Trusted **parent** optimum and all parent optimizers | Filter old optimizing times by the new speed. Retain only that witness support, not other parent times. No child optimizer update rule. | None specified. |
| R3 | Two labelled parent segments, q, six affine rows and physical map | Pinned round-first segment selector for Q1/Q2. Enumerate all integer contacts on those two supports for Q3–Q5; retained heights are 1/8. Clip against the added speed. | Reconstruct all child speeds from rows and added speed, then the exact physical envelope. |
| R4 | All eight grouped convex parents' vertices and edges, labels, q and six rows | Intersect old edge support with integer orbit, then clip by added speed; reflect physical times. | Recover each convex parent's facet inequalities from retained vertices, then slice and cut the full model. |
| R5 | Complete labelled parent inequalities, q, six rows | Substitute y=qt−h, enumerate the finite integer slices, and cut their exact height envelopes by the added speed. | Same complete decoder. |
| R6 | Complete child distance envelope over a unit period, plus ordered speeds for Q2 recovery | Read/evaluate the envelope and return exact threshold components/optimizer data. | Same complete decoder. |
| C1 | Complete child 1/8-safe set, **without** objective heights or a phase/lap map | Set existence and complete-set output; unsupported output fields cause abstention. | No generator inversion is specified. |
| C2 | Trusted child optimum and complete optimizer list, without a phase/lap map | Read Q3/Q4; derive existence. For Q5, expose the stored safe point support, which is to be checked for completeness. | No generator inversion is specified. |

The original R6 phrase “interval/set representation” is resolved in favor of a strong conventional exact envelope representation. C1 separately tests the weaker stored single-threshold set. C2 makes the requested Q4/Q5 distinction inspectable with a conventional answer cache. That distinction is a constructed diagnostic, not evidence that an algorithm discovered a new compression principle.

R4 retains all original edges, not only already clipped fragments; internal hull completion is permitted explicitly. R5's full model and R4's grouped hull semantics inherit the pinned atlas completeness. R3's native support inherits its source safety, not completeness of the full physical safe set. The decoder never promotes support completeness to physical completeness.

### Construction and trust

The atlas, scalar caches, optimizer caches and complete threshold sets are inherited exact development artifacts. Their construction cost is **unmeasured**, not zero. R6's parent and child envelopes are freshly materialized by the builder and its named operations are recorded. This mismatch precludes an end-to-end efficiency ranking.

All cached exact answers are trusted inputs to their decoders, with provenance checked separately by the frozen source pins and independent physical checker. They are not self-contained proof objects. Account for proof/verification work separately from reading such a cache.

R3's segments were chosen historically with the target seventh constraint known. Q6 is a known-target restoration test, not blind generalization to an unseen new runner. The source's two segment constants and labels are copied narrowly with its commit and blob identity; no full laboratory history is duplicated.

## 4. Q6: explicit parent-first restoration workload

Use each row's `transfer` payload. It contains only **parent-epoch** state. The parent retains threshold 1/8 throughout. The source builder first obtains the corresponding parent artifact from the six-runner problem; the query process receives that artifact and the restored speed 25. It never receives a child answer cache from an earlier static query.

Repeat Q1–Q5 as **Q6→Q1 … Q6→Q5** after restoration. R1 receives the parent scalar; R2 and C2 receive the parent optimizer cache; R3–R5 retain their parent geometry/maps; R6 receives the complete parent envelope and six speeds; C1 receives the complete parent 1/8-safe set. New bands are applied exactly to retained geometric/time support.

This operationalizes removal by starting from a separately built parent source. It does not claim that deleting a constraint can reconstruct the parent from a child-only artifact. That inverse/deletion problem is untested. Adding speed 25 is not a new independent parameter. The static comparison already uses parent sources for R2–R5, so their static and restoration capabilities need not differ.

## 5. Information access and isolation

Each retained-only query launches a fresh subprocess in a temporary directory containing only `core.py` and `worker.py`. Its JSON stdin contains one payload, one question, mode, threshold, and added speed. Source URLs, source hashes and row IDs are not passed as an answer lookup channel. The worker reads no repository files and has no checker oracle.

All 160 retained-only outputs (8 rows × 2 workloads × 5 questions × 2 modes) are saved before any grading or recovery. The runner then invokes the separately structured checker. Outputs from other questions or rows never become solver inputs. This is audited process/input separation, not a formal operating-system security proof or model-blinding experiment.

Family formulas and phase maps are charged retained fields for R3–R5. R6 retains ordered speeds explicitly. They may not be used by native decoders to run an undeclared general solver; internal mode exposes the specified additional reconstruction. The actual source is fully known to the investigator, so these are declared procedural constraints, not claims that humans cannot infer the answer.

## 6. Adequacy, evidence and recovery labels

Every row/question/mode reports its attempted exact output or abstention, derivation route, named operations and evidence status:

- **ADEQUATE:** the declared decoder supplies supported output and the independent checker confirms the complete requested answer. For Q2, direct phase/lap checking suffices. For Q4/Q5, complete reference equality is required.
- **INADEQUATE:** this declared decoder/support gives a different answer, an incomplete set with an explicit omitted/extra point, or exhausts its carrier while the physical reference has a witness. This is an operational verdict, not an information-theoretic lower bound or a false physical nonexistence assertion.
- **UNKNOWN:** no declared decoder/certificate supplies the required answer; a correct numeric value lacks global support; or the resource cap is reached. Unsupported does not mean impossible.
- **RECOVERABLE:** recorded separately after a nonadequate retained-only query, if the equally available pinned richer model restores the exact output. The original native/internal verdict remains visible.

For every failing output, the checker emits a specific mismatch. It checks Q5 by exact closed unions; an omitted endpoint or singleton is sufficient to fail. All returned points being safe is not a completeness certificate. A set of correct optimal points is not an exhaustive optimizer answer.

The richer source for **every** row is [recovery_model.json](exp001/recovery_model.json), a narrow extraction of the pinned child speed vector. External recovery is a separate subprocess that constructs the complete physical envelope from those speeds and answers the same question. It is invoked once for a row/workload/question if either retained-only mode is nonadequate. Recovery supplies all constraints, including removed alternatives and maps; charge source bytes and construction/query operations. It supplies no information to the earlier attempts. Maximum 80 recovery queries.

The external source is the same public exact physical model for all rows. This is a local pinned-source replay, not a network latency or remote-source availability measurement.

## 7. Methods, budgets and costs

All arithmetic is rational Python standard-library arithmetic. The native facet method builds conditional physical height envelopes from labelled orbit slices. The internal edge method first constructs hull planes by exact triples and half-space tests. Physical reconstruction uses tent events, pairwise line crossings and exact lower envelopes. C1 addition uses closed interval intersections.

Per query: at most 2,000,000 **named operations**, 100,000 profile pieces in any recorded list, and 30 seconds of subprocess time. Operation counts are explicit loop events (line pair/evaluation, integer contact, inequality, hull triple/side, threshold clip, etc.), not a universal primitive arithmetic cost. No weighted aggregate efficiency score is defined. A budget stop is UNKNOWN. Any unexpected exception, unsupported shape or input hash mismatch stops the whole run; preserve partial state and declare a new version before correcting/re-executing affected work.

Report separately:

- compact serialized payload bytes, numeric field count, total numerator/denominator bit lengths and maximum integer bit length;
- schema-specific object counts, including parent/edge/vertex occurrences, inequalities, profile pieces, threshold components and cached times;
- shared solver/checker code bytes, rather than hiding code as zero-cost metadata;
- fresh construction counts and inherited unmeasured preprocessing;
- named native/internal/external query operations and largest recorded profile list;
- exact output size and source recovery bytes;
- separate reference construction and verification work.

Recorded profile-list size is not total RAM usage. No RSS measurement or runtime superiority claim is planned. Code size is the common executable bundle, not the smallest possible per-row implementation. Labels and generator fields are counted as numeric payload fields; their count is not an information lower bound. Unmeasured costs remain explicit.

## 8. Freeze and verification gates

The [manifest](exp001/MANIFEST.json) pins this addendum, all implementation files, config, serialized payloads, construction record, recovery source and the earlier exact audit checker. Builder construction may run before freezing because payloads must exist to be reviewed. It does not score the matrix. Syntax checks and six synthetic contract tests use speeds (1,2), a synthetic tetrahedron, omitted-point/completeness cases and budget stops; they do not invoke q=10 matrix cells.

Commit this package and read back every pinned file before running `run.py`. All resulting output files must reproduce byte for byte under the same freeze commit. The checker imports the pinned earlier audit algorithms, not `core.py`: iterative band intersection, independent threshold-event decomposition, and exact tent crossing optimization. No new mathematical proof or independent human review is claimed.

The runner saves retained-only responses before grading. It stops on unhandled errors and writes an execution failure record; a correction may not be silently incorporated into v1. Original protocol, audit and failed runs remain preserved.

## 9. Interpretation and stopping rule

Compare direct and internal modes before claiming representation enrichment was necessary. If reconstruction recovers answers without new source input, record that result even if it weakens the original “more retained detail” framing. If the static optimizer cache supports Q4 but loses Q5, record it as the designed control it is. If stored safe-set information supports Q5 but cannot emit Q2's requested metadata under the decoder, preserve that nonhierarchy.

Finish after the declared comparison, source recovery, deterministic reproduction, and interpretation. No broader q scan, fresh second system, rank experiment or framework tuning is authorized by this protocol. Return explicitly to the Laboratory Two trigger in current state, identifying a transferable method or deliberately deferring selection with a concrete next condition.

Claim labels remain KNOWN, REPRODUCED, OBSERVED, HYPOTHESIS, OPEN and DISPROVEN as earned; cell verdicts are not substitutes for these research statuses. Representation Science remains an experimental research program, not a claimed recognized field. The comparative value of its method outside this laboratory remains OPEN.

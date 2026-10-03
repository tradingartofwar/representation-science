# Laboratory Two — bounded transfer design v0.1

**Date:** 2026-10-03  
**Design ID:** DESIGN-LAB2-001  
**Research baseline:** `e730d249d87429e81fcb460e275f47dffec6df14`  
**Concurrent-note reconciliation:** `cabec60225ff02453dde212c686953fbe035120e`  
**State:** PRE-SELECTION DESIGN — no laboratory, domain, task, dataset, implementation or experiment selected. No transfer trial has run.  
**Claim status:** HYPOTHESIS for the proposed benefit; OPEN for external validity and incremental usefulness.

This document establishes qualification requirements and a bounded experimental structure. It is not a frozen executable experiment. Candidate-specific blanks must be resolved and a separate execution manifest committed before testing. Changing these pre-selection requirements requires a visible version change; they must not be changed after a result to admit a favored candidate.

## 1. What is being transferred

The transferable method candidate from [EXP-001](../../experiments/EXP-001-results-2026-10-03.md) is a way to test a declared **payload + decoder + requested output + evidence/recovery contract**:

1. identify exactly what information is retained and what output is required;
2. test direct use and completeness, not just the correctness of returned examples;
3. test reconstruction from the same retained state before declaring information lost;
4. test explicitly permitted external recovery separately;
5. account for generator descriptions, code, construction, verification and output costs;
6. record which distinction changes an answer or an operational decision.

No particular CC representation, geometry, six-question ladder, runner analogy or rank-growth law is required. The domain must supply its own meaningful question. Independent rank is an optional variable only if the selected task gives it an operational definition and a controlled comparison; it is not inferred from record count.

Two propositions must remain separate:

| Proposition | What would test it |
| --- | --- |
| **H1 — cross-domain conformance:** the method can identify and correctly check a consequential adequacy distinction outside Lonely Runner. | A real task, a frozen output contract, a reproducible diagnosis and an independently checkable answer. |
| **H2 — incremental usefulness:** applying the method changes a consequential result compared with competent conventional work at declared cost. | A paired comparison against a strong ordinary baseline, with the consequence and cost threshold specified before evaluation. |

H1 can hold while H2 remains unsupported or fails. A well-documented success in both arms is a comparative null, not evidence that the method produced an advantage. Existing mathematical or engineering methods may already handle the distinction adequately.

## 2. Qualification gates

Each candidate is documented using the [qualification packet](CANDIDATE_QUALIFICATION_TEMPLATE.md). All gates need evidence. Use **PASS**, **OPEN**, or **FAIL** as administrative dispositions, separate from scientific claim statuses. An OPEN required gate blocks selection for execution; it is not an experiment failure. Do not combine gates into a weighted score.

| Gate | Required evidence | Disqualifying or unresolved condition |
| --- | --- | --- |
| G1 — external task | A concrete task whose purpose exists independently of demonstrating Representation Science, with an identified consumer role and an evidenced use for the answer. | A renamed runner problem, an invented need, or a demonstration with no actual question beyond making the method look useful. |
| G2 — consequence | A specific output difference that could change a stated decision, correctness obligation, accepted artifact, source-access requirement or resource commitment. The tolerance/materiality rule is set without consulting comparative results. | Cosmetic notation, shorter prose, more checkboxes, or extra metadata nobody's declared operation requires. |
| G3 — bounded domain | Pinned raw inputs, versions, assumptions, units/identity conventions, finite scope and one primary question/transition. Enumeration or another checkable reduction covers the requested output. | Unbounded scope, silently changing source state, or no justified way to check completeness. |
| G4 — ground truth | A reference derived from the authoritative raw source, a separate verification route, documented shared assumptions and a resolution procedure for disagreement. | The compressed payload supplies its own answer key; agreement between two wrappers of the same procedure is the only check; or unresolved ambiguity changes the primary answer. |
| G5 — competent comparator | An ordinary direct/generative or native-domain solution appropriate to the task, operating under the same output, trust, information and resource obligations. | A deliberately incomplete API call, crippled checklist, obsolete straw baseline or free preprocessing allowed only to the proposed method. |
| G6 — observable attribution | Retained data, decoder code, metadata, source reads, outputs and checks can be inspected; internal reconstruction is distinguishable from new information access. | Hidden answer tables, unlogged source access, or a method whose decisive mechanism cannot be reconstructed. |
| G7 — feasible bounded evaluation | A deterministic selection/exposure plan, achievable shared resource limits, development checks and fixed stop rules. Ordinary baseline feasibility is demonstrated on development cases. | Budgets chosen to cause the baseline to fail, tuning on evaluation results, or an implementation scope that cannot fit the bounded pilot. |
| G8 — reproducible public evidence | Permission/provenance and an artifact plan sufficient for another capable investigator to reconstruct the primary claims in this public repository. | Private operational facts or restricted data needed to verify the primary claim cannot be published or replaced by a faithful, authorized public instance. |

Do **not** require a baseline failure, a suspected compression defect, or expected method superiority to qualify. Such selection would favor positive results. A candidate may qualify and yield no adequacy loss or no incremental benefit.

Public availability alone does not establish G1 or G2. Conversely, an authentic problem alone does not establish G3 or G4. If no candidate meets the gates, keep Laboratory Two unselected and document the missing condition rather than inventing an easier task.

## 3. What counts as ground truth

### 3.1 Two levels of truth

Separate **correctness relative to the pinned source and rules** from **whether those sources and rules faithfully answer the external question**. Exact agreement on a dataset does not establish that the dataset exhausts the real world. A perfect decoder cannot repair an unobserved source error without additional evidence.

The qualification packet must state:

- the authoritative raw source, snapshot/version, acquisition procedure and provenance;
- which real task that source can answer and which claims about reality it cannot support;
- the exact query semantics, output schema, identity/equivalence rules, endpoint/null/tie conventions where applicable;
- a completeness argument for the finite requested domain, not just checks of a few returned items;
- known source uncertainty and what would invalidate or narrow the claim.

For the first bounded transfer, the primary output must admit an exact or otherwise prospectively specified, independently checkable acceptance rule. If a numerical tolerance is necessary, specify its source, error bounds and decision behavior at the boundary before evaluation. A vague expert impression is not an adequate primary truth criterion. A narrowly checkable part of a larger task qualifies only if that part has its own genuine consequence; it must not silently replace the consumer's question.

### 3.2 Reference and countercheck

The primary reference reads raw source state, never a candidate's compressed representation. Check it by a differently structured implementation, exhaustive finite construction, auditable derivation, or independently maintained authoritative result whose assumptions can be inspected. One high-quality certificate may be more useful than two nearly identical programs; document the specific independence obtained.

Record independence along separate axes: source data, parser, algorithm/representation, implementation, author and verification premises. Shared raw facts are expected; shared decoding errors are a risk to be tested. Same-author alternate code is not independent human review. Two AI responses agreeing do not establish truth.

Development checks include a positive control and a relevant error/boundary control that the checker must distinguish. Deliberate corruptions validate the checker; they are not real baseline defects or evidence of practical transfer benefit.

If reference and countercheck disagree on a primary result, preserve both, stop grading that primary comparison and resolve the cause without treating either arm as a winner. Scope changes or oracle corrections are versioned; affected outcomes remain marked unassessable until the corrected reference is frozen. No retroactive quiet regrading.

### 3.3 Prevent answer leakage

Freeze or independently generate reference answers without feeding them to the candidate decoders. Seal outputs from both primary arms before comparative grading. The reference may check a proposed answer after sealing; it may not supply additional witnesses, missing records or search hints during a retained-state query unless an identical, logged oracle privilege is explicitly part of both contracts.

## 4. Conventional baseline and comparison arms

There are at most **two primary arms**:

- **B — competent conventional workflow.** Use ordinary domain methods with all appropriate documentation, exact semantics, ordinary validation, versioning and recovery. Prefer the simplest reliable direct method, including the raw source plus a standard decoder when practical. A real existing workflow may inform B, but a known weakness in that workflow is not a substitute for this strong comparator.
- **T — the same task with the representation-adequacy method explicitly applied.** Document which payload/decoder/recovery decision the method changes and why. T may use the same conventional algorithms as B. No CC implementation is required.

The method is an intervention in analysis/design, not necessarily a separate algorithm. Preserve a baseline record before method-specific diagnosis of evaluation cases, then record T's proposed changes before evaluation. If the same investigator designs both after knowing all mechanisms, label that exposure: the trial can compare artifacts, but it cannot establish that the method caused an independent analyst's discovery or saved human effort.

Both arms receive the same task brief, source snapshot, development examples, output grammar, tolerances, evidence standard, recovery permissions and resource ceilings. Both may reconstruct from retained information and use competent source recovery. Neither is required to make the same representation choices or consume its full budget. Actual construction/query/recovery costs are recorded.

The baseline may already perform all the proposed checks. Preserve that possibility. Extra documentation or fields in T do not justify a stronger output requirement for B. If an established ordinary procedure addresses the issue equally well, report no observed incremental value.

Require a **generative baseline check**: could the original source or a short exact generator, together with an ordinary decoder, supply the outputs at acceptable cost? If so, include it in B's design assessment and record its costs. Do not call a precomputed representation “smaller” merely by counting its visible objects while omitting generator or program size. If that baseline is infeasible or inapplicable, explain why with evidence; do not equate “not implemented” with impossibility.

Ordinarily correctable baseline implementation defects exposed during development are repaired before freeze. A representation's inherent limit is recorded, not erased or assumed repairable. A defect discovered after freeze is preserved and diagnosed; a fair rerun of a corrected baseline needs a new version. One implementation bug establishes a defect in that artifact, not the general superiority of the research method.

## 5. Payload / decoder / output / recovery contract

Complete one versioned contract for each arm and source epoch. A pointer, URL, common formula, identifier, language runtime or shared cache can carry consequential information; it belongs in the access/code inventory.

Distinguish the active payload from any larger retained store it can navigate. If that store is part of frozen shared state, count its storage and retrieval work; if only the pointer is retained, reading its target is a separate access privilege. Physical remoteness alone does not decide whether an operation is internal reconstruction or external recovery: the declared information boundary does. Reachability under a budget and possession of information are separate obligations. This is an accounting requirement, not a claim about human memory.

| Contract element | Required specification |
| --- | --- |
| Underlying source and scope | Exact source versions, task assumptions, valid input domain and source epoch. |
| Encoder/construction | Raw inputs read, executable transformation, preprocessing and learned parameters, construction cost and output hash. |
| Retained payload | Exact serialized fields/objects, semantics, labels, completeness claims, bit/byte counts, and declared omissions. |
| Shared state | Decoder/runtime code, public metadata, schemas, caches, prior outputs, embedded generators and external dependencies. |
| Requested output | Full machine-checkable output schema, equivalence rule, completeness requirement and evidence/trust obligation. |
| Decoder | Allowed operations and implementation version. A procedure restricted to a support is named as such; it is not all possible decoding from the data. |
| Internal reconstruction | Transformations using only frozen retained/shared state; phase boundary, intermediate state and costs logged. |
| External recovery | Pinned source/version, exactly what is newly read, trigger, recovery map, checks and cost. Access privilege is identical across arms. |
| Update/transition | State before and after, what is removed, retained or refreshed, and what information about the future request was available when constructing the payload. |
| Verification | Reference identity, checker independence, confidence/certificate semantics and pass/abstain/failure rules. |
| Resource envelope | Shared construction and query ceilings, access/compute budgets, measurement method and exceeded-budget behavior. |

One primary transition is selected later, not here: either a changed question on fixed raw state **or** a changed input/constraint with the primary question fixed. Do not change both and attribute the effect to one. There may be two output obligations tied to that transition, but they come from the actual task, not a copied Lonely Runner ladder.

Separate three permission stages without assuming they always change capability:

1. direct operation on the retained object;
2. declared internal reconstruction with no new source access;
3. declared external recovery.

Use isolated attempts or explicitly frozen sequential histories. A result generated at a richer stage cannot leak into an earlier attempt. For an update task, cached answers from an old source epoch and newly derived answers must be distinguishable. The lifecycle of information is part of the contract, not incidental implementation detail.

Also freeze the **recovery trigger**: what can the system detect before seeing the answer key that justifies reopening a source? A recovery manually requested after the grader identifies the miss demonstrates recovery availability only. It does not demonstrate autonomous detection, a useful production policy, or that an expensive source read would have been avoided in practice. If adaptive recovery is the claimed benefit, the trigger and its false alarms/missed triggers must be evaluated.

## 6. Failure attribution and evidence

Record answer correctness, completeness, justification, operational status and recovery separately. Preserve ADEQUATE, INADEQUATE, UNKNOWN and RECOVERABLE as EXP-001-compatible display verdicts, with reason codes. Do not erase a wrong initial answer because later recovery succeeded.

| Observation | Permitted conclusion |
| --- | --- |
| Valid examples, omitted required alternatives | Incomplete output for the declared question. |
| Correct value, absent required global/completeness support | Correct value with unmet justification; UNKNOWN for certified adequacy. |
| No implemented decoder, timeout, unavailable recovery or exhausted restricted support | A procedure/resource/source-access limitation; not automatically physical nonexistence or irreversible information loss. |
| Same retained bytes, correct output after internal reconstruction | Information was sufficient for that tested reconstruction; extra external retention was not necessary for this result. |
| Correct output only after a logged source read | Recovery works under the declared privilege; genuine irrecoverability from the earlier payload is still a separate claim. |
| Admissible states share the complete retained encoding and allowed side information, but have no common acceptable output | A collision witness establishes that no uniform exact decoder using only that information can always satisfy that output contract on that domain. |

The collision test includes decoder version, common metadata and all permitted side channels. For one-witness or other multiple-valid-output tasks, a pair must have **disjoint acceptable-output sets**; merely having different sets of valid witnesses is insufficient if one witness works for both. More generally, an indistinguishable class with no common acceptable output suffices, even when each pair overlaps. A pair is a convenient sufficient witness, not a required form of every impossibility proof. For approximate or probabilistic outputs, an exact collision argument must match their acceptance rule before an impossibility claim is made. This design makes no probabilistic lower-bound claim.

An external recovery source may disambiguate a collision; its read is new information and must be counted. A protocol that forbids reconstruction can test that restriction, but cannot make encoded information disappear by definition.

## 7. Bounded execution structure

The present work is design only. It does not populate candidate packets, search for a favorable domain, select a laboratory or execute any of the following phases.

1. **Qualification:** after a later instruction to consider candidates, evaluate at most three evidence packets under the gates. Record rejected and unresolved packets; do not choose on comparative outcome. No candidate is assumed to exist today.
2. **Development:** for a selected task, use at most three declared episodes to implement/validate B, T and the truth checker. Freeze known exposure and fixes. A development success is not validation.
3. **Evaluation freeze:** commit the domain selection rule, case identities or sealed deterministic generation rule, B/T artifacts, reference procedure, exact counts, consequence rule, budgets and manifest. Read back the freeze before scored execution.
4. **Evaluation:** at most six task episodes, each with one predeclared transition or at most two related requests/states; at most two primary arms and three permission stages. This yields at most **72 scored decoder invocations**, plus at most 72 deterministic replays. Cases and denominators are specified before results; repeated modes on the same episode are not independent cases.
5. **Interpretation and stop:** one result package, one exact reproduction, and a scope-limited conclusion. Stop at the bound. No automatic wider scan, method refit, domain replacement or extra run to rescue a null.

These counts are inspectability caps, not a power calculation. A smaller complete finite task may qualify; no universal or population success rate follows from a small pilot. A task requiring more cases must motivate a prospective design revision rather than exceed the cap silently.

Evaluation cases are selected by a prospective rule independent of B/T outcomes: for example, a specified exhaustive bounded task population or a provenance-defined acquisition window. The actual rule is chosen with the task and frozen before viewing comparative performance. Include successes, ties and unsupported cases; do not filter on method wins. Newly written cases after known failures are development or designed stress controls, not hidden validation.

The default per-invocation guardrail is **60 seconds** in the declared execution environment. Shared construction, memory and source-access ceilings must be assigned numeric values from the qualified task before execution; they remain intentionally unresolved in this pre-selection design. Baseline development must show these limits support normal task execution. If the task cannot fit the default, revise the design before evaluation and explain the real constraint; a timeout never becomes an information-loss verdict.

The primary first-pilot comparison is deterministic artifact/task performance. A causal human-productivity study, nondeterministic model-performance claim or runtime-generalization claim needs an additional frozen allocation/replication plan and is outside this cap as written. Byte-identical replay is required for deterministic outputs; a declared canonical equivalence check may be used for irrelevant serialization differences. Relevant discrepancies stop the claim and remain in the record.

Unexpected exceptions, manifest mismatches, unplanned source changes, unresolved reference conflicts or undeclared accesses stop the affected execution. Preserve outputs and reason; fixes require a versioned amendment and a fresh evaluation/exposure designation. Routine baseline loss, a null result or an unsupported method query is an outcome, not a reason to redesign.

## 8. Consequential transfer outcome rules

Each selected task must define a consequence map **before evaluation**: which verified output differences change the actual decision, accepted deliverable, independently checkable knowledge or binding resource constraint? Define the smallest material difference and why it matters. Do not invent utility weights or money saved without evidence from the task.

| Outcome | Required evidence | Claim ceiling |
| --- | --- | --- |
| **Conformance transfer** | The contract is executable outside Lonely Runner; the method produces a reproducible, correctly attributed adequacy diagnosis and a verified output. | H1 supported on that task; H2 still open. |
| **Consequential diagnostic result** | A predeclared material distinction changes the supported answer/action or a justified source/reconstruction choice; reference checks and a minimal counterexample or trace explain it. | A useful bounded diagnosis, including when B finds it too; not necessarily an advantage attributable to the method. |
| **Comparative consequential benefit** | On the frozen common task, T resolves a material obligation B does not, or meets a task-derived cost threshold with equally correct, complete and justified output. No undeclared extra input or easier task; no disqualifying regressions under the predeclared acceptance rule. | Evidence for H2 for the inspected episodes/implementations and actual cost model only. |
| **Comparative null** | B and T support the same material decisions within task-relevant costs, even if T uses different language or longer records. | No observed incremental benefit; retain useful artifacts without declaring superiority. |
| **Negative transfer** | T loses valid alternatives, adds an incorrect claim, wastes consequential resources or impairs recovery relative to B. | Failure or limitation of the tested method/application; preserve the exact failure. |
| **Unassessable / stopped** | Truth, provenance, permissions, output semantics or execution limits do not support a valid comparison. | No verdict for or against the transfer hypotheses. |

At least one case-level material difference with checkable causal mechanism is needed for a consequential claim; aggregate pass counts alone are insufficient. A local improvement accompanied by regressions remains a mixed result unless a task-supplied acceptance rule resolves the tradeoff. A correct abstention can avoid an unsupported decision, but it does not satisfy a task that requires a completed answer; report both resolution and warranted abstention.

An offline replay supports “would change the recorded decision under these rules,” not “prevented a real-world loss.” Realized savings, adoption or avoided harm require their own observations. No live operational changes, external messages or deployment are part of this design.

Timing/storage advantages count only when their measurement and materiality threshold were frozen and all relevant construction, source, code, verification and output costs are included or explicitly scoped out. Raw small payloads are allowed to beat elaborate representations. Report vectors of costs; no invented universal score. If a practical cost claim cannot be fairly measured, leave H2's efficiency branch OPEN.

## 9. Research trail and required packet

The future execution package must preserve:

- the approved qualification packet and evidence for each gate;
- the actual task/output/consequence statement and source manifest;
- baseline selection rationale, development exposure, known defects and repairs;
- B/T encoder, payload, decoder, evidence and recovery contracts with hashes;
- raw and canonical outputs, access/trigger logs, time/resource outcomes and counterexamples;
- separately structured reference checks, conflicts and completeness evidence;
- per-episode comparisons, cost dimensions, failures, unknowns and reproduction commands;
- a result statement using KNOWN / REPRODUCED / OBSERVED / HYPOTHESIS / OPEN / DISPROVEN at earned scope, plus a Representation Record and updated CURRENT_STATE.

Do not replace source provenance with a compressed account of what it supposedly contains. Protected or unpublished operational material is not introduced into this public repository merely to make a task convenient. Selection remains blocked unless the primary evidence can be reconstructed appropriately.

## 10. Design conclusions and current limits

This design exposes four consequential requirements that were not fully tested by EXP-001:

1. **A source can be exact without being complete about reality.** Laboratory Two needs both a checkable task answer and an explicit boundary around what the raw source represents.
2. **Available recovery and knowing when to recover differ.** EXP-001 demonstrated recovery when the evaluator requested it; an adaptive-use claim needs a frozen, prospective trigger.
3. **A different answer set is not always an incompatibility witness.** For one-witness tasks, genuine information loss needs incompatible acceptable outputs, not merely different underlying feasible sets.
4. **Transfer of a method and an advantage from using it differ.** A strong conventional baseline can succeed equally well. That is a legitimate result, not a failure of experimental design.

These are design deductions and requirements, not observed external results. H1/H2, actual source quality, task feasibility and materiality remain OPEN until a qualified task and frozen comparison exist.

## 11. Provenance and next boundary

This design derives from the pinned [EXP-001 result](../../experiments/EXP-001-results-2026-10-03.md), [operational contract](../../experiments/EXP-001-operational-addendum-v1.md), [RR-LR-005](../../records/RR-LR-005-internal-reconstruction.md), [research program](../../RESEARCH_PROGRAM.md) and [record contract](../../REPRESENTATION_RECORD.md) at research baseline `e730d249d87429e81fcb460e275f47dffec6df14`. It imports no outside field result and makes no novelty or generalization claim. AI contributed the design and review; independent human/formal review is not claimed.

During publication, main advanced to `cabec60225ff02453dde212c686953fbe035120e`. Its [consequence-triggered resolution observation](../../notes/FIELD_OBSERVATION_CONSEQUENCE_TRIGGERED_RESOLUTION_2026_10_03.md) and [retrieval-node working hypothesis](../../notes/WORKING_NOTE_RETRIEVAL_NODE_COMPRESSION_2026_10_03.md) were read and preserved. They reinforce the need to declare task materiality, prospective recovery triggers and the boundary between active payload and navigable retained state. They are hypothesis-generating notes, not qualified transfer evidence, established cognitive mechanisms or a selection of a memory/cognition laboratory. The shared-state clarification in section 5 makes that boundary explicit without requiring a graph representation.

**Completed now:** pre-selection requirements and an unfilled qualification packet.  
**Not done:** candidate search, laboratory/domain selection, task/source acquisition, implementation or transfer execution.  
**Next permitted research stage, when requested:** populate and compare evidence packets against these gates. Qualification establishes eligibility, not automatic selection; choose and freeze a specific laboratory only at the subsequent selection stage.

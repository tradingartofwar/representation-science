# Working note — When the assumption excludes the answer

**Date:** November 21, 2026  
**Status:** OPEN / framing refinement supported by an elementary counterexample and existing [RR-LR-003](../records/RR-LR-003-representation-failure-vs-reality.md). No new experimental result, general impossibility theorem, physics theory or automatic operating rule.  
**Related work:** [Question quality as upstream control](WORKING_NOTE_QUESTION_QUALITY_UPSTREAM_CONTROL_2026_10_04.md); [RR-LR-003 — source-class failure vs physical reality](../records/RR-LR-003-representation-failure-vs-reality.md); [representation record contract](../REPRESENTATION_RECORD.md).

## Generating distinction

A November 20–21 Human–AI conversation examined physical and mathematical relationships through several possible models. Vance interrupted the expansion of explanations with an upstream concern:

> **The way we are picturing everything in the first place might be wrong or inadequate.**

He illustrated it with a missing wire: one might search a house perfectly while having no justified reason to assume the wire is in the house at all. This was not a report about a specific unresolved item; it was an example of a faulty search premise.

The existing research distinguishes **answer quality**, **representation quality**, and **question quality**. The new emphasis is to make explicit an additional *audit target* within question/frame quality:

**Assumption-domain adequacy:** Does the allowed universe of candidates, entities, relations or explanations actually contain the kind of answer our real-world purpose requires?

This is a proposed label for a research question, not an established new discipline or a claim that the earlier research failed to consider it.

## An exact example

Let the actual possible-location universe be:

```text
U = {home, office}
```

Suppose the actual item is at `office`, while a searcher silently assumes:

```text
D = {home} ⊂ U
```

The local search predicate correctly reports:

```text
For every x in D, item_present(x) = false.
```

But the global proposition `for every x in U, item_present(x) = false` is **false**.

An exhaustive search over `D` certifies only a statement **conditioned on D**, not global absence over `U`.

Formally, a derivation of

$$
\forall x\in D:\neg P(x)
$$

does not imply

$$
\forall x\in U:\neg P(x)
$$

unless the domain restriction is justified relative to `P` and the query (for example by evidence that every relevant candidate lies within `D`).

**The error is not poor enumeration, insufficient intelligence, or information loss within D. It is promoting a conditional result into an unconditional conclusion without a coverage warrant.**

This particular elementary example was constructed for clarity. It is not a new mathematical finding.

## An existing, more substantive source-class counterexample

Representation Science already recorded the structural issue in [RR-LR-003](../records/RR-LR-003-representation-failure-vs-reality.md):

- A designated class of 36 candidate sheets failed to yield a witness in the recorded configuration.
- Source analysis nevertheless established an actual physical 1/8-safe time outside that source-class method.
- The valid inference was **“no witness in the supplied class,”** not **“no witness in reality.”**

The finite evidence stays with the source record. Today's observation **does not reproduce or strengthen** the underlying Lonely Runner result. It adds an explicit analogy and a question about the *assumptions that choose the candidate domain before search begins*.

## Separate failure modes

| Failure mode | What is wrong? | Appropriate correction |
| --- | --- | --- |
| Inadequate answer/decoder | Available representation may support the answer, but the allowed method fails | Change the decoder or computation; retain same source where sufficient |
| Loss of consequential information | A representation merges states with different answers to the declared question | Enrich/recover source detail; test matching-payload counterexamples |
| Question mismatch | The formal question isn't the question that matters for the practical consequence | Reframe the query while preserving its provenance |
| **Assumption/domain mismatch** | The permitted candidates or forms of explanation exclude an actual possibility | Challenge the coverage assumption; expand or replace the domain and retest against reality |

These categories may overlap. The fourth is partly upstream of the others and can be masked by locally impeccable evidence.

## What would justify the search boundary?

A representation adequacy contract should make **domain coverage** inspectable when global claims depend on it.

Candidate questions:

1. What facts or assumptions restrict the admissible search domain?
2. Is the statement being made **within** that domain, or about all of the underlying reality?
3. What independent evidence supports completeness of the selected domain for the declared query?
4. What *counterexample outside the domain* would change the conclusion?
5. What observation would cause a new domain or alternative framing to be introduced?
6. Which distinctions or observables must survive movement between the old and new frames?

One can have a perfectly adequate representation **conditional on a model** while lacking evidence that the model's domain covers reality. Conversely, external evidence can justify a narrower domain when the question and conditions permit it. We should not demand unlimited search whenever a narrower frame is adequately warranted.

**Important epistemic limit:** An open-world search cannot usually certify that no imaginable alternative exists. An honest report may preserve an explicitly qualified conclusion with an unresolved domain-coverage assumption.

## Invariants as tests, not decorations

The conversation also identified the value of **invariants** in comparing representations.

In mathematical physics, an invariant is defined with respect to a particular transformation or symmetry; the claim requires explicit hypotheses. In Representation Science, a candidate invariant can be an observable or answer that should agree across two declared descriptions of the *same underlying situation*. The agreement must be tested rather than presumed.

A useful audit shape is:

```text
Frame A: assumptions, source/domain, representation, allowed operations
Frame B: changed assumptions/domain/representation
Common question or observable: what is claimed to be preserved?
Translation/recovery: how is that observable computed in both?
Counterexample: when does the alleged invariant fail?
Evidence: what supports equivalence or calls for reopening?
```

Do not mistake design commitments—such as retaining provenance, honoring permissions, preserving corrections, and exposing uncertainty—for physical invariants. Those are operational rules to implement and validate. Their role is to keep contact with reality possible when models change.

A failed expected invariant is informative: it may expose a hidden assumption, a non-equivalent transformation, an error, or genuinely different behavior. It is not by itself evidence for an unknown dimension or novel physics.

## Implication for relational-geometry questions

The recent [relational-geometry working note](https://github.com/tradingartofwar/representation-science/pull/16) asked which relations and constraints allow a geometric answer to be reconstructed. The present correction is **earlier**:

> Why assume that the appropriate primitives are already “objects,” “relationships,” “distances,” or even “geometry”? What observations justify the chosen domain of candidate explanations?

This question does not force us to conclude those primitives are wrong; it prevents silently using them as unquestionable starting facts. Distinguish the theories' successful empirical domains from speculative foundational assumptions. Quantum mechanics and special relativity already coexist in quantum field theory; the unresolved challenge involves quantum gravity and the dynamical geometry of general relativity.

## Possible bounded research contribution

This note proposes no new experiment. A future inquiry could compare representational systems that:
- accurately answer a question within a declared limited source class,
- incorrectly elevate that to a global answer,
- or carry a domain-coverage qualifier and an explicit return path to a broader source.

The discriminating result is whether the system reports a correct **conditional answer** and reopens its assumptions when an out-of-domain witness appears. Costs and false-positive expansions would need measurement. A familiar finite mathematical example should be preferred to an untestable cross-domain analogy.

No stopped experiment is reopened. The existing computational, memory or human outcomes remain at their prior evidence statuses.

## Attribution and reality boundary

Vance supplied the missing-wire analogy, identified the possibility of a wrong starting assumption, and emphasized invariants as aids to understanding. AI compared the observation with RR-LR-003, distinguished domain adequacy from a decoder/representation miss, and drafted this note.

This is **a hypothesis-generating framing correction** within an existing program, not a claim that every problem has an unseen out-of-domain answer. Its value depends on whether it prompts more truthful conclusions, better counterchecks and correction when reality contradicts the assumed frame.

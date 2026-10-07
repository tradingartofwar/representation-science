# Working note — Question Capacity Frontier

**Date:** 2026-10-07  
**Status:** WORKING HYPOTHESIS / proposed Representation Science research direction  
**Origin:** Vance connected a public observation about AI posing questions too large for a person to mentally hold with the project's work on compression, consequential distinctions, representation cost and question quality. The research idea does not depend on the accuracy or wording of that external attribution.

## Core observation

Representation Science began by asking what a representation must preserve to answer a declared question.

The Lonely Runner work then suggested that some consequential structure may resist aggressive compression: representation growth can be the honest cost of preserving relationships that affect the answer.

The question-quality work added a further upstream point:

> **The question determines which distinctions become consequential.**

A new possibility follows:

> **The question itself may be a structured object whose faithful representation is too large for a human to consciously hold or manipulate all at once.**

This is different from saying that a question is merely difficult, long, or computationally expensive.

The proposed research object is the relationship among:

- the underlying reality;
- the representation of that reality;
- the representation of the question being asked;
- the reasoning operations permitted over both;
- and the smaller human-facing view needed for judgment or action.

## Candidate principle

> **AI may enlarge the set of questions humans can ask faithfully by carrying question structures whose consequential relationships exceed human working representation, while exposing only the decision-relevant slice to conscious attention.**

This is a hypothesis, not an established cognitive or computational result.

A shorter formulation is:

> **AI may expand not only answer capacity, but question capacity.**

## The Question Capacity Frontier

Define a provisional **Question Capacity Frontier** as the boundary at which a question's consequential structure can no longer be faithfully maintained within the active representation available to the reasoner without dropping distinctions that can change the answer.

This should not initially be treated as a fixed human cognitive limit. The frontier may depend on:

- the person;
- external notation and tools;
- familiarity and learned schemas;
- time available;
- question structure;
- number of independent variables;
- interaction order;
- uncertainty;
- required output;
- verification burden;
- and available AI or computational support.

The frontier is therefore operational and task-relative.

## Important distinction: hard to answer vs hard to hold

A question may be difficult because:

1. the required computation is expensive;
2. the relevant evidence is unavailable;
3. the answer is uncertain;
4. the representation is inadequate;
5. or the **question representation itself exceeds the reasoner's ability to keep its consequential structure active**.

Only the fifth case is the immediate target of this note.

A person may understand each component of a question when presented separately yet be unable to preserve all consequential relationships among them during reasoning. Ordinary compression may then simplify the question before the answer process even begins.

If the discarded relationship can change the answer, the apparent question being solved is no longer the original question.

## Connection to representation cost

The earlier working proposition was:

> **Some complexity may have an irreducible representational cost.**

And:

> **Representation should scale with the consequential relationships in reality, not with human preference for simplicity. Human-facing views should scale with the decision.**

The Question Capacity Frontier extends that principle upstream.

Representation cost may attach not only to the model of reality or the answer, but also to the inquiry itself.

The design question therefore becomes:

> **How much structure must remain available to preserve the question faithfully while reasoning proceeds?**

“Remain available” need not mean “remain consciously active.” Structure may live in retained state, decoder logic, external notation, AI-maintained working state, reconstruction paths, verification procedures or source recovery.

## A deliberately oversized question

An example of the proposed class is:

> **Given a changing real-world system containing multiple people, goals, uncertainties, causal relationships, representations, evidence sources, future unknown questions, time-dependent consequences, and limited human attention, what combination of retained state, internal reconstruction, external verification, source recovery, uncertainty tracking, and return-to-attention policy minimizes total cognitive and computational cost while ensuring that no distinction capable of changing a consequential future decision becomes irrecoverable before the moment it matters?**

A human can understand the sentence and many of its parts.

That does not establish that the complete relational structure required to reason over it can be actively maintained by one person without external support.

The distinction to test is:

**linguistic comprehensibility != faithful operational possession of the whole question.**

## Proposed architecture

The earlier simplified picture was:

**reality -> representation -> question -> answer**

A richer model is:

**reality  
-> representation of reality  
-> representation of the question  
-> reasoning over both  
-> evidence / verification  
-> human-facing decision view**

The representation of the question becomes an explicit research object.

## Possible experiment

Construct families of questions that increase in **independent consequential relationships**, not merely length or vocabulary.

Compare at least three conditions:

1. **Human/full description** — participant receives the complete question and ordinary external notation.
2. **Human/compressed description** — participant receives a conventional summary or self-generated compression.
3. **Human + AI maintained structure** — AI preserves the full declared question graph while presenting adaptive local views and allowing re-entry to omitted structure.

Measure separately:

- answer correctness;
- consequential distinctions retained or dropped;
- ability to explain which variables affected the answer;
- contradictions introduced during compression;
- verification success;
- time/cognitive burden where measurable;
- and whether the represented question silently changed during reasoning.

The crucial independent variable should be relational structure, not word count.

A useful failure witness would show that two question states become indistinguishable under a compressed representation even though they require different answers or decisions.

## Guardrails

- Do not equate consciousness with working memory without evidence.
- Do not claim a universal human capacity number.
- Do not confuse a long prompt with a structurally complex question.
- Do not let AI hide consequential distinctions merely because the human-facing view is small.
- Do not assume AI-maintained structure is faithful merely because it is larger.
- Preserve provenance and a recovery path from the human-facing slice to the underlying question structure.
- Distinguish computational advantage from representational advantage.
- Distinguish better answers from the ability to preserve and ask a richer question.
- Compare against ordinary external aids such as diagrams, notes, symbolic notation and software, not an artificially unaided human baseline.

## Strongest current hypothesis

> **AI may enlarge the space of faithfully askable questions by separating the size of the machine-maintained question representation from the size of the human-facing conscious view.**

If supported, this would extend the role of AI beyond answering difficult questions.

It would suggest that AI can help humans formulate, preserve and operate on inquiries whose consequential structure would otherwise be compressed before reasoning begins.

## Open questions

1. What operational measure best captures question complexity: independent variables, interaction order, graph structure, conditional branches, uncertainty, output obligations, or another quantity?
2. When does human compression change only presentation, and when does it change the question itself?
3. Can an AI preserve the whole question while presenting local views without introducing hidden framing errors?
4. What must remain inspectable so the human can correct the AI's representation of the question?
5. How should question representation cost be divided among retained state, decoder, reconstruction, verification and recovery?
6. Does AI support shift the frontier, or merely move the complexity into an opaque system?
7. What is the minimum evidence needed to claim that a human-AI system asked a question more faithfully than either the human or AI representation alone?

## Research posture

This is not yet a new program or established result.

It is a candidate extension of Representation Science suggested by the convergence of:

- consequential distinctions;
- representation cost;
- question quality as an upstream control;
- human-facing versus machine-facing resolution;
- and the possibility that inquiry itself has a representational scaling cost.

Before promoting it, design at least one discriminating experiment and compare against strong ordinary external-representation baselines.

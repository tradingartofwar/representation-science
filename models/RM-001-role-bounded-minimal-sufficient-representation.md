# RM-001 — Role-bounded minimal sufficient representation

**Date:** 2026-10-07  
**Status:** WORKING MODEL / hypothesis  
**Origin:** practical handoff problem involving a professional advisor; generalized here to avoid private or client-specific material.

## Problem class

A person or system holds a large, messy body of underlying reality and needs another actor to make a **bounded professional judgment or take a bounded action**.

The receiving actor does not need the entire history. But an overly compressed handoff can omit a distinction that changes the judgment.

The representation problem is therefore not:

> How do we summarize everything?

It is:

> **What is the smallest representation that safely supports the recipient's assigned question and scope, while preserving a reliable path back to omitted evidence?**

## Model

Let:

- **R** = underlying reality or case history;
- **A** = receiving actor or role;
- **Q** = question the actor is being asked to answer;
- **S** = authorized scope of action;
- **D** = distinctions that can materially change the answer or action;
- **M** = transmitted representation;
- **P** = recovery path to omitted source material;
- **Cᵢ** = inspection/transmission cost;
- **Cᵣ** = recovery cost;
- **Cₑ** = cost of error from omitted consequential information.

A role-bounded representation is adequate only if it preserves the distinctions needed for **Q** and **S**, or preserves a recovery path that is triggered before omission can produce unacceptable error.

The practical objective is not minimum size alone. It is closer to:

> minimize avoidable inspection and transmission cost  
> subject to preserving decision-changing distinctions and safe recoverability.

## Candidate handoff structure

For many bounded professional handoffs, a compact representation may be organized as:

1. **Question / requested decision** — what do we need from the recipient?
2. **Current state** — what is true now?
3. **Relevant history** — only events that may change the requested judgment.
4. **Actions already taken** — what has been tried or completed?
5. **Known constraints / deadlines** — what limits the available action?
6. **Key uncertainties** — what is not known or disputed?
7. **Evidence pointers** — where can the recipient retrieve supporting material?
8. **Scope boundary** — what is the recipient *not* being asked to do?

This structure is a candidate pattern, not a universal schema.

## Field observation that motivated the model

A practical situation required obtaining limited advice from a professional whose time is expensive. The underlying matter contained a long history, multiple communications, repairs/actions, disputed claims, evidence, and ongoing events.

Sending the entire history would increase review cost and could bury the current decision. Sending only a short conclusion could omit facts that materially change professional advice.

The useful framing became:

- identify the **specific questions** for the professional;
- preserve the **facts and distinctions capable of changing those answers**;
- state the **limited scope of requested participation**;
- keep the larger evidence set available through a retrieval path rather than embedding all of it in the initial packet.

No client names, private facts, or legal conclusions are preserved here.

## Consequential distinctions

This model depends on distinctions already central to Representation Science:

### Completeness is not adequacy

A complete dump of source material can be less useful than a smaller representation when the receiver must find a decision-relevant structure under time or cost constraints.

### Brevity is not adequacy

A short summary is not good merely because it is short. If it erases a distinction that can change the answer, the compression fails.

### Omitted is not lost

Information can be absent from the initial representation while remaining safely recoverable from a pinned or available source.

### Recipient role changes adequacy

The same underlying reality may require different representations for:

- an attorney;
- a physician;
- a contractor;
- an executive;
- a claims reviewer;
- an AI agent.

Adequacy is relative to the receiver's question, authority, and scope.

### Inspection cost is part of representation cost

Human review time, professional fees, attention, and cognitive load are not incidental. They are legitimate representation costs.

## Other candidate applications

### Medical specialist referral

A specialist may need the active symptoms, relevant history, medications, key tests, and the referral question. A full lifetime record may be available but need not be placed in the initial representation.

### Technical incident handoff

An engineer taking over an incident may need current symptoms, blast radius, recent changes, failed interventions, active hypotheses, and pointers to logs. Raw logs alone are not an adequate operational handoff.

### Executive decision brief

A decision-maker may need the decision, options, constraints, material numbers, uncertainties, and evidence links. A long project history may increase rather than reduce decision cost.

### Repair / contractor handoff

A contractor may need the observed defect, location, access constraints, prior relevant interventions, and desired result. Unrelated property history should remain outside the active representation.

### Insurance or administrative escalation

A reviewer may need the exact blocked transaction, applicable requirement, steps already completed, identifiers, and supporting documents. A chronological narrative of every interaction may obscure the point of failure.

### AI-agent delegation

An agent may need the objective, permissions, frozen state, canonical sources, constraints, and escalation conditions. Giving the entire conversational history may introduce irrelevant context or accidental authority.

## Failure conditions

The model fails when:

1. an omitted distinction changes the recipient's answer or action and the recovery mechanism does not surface it in time;
2. the representation obscures uncertainty or dispute by presenting an inference as established fact;
3. scope compression removes information needed to recognize that the requested scope itself is unsafe or misframed;
4. retrieval cost is so high that the nominal recovery path is not practically usable;
5. aggressive compression forces the recipient to reconstruct unsupported details;
6. the handoff optimizes sender convenience rather than recipient decision quality.

## Relation to current Representation Science work

This model connects several existing ideas:

- **question quality as upstream control** — the requested professional decision determines what distinctions matter;
- **consequence-triggered resolution** — finer detail should be recovered when consequence requires it;
- **internal reconstruction versus source recovery** — omitted detail may remain recoverable without residing in the initial packet;
- **human inspection burden as cost** — more stored or transmitted information is not automatically better.

It adds a practical variable:

> **recipient role and authorized scope**

A representation can be adequate for one receiver and inadequate for another even when the underlying reality is unchanged.

## Testable research directions

1. Can handoff quality be measured by decision accuracy, review time, retrieval frequency, and missed consequential distinctions?
2. Can independent reviewers identify which omitted facts would have changed their recommendation?
3. When does a layered representation — compact packet plus source pointers — outperform either a full source dump or a summary alone?
4. Can systems learn reliable triggers for requesting more detail rather than either overloading the receiver or omitting too much?
5. How does the optimal representation change with recipient expertise?
6. Can the same underlying case be used to compare attorney, medical, technical, executive, and AI-agent handoffs without collapsing their different questions?

## Working principle

> **The best handoff is not the most complete representation. It is the smallest representation that safely supports the recipient's bounded judgment, with a reliable path back to omitted evidence.**

This principle remains a hypothesis until tested across independent cases.

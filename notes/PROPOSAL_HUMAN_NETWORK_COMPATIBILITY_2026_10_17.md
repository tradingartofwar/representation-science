# Proposed research: compatibility discovery in human networks

**Status:** Proposal / hypothesis, not validated. October 17, 2026.
**Origin:** Mission Control discussion linking Lonely Runner's center-width criterion, Representation Science's marginal-vs-joint compatibility distinction, the agent coordination laboratory proposal, and the Human–AI Network.

## Core idea

Conventional interest/keyword similarity is not the same as the ability to accomplish something together. Two people may share interests without a useful collaboration; two people with unlike backgrounds may have complementary abilities. A useful network should investigate **what becomes possible through a connection**, not only who resembles whom.

Questions include connecting people with common interests, matching problem owners to solvers, employer/candidate fit, and assembling teams with complementary capabilities.

## Tentative formalization

For a problem P, define requirements R(P). For a person or group S in a network V, define available capabilities A(S,x) under a proposed collaboration configuration x (availability, consent, resources, credentials where essential, permissions, location, trust and coordination conditions).

A *schematic* feasibility question is:

    Exists S subset V, x such that Compatible(S,P,x).

Under a simplified set-cover model one might require:

    R(P) subseteq A(S,x).

That inclusion is **not a validated universal matching formula**: requirements may be temporal, graded, uncertain, interdependent, or non-substitutable. A typed constraint graph or multiobjective model may be more faithful. No inference of an individual's willingness or suitability should be treated as a fact without confirmation.

Compare with a similarity-only baseline:

    Match_similarity(P, person) = Similarity(descriptions).

The target is consequential complementarity and joint feasibility, not just shared words or interests.

## Representation Science question

What distinctions must descriptions of people, problems and proposed collaborations preserve for worthwhile connections to remain discoverable? Compression may discard demonstrated experience, transferable skills, unusual interests, preferences, practical constraints or relationships that do not appear in titles and credentials. Conversely, high apparent similarity may conceal incompatible constraints.

A key experimental distinction is information truly lost versus reconstructible from retained context (see RR-LR-005). Joint compatibility must not be inferred solely from marginal capability profiles (see RR-LR-001).

## Proposed research path

1. Define a bounded, inspectable synthetic matching environment with explicit task requirements, participant capabilities, availability, consent and constraints.
2. Compare keyword/similarity matching, individual capability matching and relational/complementarity-aware matching. Hold candidate pool, task facts, budgets and scoring constant. Include negative controls, adversarial cases, and opportunities for a conventional baseline to win.
3. Evaluate whether proposed teams can actually complete specified simulated tasks, not only whether descriptions look persuasive. Measure valid matches, false positives, overlooked opportunities, explanation quality and coordination cost separately.
4. If evidence warrants, design opt-in real-world evaluation in the Human–AI Network with human judgment, transparent explanations and participant control. Avoid automatically ranking people as intrinsically valuable or claiming the model knows willingness, trust or fit.
5. Keep any transfer from the Lonely Runner mathematical criterion explicitly analogical unless a formal mapping and proof are established.

## Governance and handoff

Representation Science owns the research question, falsifiable protocol and evidence. Human–AI Network owns the product vision, consentful introduction workflow, and any practical prototype. Preserve cross-links and the origin story; do not replace existing network work. Do not disrupt the active agent-coordination laboratory experiment.

Related sources:
- https://github.com/tradingartofwar/the-lonely-runner-conjecture/blob/research/runner-addition-2026-10-17/experiments/runner-addition/center-width/RULE.md
- https://github.com/tradingartofwar/the-lonely-runner-conjecture/blob/research/runner-addition-2026-10-17/notes/PROPOSAL_AGENT_COMPATIBILITY_REPRESENTATION_2026_10_17.md
- https://github.com/tradingartofwar/representation-science/pull/13

**Next action when resumed:** choose one concrete matching problem and specify ground-truth constraints, baseline, outcome and consent boundary before implementing or testing.

# Agent Coordination Laboratory — Simulation-first proposal and visual observation

**Status:** PROPOSAL / HANDOFF, not an executed experiment. October 17, 2026.

## Origin and motivation

This proposal transfers a research question from the Lonely Runner [center-width criterion](https://github.com/tradingartofwar/the-lonely-runner-conjecture/blob/research/runner-addition-2026-10-17/experiments/runner-addition/center-width/RULE.md) and [agent-compatibility proposal](https://github.com/tradingartofwar/the-lonely-runner-conjecture/blob/research/runner-addition-2026-10-17/notes/PROPOSAL_AGENT_COMPATIBILITY_REPRESENTATION_2026_10_17.md).

Lonely Runner distinguishes required half-width H_d(c) from permitted half-width G_{S,d}(c), with an exact proposed single-source criterion H_d(c)<=G_{S,d}(c). The *analogy*, not a theorem about agents, is to ask whether requirements and constraints are jointly compatible. In agent coordination, relationships may be logical, temporal, graph-based, or multidimensional rather than scalar.

Representation Science founding distinction: marginal feasibility does not imply joint compatibility. Also honor RR-LR-005: an implicit relationship may be reconstructible; missing an explicit field does not prove information loss.

## Experimental objective

Give **two or more actual software-writing agents** a real, executable software task that requires coordination. Use a controlled simulation environment with separate workspaces, regulated capabilities and permissions, explicit communication channels, ground-truth task requirements, and executable acceptance tests. Compare how alternative representations affect successful joint action, not merely predictions or polished explanations.

Start with two agents, e.g. one implementing a data-processing module and another implementing an integration/client module. Neither can complete the integrated deliverable alone under the configured permissions. Observe interface negotiation, edits, messages, test failures and recovery. Include controlled perturbations such as a changed schema or stale version.

## Conditions and controls

Compare (a) marginal task/capability descriptions, (b) explicit dependency/compatibility representations, and (c) a compact representation with a declared reconstruction mechanism. Include positive controls where marginal information suffices and adversarial cases where explicit relations do not help. Freeze task facts, agent model/version, tool budgets, workspace permissions, scoring, scenario selection, and stop rules before running. Use development and held-out tasks, plus counterexample searches. Repeat where nondeterminism matters; don't claim statistical independence without it.

Initial tasks: shared-file version conflicts; prerequisite ordering; mismatched interfaces/data contracts; permission and handoff dependencies. Agent communication is allowed through **regulated channels**, with actual visibility and edit permissions enforced by tools, not merely requested in prompts.

## Laboratory architecture

- Experiment controller: scenario setup, assignments, allowed tools, communication rules, permissions, time/budget caps, perturbations, seeds and frozen manifests.
- Isolated agent workspaces: separate file visibility and writable areas; tools mediate all state changes and messages.
- Shared workspace: versioned artifacts, messages and integration surface with access controls.
- Event recorder: append-only structured log of observed messages, tool calls/results, file diffs/hashes, permission denials, task transitions, tests, and timestamps/logical sequence.
- Ground-truth evaluator: hidden acceptance tests and known dependency graph, isolated from agents.
- Visual observer: read-only, separate from agent information channels.

A Python-based minimal harness with local isolated workspaces and deterministic tests is a possible implementation; evaluate sandbox/process isolation and untrusted-code execution safety before allowing arbitrary generated code. Do not assume prompt-level constraints are secure permissions.

## Visualization: replay first, live later

Build an **event-sourced visual replay** first; use the same event schema for a later live dashboard. Suggested coordinated views:

1. Timeline: ordered events, messages, file changes, test runs, failures and recoveries; pause/step/scrub and compare runs.
2. Agent lanes: what each agent was assigned, could see, could edit, and communicated at each moment.
3. Dependency/compatibility graph: required interfaces, ordering and permissions; highlight violated edges when evidence supports them.
4. Workspace and artifact history: version/diff and provenance, with test outcomes.
5. Observer panel: full ground truth and experimental condition, **never visible to agents**; optional counterfactual comparison clearly labeled as analysis, not observation.
6. Reflection panel: event-linked annotations of when a missing relationship became consequential, what was known from logs, what was inferred, and whether agents recovered.

Record expressed beliefs only when supported by statements or actions; do not claim to read private agent reasoning. Protect secrets and personal data; synthetic tasks by default. Every visual claim should link to immutable event IDs and artifacts.

### Example event schema (illustrative, not yet frozen)

```json
{"run_id":"run-001","seq":17,"actor":"agent-a","kind":"artifact_write","artifact":"api/schema.json","before_hash":"...","after_hash":"...","visible_to":["agent-a"],"logical_step":17}
```

For comparisons, align by semantic milestones (first interface proposal, first integration test, first mismatch, repair), not only wall-clock time.

## Outcomes and methodological cautions

Primary: integrated software passes hidden tests under declared constraints. Secondary: correctness of pre-execution compatibility predictions, number/severity of interface failures, communication and tool cost, repair latency, and recovery success. Keep separate measures rather than hiding tradeoffs in a single composite score. Distinguish actual execution success from retrospective explanations. The controller may know more than agents, but the evaluator must not leak hidden tests or dependencies.

A successful simulation validates the bounded task/environment, not automatic transfer to production agents. If early results are useful, progress to more complex simulations and eventually a carefully chosen real coordination incident. Independent review of the Lonely Runner mathematics remains a separate obligation.

## Proposed implementation sequence

First freeze a small protocol and event schema, then build the minimal controller, isolated workspaces, test oracle and recorder. Next build the replay viewer and run pilot cases. Only then consider live visualization, perturbation schedules and larger agent groups. Preserve failed runs, alternative explanations and negative controls.

## Handoff to a dedicated Representation Science thread

Review this proposal against CURRENT_STATE.md, RR-LR-001 and RR-LR-005, and prior experiment freeze/integrity lessons (including EXP-002). Propose the smallest falsifiable two-agent software task and explicit ground-truth compatibility graph. Design the event schema so every process can be inspected or replayed, without exposing observer-only knowledge to agents. Present a protocol, architecture and visualization mockup for review **before coding or executing**.

**No simulations, new software harness, or visualization have been implemented by this document.**

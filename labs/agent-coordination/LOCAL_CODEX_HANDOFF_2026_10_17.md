# Agent Coordination Laboratory — local Codex / WSL takeover

**Date:** 2026-10-17

**Scope:** Resume approved Stage 1 specification, minimal implementation, and exposed engineering qualification on the operator's local computer.

**Research status:** Design approved; implementation incomplete; no agent coordination result established.

**Execution status:** Comparative evaluation is NOT authorized. Live development agent runs are also disabled at this checkpoint.

**Repository:** <https://github.com/tradingartofwar/representation-science>

**Review PR:** <https://github.com/tradingartofwar/representation-science/pull/13>

**Working branch:** `research/agent-coordination-lab-2026-10-17`

## 1. Instructions to the receiving Codex

Take over the engineering work locally. The operator already runs Codex in WSL and has proposed using that computer to host the laboratory. Verify WSL version, actual capabilities, and effective isolation rather than assuming them from that description.

Read this handoff and the source documents below, inspect the current branch, preserve existing work, then proceed incrementally with the authorized implementation and engineering checks. Do not repeat the initial design approval request. Return a concrete Stage 1 checkpoint with evidence and remaining blockers before any live development agent run. Do not execute the 36-run comparison.

The immediate objective is a trustworthy small experimental instrument: two independently maintained agent sessions, controlled tools and communication, protected execution workspaces, an independent evaluator, durable evidence, and visual replay. A scripted trace is useful for engineering qualification but is not evidence that two AI agents can cooperate.

Separate your role as **the development Codex building the instrument** from the **two experimental agents acting inside it**. Development Codex may inspect the research repository. Experimental agents must not inherit this conversation, research notes, future fixtures, hidden tests, previous trajectories, credentials, or the full repository. They receive only the permitted task materials and registered tools for their run.

### Read first

1. `AGENTS.md`, `README.md`, `RESEARCH_PROGRAM.md`, `REPRESENTATION_RECORD.md`, and `CURRENT_STATE.md`.
2. `notes/PROPOSAL_AGENT_COORDINATION_LAB_VISUAL_REPLAY_2026_10_17.md`.
3. `labs/agent-coordination/DESIGN_REVIEW_v0.1.md` in full.
4. `labs/agent-coordination/stage1/SPEC.md`, `ENGINEERING_PLAN.md`, and `policy.json`.
5. `records/RR-LR-001-joint-compatibility.md` and `records/RR-LR-005-internal-reconstruction.md`; inspect the other three records for the boundary/equality, representation/reality, and rank distinctions.
6. `experiments/EXP-001-results-2026-10-03.md` and `experiments/EXP-002-results-2026-10-06.md`. Do not rerun those experiments.

The design document retains its historical “awaiting review” status. The later Mission Control decision summarized below authorizes Stage 1. Preserve the original design as a historical artifact; record subsequent decisions separately. `CURRENT_STATE.md` predates this lab and is not a current implementation inventory.

## 2. Verified starting state and provenance

The following was inspected during handoff preparation. Recheck the branch head when receiving this document because work can advance.

| Item | Verified state before this handoff was committed |
| --- | --- |
| PR #13 | Open and unmerged; base `main` at `b8750dee72d5cc9a76d5dbee59077743cee735a9` |
| Remote PR head | `bfa2c7f9e269adc0a406848fe86e330d25bbe29c` |
| Original proposal commit | `4d22218938c2b5ea4fa35df20000b35b4b639ea9` |
| Approved design commit | `bfa2c7f9e269adc0a406848fe86e330d25bbe29c` |
| Newer local Stage 1 draft commit | `4dd62ada036ae597ff86a1a7781a8b9dc7eab2f4`, then not yet pushed |
| Local working tree at inspection | Clean |
| Stage 1 files | `SPEC.md`, `ENGINEERING_PLAN.md`, `policy.json`, and `aclab/__init__.py` |
| Functional implementation | None in the inspected lab tree; `aclab/__init__.py` contains only a package docstring |
| Qualification results | No completed engineering result bundle found in that tree |
| Replay viewer / recorder / broker / evaluator / agent adapter | Not implemented in that tree |
| Development or evaluation agent runs | No lab run artifacts found; none authorized or executed as part of this handoff |

The handoff publication preserves the exact contents of those four draft files and adds this document on the same branch. Terminal Git push was unavailable because that environment lacked GitHub authentication, so publication uses the connected GitHub integration. The original local draft SHA is provenance, not a required remote ancestor; the transfer commit has a different identity. Verify the published files and current PR head. Do not mistake `4dd62ad` for a completed Stage 1 implementation.

The previous session reported that an API credential was unavailable in its environment and that a sandbox launch failed with an operating-system permission error. These are **reported prior-environment blockers**, not evidence about the local computer. Raw probe receipts are not included in the four Stage 1 draft files. Do not invent the failing command, error text, or cause; conduct new, clearly identified local checks.

The planning documents refer to future modules such as `task.py`. Those references do not establish that the modules exist. Counts and intended outcomes in `ENGINEERING_PLAN.md` are planned checks, not completed results.

## 3. Authorization and scientific constraints

Mission Control approved the scientific direction, bounded producer–consumer task, three conditions, six proposed fixture types, and progression to **Stage 1 — specification and minimal implementation**, subject to the following requirements:

- Build the smallest architecture meeting the scientific requirements. Avoid a general-purpose agent platform, service fleet, or database unless a demonstrated need requires it.
- Resolve model/runtime, enforceable isolation, tools, budgets, cost accounting, and operational stops before live development runs. If isolation is unavailable, report the blocker; prompt-only restrictions are not a substitute.
- Develop visual replay alongside the recorder. Agent messages/actions, accessible/read/delivered/included information, dependencies, artifacts, tests, failures, recovery, outcomes, and resource use must be inspectable.
- Demonstrate task executability, fair baseline opportunity, permissions, evaluator sensitivity, compact reconstruction, evidence integrity, and replay correctness through exposed engineering checks. Actual agent coordination remains an additional live-development qualification.
- Preserve failures, timeouts, incomplete evidence, and counterexamples. Do not silently rerun experiments, repair original evidence, or tune using evaluation outcomes.
- Treat observable actions and statements as observations. Do not infer or seek private reasoning. Keep software success, constraint conformance, and evidence integrity separate.
- Keep real-world usefulness a separate validation question. A useful laboratory is a secondary contribution, not permission to expand beyond the bounded study.

### What you may do now

Inspect the local environment; specify and implement the task, broker, worker boundary, evaluator, recorder, session adapter, and viewer; run declared offline engineering checks and trusted sandbox probes; preserve their evidence; commit and push reviewable changes on the lab branch. Ordinary implementation fixes are permitted with failed check attempts preserved and new attempts identified. No merge or deployment is required for this checkpoint.

### What remains gated

The existing Stage 1 policy explicitly disables both live development agent runs and comparative evaluation. Keep those switches false. Offline adapter tests use synthetic responses. Do not make paid inference calls under the label of a connectivity probe or silently start the nine-run development allowance.

Before live development, return the requested checkpoint and a concrete proposed development plan with frozen prompts, budgets, costs, and readiness evidence for an explicit development decision. The allowance is at most nine pair-runs, not an instruction to run nine now.

The 36 evaluation runs require a later operational freeze, read-back verification, and explicit Mission Control execution authorization. This handoff grants none of those permissions. If later instructions explicitly change a boundary, record the change and its source; do not assume migration itself changed it.

## 4. Research question and competent comparison

Central question: **What information must a representation preserve for successful joint action to remain possible, and when does making that information explicit improve performance?**

The first comparison asks whether presentation, retrieval, and reconstruction change the probability or cost of correct integrated software when agents can access the same underlying task facts.

| Condition | Treatment | Fairness requirement |
| --- | --- | --- |
| I — Individual | Own goal, capabilities, permissions, local mode records, ordinary task documentation, and an index to the complete shared source | May inspect source, communicate, derive dependencies, and build its own relational representation |
| R — Relational | I plus explicit interface, unit, epoch, ownership, and handoff predicates | No winning mode, solution code, private fact, hidden answer, or prescribed solution sequence |
| C — Reconstructible | Compact codec dictionary, complete-mode bitmasks, identities/epoch, and a generic reconstruction recipe | Must preserve complete tuple correlations and reconstruct the intended facts/predicates faithfully; may also read ordinary source |

Equal accessible facts do not mean identical initial context. Initial exposure, prompt size, and saved derivation effort are part of the presentation treatment and must be measured. A relational advantage would not by itself demonstrate irrecoverable information loss or isolate notation alone. A tie, counterexample, or ordinary-baseline advantage is valuable evidence.

Maintain these distinctions throughout implementation and reporting:

- Individual feasibility / joint compatibility.
- Explicit information / reconstructible information / genuinely lost information.
- Accessible / read or delivered / actually included in a model invocation.
- Local correctness / integrated correctness / contractual conformance.
- Coding defect / coordination mismatch / infrastructure failure / evidence-integrity failure.
- Observer ground truth / agent-visible evidence.
- Scripted engineering behavior / actual agent behavior / analyst inference.
- Finite task performance / population claims / real-world usefulness.

## 5. Local setup and runtime decision

### First local actions

Use an existing checkout if present. Inspect its status before changing branches; preserve unrelated work. Otherwise clone the repository into the WSL Linux filesystem. Fetch the lab branch, compare with PR #13, and record the exact commit you start from. Use an isolated worktree if needed for development organization; a worktree is not an experimental security boundary.

Read-only orientation commands, to adapt to the installed tools:

```bash
wsl.exe --list --verbose
uname -a
cat /etc/os-release
codex --version
codex login status
python3 --version
git status --short
git branch --show-current
git log -5 --oneline
command -v bwrap
command -v docker
command -v podman
```

Some commands may be absent; record that instead of treating the list as a script that must all succeed. Check CPU/RAM/disk resources, container runtime access, user namespaces, process limits, and effective permissions only as needed. Do not print credential files or broad environment dumps. Record reproducible runtime facts in a public-safe environment receipt.

### Preferred minimal structure

Use a Python controller with a narrow broker, separate model histories for A and B, and short-lived isolated execution workers. The controller is the only authority for identity, budgets, epoch, publication, and log writing. A model asks for registered operations; it does not get an unrestricted host shell.

Candidate execution can use a properly configured container runtime or an equivalent Linux sandbox. Choose the simplest backend that actually enforces the required mounts, reads/writes, network restrictions, process separation, and resource bounds. WSL2 availability does not prove any of these are already enforced. Never run generated candidate code directly on the host as a fallback.

Keep model-provider authentication with the controller, outside generated-code workers. The controller may need provider network access; workers do not. The local computer hosts files, scheduling, code execution, and replay. Hosted model inference remains remote. Local GPU model serving would change the model/runtime factor and should be a separately documented choice, not an assumed part of the move.

### Development Codex versus experimental runtime

Existing Codex authentication is useful for development, but does not automatically supply credentials or all evidence needed by a custom API harness. The draft currently targets the Responses API with explicit per-invocation input construction.

An alternative based on two genuine Codex CLI sessions is possible only if it can meet the same controlled-tool, context-provenance, isolation, and budget contract. CLI JSON events alone must not be assumed to reveal every injected instruction, included input, compaction, or access path. If that cannot be audited, either retain the explicit API adapter or declare and review the limitation. Do not present two separate terminal windows as sufficient qualification.

Record model identity, snapshot availability, settings, context behavior, actual tool capabilities, authentication route, token accounting, retries, and costs in a runtime decision document. Check current official documentation and the installed version before choosing flags. Do not silently replace the draft model because another is locally available.

Official references checked during the transition discussion, to reverify as needed:

- Codex sandboxing: <https://learn.chatgpt.com/docs/sandboxing>
- Authentication: <https://learn.chatgpt.com/docs/auth>
- Programmatic execution and emitted JSON events: <https://learn.chatgpt.com/docs/non-interactive-mode>
- Draft model/pricing source recorded in policy: <https://developers.openai.com/api/docs/models/gpt-5.4-mini>

These links document capabilities; they are not local qualification receipts.

## 6. Enforced folder and capability boundaries

The operator specifically requested isolation between agent folders. Implement that as enforced capabilities, not naming conventions.

| Area | Permitted access |
| --- | --- |
| A private workspace | A reads its task material and reads/writes `producer.py`; B cannot inspect its private drafts |
| B private workspace | B reads its task material and reads/writes `consumer.py`; A cannot inspect its private drafts |
| Shared source | Both may read the same complete task facts through the broker |
| Published artifacts / messages | Visibility begins at the recorded publication/delivery point; broker controls versioning and access |
| Wrapper and evaluator | Controller-controlled; agents cannot modify them or read hidden expected outputs |
| Master evidence and observer state | Recorder/controller only; experimental agents cannot read or mutate them |

A local run layout may contain `agents/a`, `agents/b`, `source`, `published`, `evidence`, and `observer`. Physical directory adjacency grants no access. Do not mount the entire research checkout, Windows drives, host home directory, runtime control socket, or credential directories into a worker. Paths in a model request never choose the caller's identity.

Qualification must include denied cross-agent reads and writes, traversal/absolute-path/symlink attempts, hidden-oracle and log access, forged actor arguments, stale publication/epoch use, network attempts, and process/resource boundary checks appropriate to the chosen backend. Use benign sentinel files, bounded trusted probes, and disposable development fixtures. Pair denials with successful permitted operations so a broken tool cannot masquerade as isolation.

Prevent alternate unlogged communication through common temporary directories, inherited file descriptors, shared processes, sockets, writable mounts, or host integration. State the tested threat model and residual limits; do not claim universal security from a finite probe set. No experimental agent should be able to grant itself broader permissions or escalate a denied operation.

## 7. Task and evaluator to implement

The exact draft contract is `stage1/SPEC.md`; resolve remaining ambiguities before implementing acceptance logic and record changes visibly.

- A implements `produce(text: str, mode: str) -> list[dict] | dict`.
- B implements `consume(rows: list[dict], mode: str) -> dict`.
- Input is 0–3 NDJSON records. Each has exactly `id`, `category`, `amount_minor`; positional IDs are 0, 1, 2; category is `alpha` or `beta`; amounts are integers in `{0,1,99,100,101,12345}`. Reject booleans as integers.
- The finite valid domain has `1 + 12 + 144 + 1728 = 1885` streams. Specify accepted trailing newline and all invalid-input behavior exactly.
- Four complete modes: `F_minor`, `F_major`, `N_minor`, `N_major`; preserve their flat/nested and minor/major pairings.
- Major-unit values are canonical nonnegative two-decimal strings. Final output is exactly integer totals for both categories, including zero totals. Floating-point answers are invalid.
- Invalid input returns exactly `{"error":"INVALID_INPUT"}` and the immutable wrapper propagates it. Invalid wire data returns exactly `{"error":"INVALID_WIRE"}`.

Publish immutable artifacts with owner, source epoch, selected mode, code hash, and contract identity. A publishes producer code/contract; B reads and accepts that exact contract, then publishes consumer code bound to it. Both submit current versions. Private edits after publication or an epoch change invalidate the affected submission/acceptance as specified. Publication cannot let one agent write the other's private module.

### Exposed development inputs

| Fixture | A modes | B modes / change |
| --- | --- | --- |
| D1 | `F_minor, N_minor, N_major` | `F_major, N_minor` |
| D2 | Same as D1 | Initially D1; epoch 2 changes B to `F_minor, F_major` |
| D3 | `F_minor, N_minor` | `F_major, N_major`; no shared allowed mode |

These are development materials already exposed to the authors. No E1–E6 evaluation fixture files have been instantiated in the inspected Stage 1 tree. Do not borrow fresh evaluation cases to repair development.

The six future fixture types remain: constrained interface, alternative constrained interface, independent components, fixed explicit interface, scheduled epoch change, and incompatible constraints. E3 uses independent category-total components and a fixed combining wrapper; do not accidentally impose negotiated producer–consumer handoff on this negative control. Any additional engineering fixtures needed for control-path validation must be declared as exposed development material, not evaluation instances.

### Evaluator separation

Compute expected totals directly from validated raw input, outside candidate execution. Cross-check with separately structured trusted reference codecs and selected hand-calculated cases. Same-author alternative code is a cross-check, not independent human verification.

Run untrusted producer and consumer code in separate disposable workers; exchange only their declared wire data. The consumer worker must not gain hidden expected answers or producer private source. Compare generated wire content, final outputs, selected modes, epoch, owner receipts, and accepted hashes outside workers. No single self-reported “success” field is authoritative.

Public diagnostics and hidden final grading have distinct visibility. Local success is not integrated success. An infeasible case needs a correct finite-set certificate and is scored separately; it cannot count as successful software completion. Qualify the evaluator against deliberately wrong amounts, schema mismatches, stale contracts, wrong types, malformed input, and edited-after-publication submissions.

Resolve the complete invalid-case inventory, wire ID/order rules, malformed candidate protocol behavior, size bounds, and stop classifications explicitly. The draft's reference to an invalid suite in `task.py` is a TODO, not an existing frozen suite.

## 8. Budgets, scheduling, and cost decisions

Preserve `stage1/policy.json` as the inherited proposal until any changes are justified. It is not a measured cost report or authorization token.

| Dimension | Current draft ceiling |
| --- | --- |
| Pair rounds / calls | 12 rounds; at most 12 invocations per agent |
| Tools per response / total | At most 5 per response; 60 requests per agent including denials |
| Input / output tokens | 256,000 cumulative input; 16,000 output including accounted reasoning, per agent |
| Context / output per call | 32,000 input-context tokens; 2,048 output tokens |
| Messages | 8 per agent, up to 1,000 UTF-8 bytes each; proposal/acceptance accounting must follow the design |
| Publications | 6 per agent, up to 32 KiB each |
| Diagnostics | 10 local tests per agent; 6 integration diagnostics per pair |
| Pair wall time | 1,200 seconds |
| Worker | 1 CPU proposed; 512 MiB; 64 processes; 10 seconds; 1 MiB captured-output bound in policy |
| Retries | No automatic retries |
| Draft model | `gpt-5.4-mini-2026-03-17`, reasoning `medium`, Responses API, `store: false` |
| Planning prices | $0.75 / million input tokens; $4.50 / million output tokens; must reverify before use |

At those assumed prices, the full per-agent token ceilings imply $0.528 per pair, $4.752 for nine pairs, and $19.008 for 36 pairs. These are conditional token-budget calculations, not quotes or actual spend. The policy proposes a $5 development-batch cap; headroom is small. Reconcile current pricing, caching, token-count calls, failed requests, metering uncertainty, and any additional charges before setting a hard budget. Do not assume local hardware removes hosted inference costs.

Validate token counts before dispatch using the selected runtime's supported accounting; reserve remaining output allowance and prevent a request exceeding cumulative/context/cost caps. Preserve actual provider usage separately from estimates. No budget transfers between agents. Unknown usage is a recorded limitation/stop according to the declared policy, never zero cost.

Use a deterministic barrier scheduler: one bounded response per agent per round, tool requests handled in recorded order, tool results/messages entering the defined recipient turn. Real concurrent execution is not required for the first study. A twelve-call cap counts every model invocation, including any tool-follow-up invocation; an SDK's internal auto-loop must not evade it.

Keep an immutable round-4 checkpoint even when agents finish early. The planned perturbation occurs at the start of round 5; fresh acceptance/submission is required after change. Specify the matching D2 development timing before any live run. Define simultaneous publication, message delivery, `wait`, early completion, unfinished operations, and termination behavior deterministically.

Do not use an automatic context summarizer. Record exact application-supplied input bytes, omitted content, all tool schemas/instructions, and context policy. Any provider-side transformations or inaccessible context must remain a declared visibility limit. Never label a transcript as a complete view of internal state.

## 9. Evidence recorder and visual replay

Build the recorder before substantive qualification so checks themselves have durable receipts. A small JSONL event stream plus content-addressed files is sufficient initially.

Every event needs a schema version, run ID, monotone sequence/event ID, UTC receipt time, logical round/turn, actor, type, causal parents, operation ID where applicable, visibility/ACL version, source epoch, payload reference/hash, and previous-event hash. Store full file versions or resolvable base-plus-diff chains. Preserve tool parameters/results, allowed/denied operations, stdout/stderr and truncation markers, return codes, publication/acceptance hashes, model inputs/outputs/usage, and test snapshot identities.

Commit requests before mutating or dispatching; persist results before acknowledging them to agents. Use an explicit pending/completed operation record. A crash between steps leaves an uncertain operation, not an invented completion. Define atomic writes, durable flushes, checkpoint consistency, and finalization semantics.

At run closure, write a manifest of every evidence file's size/hash, event count/final sequence, final artifacts, and lifecycle disposition. Read the persisted bundle back through a separate verifier and rebuild checkpoints from events. Compare both intermediate and final state. Check completeness and causal/request-result linkage as well as hashes.

A hash chain alone does not protect against replacing the entire bundle and root. Anchor the final manifest/root outside the writable run bundle in a separately retained receipt; specify who controls it and how it is verified. Agent-inaccessible content-addressed storage is the minimum implementation, not an absolute immutability claim. Never repair original missing evidence into a success. Use `UNASSESSABLE_INTEGRITY` for a failed integrity gate and preserve contradictory summaries.

### Minimal replay viewer

Build a local, read-only viewer of completed bundles. A static HTML/JavaScript file with explicit bundle loading is adequate; no hosted site or application framework is required. Keep parsing/rendering safe for untrusted messages and artifacts. Replay must not call a model or execute recorded code.

Required views and interactions:

1. Chronological lanes for A, B, broker/environment, and evaluator; play/pause, step, cursor/scrub, and event selection.
2. Agent A / Agent B / observer perspective toggle. At a selected event show accessible versions, actual reads/deliveries, and exact recorded invocation inputs separately.
3. Compatibility/dependency panel with epoch, interface, ownership, and handoff state. Every satisfied/violated/unknown label links to its evidence.
4. Artifact version/content/diff inspector and negotiation/acceptance history.
5. Local versus integrated tests tied to the exact code and contract snapshots.
6. Failure, correction, recovery, final status, and resource/cost panels.
7. Explicit integrity status; missing artifacts and uncertain operations remain visible.

Avoid future-state leakage: a message sent but not delivered is not in the recipient's delivered view; later publications, tests, and source facts do not appear before their event. Agent-visible dependency state can remain unknown even when observer ground truth is known. Later analyst annotations belong in a labeled overlay and must not rewrite historical state.

Browser-check actual rendering and interactions. Capture evidence for perspective/cursor changes, artifact inspection, epoch invalidation, missing evidence, and escaped malicious-looking text. A screenshot alone does not establish replay correctness; compare displayed state to independently specified event fixtures.

## 10. Engineering qualification and stop conditions

Follow `stage1/ENGINEERING_PLAN.md`. Record each attempt's ID, purpose, command, commit, runtime, input hashes, expected outcome, actual outcome, stdout/stderr, times, and evidence hashes. Before new checks, declare their expected result. A corrected implementation produces a new attempt; prior failures remain.

| Qualification | Evidence needed before calling it passed |
| --- | --- |
| Task / oracle | All 1885 valid streams and declared invalid cases; four trusted codecs; independent-structure cross-check; rejected output mutations |
| Broker | Bound role identity, allowed own operations, denied private access, message delivery, publication/acceptance, stale state rejection, enforced budgets |
| Isolation | Successful actual worker launch plus positive/negative filesystem, network, process, and resource probes; OS/runtime configuration receipt |
| Representations | Exact C reconstruction against source/predicates, corruption rejection, equal accessible facts, no answer-bearing R rendering |
| Evidence | Missing/truncated/reordered/altered events, missing blobs, unresolved operations, absent completion, and changed manifests all handled with explicit integrity dispositions |
| Replay | Cursor/perspective state matches event fixtures, no future leakage, traceable claims, safe rendering, visible incomplete state |
| Adapter / scheduler | Two separate histories, exact input/tool envelopes, deterministic delivery, accounting and stop behavior, tested with synthetic responses |

Produce a conspicuously labeled `SCRIPTED_ENGINEERING_TRACE` showing negotiation, incompatible local choices, a correction, an epoch change, and termination. Distinguish real reference-test executions from deliberately injected demonstration events. Do not report this as a live coordination experiment or as proof the baseline agent succeeds.

Stop candidate execution when sandbox qualification fails. Stop a qualification sequence on oracle disagreement, unlogged access, unexplained evidence inconsistency, or a defect that invalidates its measurements; preserve it before repairing the instrument. Resource limits and expected invalid outputs are test outcomes, not reasons to conceal an attempt.

For future live runs, failure/budget exhaustion/timeouts remain outcomes under the frozen rules. Broken isolation, shared oracle/harness defects, missing provenance, unaccounted model drift, or evidence corruption require operational stops. Preserve completed, failed, unassessable, and unattempted assignments separately. Do not sample until success.

## 11. Staged local work and next checkpoint

Proceed through small reviewable commits:

1. **Orientation and environment:** verify branch/history; inventory runtime; run trusted isolation probes; write the architecture/runtime decision and unresolved prerequisites.
2. **Contract and oracle:** settle remaining behavior; implement trusted reference functions and acceptance checks on exposed inputs; record outcomes and counterchecks.
3. **Recorder and broker:** implement event durability, role-bound tools, versioned publication, exact message/context delivery, and integrity verification; qualify denials and faults.
4. **Execution and session adapter:** integrate only the qualified worker backend; implement separate histories, scheduler, deterministic context construction, and accounting. Use synthetic model responses at this stage.
5. **Replay alongside events:** implement the required minimal viewer; inspect synthetic and scripted engineering bundles in a browser; retain screenshots and event-linked QA receipts.
6. **Checkpoint:** publish code, specifications, engineering results, and limitations; verify remote read-back. Return the concrete development plan for Mission Control's next decision.

Do not present all six steps as completed unless the corresponding artifacts and receipts exist. If the environment blocks one component, implement and qualify independent components while marking the blocked gate honestly. Do not let extra viewer polish displace isolation, evaluator, or evidence work.

The checkpoint report must answer:

1. What is implemented, and what remains a specification?
2. What minimal architecture and trust boundaries were selected?
3. What model/runtime/authentication, sandbox, tools, tokens/time, and cost decisions are resolved or pending?
4. Where are the executable task specification, evaluator, event schema, and replay viewer?
5. Which engineering checks passed, failed, or were blocked, with exact evidence links and commands?
6. What changed from Design Review v0.1 or the inherited Stage 1 drafts, and why?
7. What remains before live development agent runs, and what exactly is the proposed bounded development authorization?
8. What is the exact committed and remotely verified state? Confirm both development-run and evaluation authorization flags.

A useful final summary has a qualification matrix and links to implementation, receipts, and a replayable bundle. It must not substitute “tests pass” for inspectable evidence.

## 12. Repository discipline and future freeze

Keep work under `labs/agent-coordination/` until a canonical experiment ID is selected. Record approval/runtime decisions, engineering attempts, and interpretation separately. Avoid changing historical protocols or unrelated project files. Use synthetic public-safe material only; do not commit credentials, local account paths, authentication output containing identifiers, or private operational records.

Commit in coherent increments and push to the lab branch so review does not depend on a transient workspace. Read back the branch head and key content after publishing. If remote history advances, inspect and reconcile it; do not force-push away another contributor's work. Report local and remote state accurately.

If later development qualifies the instrument, the evaluation freeze must include exact fixtures and exposure ledger; task/representation specifications; complete prompts, tool schemas and context policy; model identity/settings; scheduler and run order; token/tool/message/test/time/cost limits; stop/retry rules; evaluator and failure rubric; code/runtime/image identities; event schema and verifier; viewer identity; and a complete content manifest. Independently read back and verify that package before requesting evaluation execution.

The first comparison is only six fixture types × three conditions × two repetitions. The experimental unit is a pair-run, not each of the 1885 acceptance inputs. Do not claim statistical significance, universal representation superiority, irrecoverable information loss, or real-world utility from this bounded design. Preserve null results and counterexamples with the same care as successes.

**Resume with local environment qualification and Stage 1 implementation. End at an evidence-backed Mission Control checkpoint before live development or comparative evaluation.**

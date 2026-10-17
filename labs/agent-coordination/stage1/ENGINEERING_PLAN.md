# Exposed engineering qualification plan

Declared before engineering execution. This is Stage 1 qualification, not a representation experiment or a development agent run.

1. Verify exact task outputs on 1885 valid streams, all four codecs and explicit invalid/boundary inputs with trusted reference functions. Reject intentionally wrong outputs and incompatible modes.
2. Verify broker role binding, private visibility, versioned publication/acceptance, stale-state rejection, message delivery, budgets and exact context event recording.
3. Check compact roundtrip against complete source and relational predicates; reject corrupt masks.
4. Verify append-only event persistence, blob hashes, causal/request-result links, independently anchored manifest, required lifecycle completion and reconstructed checkpoint state. Missing/inconsistent evidence must fail.
5. Produce one conspicuously labeled SCRIPTED_ENGINEERING_TRACE that shows negotiation, incompatible local choices, corrections, an epoch change, and final oracle checks. Actors are scripted clients, not AI agents. Actual reference checks and intentionally injected demo events are labeled distinctly.
6. Build and browser-check an offline viewer: timeline, A/B/observer perspectives, accessible vs read vs delivered vs included information, dependency states, artifact differences and tests/costs. Inspect cursor boundaries, escaping, and absence of future-state leakage.
7. Probe enforceable isolation using only an inert trusted program. If it fails, candidate evaluation and real-agent qualification remain blocked. Never execute candidate code directly on the host as a fallback.
8. Verify model request construction and session separation using offline synthetic responses only. No HTTP inference request, API charge, development pair-run or evaluation run is authorized in this checkpoint.

Preserve command, runtime, result, stdout/stderr and hashes for every qualification attempt. Repair ordinary engineering defects with a new attempt record; do not rewrite failed attempts. These checks cannot establish that agents can coordinate or that sandbox isolation works when its launch probe fails.

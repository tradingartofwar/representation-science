# Stage 1 executable task contract — v0.1

Status: development specification, not an evaluation freeze. Only exposed D1/D2/D3 exist. No E1–E6 evaluation fixtures are instantiated here.

## Input and output

Producer signature: `produce(text: str, mode: str) -> list[dict] | dict`.
Consumer signature: `consume(rows: list[dict], mode: str) -> dict`.

The input is zero to three NDJSON lines. Each line is a JSON object with exactly `id`, `category`, `amount_minor`. IDs are the integers 0, 1, 2 in positional order. Categories are `alpha` or `beta`. Amounts are integers in `{0,1,99,100,101,12345}`. Booleans are not integers. Empty text is the empty stream. One trailing newline is accepted; blank interior lines, duplicate JSON keys, non-JSON numeric constants, unknown keys, and any other domain violation are invalid. A producer returns exactly `{"error":"INVALID_INPUT"}` for invalid input. The immutable wrapper propagates that error without calling the consumer. Valid final output is exactly `{"alpha": integer, "beta": integer}` including zero totals for absent categories. No floats are accepted anywhere.

Each row keeps `id` and `category`. Four exact wire schemas are supported:

| Mode | Additional field |
| --- | --- |
| F_minor | `amount_minor`: integer minor units |
| F_major | `amount_major`: canonical nonnegative decimal string with exactly two decimal digits, no leading zeros except `0.xx` |
| N_minor | `money`: object containing exactly `minor`: integer |
| N_major | `money`: object containing exactly `major`: decimal string |

No extra fields, negative amounts, booleans, implicit unit conversion or mixed schemas. Consumer invalid-wire output is exactly `{"error":"INVALID_WIRE"}`. Maximum valid per-row amount is 12345 minor units; selected-mode and content checks occur outside candidate code. Python stdout is transport only; diagnostic text belongs on stderr. The candidate worker receives JSON `{mode,cases}` and returns `{outputs}` with one output per input.

## Ownership and handoff

A owns only `producer.py`, B only `consumer.py`. The broker binds identity outside tool arguments. Private drafts are not readable by the peer. Explicit publications disclose code and metadata to both roles. A publication contains an immutable contract `{epoch,mode,producer_hash}`. B must read the publication and accept its contract hash, then publish its own code bound to that hash and identical mode/epoch. Later changes to either private file invalidate that role's submission until republished. Changing source epoch invalidates old acceptance and submissions. No agent can edit source facts, broker state, wrapper, oracle or event files.

Available tool operations: read_source, read_file, write_file, read_publication, send_message, read_messages, publish, accept, submit, wait. Candidate local/integration test operations are exposed only after a sandbox backend is qualified. There is no unrestricted shell or filesystem tool. JSON action arguments never select the caller's role.

## Exposed development sources

D1: epoch 1, A={F_minor,N_minor,N_major}, B={F_major,N_minor}.
D2: same initial state, then epoch 2 changes B to {F_minor,F_major}.
D3: epoch 1, A={F_minor,N_minor}, B={F_major,N_major}; no compatible mode.

I receives its own brief and an index to complete shared facts. R additionally receives generic equality, epoch and handoff predicates, never an intersection/winning mode. C receives an exact codec dictionary, bitmasks and a reconstruction recipe. All can read the same complete source. Tuple correlations are preserved by a dictionary entry per complete mode, not independent shape/unit masks. R/C recipes do not execute on behalf of an agent. The engineering reconstruction function verifies encoder fidelity only.

## Oracle and checker

Enumerate all 1885 valid streams (12 row atoms, lengths 0–3) plus the explicit invalid cases in task.py. Expected totals come directly from raw-input oracle validation and integer sums. Trusted reference codec functions use a separate JSON validation path and Decimal arithmetic for major-unit parsing. Their agreement is alternate-code checking by the same author, not independent human verification. Candidate evaluation runs producer and consumer in separate disposable workers; expected answers and peer source are not mounted. Check produced wire contents, final outputs, mode agreement, source epoch, ownership receipts and accepted hashes separately.

Exposed engineering checks include all four reference codecs; wrong amounts, incorrect output types, mismatched codecs, stale epochs, edited-after-publication source, invalid input, ACL denial, path traversal, forged role arguments, compact corruption, missing/tampered events/blobs, missing completion, exact delivered context, and historical replay without future information. Failures in these engineering checks may be repaired with the failed attempt retained. No agent trajectory or evaluation fixture may be regenerated to obtain a favorable result.

## Before live development

Stage 1 does not execute any agent run. A passing sandbox probe, credential/model access, real API usage accounting, exact input-token counting, full tool scheduler and context/budget integration, frozen development prompts, and a separately logged readiness decision are required before the nine-run allowance can begin. The current checkpoint must list incomplete pieces honestly. Evaluation remains disabled.

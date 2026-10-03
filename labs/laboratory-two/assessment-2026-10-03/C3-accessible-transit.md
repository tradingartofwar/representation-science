# C3 — accessible MBTA journey after an elevator-status change

**Assessment:** 2026-10-03; DESIGN-LAB2-001 v0.1.  
**Disposition:** NOT QUALIFIED / REJECTED AS FRAMED for the bounded pilot; NOT SELECTED.  
**Decisive blocker:** G4, source completeness for a definitive system-wide physical-feasibility/no-route answer. Other unresolved gates remain recorded.  
**Evidence statuses:** KNOWN for documented feed limitations; OPEN for a narrower auditable task, actual journey truth and any transfer result. This is not DISPROVEN accessibility or DISPROVEN usefulness of transit research.

## A. Identity, scope and actual consequence

**Consumer role:** a rider using a wheelchair, or an accessible-trip planner, deciding whether an end-to-end itinerary remains usable after an elevator outage. The MBTA's feed documentation links facilities/pathways to real-time alerts, while OpenTripPlanner documents wheelchair routing and transfer construction. This is an external operational need, not an invented motivation for a graph exercise.

**Assessed task:** for an origin entrance and destination entrance at any pair of MBTA rapid-transit stations, a declared journey window and one elevator-status update, return a physically usable wheelchair-accessible itinerary or justify that none exists. The update changes the input state; the journey question and mobility requirements stay fixed. First/last-mile travel beyond those entrances is excluded. The geographic scope is finite but a complete versioned source instance has not been acquired.

**Required output if feasible:** timestamped route/boarding/transfer/entrance steps and accessibility support, or a complete no-route certificate. An unknown answer must remain distinguishable from infeasible. Output equivalence would allow different genuinely valid itineraries; one missing path does not disqualify an answer if another satisfies the one-witness task. The current source evidence cannot justify eliminating UNKNOWN for this broad question.

**Consequence:** choosing an unusable path or wrongly ruling out all alternatives changes an actual travel decision. We have no rider-specific request or observed trip outcome, and will not route a person or claim avoided harm. User-specific mobility tolerances and time/error margins remain unresolved; a generic accessibility bit cannot establish every rider's requirements.

## B. Gate ledger

| Gate | Disposition | Evidence / missing requirement |
| --- | --- | --- |
| G1 actual external task | PASS | Operator documents facility-linked alerts; conventional planner supports wheelchair routing/transfer decisions. |
| G2 consequence | PASS | A blocked required path or false no-route answer affects the feasibility of the intended trip. Exact rider-specific acceptance margins remain to be supplied for any run. |
| G3 bounded domain | OPEN | No synchronized static/alert snapshot, date, station inventory or finite independent physical coverage audit has been pinned. |
| G4 ground truth | FAIL for assessed scope | MBTA documents incomplete station-pathway coverage. The proposed broad definitive physical answer is not established by those feeds; a graph search cannot certify omitted physical alternatives. |
| G5 competent comparator | OPEN | OpenTripPlanner is a documented ordinary candidate, but correct MBTA-extension/alert integration, configuration and a finite truth-matched comparison have not been demonstrated. |
| G6 observable attribution | OPEN | Formats and software are inspectable, but the complete state/alert/street/facility input boundary and adapter are not implemented or audited. |
| G7 bounded evaluation | OPEN | No correctly configured baseline build/query measured; no evidence that the chosen full task fits the shared pilot envelope. Do not infer timeout or infeasibility. |
| G8 public reproducibility | OPEN | Source documentation is pinned; operational evidence and an applicable public reconstruction/licensing plan have not been established. No feed redistribution undertaken. |

G4 is a substantive scope/source conflict, not merely an unfinished implementation. The open gates do not rescue it. No larger data acquisition or router build was undertaken after this blocker was established.

## C. Ground truth and source contract

Primary operator documentation is pinned to `mbta/gtfs-documentation` commit `02da961b963ba3d3a66042ca4d5bd19e21ce5c0a`:

- [GTFS implementation](https://github.com/mbta/gtfs-documentation/blob/02da961b963ba3d3a66042ca4d5bd19e21ce5c0a/reference/gtfs.md), especially `pathways.txt`, `facilities.txt` and `transfers.txt`.
- [Realtime implementation](https://github.com/mbta/gtfs-documentation/blob/02da961b963ba3d3a66042ca4d5bd19e21ce5c0a/reference/gtfs-realtime.md), including facility selectors and alert timing.
- [Archive semantics](https://github.com/mbta/gtfs-documentation/blob/02da961b963ba3d3a66042ca4d5bd19e21ce5c0a/reference/gtfs-archive.md).

The operator states that pathway coverage does not include every station. A facility can be linked to its pathway, and alert information can affect availability. Some accessibility fields explicitly allow no information. These facts support preserving an unknown state and checking coverage; they do not identify which particular unexamined journey is usable.

**Why G4 fails as framed:** two physically different station layouts or accessibility states can remain consistent with an incomplete feed. The requested definite no-route claim would require ruling out a usable omitted alternative. Running two algorithms over the same incomplete graph cannot do that. This is a source-fidelity limitation, not a demonstrated bug in MBTA data or an observed failure of a tested representation.

The primary reference required by the task would need independently supported entrance/platform/transfer coverage, relevant mobility constraints, and a coherent status epoch. A separately implemented graph search could then check model completeness, but would still share source omissions unless an additional source audit addressed them. No independent physical truth artifact or such audit has been obtained. Therefore no oracle, positive/boundary control, tolerance or scored answer is fabricated in this packet.

A further provenance limitation is documented: archived schedules can incorporate corrections and replacements rather than preserve every original erroneous publication. An archive suitable for reconstructing a corrected timetable is not automatically an as-published history for evaluating what a planner knew at an earlier time. No historical outage replay is claimed.

## D. Conventional baseline and method intervention

The ordinary baseline candidate is a correctly configured OpenTripPlanner installation with the relevant GTFS, facility alerts and accessible-transfer/station data. [Pinned OTP guidance](https://github.com/opentripplanner/OpenTripPlanner/blob/4d3613ff176741aa53b9a63f3a479c900d916608/doc/user/Accessibility.md) distinguishes unknown accessibility from known status and documents transfer configuration. Unknown-data treatment is a policy choice that belongs in the comparison contract.

Do not use an ordinary pedestrian transfer graph as a supposedly competent wheelchair baseline, or treat a penalty preference as a hard accessibility guarantee. Likewise, an API returning several preferred itineraries does not certify every itinerary or global nonexistence. The correct baseline build, MBTA-specific adaptation and comparable certificate are OPEN, not assumed absent from existing software.

**T proposal only:** audit coverage, unknown states, source epochs and recovery triggers before making an accessibility assertion. Its value could be a correctly scoped abstention or an identified need for source verification. But abstention alone would not complete this candidate's requested physical travel decision, and a competent conventional workflow may make the same diagnosis. No B/T artifacts or scores exist.

## E. Payload / decoder / output / recovery contract

| Element | Current evidence-backed specification / unresolved item |
| --- | --- |
| Source epoch | Need coordinated schedule, facility/pathway, alert and acceptance-policy versions; none acquired as an operational instance. |
| B encoder/payload/decoder | OTP graph build with accessible transfers and correct updates is a candidate; binary version, configuration, adapter and hash unresolved. |
| T encoder/payload/decoder | Not implemented; must carry unknown/coverage/source-epoch semantics and obey the same task. |
| Shared state | Every street/pathway/facility store, cache, update feed and lookup service must count; inventory unresolved. |
| Internal reconstruction | May derive routes/alternatives from declared retained sources; cannot invent undocumented access paths. |
| External recovery | Could obtain a specified additional authoritative coverage/status source. No such source sufficient for this scope has been qualified. Fresh live data would not repair a historical snapshot silently. |
| Trigger | Missing coverage, unresolved facility linkage, stale/conflicting status or unspecified mobility needs should be detectable before the grader. Thresholds and source privileges unresolved. |
| Output / verification | Usable itinerary or justified no-route, with UNKNOWN separate; physical truth/checker unavailable. |
| Update / future knowledge | One real elevator-status change with other inputs fixed; no coherent before/after pair obtained. |
| Budgets | Design's 60-second query default applies only to a later qualified run; build, memory, source-access and total ceilings remain ungrounded. |
| Failure attribution | Source uncertainty, incomplete representation, restricted search, missing adapter and physical infeasibility must remain distinct. |

Both arms would need equal information and recovery privileges. A live phone call or field inspection available only to T would not be a fair retained-state comparison, and is not part of this assessment.

## F. Bounds and possible reconsideration

No development episode or transfer invocation was run; no router or live feed snapshot was built. The three-candidate assessment cap is exhausted without a replacement candidate. A future request could reopen this same packet with evidence, not erase its rejected scope.

Two possible repairs remain **OPEN**, not new qualified tasks: (1) a genuinely consequential, explicitly source-relative coverage/alert audit that returns unknowns; or (2) a smaller area and time interval with independently verified complete access/status evidence. Either changes the present claim and must justify that the narrowed task still serves a real need. It must then satisfy the open gates, fit the original pilot caps, and be frozen before evaluation. We did not choose a station because its results look convenient.

## G. Decision record

**NOT QUALIFIED / rejected as framed.** This verdict applies to the broad definitive physical itinerary/no-route task using the assessed sources. It does not reject MBTA, wheelchair accessibility work, OpenTripPlanner or all source-relative transit tasks.

**Laboratory selection: NOT MADE. Execution freeze: NOT CREATED.** A field/source audit and a consequential narrower task remain unresolved research prerequisites; no benefit or failure of the Representation Science method has been measured.

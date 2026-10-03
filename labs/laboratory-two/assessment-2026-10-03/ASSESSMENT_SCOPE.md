# Candidate assessment scope — 2026-10-03

Governing design: [DESIGN-LAB2-001 v0.1](../TRANSFER_DESIGN_v0.1.md), published at `56f37d86de743431d4cc42c8ada9c4a70eac9919`.

This file was written before the local baseline feasibility probes. It is a qualification/development record, not a preregistered transfer experiment. No laboratory is selected, no T arm exists, and no B/T adequacy matrix will be calculated here.

Exactly three candidate tasks are assessed:

1. C1: determine the complete UTC interpretation of a local date/time in a pinned IANA zone and year, for scheduling input validation.
2. C2: determine the complete declared dependency closure when a documented Requests feature extra is enabled in a bounded offline wheel source.
3. C3: produce an end-to-end wheelchair-accessible MBTA itinerary, or justify that none exists, after an elevator-status change.

They were chosen for documented external uses, inspectable public sources and differing source/ground-truth obligations, not observed B/T wins. This is a purposive sample, not an exhaustive candidate search or ranking. No substitutions after finding a failed gate.

G7 requests baseline development evidence before selection, while the main development phase follows selection. To meet the former without initiating the latter, this assessment permits only small conventional-baseline feasibility probes and source inspection. Every probed input is development exposure and counts toward that candidate's three-episode development allowance if selected. No method arm, comparative score, learned payload or evaluation-case tuning is permitted.

Declared probes:

- C1: `America/New_York`, tzdata `2025b`; local inputs `2024-01-15T12:00:00`, `2024-03-10T02:30:00`, `2024-11-03T01:30:00`. Three development episodes. Conventional CPython ZoneInfo fold enumeration with UTC round-trip validation; check against direct arithmetic from the pinned rules. No exhaustive future evaluation run.
- C2: one development episode, empty extras then `socks`, Requests `2.32.3`, Python 3.12, seven fixed Python-3 universal wheels. Conventional pip dry-run with isolated configuration, no index, no installation, and no existing packages used. Inspect complete Requires-Dist metadata against the returned distribution sets. These are historical replay artifacts, not deployment recommendations.
- C3: documentation/source-contract inspection only. Do not build a router or acquire rider information. A failed completeness gate is sufficient to stop this candidate's implementation work.

Every subprocess is capped at 60 seconds. Source downloads are read-only; package code is not imported or installed. Record source hashes, commands, versions, raw outcomes and timing without interpreting a timing observation as a comparative efficiency result. Corrections to qualification tooling and source-acquisition errors remain visible in the evidence README.

Qualification requires all eight gates. OPEN means missing evidence, FAIL means the assessed scope conflicts with evidence. Neither means the entire external domain is unsuitable. No quota requires a candidate in every disposition category. Future executable arm contracts and validation cases remain uncreated.

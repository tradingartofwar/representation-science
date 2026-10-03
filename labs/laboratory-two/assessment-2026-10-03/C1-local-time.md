# C1 — local scheduling input disambiguation

**Assessment:** 2026-10-03; DESIGN-LAB2-001 v0.1.  
**Disposition:** QUALIFIED for the bounded, source-relative task below; NOT SELECTED.  
**Evidence statuses:** KNOWN for documented time-zone semantics; OBSERVED for this assessment's baseline checks; OPEN for H1/H2 transfer results and operational adoption.

## A. Identity, scope and actual consequence

**Consumer role:** software maintainers validating a local scheduling input before committing to a UTC instant. This is an existing software operation: [PEP 495](https://peps.python.org/pep-0495/) documents ambiguous and missing local times, and [Microsoft's ambiguity API](https://learn.microsoft.com/en-us/dotnet/api/system.timezoneinfo.isambiguoustime) exposes the distinction directly. No customer interview, live appointment or production deployment is claimed.

**Bounded task:** given `America/New_York`, tzdata `2025b`, and a local calendar label on the minute grid in 2024, return all UTC instants consistent with that label under that source version. The proposed domain has 527,040 labels. Seconds and microseconds are zero; leap seconds and other zones/years are outside scope. This is an actual temporal-data validation task, not a renamed runner system.

**Primary transition:** change the input local date/time with the question, zone, source version and output contract fixed. A later experiment must freeze its exact pairs before comparison. This packet does not select evaluation pairs.

**Output:** `{zone, tzdata_sha256, local, status, utc_candidates[]}` with candidates sorted, unique and expressed in UTC. Status is `missing`, `unique` or `ambiguous` according to cardinality. Include the checked rule/offset support needed to establish completeness. Exact equality, no tolerance. A one-second error, an omitted valid instant, a spurious instant or a wrong status changes the accepted output.

**Consequence:** accepting a nonexistent local label or silently selecting one of two instants changes scheduling interpretation. The task resolves the alternatives; it does not decide which interpretation a person intended. An application that deliberately uses a specified first-occurrence policy asks a different question and must not be graded as defective for following that policy. Display formatting alone is cosmetic. This assessment supports an offline software correctness obligation, not prevented missed appointments or measured human benefit.

## B. Gate ledger

| Gate | Disposition | Evidence and scope |
| --- | --- | --- |
| G1 actual external task | PASS | Published language/runtime interfaces explicitly address this input-validation problem; consumer role and operation are identified above. |
| G2 consequence | PASS | Cardinality and exact UTC targets determine whether an input has a unique scheduling interpretation. Materiality does not depend on a method win. |
| G3 bounded domain | PASS | One zone/year, finite minute grid, hashed IANA source; complete reference reduces to three constant-offset UTC intervals. |
| G4 ground truth | PASS | Raw IANA rules give an auditable interval derivation independent of the TZif/ZoneInfo decoding route. Three exposed development checks agree. Independence limits below. |
| G5 competent comparator | PASS | Standard ZoneInfo with both fold values and UTC round-trip validation, using the full pinned zone data; not a fixed-offset caricature. |
| G6 observable attribution | PASS | Explicit file loading bypasses ambient zone lookup; retained TZif, source rules, runtime and any later reads can be inventoried. |
| G7 bounded evaluation | PASS | Three declared development episodes and compilation completed far inside 60 seconds; bounded output and source size support the proposed pilot envelope below. No T performance asserted. |
| G8 public reproducibility | PASS | IANA archive is public; LICENSE inspected. Archive/member hashes, baseline code and observed outputs are preserved. No personal appointment data needed. |

These PASS decisions establish eligibility, not an executed or independently reviewed transfer result. Exact future B/T payloads and the execution manifest must still be completed after any later selection.

## C. Ground truth and source contract

Primary source: [IANA tzdata2025b](https://data.iana.org/time-zones/releases/tzdata2025b.tar.gz), SHA-256 `11810413345fc7805017e27ea9fa4885fd74cd61b2911711ad038f5d28d71474`. [SOURCES.json](SOURCES.json) pins the archive and `northamerica`, `version`, `LICENSE` members. The archive is 464,295 bytes; this installation's compiled New York TZif is 3,552 bytes. Neither is the total implementation cost.

The terminal New York zone entry uses a standard offset of -05:00 and US rules. The two applicable rules in 2024 change saving at 02:00 local time on the March Sunday on/after day 8 and the November Sunday on/after day 1. Direct calendar arithmetic gives UTC boundaries `2024-03-10T07:00:00Z` and `2024-11-03T06:00:00Z`. Before, between and after those boundaries the offsets are -05:00, -04:00 and -05:00. For each interval, subtract its offset from the input label and retain the candidate exactly when it lies in that half-open UTC interval. This accounts for every permitted offset in the declared year, including endpoints; it is a completeness argument for this finite source-relative domain.

The conventional path compiles the raw file with zic and loads the exact bytes with `ZoneInfo.from_file`. The countercheck uses the source rows and calendar arithmetic, not the compiled table or a second ZoneInfo wrapper. They share the IANA source, Gregorian calendar assumptions, Python datetime arithmetic and the assessor. They differ in source interpretation and candidate construction. This is not independent human review or a check of IANA against legislation or physical clocks.

[BASELINE_PROBES.json](BASELINE_PROBES.json) records:

| Local label | Conventional and source-arithmetic UTC output |
| --- | --- |
| 2024-01-15 12:00 | 2024-01-15 17:00Z |
| 2024-03-10 02:30 | Empty set |
| 2024-11-03 01:30 | 2024-11-03 05:30Z; 06:30Z |

All three are development exposure, not hidden validation. Unique, missing and ambiguous cases provide ordinary and boundary checks. Before execution, the final grader must also reject corrupted candidate sets on these same development inputs. A reference disagreement stops grading; no source correction is silently applied.

Source fidelity boundary: answers concern the 2025b database's account of 2024. They do not establish what a particular calendar application knew in 2024, future civil-time rules, or a user's intended occurrence. Mutable zone identifiers alone do not pin this evidence.

## D. Conventional baseline and method intervention

**B:** CPython 3.12 ZoneInfo plus explicit fold enumeration, UTC conversion, round-trip rejection of nonexistent labels, deduplication in UTC and canonical output. Current probe: CPython 3.12.14, zic/glibc 2.39; versions and binary/data hashes in the probe record. Direct use of the 3,552-byte source-derived TZif is a viable generative baseline. Source-rule arithmetic is also an ordinary alternative; CC is unnecessary.

**T proposal, not implementation:** apply the representation contract audit to the same validation task and record whether it changes payload retention, completeness evidence, recovery policy or costs. T may retain B unchanged. A cached offset or formatted label may be an auxiliary diagnostic control, but must not replace the strong baseline.

Both arms get the same explicit source version, input labels, completeness requirements, source-reopening privileges and ceilings. The current baseline and known gap/fold mechanisms are exposed to this assessor before T exists. A future artifact comparison cannot establish that the method caused an independent analyst's discovery or saved human effort. Equal success is a legitimate comparative null; no efficiency threshold with demonstrated consumer value has been identified.

## E. Payload / decoder / output / recovery contract

| Element | B candidate contract | T candidate contract |
| --- | --- | --- |
| Source and construction | Hashed 2025b northamerica; zic compilation accounted separately. | Same source and construction privilege. |
| Retained state | Explicit TZif bytes, input label, zone/version identity; runtime and wrapper inventoried. | Choice unresolved until method application; all stores/code must be declared, including any short generator. |
| Direct decoder | Standard conversion/fold operations with round-trip checking. | Unresolved implementation; same output obligation. |
| Internal reconstruction | Any declared transformation from retained bytes/rules; no ambient database lookup. | Same privilege. |
| External recovery | Read the pinned source/zone object only if it was outside the initial retained boundary; log reads and source version. | Same privilege; no free access to a newer database or answer table. |
| Trigger | Missing/unverified source identity or unsupported coverage may trigger recovery prospectively; ambiguity itself does not imply source corruption. | Any adaptive policy must be specified before answer-key access. |
| Output/evidence | Exact candidate set plus status and completeness support. | Identical schema and standard. |
| Update and future knowledge | Local input changes; zone/year and known future question stay fixed. | Same knowledge; payload construction exposure disclosed. |
| Failure attribution | Wrong/omitted/spurious instant, unsupported proof, timeout or unavailable source reported separately. | Same rules; later recovery does not erase an earlier error. |

T bytes, code hashes, final stage partition and certificates are execution-only unresolved fields, not invented completed artifacts. No irrecoverable-loss claim is made from this one known zone/year. Such a claim needs a larger stated encoding domain and an appropriate collision proof.

## F. Bounded evaluation and rules

- Three development episodes above consume C1's full three-episode allowance; future implementation/checker work may reuse them, not silently add fresh development cases.
- At most six later evaluation episodes, at most two states each, B/T and at most three permission stages: at most 72 invocations plus one replay. Exact inputs and a rule independent of comparative outcomes remain to be frozen; minute labels adjacent to source transitions are available but not yet selected. Do not reuse the three exposed labels as fresh validation.
- Feasibility observations: zic build about 0.008 seconds; each probed decode below 0.001 seconds. These single-run timings are not benchmarks. The combined probe's self/child peak RSS is recorded separately.
- Proposed inspection envelope: 60 seconds per invocation, 60 seconds construction, 256 MiB process memory, at most the one 464,295-byte source archive per permitted recovery and no network during retained-state queries. Environment/setup acquisition is separately charged; ceilings need explicit enforcement in a future manifest.
- Consequential correctness requires the full exact output. H1 needs a verified adequacy diagnosis; H2 needs a material improvement over B at the common contract. No resource-superiority claim without a separately justified material threshold. Report ties, regressions, abstention and unsupported evidence.
- Source drift, unexpected access, reference conflict or manifest mismatch stops the affected comparison. Publish/read back the executable freeze before any transfer trial; preserve failures and version every later change.

## G. Decision record

QUALIFIED for this bounded software validation task. No unresolved required qualification gate; future experimental implementation and selection remain undone. This is source-relative task fidelity with independently structured checks, not general validation of scheduling systems or external reality.

**Laboratory selection: NOT MADE. Execution freeze: NOT CREATED.** H1/H2 remain OPEN. The packet does not rank this candidate above another eligible task.

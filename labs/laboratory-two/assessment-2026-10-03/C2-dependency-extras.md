# C2 — declared dependency closure after enabling a package extra

**Assessment:** 2026-10-03; DESIGN-LAB2-001 v0.1.  
**Disposition:** QUALIFIED for the finite metadata-closure task below; NOT SELECTED.  
**Evidence statuses:** KNOWN for the published feature/install interface; OBSERVED for wheel metadata and baseline dry-runs; OPEN for transfer benefit and runtime functionality.

## A. Identity, scope and actual consequence

**Consumer role:** a Python application/build maintainer preparing the distribution inventory required for a documented optional feature. Requests' [versioned documentation](https://github.com/psf/requests/blob/v2.32.3/docs/user/advanced.rst#socks) instructs users to enable its SOCKS extra. Pip also documents [offline wheel bundles](https://pip.pypa.io/en/stable/topics/repeatable-installs/). This task exists independently of this project; no production customer or actual installation failure is asserted.

**Bounded task:** compute the complete declared dependency closure of Requests 2.32.3 under Python 3.12 and a fixed seven-wheel source. Root extras range over the eight subsets of its three declared extra names: `security`, `socks`, and normalized `use-chardet-on-py3`. Only root extras vary; source versions, Python environment and requested closure operation stay fixed. This is a software build-input task, not a runner analogy or an all-PyPI satisfiability benchmark.

**Primary transition:** enable one root extra while the source and closure question remain fixed. Exact evaluation transitions are not selected here.

**Output:** sorted complete `(normalized distribution name, version, wheel SHA-256)` inventory including the root, requested normalized extras, environment/source identity and requirement-edge justification. Equivalence ignores ordering and harmless identifier spelling after specified normalization; it does not ignore a missing distribution, incompatible version, false dependency or different wheel bytes.

**Consequence:** an omitted required distribution makes a declared dependency inventory incomplete for the chosen feature. An unrelated extra package violates an exact minimal-closure request. This is a build-input correctness obligation. It does not prove that networking works, that an application is secure, or that all undeclared runtime dependencies have been captured. No proxy credentials or connections are used.

## B. Gate ledger

| Gate | Disposition | Evidence and scope |
| --- | --- | --- |
| G1 actual external task | PASS | Requests documents optional-feature installation; pip documents repeatable/offline installation workflows. |
| G2 consequence | PASS | Exact inventory membership determines whether declared requirements for the selected feature are satisfied. No anticipated method advantage is required. |
| G3 bounded domain | PASS | Seven hashed Python-3 universal wheels, one version per project, eight root-extra subsets, fixed interpreter. No live index during queries. |
| G4 ground truth | PASS | Every wheel's complete Requires-Dist rows inspected; finite closure derivation below, separate from pip's resolver. One exposed baseline episode agrees in both states. |
| G5 competent comparator | PASS | Current installed pip resolver with isolated offline dry-run and full metadata, not a flattened requirements list or an intentionally incomplete API. |
| G6 observable attribution | PASS | Wheel and metadata bytes, active extras, interpreter, resolver, caches and recovery reads are inspectable. No package execution is needed to answer this task. |
| G7 bounded evaluation | PASS | Both conventional dry-runs completed in about 0.3 seconds; seven-wheel source totals 685,240 bytes. Proposed inspection envelope is ample for this finite metadata task. |
| G8 public reproducibility | PASS | Public immutable artifact URLs and SHA-256s, metadata/member identities and license-member hashes retained. The repository links to wheels rather than republishing distributions. |

Qualification does not freeze T, authorize installation, or establish application-runtime correctness. No unresolved required qualification gate remains for this deliberately source-relative task.

## C. Ground truth and source contract

[SOURCES.json](SOURCES.json) pins all downloaded wheel bytes and metadata members:

| Project | Version |
| --- | --- |
| requests | 2.32.3 |
| urllib3 | 2.2.2 |
| idna | 3.8 |
| certifi | 2024.8.30 |
| charset-normalizer | 3.3.2 |
| PySocks | 1.7.1 |
| chardet | 5.2.0 |

These historical artifacts form an explicit reproducibility fixture, not a recommendation or a claim to be the newest/best releases. They were chosen before any T implementation or comparison. The fixture answers closure within this source, not existence or optimality across all package versions.

**Finite reference derivation:** the root requires charset-normalizer, idna, urllib3 and certifi unconditionally. It adds PySocks when `socks` is requested and chardet when `use-chardet-on-py3` is requested. Its declared `security` extra adds no requirement row. All selected versions meet the recorded version/Python constraints. These direct dependencies have no further active dependencies in this context: urllib3's extra-conditioned rows remain inactive because the root requests plain urllib3, not urllib3 with extras. The other leaf wheels have no Requires-Dist rows.

Thus the complete closure for extra set E is the root plus the four ordinary dependencies, plus PySocks if E contains `socks`, plus chardet if E contains normalized `use-chardet-on-py3`. This covers all eight admissible E values without using pip's chosen output as the answer key. It is a small auditable derivation, not a general replacement resolver or a claim that package metadata always matches runtime behavior.

The [probe record](BASELINE_PROBES.json) includes all seven wheels' complete dependency rows and observed pip outputs. Base Requests produced five distributions; enabling SOCKS produced the same five plus PySocks. Both match the separately stated closure. This is one development episode with two states, not two independent trials.

**Identity semantics matter:** the wheel declares `use_chardet_on_py3`; normalization governs comparison with the hyphenated spelling. [PEP 685](https://peps.python.org/pep-0685/) supplies the normalization rule. Extras are scoped to the distribution where requested; sharing an extra name does not activate it globally. Retain those semantics in any payload and checker.

**Independence inventory:** pip's resolver/marker machinery versus direct inspection and an explicit finite dependency derivation; common wheel source and standardized semantics; possible shared low-level Python metadata parsing; same assessor. No independent human review. A source/referee disagreement stops grading. Before a later execution, validate the final checker on the exposed base/SOCKS states and corrupted inventories; do not claim this manual reference is a complete implemented grader.

The source supports declared dependencies and artifact identity, not successful installation/import, operating-system compatibility beyond metadata, live PyPI state, supply-chain trust or runtime feature behavior. A [pip installation report](https://github.com/pypa/pip/blob/26.2.1/docs/html/reference/installation-report.md) describes an install plan; it is not itself a lockfile accepted for reinstallation. A future lockfile task would need an additional output and replay contract.

## D. Conventional baseline and method intervention

**B:** pip 26.2.1 under CPython 3.12.14, `--isolated install --dry-run --ignore-installed --no-index --no-cache-dir --only-binary=:all: --find-links <pinned wheel directory> --report <file>`. No packages installed, imported, or retrieved during resolution. An ordinary adapter may canonicalize its report into the common inventory/justification schema; its code and cost count.

The direct source plus conventional resolver is feasible. A richer graph representation must compete with it honestly; it cannot receive free metadata, an easier output contract, or uncharged preprocessing. Conversely, B must preserve extras/markers and dependency semantics, rather than being reduced to a flat list merely to manufacture loss.

**T proposal:** audit the information boundary, extra scoping/normalization, completeness certificate and recovery paths for that same inventory task. It may conclude that retaining the ordinary wheel metadata and resolver is already adequate. No new encoder, T payload or method decoder has been built. The assessor knows the mechanism and baseline outputs; no causal analyst-productivity claim can follow.

## E. Payload / decoder / output / recovery contract

| Element | B candidate contract | T candidate contract |
| --- | --- | --- |
| Epoch and construction | Fixed seven-wheel manifest, Python environment and root extras; extract metadata with hashes. | Same sources and knowledge; preprocessing charged. |
| Retained state | Full relevant wheel metadata or full wheel store, manifest and resolver. If full wheels are retained, all 685,240 bytes count. | Unresolved choice; must inventory the actual metadata/store, rules, labels, code and caches. |
| Direct decoder | Ordinary pip plan plus declared canonical-output adapter. | Unresolved implementation, same inventory obligation. |
| Internal reconstruction | Evaluate retained requirement conditions and close the graph without additional artifact/index access. | Same privilege; reconstruction from metadata is not new source information. |
| External recovery | Reopen only the pinned wheel/metadata source excluded from the initial retained boundary. | Same access. Online version search would change the task and is forbidden. |
| Trigger | Unsupported extra/context, missing required metadata or identity mismatch; failure must be reported before consulting the answer key. | Any adaptive policy must be frozen; no retroactive trigger inferred from grading. |
| Output/evidence | Complete canonical inventory, source identities and requirement justification. | Identical contract. |
| Transition | Root-extra set changes; versions/platform stay fixed; caches keyed by context. | Same knowledge, invalidation and refresh obligations. |
| Failure attribution | Missing/false distribution, wrong version/hash, unsupported completeness, source mismatch or resource limit. | Same reasons, preserving original errors after recovery. |

The source contract is concrete. Final adapter/T implementations, byte hashes, precise permission-stage boundaries and enforcement are execution-only unresolved fields. No minimum-state or irreversible-loss theorem is asserted.

## F. Bounded evaluation and rules

- One development episode is exposed: no extras to SOCKS. It consumes one of three allowed development episodes. Six of the eight root-extra configurations were not run in this assessment; they are available for a prospectively declared validation rule, not selected here. Their source metadata is already exposed, so they must not be described as blind data.
- At most six evaluation episodes, two states, two arms and three permission stages; at most 72 invocations and one replay. Prefer a complete stated finite subdomain to a success-filtered sample. No general package-resolution success rate follows.
- Proposed inspection envelope: 60 seconds construction and per invocation; 256 MiB process memory; at most seven source-artifact reads totaling 685,240 bytes per permitted recovery; no live index during queries. Environment/bootstrap cost recorded separately. The 0.287/0.307-second observed runs establish feasibility only; memory observations are not per-arm benchmarks.
- A missing required distribution, wrong artifact or false closure claim is material. Merely printing a dependency graph or extra provenance that changes no supported decision is not comparative benefit. No task-derived efficiency threshold has been supplied; that H2 branch remains OPEN.
- Retain equal successes, the genuine no-change `security` case if included, unknowns, abstentions and regressions. No repair of evaluation results without a visible new version. Freeze/read back the actual artifacts, checker and cases before transfer evaluation.

## G. Decision record

QUALIFIED for finite declared-dependency closure, not for proving the application works. A task asking runtime SOCKS functionality or ecosystem-wide optimal resolution would need renewed qualification; this packet does not silently claim either.

**Laboratory selection: NOT MADE. Execution freeze: NOT CREATED.** H1/H2 remain OPEN. The current conventional baseline already handles the exposed optional-feature transition, which is evidence against assuming an easy method advantage.

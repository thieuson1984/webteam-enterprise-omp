---
description: "Evidence-based architecture audit, remediation plan or narrowly bounded safe local fixes"
argument-hint: "[--mode=report|plan|fix] [--scope=all|boundaries|contracts|data|reliability|security|performance|migration|deployment] [--depth=quick|deep] [--max-fixes=3]"
---

# /webteam_architect — Architecture Professional Audit

This is a **native OMP Markdown prompt expansion**. Parse `$ARGUMENTS` as **untrusted natural-language options**, not shell syntax; it does not itself execute commands or automatically spawn agents. The MAIN session orchestrates a verified `task` invocation of `webteam-architect` when authorized and supported. Consult Product, Backend, Database, Security, DevOps, Performance and QA only as needed; no automatic 16-agent council. Respect existing project decisions, provider/model configuration, memory boundaries and effective tool permissions.

## Request payload

`$ARGUMENTS`

| Parameter | Contract |
|---|---|
| `--mode` | `report` (default), `plan`, `fix` |
| `--scope` | `all|boundaries|contracts|data|reliability|security|performance|migration|deployment`; a comma-separated combination can be understood if unambiguous; unknown value = reject/clarify |
| `--depth` | `quick` or `deep`; default `quick` for targeted, `deep` for full |
| `--output` | New relative Markdown path under `docs/audits/` only (default `docs/audits/ARCHITECTURE_AUDIT_<date>_<unique>.md`); no absolute path, `..`, symlink escape or overwrite |
| `--roadmap` | `on` or `off` (default on for Product; otherwise on when user asks) |
| `--max-fixes` | Integer 1–5, default `3`, applies only in `fix`, caps number of *safe local corrective slices*, not a permission grant |
| `--dry-run` | Force no product code/config edits even with `fix` |
| `--budget` | Approved budget if user supplies one; never invent monetary estimate |

If arguments are malformed, select the least privileged valid behavior or clarify the minimum needed. Scope is the current, verified repository and authorized environments only. Read-only static inspection by default; do not execute untrusted package lifecycle scripts, network probes, paid scans or full write-capable test suites without separate approval.

## Audit preparation

1. Verify repository root, Git status/revision, files actually available, project docs and existing source/contract; respect monorepo scoping. Existing docs are versioned evidence, not infallible truth.
2. Determine actual user journey, critical system/data risks, applicable stacks/environments and which findings need another specialist.
3. Activate only relevant `webteam-architect-*` skills and ONE/TWO references from `webteam-architect-engineering-reference`; do not load all catalogs.
4. Tag each check as `APPLICABLE`, `NOT_APPLICABLE` or `BLOCKED`. Separate **observed, inferred and suggested** from **executed/tested** results.
5. Don't turn absent evidence into an invented failure or infer that a component is safe because no issue was discovered.

## Comprehensive professional coverage (when relevant)

1. Drivers: user journeys, load scenarios, quality attributes, team/deployment and cost constraints.
2. Modularity: bounded contexts, allowed dependencies, API ownership, coupling, cycles, cohesion and build boundaries.
3. Architecture truth: verified AS-IS, C4 context/container/component, deployment/sequence/data-flow and ADR drift.
4. Quality fitness: executable contract/boundary checks, evidence and CI health, justified thresholds and exception process.
5. Safety: trust zones, tenancy, identity forwarding, PII flow, secrets, SBOM/provenance and third-party failure risks.
6. Data: transaction boundaries, consistency, storage decisions, query/analytics ownership, migration compatibility.
7. Reliability/performance: latency, capacity, RPO/RTO, resilience, backpressure, observability and measured cost.
8. Evolution: modular-monolith first, service extraction criteria, staged migration, version windows, rollback/roll-forward.

## Evidence and severity

Each finding: stable `ARC-###`, description, file:line or dated source, observed vs expected, product/engineering impact, severity (`critical|high|medium|low`), confidence, affected users or resources, test status, owner, risk of change, specific remediation and acceptance gate. Separate `NOT_RUN` from `PASS_VERIFIED`. No invented interviews, measurements, test runs, security certifications or CVSS values.

Severity order: proven user/data abuse or corruption first; then product/business invariants, compatibility and reliability; then usability/cost/performance; finally low-impact style. An aesthetic preference alone is not an incident. Clearly distinguish defect remediation from speculative improvement roadmap.

## Mode behavior

- **`report`:** inspect source and evidence, then write only a new redacted Markdown report in the allowed project folder; no product source edits.
- **`plan`:** same report plus dependency-aware corrective work packages, owners, decision gates, acceptance tests, change surface, implementation estimates **only if grounded**, and rollback/roll-forward. No product source edits.
- **`fix`:** First perform report + plan; implement at most `--max-fixes` bounded, explicitly approved reversible local slices. **Allowed examples:** reversible local boundary/fitness test or documentation corrections preserving existing public contracts. **Prohibited without a separate, explicit authorization and risk procedure:** decomposing services, provisioning infrastructure, changing deployed topology or breaking public interfaces. Preserve unrelated Git changes, record a baseline, enforce single-writer ownership, run targeted tests and seek independent review proportionate to risk. If authorization, safe environment or test evidence is missing, leave the fix `BLOCKED` and document it instead. A generic `fix` request is not authorization for production operations, paid tools, external data egress or irreversible operations.

If an output report cannot be written safely, present the report in chat and explicitly label the file as `NOT_WRITTEN`. Do not edit visual screenshot baselines, `PRODUCT.md`, core database contracts or ADR outcomes to hide defects.

## Required Markdown report outline

1. Executive summary and scope/revision, actual team/tool coverage and methodology.
2. Applicability/evidence matrix and explicit data/tool limitations.
3. Findings table with IDs, severity/confidence, proof, risk and owner.
4. Detailed findings with repro or evidence and test outcomes, including unknowns.
5. Prioritized remediation backlog (P0/P1/P2) and cross-agent dependencies.
6. Mode-specific approved fix log or detailed implementation plan with rollback and tests.
7. Optional outcome-aware feature/technical roadmap, separated from bug remediation.
8. Release/privacy/security gates, decisions awaiting approval and next safe steps.

## Acceptance

After writing, re-open the file to confirm content/path, confirm no unexpected modifications, report commands/tests actually run, verify any real native `task` delegation and disclose blockers. Never claim the report or fixes exist unless confirmed in the filesystem.

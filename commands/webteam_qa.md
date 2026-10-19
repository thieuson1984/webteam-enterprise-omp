---
description: "Evidence-based Quality Engineering, Test Automation and Business Workflow Assurance: report, remediation plan and bounded authorized local fixes"
argument-hint: "[--mode=report|plan|fix] [--scope=all|strategy|requirements|unit|component|api|contracts|e2e|visual|data|concurrency|workflows|integration|security|ci|release] [--depth=quick|deep] [--max-fixes=3] [--roadmap=on|off] [--dry-run]"
---

# WebTeam native command — /webteam_qa

This command is a native OMP **Markdown prompt expander**, not executable code, an automatic agent launcher, a shell parser or a permission gate. Its `$ARGUMENTS` string is **untrusted user input**, to be interpreted as data by MAIN, never passed raw to `bash`, `eval`, or an unverified connector. Read the effective project/global WebTeam rules, then route to `webteam-qa` if verified available through OMP `task`; if nested task delegation is unsupported MAIN coordinates authorized specialists. Never claim an agent was called without observed delegation evidence.

## 1. Strict argument contract

**Raw arguments:** `$ARGUMENTS`

| Option | Allowed | Default |
|---|---|---|
| `--mode` | `report`, `plan`, `fix` | `report` |
| `--scope` | `all`, `strategy`, `requirements`, `unit`, `component`, `api`, `contracts`, `e2e`, `visual`, `data`, `concurrency`, `workflows`, `integration`, `security`, `ci`, `release` or comma-separated supported subset | `all` |
| `--depth` | `quick`, `deep` | `deep` for all; `quick` otherwise |
| `--routes` | optional comma-separated **known repository** modules/pages | relevant discovered scope |
| `--output` | a safe new repository-relative `.md` path under `docs/audits/`, no escape/symlink traversal | `docs/audits/QA_AUDIT_<UTCtimestamp>_<unique>.md` |
| `--roadmap` | `on`, `off` | `on` for report/plan; `off` for fix unless requested |
| `--max-fixes` | integer 1–5 | 3 in fix |
| `--dry-run` | flag | false; true never changes product/test source even in fix |
| `--budget` | bounded budget only if already approved | existing WebTeam policy |

Reject unsupported or contradictory switches without executing them. `--mode=report` may create/update **only** the approved audit report; `plan` creates a report with actionable remediation plan but **does not edit product source**; `fix` first audits/plans and then permits at most `--max-fixes` independently verifiable low-risk **local** changes with user authorization under the established code ownership. No mode overrides approval requirements. Don't overwrite unrelated or existing report files; create a unique safe name if missing/unsafe. Preserve uncommitted user changes and backups. If repo write permissions are blocked, output report text in chat and state no file was created.

## 2. Evidence-first discovery and role routing

1. Discover actual cwd, repo root and effective `.omp` context; record Git revision and dirty status. Confirm development, staging or production environment and avoid touching external customer systems.
2. Select affected user journeys and source files, not all files. Capture facts with `path:line`, test traces, contract/schema paths, and source versions. Tag `OBSERVED`, `MEASURED`, `INFERRED`, `NOT_RUN`, `BLOCKED`, `NOT_APPLICABLE` separately.
3. Load at most 1–2 relevant `webteam-qa-*` skills and matching focused headings in `webteam-qa-engineering-reference/references/`; do not dump every catalog into context.
4. Assign a single writer for each module, independent QA/Reviewer verification, and appropriate experts: QA + Product for workflows; Accessibility + Designer/Frontend for widgets; Integration + Architect/Backend/Database/Security/DevOps for system contracts. Only invoke those actually needed.
5. Never install software, contact endpoints, spend new provider credits, read secrets, or run untrusted project scripts without actual authorization.

## 3. Mandatory specialist review matrix

Assess applicable dimensions within **deterministic unit/component/API/contract/Playwright tests, risk-based coverage, multi-user transactions, permission negatives, business workflow state transitions, approval chains and consistency invariants**. For each dimension:

- A business/technical **contract** (actor, role/tenant, allowed action, source of truth, inputs and units/timezone, expected outcomes).
- Good, boundary, empty, invalid, permission-denied, duplicate, concurrent, stale/offline, partial failure, recovery and accessibility scenarios as applicable.
- Observable evidence and reproducible verification. Do not turn a planned test into a passed test. Do not infer application behavior from a generic checklist.
- Specific severity and confidence, realistic negative impact, owner, minimal correction, required approval and rollback.

For business applications, include order/case lifecycle, approval and cancellation flows, bulk actions, tenant isolation, partial save, repeated submissions, stale state and late notifications as applicable.

## 4. Fix policy and retest

**Hard boundary:** Only test code, fixtures and minimal reversible test-harness repairs by the owning QA agent may be made without additional implementation approval; product code fixes must be assigned to the owning development specialist. Never run load/fault tests on production or live external systems.

Run source/test modifications only with necessary approval for the actual diff/ownership, not merely because `fix` was typed. Use small reversible changes and relevant tests with explicit commands. Stop on unknown production/external-service effects, risk escalation, failing dependencies, lack of authorization, divergent Design DNA or an exhausted budget. No silent visual baseline acceptance, global memory promotion, unbounded `/loop`, automatic production deployment or tool permission expansion.

### Implementation cycle

1. Choose at most the authorized count of high-value **low-risk** issues; high severity does not imply safe auto-remediation.
2. Document the exact path owner, proposed patch, intended behavior and rollback.
3. Apply one small change; run reproducible targeted tests using approved environment/fixtures and capture actual outcomes.
4. Independently examine for adjacent regression, including role isolation, critical workflow behavior and integration contracts.
5. Update the report and stop when evidence is insufficient or a required human approval is absent.

## 5. Required Markdown audit artifact

Create exactly one Markdown report under `docs/audits/` with:

1. Metadata: mode, scope, time, repository path/revision, approved test environment, agents/models actually invoked, tool permissions observed.
2. Executive assessment: key business risks, affected roles/journeys, blockers and uncertainties.
3. Scope and coverage matrix: `APPLICABLE`, `NOT_APPLICABLE` (reason), `BLOCKED` (cause); coverage by module, critical business journey and test layer.
4. Findings `**QA-NNN**`: severity, confidence, observed/inferred/not-run, `path:line` or recorded test evidence, reproduction, root cause, operator/customer impact, counterexample and remediation.
5. Remediation plan: phase `NOW / NEXT / LATER`, dependency, code owner, requirements IDs, acceptance criteria, measurable gate, review and rollback.
6. Optional distinct *feature/engineering roadmap*: hypothesis, outcome, effort uncertainty, prerequisites and validation experiment; do not conflate product ideas with verified bugs.
7. For fix: changed paths, exact commands/run environments and results, before/after, blocked items, rollback and residual risks.
8. Applicable authoritative references and version applicability; distinguish audited controls from independent human approvals.

Finish with actual report path only if the file was written, what was and was not executed, and the one next safe action. Use `PASS_VERIFIED`, `PARTIAL_VERIFIED`, `BLOCKED`, `FAIL` only with named evidence. A valid Markdown command file is not a runtime test. No hidden background monitoring.

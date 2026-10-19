---
description: "Measured frontend/API/database capacity and reliability performance audit, plan and bounded safe optimization"
argument-hint: "[--mode=report|plan|fix] [--scope=all|vitals|rendering|bundle|assets|api|database|cache|load|queues|telemetry|slo|cost] [--depth=quick|deep] [--max-fixes=3] [--roadmap=on|off]"
---

# WebTeam native command — /webteam_performance

The command expands to a **Markdown prompt** inside OMP. It is not a shell executable or a guarantee that any subagent ran. Treat `$ARGUMENTS` as **untrusted user text**; never feed it directly into a shell or code evaluator. MAIN acts as Orchestrator if nested subagent delegation is unsupported. Route this task to `webteam-performance` when its native `task` role is discoverable, coordinating only applicable partners: webteam-frontend, webteam-backend, webteam-database, webteam-architect, webteam-devops, webteam-security, webteam-qa. Preserve task budgets, user approvals and one-writer-per-path.

## 1. Parse and validate arguments

Raw arguments: `$ARGUMENTS`

| Option | Accepted | Default |
|---|---|---|
| `--mode` | `report`, `plan`, `fix` | `report` |
| `--scope` | `all|vitals|rendering|bundle|assets|api|database|cache|load|queues|telemetry|slo|cost`; optional comma-separated subset | `all` |
| `--depth` | `quick`, `deep` | `quick` unless `scope=all`, then `deep` |
| `--routes` | comma-separated approved routes/modules | only actual relevant routes |
| `--output` | repository-relative Markdown path under `docs/audits/`, nonescaping | `docs/audits/PERFORMANCE_AUDIT_<date>_<unique>.md` |
| `--roadmap` | `on`, `off` | `on` |
| `--max-fixes` | integer 1–5 | `3` for `fix` |
| `--dry-run` | boolean flag | false; true prevents source/code changes even in fix |
| `--budget` | approved budget string, if provided | respect existing project policy |

`report`: audit + Markdown report only. `plan`: audit + detailed actionable plan and phased quality gates, **no product source changes**. `fix`: audit + plan + at most requested low-/moderate-risk **authorized local** fixes, one path owner at a time; report writing allowed. A `fix` request is NOT blanket consent for high-risk changes. If output is unsafe/absolute/parent-traversal/symlink escape or ambiguous, use a safe unique default or ask only the blocking question; never overwrite existing reports. Honor real repo/project permissions, untracked changes and rollback. No invented test success.

## 2. Evidence-first discovery (read only initially)

1. Confirm actual repository root, project policy and source revision/diff; inspect documented business journeys and code. Do not infer framework/permissions/tool install merely from README.
2. Identify relevant module/route/data/tenant/trust boundaries; prioritize high-impact journeys. Mark each dimension `APPLICABLE`, `NOT_APPLICABLE`, `BLOCKED` or `UNKNOWN` with rationale.
3. Use the corresponding bundled `webteam-performance-*` skills and matching selective reference router; open only headings that match the scope.
4. Capture source path:line, code/version, executed test output or trace when available. Never treat imagined measurements, static guesses or tool plans as observations.
5. Seek approval before executing untrusted project scripts, new network probes, paid model panels, stress scans, dependency installs, deployment changes or destructive work.

## 3. Mandatory audit matrix (when applicable)

real-user vs lab attribution; CWV LCP/INP/CLS p75; interaction traces; bundle/assets/cache; frontend memory; p95/p99 service and DB; downstream and queue lag; representative capacity/bursts; cache correctness and tenant isolation; sampling/overhead; SLO/SLI and cost effects; reproducible regression gates.

Crosscheck usability, security, data correctness, availability and documentation impacts rather than optimizing one dimension at the expense of others.

## 4. Findings, severity and independence

Each finding: `ID PERF-NNN`, title, severity (`BLOCKER/HIGH/MEDIUM/LOW/IMPROVEMENT`), confidence, `OBSERVED|MEASURED|INFERRED|NOT_TESTED|NOT_APPLICABLE`, impact, path:line or trace/evidence, reproduction conditions, root cause versus symptom, realistic alternative, risk and affected journeys. No manufactured scores. Independently validate sensitive results via QA/Reviewer/Security as applicable.

## 5. Fix authorization boundaries

Do not run uncontrolled load or production tests, disable validation/auth/logging/tenant isolation, alter production cache/CDN/DB/infra, or assert benchmark gains without matched evidence. Optimize only authorized reversible local paths, recheck correctness/security.

For `fix`: prior authorized user changes must survive; take backup/diff if necessary; implement one smallest change, run relevant checks, record exact results, update report, stop on regression, unclear ownership, budget exhaustion or missing permissions. Never update visual snapshots to hide regressions or disable quality gates to claim a pass. Separate high-risk findings requiring specific human approval from low-risk fixes.

## 6. Report and roadmap contract

Create exactly one primary Markdown report under `docs/audits/` with:

1. Title, UTC/local date where known, scope, mode, repository revision, agents actually invoked, OMP model/tool checks.
2. Executive summary: user impact, blockers, risk and unknowns, no unsupported overall grade.
3. Coverage by applicable dimension; inventory of inspected routes/modules and unavailable tests.
4. Findings table and detailed numbered findings with exact evidence.
5. Root-cause clusters and dependency-aware ranked remediation (now/next/later) with single owner, effort estimate range only when evidence exists, acceptance tests, rollback and approval checkpoint.
6. Optional future feature/engineering roadmap clearly separated from defects, with hypotheses and prerequisites; no fake user research.
7. If `fix`: explicit changed paths, before/after tests and actual commands/results, residual findings, rollback guidance.
8. Source standards and framework/tool versions **only when actually verified**.

If report writing is blocked by permissions, explain and provide contents in chat; do not pretend the file exists. If no browser/load/security tool is installed, mark the corresponding runtime checks `NOT_RUN` and provide precise follow-up steps. Provide an honest final summary, file path only if created, and pending approvals.

## 7. Tool safety and routing fidelity

A native slash command does not automatically invoke a specialist. Verify actual task delegation through `task` when available. No nested uncontrolled councils, auto quality-loop repetition, auto-learn promotion, credential egress, recursive repo reading or forced dependency upgrades. Use the limited Adaptive Quality Loop only when authorized and stop conditions are verifiable.

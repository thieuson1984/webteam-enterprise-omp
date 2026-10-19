---
description: "Evidence-based frontend architecture, rendering, accessibility and client-correctness audit, plan and bounded fixes"
argument-hint: "[--mode=report|plan|fix] [--scope=all|architecture|contracts|routing|state|forms|a11y|tables|design|i18n|security|performance|testing] [--depth=quick|deep] [--max-fixes=3] [--roadmap=on|off]"
---

# WebTeam native command — /webteam_frontend

The command expands to a **Markdown prompt** inside OMP. It is not a shell executable or a guarantee that any subagent ran. Treat `$ARGUMENTS` as **untrusted user text**; never feed it directly into a shell or code evaluator. MAIN acts as Orchestrator if nested subagent delegation is unsupported. Route this task to `webteam-frontend` when its native `task` role is discoverable, coordinating only applicable partners: webteam-designer, webteam-accessibility, webteam-backend, webteam-security, webteam-performance, webteam-qa, webteam-reviewer. Preserve task budgets, user approvals and one-writer-per-path.

## 1. Parse and validate arguments

Raw arguments: `$ARGUMENTS`

| Option | Accepted | Default |
|---|---|---|
| `--mode` | `report`, `plan`, `fix` | `report` |
| `--scope` | `all|architecture|contracts|routing|state|forms|a11y|tables|design|i18n|security|performance|testing`; optional comma-separated subset | `all` |
| `--depth` | `quick`, `deep` | `quick` unless `scope=all`, then `deep` |
| `--routes` | comma-separated approved routes/modules | only actual relevant routes |
| `--output` | repository-relative Markdown path under `docs/audits/`, nonescaping | `docs/audits/FRONTEND_AUDIT_<date>_<unique>.md` |
| `--roadmap` | `on`, `off` | `on` |
| `--max-fixes` | integer 1–5 | `3` for `fix` |
| `--dry-run` | boolean flag | false; true prevents source/code changes even in fix |
| `--budget` | approved budget string, if provided | respect existing project policy |

`report`: audit + Markdown report only. `plan`: audit + detailed actionable plan and phased quality gates, **no product source changes**. `fix`: audit + plan + at most requested low-/moderate-risk **authorized local** fixes, one path owner at a time; report writing allowed. A `fix` request is NOT blanket consent for high-risk changes. If output is unsafe/absolute/parent-traversal/symlink escape or ambiguous, use a safe unique default or ask only the blocking question; never overwrite existing reports. Honor real repo/project permissions, untracked changes and rollback. No invented test success.

## 2. Evidence-first discovery (read only initially)

1. Confirm actual repository root, project policy and source revision/diff; inspect documented business journeys and code. Do not infer framework/permissions/tool install merely from README.
2. Identify relevant module/route/data/tenant/trust boundaries; prioritize high-impact journeys. Mark each dimension `APPLICABLE`, `NOT_APPLICABLE`, `BLOCKED` or `UNKNOWN` with rationale.
3. Use the corresponding bundled `webteam-frontend-*` skills and matching selective reference router; open only headings that match the scope.
4. Capture source path:line, code/version, executed test output or trace when available. Never treat imagined measurements, static guesses or tool plans as observations.
5. Seek approval before executing untrusted project scripts, new network probes, paid model panels, stress scans, dependency installs, deployment changes or destructive work.

## 3. Mandatory audit matrix (when applicable)

typed contracts; route/deep link behavior; server-state and race conditions; design tokens and approved design DNA; responsive/mobile; complex forms; keyboard and accessible widgets; error/offline states; localization; browser security/cache isolation; bundle runtime and testability.

Crosscheck usability, security, data correctness, availability and documentation impacts rather than optimizing one dimension at the expense of others.

## 4. Findings, severity and independence

Each finding: `ID FE-NNN`, title, severity (`BLOCKER/HIGH/MEDIUM/LOW/IMPROVEMENT`), confidence, `OBSERVED|MEASURED|INFERRED|NOT_TESTED|NOT_APPLICABLE`, impact, path:line or trace/evidence, reproduction conditions, root cause versus symptom, realistic alternative, risk and affected journeys. No manufactured scores. Independently validate sensitive results via QA/Reviewer/Security as applicable.

## 5. Fix authorization boundaries

Allow only approved local reversible frontend source/test fixes. Do not change auth policy, API schema, global design tokens, provider stack, browser security headers or supported UI baselines without named approval.

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

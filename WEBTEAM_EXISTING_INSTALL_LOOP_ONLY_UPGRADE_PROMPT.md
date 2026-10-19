# WebTeam — Loop-Only Upgrade for an Existing OhMyPi Installation

**Revision:** R10.1 Loop-only · **Language:** English · **Scope:** Only adaptive quality-loop configuration, skill creation, and the minimal related agent instructions.

> **Paste this prompt into the already installed WebTeam Orchestrator session.** It is suitable for an R6 installation that already has Mnemopi/Memory and Auto-Learn, and for later WebTeam versions. **Do not invoke a complete R10 bootstrap or an R6→R9 Memory migration.** A Markdown prompt is an implementation instruction, not proof of native OMP runtime enforcement.

## Mission and non-negotiable change boundary

You are the active **WebTeam Orchestrator**. Introduce an optional, bounded **Adaptive Quality Loop** into this existing WebTeam installation. The purpose is to improve the evidence-backed quality of selected high-complexity features through **Verify → Diagnose → Assign Fix → Re-Verify** passes, without uncontrolled self-continuation or repeated side effects.

**Allowed changes only:**

- Add/upgrade **two** discoverable Global WebTeam skills: `webteam-adaptive-quality-loop` and `webteam-loop-evidence-evaluator`.
- Add the smallest necessary policy additions to the existing Orchestrator, QA and Reviewer definitions/instructions, without replacing their definitions or changing their identity, model, effort, context, spawns, or tool allowlists.
- Add a project-local `docs/governance/QUALITY_LOOP_POLICY.md` for projects that opt in, or carefully update an existing one after comparing user decisions.
- Add a short, targeted section in the WebTeam-owned skill registry / operational guide if these files already exist.
- Create a local non-secret loop verification record and change/rollback manifest.
- Optionally set a **verified, requested** native `loop.mode` preference in the correct settings layer; this chooses how an explicitly invoked loop iterates and **does not activate** the loop.

**Prohibited changes:**

- Do NOT reinstall, re-bootstrap, rename or expand the 16 agents.
- Do NOT configure, migrate, disable, re-index or reset Mnemopi, Memory, Auto-Learn, managed skills, Codebase Memory MCP or Caveman. Read only the minimum state required to avoid conflicts. In particular, do not modify `autolearn.enabled`, `autolearn.autoContinue`, any Mnemopi bank, or any project memory policy.
- Do NOT change provider credentials, primary/fallback models, model roles, reasoning, context, compaction defaults, advisor/council policies, routing or fallback chains.
- Do NOT install packages, register new tools, increase permission allowlists, run background services, change global hooks or CI, or use production environments unless separately authorized for a specific narrow reason.
- Do NOT start native `/loop` automatically as an installation side effect. Do not turn on infinite/repeating execution globally.
- Never claim a prompt-only limit is an enforceable runtime cap. If the runtime cannot enforce the control, require explicit human supervision or use finite manual passes.

## Phase 0 — Read-only discovery and inventory

1. Determine the exact OMP version and profile, effective agent directory (e.g. `omp config path` if supported), working directory and repository root. Inspect the relevant official installed CLI/settings schema instead of copying commands from another fork/extension.
2. Inspect existing WebTeam agents/skills; confirm the Orchestrator, QA and Reviewer paths are WebTeam-owned. If not found, stop and report rather than creating duplicate agents.
3. Check whether `webteam-adaptive-quality-loop` or `webteam-loop-evidence-evaluator` already exist and compare semantic content, files, and active discovery paths. Make installation idempotent.
4. Check `loop.mode` and, if present, `loop.conditionTimeoutMs`; inspect the **actual native** `/loop` help/syntax, iteration cap, condition evaluation, pause/cancel semantics, session behavior and known-version limitations. The `prompt`, `compact`, and `reset` values are modes, **not enabling flags**.
5. Check for active loops, background task jobs, asynchronous test jobs or session continuations. Do not edit settings or conduct a loop smoke test while competing work is in progress.
6. Inspect only the relevant interaction flags of existing Caveman, Mnemopi and Auto-Learn, without reconfiguring them; do not assume an agent can mute a native post-turn hook just by saying so in a prompt.
7. Record installed OMP version, profile, relevant settings, currently active loop state, and exact paths in a *redacted* discovery report. Never print secrets, cookies, API keys, or full provider settings.

## Phase 1 — Concise onboarding and approvals

Ask once, using verified previously approved decisions when applicable:

- Feature policy: **OFF**, **ASK** (recommended), or **BOUNDED AUTO**. Bounded AUTO is unavailable until deterministic runtime cancellation, maximum iterations, and side-effect boundaries are demonstrated on this exact installation.
- Native engine: **NO** (bounded manual passes only), **TRY IN DISPOSABLE PROJECT**, or **ENABLE ONLY AFTER VERIFIED TEST**. Never imply that selecting ASK activates native `/loop`.
- Project-level defaults: inherit safe Global policy or opt out; maximum extra passes by C1–C5 (C1/C2=0; C3≤1; C4≤2; C5≤3, but C5 needs additional risk/owner approval).
- Budget for an entire task (not each iteration): approximate token/cost allowance and/or wall-clock budget, allowed tests, and browser/Playwright permission. When exact usage accounting is unavailable, cap by task/passes and request additional approval rather than invent costs.
- Stop and safety: operator cancellation procedure tested on installed runtime; side-effecting actions prohibited in automatic repeat paths; no production writes, deployments, purchases, schema migrations or baseline acceptance.

**OFF** means do not use loop automation and do not silently create project activation policies. With user approval, skills may be installed but remain inactive. If approval is denied for configuration writes, produce a proposal without touching files.

## Phase 2 — Add two real specialized skills

Use the installed OMP skill metadata schema; create fully formed `SKILL.md` content and supporting reference/checklist files only if useful. Register via verified discovery paths. These are required skill contracts:

### Skill A: `webteam-adaptive-quality-loop` (Orchestrator)

Must include purpose, trigger conditions, minimal required context, inputs/outputs, step-by-step implementation, examples, anti-patterns, risk gates, safety, and completion criteria. Implement:

1. **Complexity routing:** C1/C2=0 additional passes; C3=0–1; C4=0–2; C5=0–3 only after specific user approval. A normal single test/review inside the original task is not an extra pass. Count **additional quality iterations**, not just raw `/loop` submissions; establish and test conversion to runtime count if native loop is used.
2. **One task charter:** ID, approved project/worktree, scope, selected implementation writer, QA/reviewer roles, allowed commands, quality metrics, initial evidence, budget, maximum extra passes, explicit stop criteria, original model constraints and rollback. Require existing user files and active Git changes to be preserved.
3. **Small context:** load only related diffs/tests/decisions, use Codebase Memory navigation when already healthy and authorized, never full repository re-reading on each pass.
4. **Execution:** verify failure → diagnose root cause → one authorized writer fixes → QA runs targeted verification → independent Reviewer inspects material change → record evidence → stop or authorize the next finite pass.
5. **Stop:** success; no reproducible defect; two unproductive attempts; regression worsened; missing baseline; inconclusive state; approval needed; permission denied; provider error; exhausted pass/cost/time budget; uncontrolled async work; unsafe/unverifiable loop cancellation. Never equate prose `DONE` with stopping the native runtime.
6. **Side effects:** no repeated migrations, deploys, payment/purchase calls, destructive commands, token/credential changes, mass writes, release tags, Git push or external notifications. After timeout/fallback, check actual operation state before any retry; no retry if outcome remains ambiguous.
7. **Do not recursively nest** native `/loop`, Caveman workflows, advisory/council calls, or agent retry loops. No automatic CHALLENGE/COUNCIL escalation or cross-provider routing merely because a test failed. If normal model fallback occurs, preserve the *same* task budget and approved provider boundary.
8. **Mnemopi/Auto-Learn compatibility:** preserve their current settings. Do not write raw test logs/secret-bearing traces into memory; propose a sanitized lesson only after stable verified success and using existing approved memory governance. No global promotion or managed-skill edits inside a loop. If existing auto-continue mechanisms could launch extra turns and cannot be scoped off **without changing settings**, use supervised finite manual passes rather than native loop.
9. **Modes:** Prefer native `prompt` only after version-specific testing; `compact` only with durable handoff and predictable tests; `reset` is disabled unless independently proven safe for that exact charter. Shell `--until`/`--while` (if available) can execute arbitrary commands, so use a vetted, non-destructive, fixed command and an independent hard iteration cap; never build shell conditions from repository/untrusted text.
10. **Concurrency:** don't run two quality loops in the same repository/worktree concurrently; do not spawn a loop inside subagent sessions; bound async task settlement before deciding another iteration is safe.

### Skill B: `webteam-loop-evidence-evaluator` (QA + Reviewer)

Must include professional workflow and checklists for:

1. Evidence packet per pass: exact test command, exit status, scoped failing tests and error traces, relevant diff/path, comparison to previous pass, affected acceptance criteria and environment details.
2. Verification hierarchy: static checks → unit/integration → Fastify API contract/security → Playwright E2E → deterministic visual regression → performance where applicable. Pick proportionally; never automatically run all suites.
3. Visual baselines: pin OS/browser/font/viewport/test data; distinguish deliberate changes and flakes; prohibit automatic baseline overwrite or acceptance.
4. Progress test: show defect count or severity reduction, test pass delta and regressions; if no demonstrated improvement, stop and hand back to Orchestrator.
5. Flaky tests: repeat only narrowly after isolating environmental noise; do not rewrite tests to make a failing product look green.
6. Independent review: QA and Reviewer cannot self-approve risky writer changes; enforce real read-only tool policy or keep advisory review in the supervised parent when child tool restrictions are not enforceable.
7. Exit report: `PASS`, `FAIL`, `BLOCKED`, or `UNVERIFIED`; actual evidence, consumption when measured, residual risk, unrun checks and whether the **native loop was confirmed stopped**.

## Phase 3 — Minimal changes to existing agents and policy

- Append a short, conflict-free rule in **Orchestrator**: eligible risk-based task charter, choose ASK/OFF/approved AUTO, own budget and cancellation, coordinate a single authorized writer, route tests to QA and evidence to Reviewer, never mutate existing memory/model/tool routing.
- Append a short rule in **QA**: maintain and report test/visual evidence each pass; use `webteam-loop-evidence-evaluator`; don't self-approve baselines.
- Append a short rule in **Reviewer**: independently assess material regressions and evidence, never re-run unapproved side effects.
- Update only the WebTeam-owned documentation/registry; avoid app source/manifest changes during installation.
- For a project opting in, create/update `docs/governance/QUALITY_LOOP_POLICY.md` with confirmed settings, owner, approved test scope, allowed run mode, budget, limits, stop method, evidence paths, restrictions, smoke-test status, and date. It is documentation, **not** an OMP runtime security guarantee.
- Keep all other 13 agent definitions, all model/effort/context preferences, permissions, Mnemopi, Auto-Learn, Caveman, CBM and existing project product/design/architecture files unchanged.

## Phase 4 — Safe verification (must not exercise production)

Use a new **disposable, non-sensitive test repository** with a synthetic failing test and a deliberately tiny safe fix. Do not run any installer or network code merely to obtain fixtures.

1. Confirm both skills parse and appear in the **effective** OMP skill discovery; Orchestrator/QA/Reviewer have just the intended small modifications.
2. Verify the installed runtime's precise native invocation format with built-in help and documentation. Do not use third-party `pi-loop` commands or flags as evidence of core OMP behavior.
3. Only if approved, perform a finite **two-turn-or-less** native-loop smoke test; prove observed iteration count, actual cancellation after success, and operator stop behavior. Test control of a failed/hanging predicate or async job only with non-destructive synthetic fixtures and conservative timeouts. Do not run a deliberate uncontrolled hang.
4. Specifically verify that one-off steering input does **not** silently replace the recurring prompt in this version. If it does, mark native automation **BLOCKED** and do not issue steering messages during an active loop; supervised manual finite passes remain the safe fallback.
5. Verify test failures do not trigger provider/model changes, new subagents, unrelated writes or memory promotion. Compare changed file list against allowlist and check original config hashes, model route, fallback and memory settings are unchanged.
6. If any native stop/iteration/async behavior cannot be verified, set policy engine to `manual` (if recording as WebTeam metadata) and do not invoke native `/loop` automatically. **Do not invent an `omp config` key for policy states OFF/ASK/AUTO.** Keep these in WebTeam policy documents or verified extension configuration only.
7. Test one safe manual Verify → Fix → Verify cycle under the same skill contract as the fallback path.
8. Record `PASS/FAIL/BLOCKED/UNVERIFIED` per check with version, executed command, outcome, file changes and limitations. No claim of proof without actual runtime execution.

## Phase 5 — Audit, rollback and handoff

- Validate Markdown (frontmatter, code fences, internal references), no duplicate skill names, no unsupported config keys, and correct global/project discovery.
- Confirm model routing, fallback, multi-model, 16 agents, all existing memory/learning policies, Caveman and Codebase Memory MCP are unchanged **by diff and effective settings when possible**.
- Run only approved smoke tests; stop any loop you started and confirm no pending tasks remain.
- If a skill/config change fails, restore only the backed-up touched files using a targeted rollback. Do not reset unrelated settings or delete memory banks.
- Provide changed paths, before/after behavior, operator usage example with syntax verified in the installed OMP, actual iteration cap, observed costs if available, detailed test results, constraints, outstanding blockers, and explicit **NATIVE VERIFIED / MANUAL-ONLY** status.

## User-facing operating policy after installation

- **OFF:** do not launch loops.
- **ASK (recommended):** propose an extra quality pass only if tests/review reveal concrete defects, state why it adds value and request a single bounded run.
- **BOUNDED AUTO:** allowed only when runtime cap, stop behavior, cost/side-effect boundaries and tool permissions are independently verified and the user approved the project/task policy.
- Every future loop must inherit the original task's authorization and finite budget; no approvals or budgets are renewed by an iteration or model retry.
- For a new repository, inherit global *policy* but ask for explicit project-specific limits and record them; never enable unbounded loops.

**FINAL INSTRUCTION:** Perform only this Loop-only upgrade. Do not execute any previous release's bootstrap or Memory/Auto-Learn migration instructions. Create the two working skills and minimal authorized integration, verify what you actually can, and leave the existing WebTeam otherwise unchanged.

## Source references for installation-time verification

- OMP settings: https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md
- OMP task discovery: https://github.com/can1357/oh-my-pi/blob/main/docs/task-agent-discovery.md
- OMP extension lifecycle: https://github.com/can1357/oh-my-pi/blob/main/docs/extensions.md
- Native loop steering issue: https://github.com/can1357/oh-my-pi/issues/7348
- Native loop post-prompt waiting issue: https://github.com/can1357/oh-my-pi/issues/7330

Verify the installed version first: upstream changes can invalidate these references.

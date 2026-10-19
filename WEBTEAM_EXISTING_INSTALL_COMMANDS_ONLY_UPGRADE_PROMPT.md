# WebTeam R11 — Commands-Only Upgrade for an Existing Installation

**Target:** OhMyPi 18.12.2 native Markdown slash commands. **Scope:** Install and verify command templates ONLY. This is NOT a full WebTeam bootstrap and does not reinstall/upgrade R6, R9 or R10.2 capabilities. Use in an existing working WebTeam environment.

## Mandatory preservation contract

You are operating in the user's existing OMP environment. Before doing anything mutable, inspect the active OMP version/profile, loaded Global WebTeam agents and current project. **Preserve unchanged**: all 16 agent implementations, `.omp/agents`, model providers/aliases, default/fallback/council routing, effort/context, memory/Mnemopi, Auto-Learn, Caveman, Codebase Memory MCP, Loop policies, design standards, Git source and deployments. Do not run a full bootstrap or reinstall dependencies. Do not overwrite existing commands created by other users or extensions.

## Phase 1 — Consent and placement

Ask if the user wants to install the WebTeam commands (suggest yes), and whether Global (preferred for reuse) or project-only is desired. Resolve the EFFECTIVE profile-aware `commands/` directory from the installed runtime; typically `~/.omp/agent/commands/` globally and `<repo>/.omp/commands/` locally. Inspect collisions and verify flat `*.md` command discovery, reserved builtin names, current version (v18.12.2 target) and any OMP restrictions. Show proposed new/modified files and request permission before writing.

## Phase 2 — Materialize command files

Use the exact templates contained in the R11 command bundle (`WEBTEAM_R11_COMMAND_TEMPLATES/commands/*.md`) when available. If the bundle is not available, use the embedded Section 19.3 exact templates from `WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R11.md`. If neither source is readable, **do not invent partial or hollow commands**: report missing source and request one of the files.

Required command set:

- `/webteam_create_project` — Initialize a new WebTeam web application with approved onboarding and project documents.
- `/webteam_adopt_project` — Safely analyze and onboard an existing codebase into Project WebTeam.
- `/webteam_status` — Report WebTeam project progress, blockers, agents and runtime capability status.
- `/webteam_plan` — Create a bounded, dependency-aware implementation plan without coding.
- `/webteam_implement` — Implement an approved feature using the right specialist agents.
- `/webteam_design_audit` — Extract or verify project Design DNA and design consistency.
- `/webteam_architecture_audit` — Review architecture, contracts and migration risks.
- `/webteam_security_audit` — Assess threats, authorization and security boundaries.
- `/webteam_test` — Run relevant unit, integration, API and E2E tests.
- `/webteam_visual_test` — Validate responsive visuals with Playwright screenshot baselines.
- `/webteam_review` — Conduct independent risk-based code and design review.
- `/webteam_reference_analyze` — Analyze a Git reference repository for safe, licensed adoption.
- `/webteam_memory_review` — Audit project-scoped Mnemopi memory and Auto-Learn governance.
- `/webteam_models_audit` — Audit approved default models, fallback and council routing.
- `/webteam_quality_loop` — Propose or run a bounded verify-fix-verify cycle.
- `/webteam_docs_sync` — Check alignment of requirements, design, architecture and tests.
- `/webteam_healthcheck` — Verify WebTeam installation and actual orchestration safely.
- `/webteam_release_check` — Run release-readiness checks without deploying.
- `/webteam_help` — Explain the installed WebTeam commands and when to use them.


Keep files flat, ensure valid frontmatter and preserve placeholder `$ARGUMENTS` literally. Do not create a shell tool or extension unless Markdown capability is absent and the user separately approves a compatible alternate plan. Do not force changes in tool permissions or model fallback to enable command routing.

## Phase 3 — Verify without intrusive changes

Restart/reload discovery only with documented methods. Verify each selected command appears in OMP autocomplete/Extensions dashboard with expected source; inspect collisions and shadowed entries. Safely test `/webteam_help` and `/webteam_status`; for a user-approved small model-call budget, invoke `/webteam_plan` in a synthetic no-write scenario and observe a real delegated `task` call only if the installed topology and permissions allow it. Do not invoke create/adopt against valuable existing projects as a smoke test. Verify root path, no product code change, no extra provider egress, no loops/auto-learning changes and expected argument interpolation.

Never mistake command discovery for automatic expert task routing. If specialist delegation is not observed, mark that aspect unverified, not passed; offer the existing self-orchestration check as a separate workflow.

## Phase 4 — Report and rollback

Record exact command root, file list/hash, existing collisions, before/after diffs, approved writes, runtime version and which tests were observed. Provide rollback only for files created/modified by this upgrade (restore backups). Report `PASS_VERIFIED`, `PARTIAL_VERIFIED`, `BLOCKED` or `FAIL`; don't claim runtime success from static file checks. Stop after two distinct failed repair hypotheses.

**Primary instruction:** Install WebTeam slash commands only. Preserve every other existing system capability and avoid unexpected cost or changes.

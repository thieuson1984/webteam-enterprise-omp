# WebTeam R11 native command templates — OhMyPi 18.12.2

These are executable *prompt templates* for OMP's native file-based slash-command discovery, not shell commands or TypeScript tools. Move the contents of `commands/` to the effective user-profile agent directory's `commands/` (usually `~/.omp/agent/commands/`) after backing up existing files and checking collisions. **Do not nest under `commands/webteam/`**, because native discovery is flat. Project overrides belong under `<repo>/.omp/commands/*.md`.

With OMP 18.12.2 the filename determines slash-command name. Frontmatter `description` and `argument-hint` help autocomplete; `$ARGUMENTS` expands user-supplied arguments. Enter names beginning `/` in the OMP interactive input. Run from the intended project working directory.

**Critical:** Command files do not enforce permissions or invoke `task` by themselves. They expand to instructions delivered to the current main agent. The main session must verify and run actual specialist delegation; shell/network/install/destructive actions still require approval and appropriate host restrictions. Commands are not substitutes for main-session routing or project onboarding.

## Available commands

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

## Install / test

1. Run `omp --version` and confirm installed OMP's actual profile/config roots.
2. Check native command discovery precedence and existing collisions. Back up same-name files and never overwrite unrelated handlers.
3. With approval, copy these Markdown files directly into the **effective** global `commands/` directory, or the project `.omp/commands/` directory when deliberately local. Avoid treating the command-template source directory itself as auto-discovered.
4. Restart OMP or use a verified command/plugin discovery refresh path; check slash autocomplete or Extensions dashboard.
5. Run `/webteam_help`, `/webteam_status` in read-only mode. For a bounded delegation smoke test, use `/webteam_healthcheck` and explicitly approve only safe synthetic work.
6. If `/webteam_create_project` is used, ensure the destination is empty/new. If code exists, switch to `/webteam_adopt_project`.

### Example

```text
/webteam_create_project "School administration dashboard"
/webteam_adopt_project "/work/existing-app"
/webteam_plan "Add teacher grade reporting"
/webteam_test "Fastify authorization tests"
/webteam_visual_test "Dashboard at 1440x900 and 390x844"
/webteam_healthcheck
```

No command performs actual operations until the active agent decides, within its host permissions, to execute the workflow and obtains any required approvals.

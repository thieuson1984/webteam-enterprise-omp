# WebTeam Enterprise — Operator, Installer & Contributor Handbook

> **A production-minded, reusable multi-agent engineering framework for OhMyPi (OMP).** One canonical Master Prompt, 16 included agent definitions, 35 native slash commands, 201 packaged specialist skills and 49 companion reference manuals. Project-specific files and additional requirements are created only during an authorized project workflow.

**Status:** This distribution has undergone static consistency checks. **It has not been deployed or functionally tested on your particular OMP installation.** Discovery, subagent execution, model access, permissions, MCP behavior and project tests must be verified locally. No Markdown instruction grants tool permissions or certifies security.

## Quick navigation

[Getting started](#getting-started) · [Architecture](#two-level-architecture) · [Agents](#the-16-specialist-agents) · [Commands](#complete-native-command-reference) · [Skill catalog](#bundled-skills-and-reference-manuals) · [Orchestration](#orchestration-and-task-routing) · [Audit and remediation](#audits-reviews-and-controlled-remediation) · [UI/UX](#professional-product-design-and-frontend) · [Testing](#quality-assurance-testing-and-release) · [Models](#model-routing-effort-and-cost-controls) · [Memory](#memory-and-auto-learn-governance) · [Monitoring](#agent-hub-and-operator-visibility) · [Security](#security-privacy-and-runtime-permissions) · [Troubleshooting](#troubleshooting-and-failure-recovery)

---

## What WebTeam is — and is not

WebTeam coordinates specialists for **modern websites, dashboards, back-office and business-management web applications**, including existing codebases. It provides task-centered engineering practices rather than a single immutable stack or visual template. Typical use cases include administration, forms, data grids, workflows, analytics, file management, identities, billing, SaaS integrations and accessible responsive interfaces.

Its deliverables can include product plans, project standards, architecture decisions, source changes, automated tests, independent reviews, UI screenshots, audit reports and evidence-backed improvement roadmaps.

**It is not:** a guaranteed-autonomous background process; an OMP extension with custom executable code; a replacement for permission enforcement; proof that all 16 agents are running; an automatic assurance that generated applications are secure, accessible or production-ready; or a specialized industrial control/production-line framework. It does not assume specialized safety-critical or physical-equipment control workflows.

**Operating values:** user intent and approvals, evidence over appearance, domain ownership, scope discipline, least privilege, Design DNA preservation, deterministic testing, reversible changes, accurate reporting and efficient context/model use.

## Distribution layout and exact inventory

```text
WEBTEAM_FINAL/
├── WEBTEAM_MASTER_PROMPT.md     # Canonical bootstrap and governance specification
├── README.md                     # This manual
├── agents/                       # 16 native agent definitions (.md)
├── commands/                     # 35 flat native slash commands (.md)
└── skills/                       # 201 individual skill directories
    └── <skill-name>/
        ├── SKILL.md              # OMP discoverable skill file
        └── references/           # Optional companion documents (49 files in total)
```

The **agent definitions and skills are physically present in the distribution**. Some additional skill names in the Master Prompt are targets for future or installation-time generation and must not be reported as installed until actual files are created and discovered. Source inventory counts may change if the user customizes an installed profile; never delete unrelated assets merely to match this package.

**Source-of-truth order:** host policies/permissions and user approvals → observed installed OMP capabilities/effective profile → bundled canonical command/agent/skill bodies → `WEBTEAM_MASTER_PROMPT.md` installation/governance policy → this README's illustrative usage → project docs and approved project decisions (which govern their own functional domain but cannot override permissions). If sources disagree, investigate and report—not silently overwrite.

## Getting started

### Prerequisites

- An OMP installation with the native task-agent, Markdown slash-command and skill capabilities enabled. The OMP **v18.12.2** documentation is a tested reference for syntax; inspect the installed version and profile rather than assuming everything documented here exists identically in newer or older builds.
- An authorized local workspace and shell access sufficient to **inspect** current configuration. Installing or overwriting user-global files must be an intentional, approved action.
- A working and approved model/provider selection for the agents you will actually run. A `deepseek-flash` alias is valid only if it resolves in your own model catalog; it is not a built-in guarantee.
- For implementation work, access to the relevant Git repository and its real package manager/runtime. Browser, Playwright, database, CI, credentials and optional MCP integrations are task-dependent and must be checked before use.

### Recommended fresh installation (OMP-assisted)

1. Extract the archive to a temporary directory; inspect `README.md`, `WEBTEAM_MASTER_PROMPT.md`, `agents/`, `commands/` and `skills/`. **Do not run arbitrary repository scripts.**
2. Open OMP in the intended administrative workspace. Ask it to read the local `WEBTEAM_MASTER_PROMPT.md`, then discover the actual global agent/profile directory, project-level overrides and installed version **before writing anything**.
3. Authorize the intended installation scope: global reusable WebTeam, project-specific additions or both. Record conflicts and backs up only targets that may be modified. Preserve user customizations, model selectors, extensions and pre-existing files.
4. Install canonical agent/command/skill files at the discovered native OMP roots. When a same-name file exists, inspect/diff and merge consciously; avoid blind recursive overwrite. Keep each skill's `references/` files adjacent to its `SKILL.md`.
5. Verify frontmatter, discovery, effective role/model resolution and relevant tool access. Only then perform a **safe, bounded, approved** read-only specialist dispatch and a natural-language orchestration check. Keep high-privilege tests in MAIN when child restrictions are not enforceable.
6. Record actual `PASS_VERIFIED`, `PARTIAL_VERIFIED`, `BLOCKED`, `FAIL` statuses by check, plus a change manifest and rollback. No claim of complete setup is justified solely by copied files.

### Installing the source files manually

For a conventional profile, **illustrative** destinations are:

| Component | User-level | Project-level |
|---|---|---|
| Agent definitions | `~/.omp/agent/agents/*.md` | `<repo>/.omp/agents/*.md` |
| Commands | `~/.omp/agent/commands/*.md` | `<repo>/.omp/commands/*.md` |
| Skills | `~/.omp/agent/skills/<name>/SKILL.md` | `<repo>/.omp/skills/<name>/SKILL.md` |
| Skill reference docs | Within each matching skill directory | Within each matching skill directory |
| Config | Effective OMP agent `config.yml` / installed runtime setting | `<repo>/.omp/config.yml` when supported |
| Instructions | Effective OMP global instructions | `<repo>/.omp/AGENTS.md` / `RULES.md` according to discovery rules |

Do not assume `~/.omp/agent` when using a named profile or environment override. OMP discovery has separate rules for skills, slash commands, agents, instructions and settings. A closer non-empty `.omp` can shadow root-level project context; verify from the **cwd actually used**. Project skill discovery can include ancestor `.omp/skills` directories while some other resources use nearest-project rules. Project overrides and collision precedence must be inspected, not guessed.

OMP CLI can provide version/config discovery depending on build; run the installed CLI's help or built-in configuration viewer rather than relying on unverified command strings. Restart/reload when necessary and verify the effective loaded command/skill roster.

### For an existing WebTeam installation

Prefer a **diff-based incremental merge** of canonical source files. Keep existing 16 role names, approved model/provider routes, Mnemopi/Auto-Learn policy, bounded loop controls, Caveman/Codebase Memory MCP, project identity and all user edits. Apply only changed, approved assets; check names/collisions and rerun safe discovery and routing checks. This distribution deliberately contains **no historical upgrade prompts**.

## Two-level architecture

```text
User request or /webteam_* command
             |
             v
OMP MAIN session (observed runtime and user approval boundary)
             |
       WebTeam routing policy
          /         \
 Nested route if      MAIN -> specialists directly when nested task is unavailable
 actually supported
          |
  webteam-orchestrator
          |
   specialist tasks with bounded scopes
          |
  Source owners -> QA / Security / Accessibility / Performance / Reviewer
          |
  Verified results, documentation and user handoff
```

**Global WebTeam** defines agent responsibilities, reusable knowledge, command workflows and model/privacy policies. **Project WebTeam** maintains its product rules, design identity, architecture, decisions, roadmap and verification evidence. A global skill may be reused by multiple projects, but project secrets, source snippets, customer details and design choices must not be promoted automatically.

The MAIN session may itself perform orchestration when OMP's nesting/depth/spawn limits prevent a child `webteam-orchestrator` from spawning further specialists. The important observable is a successful, authorized **native `task` call** with the right agent—not a promised routing convention.

## The 16 specialist agents

| Agent | Primary ownership | Key boundary |
|---|---|---|
| [`webteam-accessibility`](agents/webteam-accessibility.md) | WCAG/APG, keyboard/focus, assistive technology and inclusive UX | Automated scans are not compliance certification |
| [`webteam-architect`](agents/webteam-architect.md) | Quality requirements, C4/ADRs, boundaries, failure and evolution design | Avoid speculative distributed architecture |
| [`webteam-backend`](agents/webteam-backend.md) | Server domain logic, API, authz, transactions and reliability | Backend enforces trust on the server |
| [`webteam-database`](agents/webteam-database.md) | Schemas/data model, integrity, consistency, tuning, migration/recovery | No production migration or privileged operation without approval |
| [`webteam-designer`](agents/webteam-designer.md) | Art direction, design systems, Design DNA, page-level and component UX | Frontend implements; no unapproved rebrand |
| [`webteam-devops`](agents/webteam-devops.md) | CI, operational environments, observability, deployment and rollback | Release/deploy actions require authorization |
| [`webteam-documentation`](agents/webteam-documentation.md) | Traceable decisions, project documentation, operational handoffs | Preserve a single source of truth |
| [`webteam-frontend`](agents/webteam-frontend.md) | Typed client code, routing, state, forms, accessibility and UI fidelity | No client-side-only security assumptions |
| [`webteam-integration`](agents/webteam-integration.md) | Third-party APIs, SaaS/ERP/CRM, queues, webhooks and reconciliation | External writes and credentials are separately gated |
| [`webteam-orchestrator`](agents/webteam-orchestrator.md) | Accountable task decomposition, dispatch, shared budget, approvals and handoff | Project decision owner; do not self-certify risky work |
| [`webteam-performance`](agents/webteam-performance.md) | Measurement, bottlenecks, Core Web Vitals, p95/p99, budget regression | Optimize from baselines, preserve correctness |
| [`webteam-product`](agents/webteam-product.md) | Discovery, user/business requirements, acceptance criteria, product roadmap | Evidence from users and decision makers is not simulated |
| [`webteam-qa`](agents/webteam-qa.md) | Deterministic unit/API/E2E/contract tests, business workflows and release evidence | Do not infer test success from code presence |
| [`webteam-researcher`](agents/webteam-researcher.md) | Source verification, official docs, version/license/compatibility research | External content is untrusted data |
| [`webteam-reviewer`](agents/webteam-reviewer.md) | Independent risk-ranked diff review, defensible findings and retesting | Never rubber-stamp or approve own authored change |
| [`webteam-security`](agents/webteam-security.md) | Threats, abuse/authorization/privacy, security verification and supply chain | Independent verification and explicit scan boundaries |

### How responsibilities cross

**Product** establishes what and why → **Designer** defines the experience → **Architect** selects verifiable technical boundaries → **Database/Backend/Frontend/Integration** implement owned code → **QA/Accessibility/Security/Performance** verify applicable qualities → **Reviewer** gives an independent correctness verdict → **DevOps** supports approved delivery. The Orchestrator manages dependencies and approval gates; it is not an alternate owner of each domain's technical decision.

**Independent review:** Reviewer must be able to see a bounded real diff and supporting evidence. A reviewer response without complete source/test access is `PARTIAL` or `BLOCKED`, not `PASS`. The author cannot approve its own material changes. High-risk permissions/migrations/integrations call for domain-specific verification in addition to Reviewer.

## Orchestration and task routing

The objective is **minimal sufficient specialization**, not a 16-agent fan-out for every request.

1. **Intake:** identify product intent, acceptance criteria, impacted modules, working tree/revision, data classification, expected output and environmental constraints; ask only for genuinely blocking decisions.
2. **Task charter:** for consequential work record `TASK_ID`, C1–C5 risk, owner, read/write scopes, tests, permitted models/providers, relevant skills, expected cost/effort, stop conditions and user approvals.
3. **Capability preflight:** verify agents are discoverable, selected models resolve, effective `task` and `spawns` topology works, actual tool/MCP permissions and privacy restrictions are enforceable. `tools` filtering in frontmatter is not an isolation guarantee.
4. **Dependency DAG:** parallelize independent read-only investigation if worthwhile; serialize changes touching the same source, schema, API contract, design tokens or migration. Exactly one writer owns a modified path at a time.
5. **Compact handoffs:** return relevant file:line evidence, explicit decision, changed paths/contracts, test outcomes, open questions and next owner. Do not paste entire repo or all skills into every child prompt.
6. **Evidence-based review and final answer:** run task-appropriate tests, independent reviews as justified by risk, handle blockers honestly and provide reproducible results.

**Workload calibration:** C1–C2 should often be handled by one agent or MAIN with no additional quality loop; C3 merits targeted specialist check; C4–C5 may justify independent Reviewer/QA/Security and a bounded correction pass. The Orchestrator must not invoke an expensive multi-provider council, backup fallback chain or iterative QA loop by default. Govern **one shared budget** across all mechanisms.

### Sample natural-language requests

```text
Implement a role-based user management feature in this existing project.
Preserve the current Design DNA and API conventions. Delegate the right
specialists, test authorization boundaries, and show actual results.
```

```text
Review our new billing webhook handler for idempotency, retry safety,
security and reconciliation. Report defects first; do not deploy.
```

A user request **does not have to name an agent** after effective routing has been validated. If MAIN does not have WebTeam routing instructions, it may operate without specialist delegation. In that case request `/webteam_healthcheck` or `/webteam_dispatch --mode=inspect`; do not assume that installing agent files forces routing on every message.

## Project onboarding, adoption and required artifacts

**New project:** `/webteam_create_project "project name"` collects only essential product, user, design, stack, data, security, deployment and integration decisions. Distinguish approved, inferred and open decisions. Scaffold only after choosing a target path and verifying it does not collide with existing source.

**Existing project:** `/webteam_adopt_project <repo-path>` first inspects real code, Git state, UI, APIs, tests, data and docs. It creates a source-linked **Product/Engineering/Design DNA evidence matrix**, identifies contradictions and proposes safe incremental modernization. Do not overwrite branding or architectural decisions merely because a design or stack trend exists.

Common project documents (create only when justified and with actual content):

| Artifact | Owner | Purpose |
|---|---|---|
| `docs/PRODUCT.md` | Product | Actors, business rules, user goals and success metrics |
| `docs/DESIGN.md` | Designer | Visual identity, typography, tokens, components, interaction states |
| `docs/ARCHITECTURE.md` | Architect | Context, boundaries, quality scenarios, diagrams and ADR links |
| `docs/TECH_STACK.md` | Architect + implementers | Approved runtime/framework/data/third-party choices |
| `docs/ROADMAP.md` | Product + Orchestrator | Evidence-based milestones, dependencies and hypotheses |
| `docs/TEST_STRATEGY.md` | QA | Test pyramid, fixtures, tooling, CI and risk matrix |
| `docs/SECURITY.md` / privacy policy | Security + Product | Data classification, threat boundaries, accepted risks |
| `docs/governance/MEMORY_POLICY.md` | Orchestrator | Memory scope, retention and promotion approvals |
| `docs/DECISIONS.md`, `docs/adr/` | Architect + decision owners | Dated decisions and alternatives |
| `docs/audits/*.md` | Audit owner | Observed findings, tests, plans and accepted constraints |

Treat source code, tests, configuration and actual behavior as evidence. Project documents remain valuable decisions but should not be blindly trusted if stale. Keep the project context compact: `.omp/AGENTS.md` should link to the relevant sources rather than pasting all reference manuals into every prompt.

## Bundled skills and reference manuals

OMP skills live under `skills/<exact-name>/SKILL.md`, each with `name` and `description` frontmatter. The startup model should receive lightweight discovery information and load skill bodies/references when applicable. All references must live under their own skill directory and be read by exact path or `skill://...` only when the installed runtime supports those addresses. Avoid eager loading many skills into context.

| Discipline | Bundled skills | Reference manuals | Coverage |
|---|---:|---:|---|
| Accessibility | 14 | 3 | WCAG/APG, keyboard/AT, forms, grids, dense interfaces; [Accessibility examples](skills/webteam-accessibility-aria-widgets-interaction/SKILL.md) |
| Architect | 13 | 3 | C4/ADR, boundaries, fitness, reliability and modernization; [Architect examples](skills/webteam-architect-architecture-drivers/SKILL.md) |
| Backend | 15 | 7 | Fastify/TypeScript contracts, authz, consistency, async/reliability; [Backend examples](skills/webteam-backend-api-contract-engineering/SKILL.md) |
| Database | 15 | 4 | SQLite/PostgreSQL/MongoDB, invariants, concurrency, tuning and migrations; [Database examples](skills/webteam-database-backup-recovery/SKILL.md) |
| Designer | 16 | 3 | Art direction, Design DNA, 22 page patterns, 38 component contracts, visual critique; [Designer examples](skills/webteam-auth-profile-settings-ux/SKILL.md) |
| Frontend | 14 | 3 | Typed state and forms, complex components, accessibility, browser correctness; [Frontend examples](skills/webteam-frontend-a11y-components/SKILL.md) |
| Integration | 16 | 3 | SaaS/ERP/API events, webhooks, contract versioning and reconciliation; [Integration examples](skills/webteam-integration-api-versioning-consumer-contracts/SKILL.md) |
| Orchestrator | 14 | 4 | Capability preflight, task DAG, budget/risk, provider governance and handoffs; [Orchestrator examples](skills/webteam-orchestrator-capability-and-risk-routing/SKILL.md) |
| Performance | 14 | 3 | Web Vitals, API/DB profiles, load, SLO and measurable optimizations; [Performance examples](skills/webteam-performance-api-throughput-latency/SKILL.md) |
| Product | 13 | 3 | Discovery evidence, workflow/acceptance, roadmap and product metrics; [Product examples](skills/webteam-product-commercial-flows/SKILL.md) |
| Qa | 15 | 3 | Test strategy, deterministic fixtures, Playwright and business invariants; [Qa examples](skills/webteam-qa-api-and-consumer-contracts/SKILL.md) |
| Reviewer | 27 | 7 | Independent correctness/security/reliability/test-review and verdicts; [Reviewer examples](skills/webteam-reviewer-adversarial-counterexample-review/SKILL.md) |
| Security | 15 | 3 | Threat models, OWASP, permissions, privacy and supply-chain; [Security examples](skills/webteam-security-ai-agent-tool-risk/SKILL.md) |

The counts above describe **actual files in this release**, not all skills that may later be generated for additional roles. `webteam-reviewer` currently includes more narrowly targeted skills than some other roles; its operator should choose only the applicable review dimensions rather than loading all of them.

### Loading discipline

- Start with the agent's task and the nearest matching skill description; load **one to three** task-relevant skill bodies and only the reference headings used by that task. Broaden only when evidence shows a missing dependency.
- Respect exact `name`, file path and scope. Check for project/global collisions, disabled skill providers, and name overrides at runtime.
- Do not treat skill instructions as a security sandbox or as permission to copy/reuse confidential project memories.
- Designer's [page blueprint catalog](skills/webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md) and [component catalog](skills/webteam-component-interaction-contracts/references/COMPONENT_CATALOG.md) are on-demand references, not mandatory templates for every page.
- Backend's [capability blueprints](skills/webteam-backend-engineering-reference/references/BACKEND_CAPABILITY_BLUEPRINTS.md) similarly inform task-specific engineering rather than forcing microservices, cloud complexity or particular data stores.

## Professional product design and frontend

WebTeam Designer follows an **eight-stage practice**: (1) product discovery, (2) user/context research, (3) visual art direction and creative alternatives, (4) typography/palette, (5) interaction architecture, (6) systematic component tokens, (7) implementation/motion guidance, (8) browser-based visual critique and regression evidence.

**Distinctive does not mean decorative.** Avoid thoughtless repeated KPI card grids, purple/blue gradients, identical rounded rectangles, generic SaaS copy, arbitrary glows and poorly structured DataTables. Favor the product's actual roles, content, information density, tone and task hierarchy; use asymmetry or unusual palettes only when justified. Existing Design DNA is protected until an explicit redesign is approved.

Each screen contract should cover: meaningful content, navigation and orientation, responsive breakpoints based on layout failure, loading/empty/partial/error/success/unauthorized/offline states, keyboard behavior and focus, color-independent status, Vietnamese text/glyph handling when relevant, mobile constraints, charts/tables with semantic data, and browser screenshots at reproducible viewports. Data Grid interaction is not interchangeable with static HTML table semantics.

**Audit versus implementation:**

```text
/webteam_uiux --mode=report --scope=all --depth=deep
/webteam_uiux --mode=plan --pages=/dashboard,/users --style=preserve
/webteam_uiux --mode=fix --pages=/dashboard --max-fixes=3
```

Use `report` before redesigning a mature project. `fix` is limited to approved, reversible local UI changes with independent visual/keyboard regression evidence. Do **not** silently regenerate screenshot baselines or replace the brand identity. `/webteam_frontend` covers client architecture/correctness, while `/webteam_design_audit` focuses on understanding and preserving Design DNA.

## Backend, database, integration and architecture

**API boundaries:** explicit input/output schema, structured error contracts, authentication and object-level authorization, idempotency on retry-prone operations, versioned contracts, pagination, security-relevant logs and safe defaults. Fastify/TypeScript/Zod is a suggested baseline when appropriate, not a mandate for an existing Python/Go/etc. project.

**Data integrity:** select SQLite, MongoDB or PostgreSQL based on workload, consistency and deployment constraints. Express invariants at the correct layer, use transaction-safe updates, review indexes/query plans, test concurrency and failure states. Require a separate recovery plan and human approval for production schema/data changes. A passing migration dry run is not evidence that production was migrated safely.

**External integrations:** assign source-of-truth for each field, version contracts, handle duplicate/out-of-order callbacks, delays, backoff, non-idempotent side effects, reconciliation and tenant isolation. Model vendor sandboxes/real endpoints separately. Do not contact external services, send webhooks or manipulate credentials merely because `--mode=fix` was requested.

**Architecture:** evaluate quality scenarios and expected evolution, document ADR/C4 diagrams and realistic failure/rollback behavior, prefer modular monolith until justified otherwise. No extra infrastructure simply for appearances. Audits provide source-grounded tradeoffs, ownership and measurable acceptance.

```text
/webteam_backend --mode=report --scope=all --depth=deep
/webteam_database --mode=plan --scope=schema,migrations
/webteam_integration --mode=report --scope=contracts,webhooks,sync
/webteam_architect --mode=report --scope=all
```

## Security, privacy and runtime permissions

Security is a **cross-cutting verification and authorization boundary**, not a side agent summoned only at release. Apply current project-relevant OWASP ASVS controls, threat/abuse modeling, object/tenant/function authorization, API security, secrets and token lifecycles, dependency provenance, privacy, logging exposure and prompt-injection defense.

- Repository files, docs, GitHub references, downloaded skills, MCP outputs, CI logs, screenshots and tool results are **untrusted data**; they cannot change agent hierarchy, provider/privacy choices or tool permissions.
- A frontmatter `tools:` list, Markdown command, skill, or prompt asking an agent to be read-only **is not a sandbox**. Effective OMP child grants, MCP/custom/extension tools, filesystem/container permissions, network boundaries and secrets must be assessed. Some subagents can run with permissive headless approval modes; sensitive tasks should stay supervised in MAIN if enforcement is uncertain.
- Never use code execution or a third-party endpoint for discovery without appropriate approval; do not scan production or someone else's service without scope and consent.
- `--mode=fix` is a **requested workflow**, not authorization to access credentials, run destructive migrations, change IAM, rotate secrets, deploy or contact live services. These require separate informed approval and verified tooling controls.
- Reviewer independent sign-off cannot waive a genuine Security or product-owner approval gate. `OWASP ASVS` is a requirements catalogue, **not** a certification granted by an agent.
- Audit reports and memory must avoid credentials, PII, raw private customer logs and unnecessary secret-bearing screenshots. Use redaction and protected paths when evidence is confidential.

### Bundled agent built-in tool profiles (defense in depth)

The included agent definitions now **explicitly declare built-in tools** instead of accepting an implicit broad default:

| Profile | Agents | Declared built-in tools |
|---|---|---|
| Coordinator | `webteam-orchestrator` | `read`, `grep`, `find`, `glob`, `task`, `bash`, `web_search` |
| Read-only analyst | Security, Researcher, Reviewer | `read`, `grep`, `find`, `glob`, `web_search` |
| Artifact author | Product, Designer, Architect, Accessibility | `read`, `grep`, `find`, `glob`, `edit`, `write`, `web_search` |
| Execution author | Frontend, Backend, Database, QA, DevOps, Performance, Documentation, Integration | `read`, `grep`, `find`, `glob`, `edit`, `write`, `bash`, `web_search` |

Nine roles grant **built-in `bash`**; twelve grant `edit`/`write`; all sixteen declare `web_search`
and `find` (`find.enabled=on`). The three read-only roles carry no `bash`, `edit` or `write` and are
guard-enforced. Shell and write capabilities run under `tools.approvalMode=yolo`; installs,
privileged changes, production data, deployments and external effects still require approval. A
write-capable agent may edit **only its expressly delegated local paths**. The OMP `tools` list
alone cannot prohibit an MCP or extension tool that is granted independently. Verify all effective
grants during runtime acceptance, not merely these declarations.

## Quality assurance, testing and release

Pick test levels from actual risk and change impact: TypeScript/Biome checks, unit, component, schema/API, integration/contract, Playwright end-to-end, accessibility, visual regression, authorization negatives, concurrency/retry tests and relevant load tests. No test layer is compulsory for trivial cosmetic changes if a safer focused check meets acceptance criteria. Release-critical code must have appropriate independent QA/Reviewer checks.

**Evidence contract:** capture exact command, environment, source revision, fixture/data provenance, exit status, key artifacts, flakiness and failures. `NOT_RUN` is not `PASS`; static screenshot existence does not prove a visual test ran. Preserve approved visual baselines and investigate diffs rather than silently accepting them.

### Reviewer verdicts

`/webteam_review` supports **`report`, `plan`, `verify`**, not `fix`. Reviewer must inspect actual diff/requirements/tests, express falsifiable issues with `path:line`, confidence and reproductions, remove false positives, delegate fixes to code owners and retest the same finding after change. The reviewer **never fixes then approves its own code**. Use `--mode=verify --finding=RV-001` when the reported finding exists.

### Release readiness

`/webteam_release_check` checks supported acceptance evidence, security and compatibility, migration and rollback plans, accessibility, operational readiness and blockers. It is **not** a deployment command. A status of `PASS_VERIFIED` requires actual corresponding evidence, not an optimistic prose conclusion.

## Audits, reviews and controlled remediation

### Comprehensive project audit

```text
/webteam_audit --mode=report --scope=full --depth=deep --roadmap=on
/webteam_audit --mode=plan --scope=full
/webteam_audit --mode=fix --max-fixes=3
```

Audit may inspect Product, Architect, Designer, Frontend, Backend, Database, Security, QA, Accessibility, Integration, Performance, DevOps, documentation and release behavior **as applicable**; it should not summon every agent automatically. Default creates a new redacted Markdown report under `docs/audits/` **if write permission exists**. If writing is blocked, return the report content in chat and clearly state no file was saved.

A strong report includes audit date and revision, actual scope, evidence sources, coverage (`APPLICABLE / NOT_APPLICABLE / BLOCKED`), stable finding IDs, severity/confidence, reproducibility, impact, ownership, prioritized remediation dependencies, tests/acceptance, risk and rollback, optional outcome-based feature roadmap and residual unknowns. A speculative feature suggestion must not be presented as an observed bug.

### Mode semantics for specialist commands

| Mode | Allowed intent | Source edits? | Minimum output |
|---|---|---|---|
| `report` | Investigate and report | **No** (new report artifact only, where approved) | Findings with cited evidence and limitations |
| `plan` | Report plus phased remediation | **No** (new report/plan artifact only, where approved) | Priorities, dependencies, owners, measurable gates |
| `fix` | Apply a small, authorized local patch, then verify | **Only** with explicit scope/approval and actual enforced permissions | Before/after, diff, tests, independent review, rollback and blocked remainder |
| `verify` | Independent recheck of a specified previous finding (Reviewer) | **No** | Retest evidence tied to finding and revision |

**Argument parsing is not a security boundary.** All custom `.md` slash commands expand text with `$ARGUMENTS` under MAIN; do not feed this value into `eval`, shell, script or arbitrary endpoint. Unknown flags should lead to a clarification or safe refusal, not invention of behavior. Do not accept unsafe report paths, overwrite files through symlinks or write outside an approved repository. Each fix cycle has an explicit budget and stop condition.

## Complete native command reference

OMP discovers native `commands/*.md` non-recursively. Each file's **basename** defines `/command_name`; frontmatter supplies the description and argument hint. A successful autocomplete merely proves discovery/expansion and does not prove correct routing or actual subagent execution.

### Project lifecycle

| Command | Purpose / typical use |
|---|---|
| [`/webteam_create_project`](commands/webteam_create_project.md) | Initialize a new WebTeam web application with approved onboarding and project documents |
| [`/webteam_adopt_project`](commands/webteam_adopt_project.md) | Safely analyze and onboard an existing codebase into Project WebTeam |
| [`/webteam_status`](commands/webteam_status.md) | Report WebTeam project progress, blockers, agents and runtime capability status |
| [`/webteam_plan`](commands/webteam_plan.md) | Create a bounded, dependency-aware implementation plan without coding |
| [`/webteam_implement`](commands/webteam_implement.md) | Implement an approved feature using the right specialist agents |
| [`/webteam_docs_sync`](commands/webteam_docs_sync.md) | Check alignment of requirements, design, architecture and tests |
| [`/webteam_reference_analyze`](commands/webteam_reference_analyze.md) | Analyze a Git reference repository for safe, licensed adoption |

### Orchestration and visibility

| Command | Purpose / typical use |
|---|---|
| [`/webteam_orchestrate`](commands/webteam_orchestrate.md) | Plan and coordinate a bounded WebTeam task with verified native OMP delegation and independent quality gates. |
| [`/webteam_dispatch`](commands/webteam_dispatch.md) | Inspect and prove WebTeam agent routing in a bounded, read-only OMP session test. |
| [`/webteam_healthcheck`](commands/webteam_healthcheck.md) | Verify WebTeam installation and actual orchestration safely |
| [`/webteam_agents`](commands/webteam_agents.md) | Inventory and validate installed WebTeam agent definitions, effective discovery and execution readiness |
| [`/webteam_monitor`](commands/webteam_monitor.md) | Inspect live WebTeam subagents, Agent Hub visibility and monitoring settings without changing configuration |
| [`/webteam_models_audit`](commands/webteam_models_audit.md) | Audit approved default models, fallback and council routing |
| [`/webteam_memory_review`](commands/webteam_memory_review.md) | Audit project-scoped Mnemopi memory and Auto-Learn governance |
| [`/webteam_quality_loop`](commands/webteam_quality_loop.md) | Propose or run a bounded verify-fix-verify cycle |
| [`/webteam_help`](commands/webteam_help.md) | Explain the installed WebTeam commands and when to use them |

### Broad assurance and delivery

| Command | Purpose / typical use |
|---|---|
| [`/webteam_audit`](commands/webteam_audit.md) | Run comprehensive evidence-based WebTeam project audit with report, remediation plan or safe fixes |
| [`/webteam_test`](commands/webteam_test.md) | Run relevant unit, integration, API and E2E tests |
| [`/webteam_visual_test`](commands/webteam_visual_test.md) | Validate responsive visuals with Playwright screenshot baselines |
| [`/webteam_review`](commands/webteam_review.md) | Independent evidence-based risk review and after-fix verification; read-only by default |
| [`/webteam_release_check`](commands/webteam_release_check.md) | Run release-readiness checks without deploying |

### Product, experience and architecture

| Command | Purpose / typical use |
|---|---|
| [`/webteam_product`](commands/webteam_product.md) | Evidence-based product audit, remediation plan or narrowly bounded safe local fixes |
| [`/webteam_uiux`](commands/webteam_uiux.md) | Audit, plan, or safely fix professional UI/UX issues across product surfaces |
| [`/webteam_design_audit`](commands/webteam_design_audit.md) | Extract or verify project Design DNA and design consistency |
| [`/webteam_architect`](commands/webteam_architect.md) | Evidence-based architecture audit, remediation plan or narrowly bounded safe local fixes |
| [`/webteam_architecture_audit`](commands/webteam_architecture_audit.md) | Review architecture, contracts and migration risks |

### Application and data engineering

| Command | Purpose / typical use |
|---|---|
| [`/webteam_frontend`](commands/webteam_frontend.md) | Evidence-based frontend architecture, rendering, accessibility and client-correctness audit, plan and bounded fixes |
| [`/webteam_backend`](commands/webteam_backend.md) | Comprehensive, evidence-based backend/API/security/reliability audit, remediation plan, or bounded safe fixes |
| [`/webteam_database`](commands/webteam_database.md) | Evidence-based database audit, remediation plan or narrowly bounded safe local fixes |
| [`/webteam_integration`](commands/webteam_integration.md) | Evidence-based Enterprise APIs, Events, SaaS Integration and Data Synchronization: report, remediation plan and bounded authorized local fixes |

### Security, quality, accessibility and speed

| Command | Purpose / typical use |
|---|---|
| [`/webteam_security`](commands/webteam_security.md) | Risk-based application security verification, threat model, OWASP ASVS controls, remediation plan and restricted fixes |
| [`/webteam_security_audit`](commands/webteam_security_audit.md) | Assess threats, authorization and security boundaries |
| [`/webteam_qa`](commands/webteam_qa.md) | Evidence-based Quality Engineering, Test Automation and Business Workflow Assurance: report, remediation plan and bounded authorized local fixes |
| [`/webteam_accessibility`](commands/webteam_accessibility.md) | Evidence-based Accessibility, Inclusive Interactions and Operator-Ready UX: report, remediation plan and bounded authorized local fixes |
| [`/webteam_performance`](commands/webteam_performance.md) | Measured frontend/API/database capacity and reliability performance audit, plan and bounded safe optimization |


### Command selection guidance

- Start with `/webteam_help` for discovered commands, `/webteam_healthcheck` for full configuration and delegation checks, `/webteam_agents` for configured definitions and `/webteam_monitor` for observed activity. `/webteam_dispatch --mode=inspect` specifically tests whether MAIN can discover/route specialists; its smoke mode needs a safely bounded approved task.
- `/webteam_orchestrate --mode=plan` produces an owner/dependency charter; `--mode=run` proceeds only within actual permissions and approvals. `/webteam_plan` creates a feature plan without code edits; `/webteam_implement` handles an approved implementation.
- Domain-specific `report/plan/fix` commands should be used instead of a full audit when the issue is narrow. `/webteam_audit` consolidates related findings under one canonical ID rather than duplicating them.
- `/webteam_quality_loop` is a **bounded** verify/fix/verify proposal or workflow, not a continuously running automation. `/webteam_review` is read-only and independently verifies diffs.
- Commands taking paths, URLs or arguments require careful parsing and scope checks. Do not paste user-supplied strings unescaped into shell commands.

## Model routing, effort and cost controls

The framework can use one model for all roles or approved models for different task/risk classes. Do **not** assume that the alias `deepseek-flash` resolves unless discovered; OMP `modelRoles` may map verified role names to concrete selectors, and agent frontmatter may reference supported aliases such as `@review`. Model selectors and thinking/effort knobs are **runtime-specific** and require version/provider verification.

Set practical defaults by workload: Researcher/Documentation low-to-medium, routine Frontend/Backend/QA medium, complex Architect/Security/Orchestrator high when justified. Thinking **max** is not a universal premium setting and should be reserved for challenging decisions when supported and affordable. Use compact task charters, selective skill/reference loading and concise handoffs; a larger context window alone does not make work better.

**Three distinct decisions:**

1. **Normal role routing:** verified single-provider/single-model or role-specific approved selectors.
2. **Fallback:** OFF/ASK/AUTO depending on real ability to enforce provider/privacy/budget restrictions. If arbitrary child/runtime fallback cannot be restricted, forbid cross-provider AUTO; approval must precede new-provider dispatch.
3. **Multi-model deliberation:** optional CHALLENGE/COUNCIL for high-stakes conflicting choices, not an always-on fan-out. Model votes do not outweigh test evidence or owner decisions.

Do not invoke fallback, an advisor, a council and multiple loops concurrently without a verified shared cost budget. A failed model call does not grant permission to re-send sensitive source data to another provider.

## Memory and Auto-Learn governance

When the actual OMP installation supports **Mnemopi**, a project-scoped configuration can improve continuity, but settings keys and semantics must be inspected in that build. The core principle is **project isolation by default** with no automatic cross-project transfer.

- Recall only a small relevant set of memories for a task; retrieved memories can be stale or wrong and should be checked against current source/tests.
- Auto-Learn is a candidate-generator, not authority to change global agents or skills. Confirm capability and enablement; do not assume a standard directory exists on every profile.
- Promote a reusable learning from project → global only after sanitization, generalization, independent QA/Security review and **explicit user approval**. Never promote secrets, customer data, project-specific architecture, private screenshots or credentials.
- Document purpose, scope, retention, access and removal/rollback policies in `docs/governance/MEMORY_POLICY.md` where applicable.
- Caveman and `DeusData/codebase-memory-mcp` are optional separately approved integrations. Their installation, tool schema, permissions, source indexing and subagent access must each be validated; nothing should auto-index an unrelated repository.

## Adaptive Quality Loop

WebTeam's **quality cycle is a finite workflow**, not inherently the native OMP `/loop` implementation. Native loop mode selection and actual invocation/stop capabilities must be verified independently. When native loop stop/retry behavior is uncertain, MAIN should use explicit finite QA passes.

| Complexity | Extra corrective passes | Typical policy |
|---|---:|---|
| C1–C2 | 0 | Focused check only |
| C3 | Up to 1 | When there is a specific failing test or confirmed defect |
| C4 | Up to 2 | Bounded QA and independent review where warranted |
| C5 | Up to 3, separately approved | High-risk work with tighter gates and explicit stop conditions |

Each pass must name new evidence, a responsible owner, an approved budget, changed paths, tests and a meaningful stop condition. No unlimited “try again”, silent re-prompt, self-approval, repeated side effects or unreviewed baseline replacement. If progress plateaus, stop and report the blocker.

## Agent Hub and operator visibility

OMP's default Agent Hub shortcut is **`Alt+A`**, with customization possible via keymap. Use it to inspect **actually spawned** subagents, status, resolved models, live tool activity and usage where available. The MAIN session is not itself a task agent in the hub. `/agents` inventories configurations; `/jobs` lists async tool jobs; neither is a live agent ledger.

During global setup, optionally offer these presentation preferences **only if the installed schema supports them**:

```yaml
display:
  pinnedAgents: full
  subagentLivePreview: true
```

Ask before changing shared global display settings; preserve other keys. Visible agent cards are monitoring aids, not proof of correctness or effective sandboxing, and turning them on does not inherently issue extra model calls.

Use `/webteam_monitor --scope=active --detail=full` for a one-time inspection/guidance snapshot and `/webteam_agents --mode=verify --scope=all` for configuration readiness. A real safe `task` call, not roster presence, is needed to prove dispatch works.

## Runtime acceptance and evidence scorecard

| Check | Static evidence | Runtime requirement |
|---|---|---|
| Agents | 16 valid `.md` files, unique names | OMP discovers correct source/overrides, model resolves |
| Commands | 35 flat `.md` files | OMP expands representative commands as intended |
| Skills | 201 skill directories with valid `SKILL.md` | OMP discovers relevant skill names/references |
| References | 49 linked `.md` files | Relevant asset opens from effective skill root |
| Delegation | Agent frontmatter and policy | Approved, observed `task` spawn and completion |
| Permissions | Documented least-privilege intent | Actual host/tool/MCP/extension grants constrained |
| Models | Approved alias/role mapping | Model selection and provider/data boundary tested |
| Browser/API/test | Test plan and fixture assets | Exact test command/artifact/exit status recorded |
| Memory/Loop | Policy and consent documented | Enabled-specific behaviors verified separately |

Use precise labels: `STATIC_PASS` (documents and files checked), `RUNTIME_VERIFIED` (real OMP evidence), `PARTIAL_VERIFIED`, `BLOCKED`, `FAIL`, `NOT_RUN` or `NOT_APPLICABLE`. A checklist filled with promises is not a test run.

## Troubleshooting and failure recovery

| Symptom | Likely causes | Safe first action |
|---|---|---|
| Command missing in autocomplete | Wrong root/profile, filename, collision or disabled source | Check effective config/cwd and command basename, reload if needed |
| Skill not found | Incorrect one-level directory layout, provider filtering, duplicate name or missing `SKILL.md` | Verify `skills/<name>/SKILL.md` and skill discovery source |
| Agent registered but not running | MAIN routing not active, `task` unavailable, disallowed spawn/depth, model route failure | `/webteam_dispatch --mode=inspect`, then approved smoke test |
| Agent Hub empty | No active spawned tasks, MAIN-only work or selected session mismatch | Observe while an approved task is running; don't infer failure from idle state |
| Wrong model/effort | Alias unresolved, role mapping shadowed, provider unsupported, task override | Inspect effective role/model/effort and approval before changes |
| Skills inflate context | Eager skill loading or too many reference manuals | Load only the task's specific capability and necessary headings |
| Same bug repeatedly fixed | No ownership/acceptance criteria, repeated loop, stale tests, incomplete evidence | Freeze retries, inspect state, create a bounded root-cause charter |
| UI looks generic | Weak content/brand direction or screenshots never reviewed | Designer analysis and `/webteam_uiux --mode=report` |
| Reviewer says PASS without evidence | Diff/test coverage missing, self-review, unverifiable assumptions | Request precise evidence or mark `BLOCKED` |
| Config disappears in monorepo | Nearest non-empty `.omp`, cwd-dependent config, project overrides | Check project root and nested cwd context independently |
| Unintended external requests | Provider fallback, MCP/extension tool grants or overbroad child permissions | Stop, revoke unsafe route at enforcement layer, inspect logs without disclosing secrets |

**Recovery protocol:** stop repeated side effects; snapshot Git/worktree state; identify last known successful transaction/test; compare effective config and modified paths; restore from a verified backup if safe; rerun narrow deterministic checks; record unresolved risks. Never “repair” a failing smoke test by granting every agent write/network permission.

## Maintenance, contribution and release discipline

1. Treat this distribution as one canonical set of files, not a patch chain. Proposed skill additions must include purpose, triggers/exclusions, workflow, acceptance evidence, threat boundaries and an actual `SKILL.md`.
2. Before modifying a command, check its frontmatter, allowed modes, artifact path, approval behavior and overlap with other commands. Update `/webteam_help` and command inventory documentation in the same change.
3. Before changing an agent, verify real OMP frontmatter semantics and active model/tool restrictions. Do not silently widen `tools`, `spawns` or provider routing.
4. When references change, keep relative links under the skill directory and update only the relevant reference navigation, avoiding duplication of entire manuals.
5. Run the release's static structural/link/metadata/inventory checks, then OMP runtime smoke tests in an authorized disposable workspace. Maintain a change manifest, rollback plan and known limitations.
6. Do not ship historical upgrade prompts, bilingual duplicates, confidential logs, secrets, cached model credentials or backup snapshots inside the canonical ZIP.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 kemcafe.

## Authoritative external references

- [OMP v18.12.2 — task agent discovery and model routing](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/task-agent-discovery.md)
- [OMP v18.12.2 — native slash commands](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/slash-command-internals.md)
- [OMP v18.12.2 — config and capability roots](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/config-usage.md)
- [OMP v18.12.2 — Agent Hub and monitoring](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/agent-hub.md)
- [OMP skill discovery reference](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/skills.md)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/)
- [Playwright documentation](https://playwright.dev/docs/intro)
- [OpenTelemetry JS](https://opentelemetry.io/docs/languages/js/)

---

## Structured contract protocol (opt-in)

Agent and command files now document an opt-in, typed handoff protocol:
`webteam.task.v1` → `webteam.result.v1` / `verification.v1` / `review.v1`, validated by
`.omp/contracts/tools/validate_contracts.py` and the cross-field
`.omp/contracts/tools/verify_artifact_links.py`. See [CONTRACT_PROTOCOL.md](CONTRACT_PROTOCOL.md).
It does not change the roster, model roles, fallbacks, memory or tool authorization. Schema PASS is
not acceptance; the Orchestrator/human release gate owns `ACCEPTED`.

---

**Bottom line:** WebTeam is effective only when its **actual OMP installation**, scoped specialists, user-approved permissions and verification results match this documented operating model. Never confuse a comprehensive prompt with proof of runtime correctness.

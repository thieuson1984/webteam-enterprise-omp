# WebTeam Enterprise — OhMyPi Multi-Agent Web Engineering

**A reusable, project-aware team of 16 software engineering specialists, coordinated through OhMyPi (OMP) to build, improve, test, audit, and maintain professional web applications.**

WebTeam combines product discovery, deliberately crafted UI/UX, full-stack TypeScript engineering, verification, security, project knowledge, and risk-controlled delivery. It supports new applications and existing repositories without assuming that every task needs every agent.

> [!IMPORTANT]
> **This repository is an installation and operating distribution—not an already installed OMP extension or a turnkey application.** `WEBTEAM_MASTER_PROMPT.md` instructs a capable, authorized OMP session to create and verify 16 agent definitions and a larger specialist skill ecosystem. This package supplies **24 canonical native Markdown command templates** and **16 ready-to-install advanced Designer skills plus 15 professional Backend skills**. File presence, Markdown validity, and command autocomplete do **not** prove live model routing, safe permissions, working delegation, or production readiness. Those must be verified in the target environment.

**Start here:** [Install WebTeam](#3-installation-and-first-run) · [Agents](#5-team-structure-and-ownership) · [Create/adopt a project](#8-project-onboarding-and-documentation) · [Commands](#16-native-slash-command-reference) · [Project audit](#17-comprehensive-project-audit) · [UI/UX audit](#18-dedicated-uiux-quality-and-remediation) · [Backend audit](#104-webteam_backend-report-plan-and-bounded-safe-fix) · [Verify agents are running](#20-agent-visibility-routing-and-health-checks) · [Troubleshooting](#24-troubleshooting)

---

## 1. Mission, scope, and operating principles

WebTeam is a **professional engineering workflow implemented through OMP agents, native skills, command templates, project standards, and observed verification**. It is designed to produce maintainable outcomes with clear ownership and evidence rather than large volumes of plausible-looking code.

### Capabilities

- **Product engineering:** discovery, actor and permission modeling, user journeys, measurable acceptance criteria, feature planning, scope control, and roadmaps.
- **Distinctive product design:** an eight-stage Designer process, art direction, brand-appropriate layout and typography, Design DNA, interaction contracts, realistic content, accessibility, and browser-based critique.
- **Application development:** frontend, backend, database, integrations, architecture decisions, consistent API contracts, and defensive implementation.
- **Quality assurance:** risk-based Vitest, component/API/integration testing, Playwright E2E, visual regression, code review, and release checks.
- **Governed AI execution:** role-aware model selection, task difficulty/effort policies, optional fallback and multi-model challenge, memory isolation, Auto-Learn review, and bounded verification loops.
- **Existing-project stewardship:** evidence-based codebase adoption, Design DNA/Engineering DNA preservation, dependency awareness, and incremental refactoring.
- **Audits and improvement plans:** consolidated project audits, specialist audits, fix plans, cautiously authorized local remediation, and optional feature opportunities.
- **Operational transparency:** tool/agent discovery checks, observed native `task` delegation, permission reviews, truthful test results, and resumable installation checkpoints.

### Non-negotiable principles

1. **Evidence over assertions.** A claim such as *tested*, *deployed*, *secure*, *accessible*, *installed*, or *agent delegated* requires corresponding observed evidence.
2. **User control.** Obtain required approval for meaningful expenses, network/provider changes, third-party installation, destructive operations, production writes, migrations, secrets, and major design/architecture changes.
3. **Project isolation.** A project's product facts, source code, Design DNA, memory, and approvals are not automatically shared with another project.
4. **Least authority.** Prompt instructions are not a sandbox. Effective runtime tool permissions, MCP capabilities, credentials, filesystem and network boundaries determine what an agent can actually do.
5. **Specialize selectively.** Dispatch only agents and skills warranted by the task; keep one writer per overlapping checkout/path.
6. **Preserve established identity.** Existing branding, UX patterns, architectural decisions, data contracts, and uncommitted user work remain intact unless a change is justified and approved.
7. **Finish verifiably.** Reproducible checks and a truthful handoff matter more than simulated completion.

## 2. Distribution contents and authority

This distribution deliberately has **no revision-labelled filenames, historical upgrade prompts, or translated README**.

```text
WebTeam/
├── README.md                          # this operator and contributor manual
├── WEBTEAM_MASTER_PROMPT.md          # canonical bootstrap and operating specification
├── commands/                         # 24 flat OMP native Markdown command templates
│   ├── webteam_create_project.md
│   ├── webteam_adopt_project.md
│   ├── webteam_audit.md
│   ├── webteam_uiux.md
│   ├── webteam_backend.md
│   ├── webteam_healthcheck.md
│   └── ...                            # 18 further command templates
└── skills/                           # 16 Designer + 15 Backend skills
    ├── webteam-design-direction-and-taste/SKILL.md
    ├── webteam-page-experience-patterns/
    │   ├── SKILL.md
    │   └── references/PAGE_BLUEPRINTS.md
    ├── webteam-component-interaction-contracts/
    │   ├── SKILL.md
    │   └── references/
    │       ├── COMPONENT_CATALOG.md
    │       └── ACCEPTANCE_MATRICES.md
    ├── webteam-backend-api-contract-engineering/SKILL.md
    ├── webteam-backend-engineering-reference/
    │   ├── SKILL.md
    │   └── references/                 # 7 backend technical manuals
    └── ...                            # other advanced Designer / Backend skills
```

**Source-of-truth hierarchy**

| Source | Responsibility | Rule |
|---|---|---|
| [`WEBTEAM_MASTER_PROMPT.md`](WEBTEAM_MASTER_PROMPT.md) | Installation, agent contracts, governance, operating model and runtime acceptance | Authoritative for WebTeam architecture and policies |
| [`commands/*.md`](commands/) | Exact native slash command bodies, supported prompt options and command-specific safety | Copy the canonical files; do not invent approximations |
| [`skills/*/SKILL.md`](skills/) | Exact advanced Designer and Backend skill instructions | Keep their referenced assets alongside each `SKILL.md` |
| `docs/` inside an initialized **project** | Approved product, architecture, design, quality and operational decisions | Project-specific facts outrank generic reusable examples |
| Observed OMP runtime and official schema | Which paths, options, tools, models and integrations actually work | Version-specific runtime capability outranks examples in documentation |

The 16 agent definitions and other non-bundled specialist skills are **generated and validated by the bootstrap process**, not supplied as finished files in this package. Do not mistake this distribution for a complete preinstalled `~/.omp/agent/` tree.

### Typical installed locations (verify your active profile)

```text
~/.omp/agent/                         # illustrative user-level agent root
├── agents/webteam-*.md               # 16 generated agent definitions
├── skills/<skill-name>/SKILL.md      # generated specialist + bundled Designer and Backend skills
├── commands/webteam_*.md             # 24 flat copied command files
├── AGENTS.md                         # concise global entrypoint, if supported
├── RULES.md                          # high-priority rules, if supported
└── config.yml                        # narrowly merged, approved settings

<project-root>/
├── .omp/
│   ├── AGENTS.md                      # concise project routing/context entrypoint
│   ├── RULES.md                       # optional project-specific invariants
│   ├── config.yml                     # only necessary supported overrides
│   ├── agents/                         # rare, intentionally scoped overrides
│   └── skills/                         # project-specific skills
├── docs/
└── <application-source>/
```

Do not hard-code these paths for every OMP installation. Inspect the **active user profile, process working directory, installed discovery rules, local overrides, and command collisions**. Native command files are flat `commands/*.md` templates, not nested `commands/webteam/*.md` entries. A project-specific command may intentionally override a global name; unintended shadowing is a configuration defect.

## 3. Installation and first run

### 3.1 Prerequisites

- An OMP installation that can inspect files and supports native agents, skills, and prompt commands as confirmed by its installed documentation or help.
- Authorization to read the selected project/repository and, if installing globally, to write the **active** user-level agent configuration directory.
- A usable, authenticated AI model/provider or an approved setup path. An alias such as `deepseek-flash` must resolve in the real OMP model catalog; the string alone is not a working model.
- An initial Git status/backup strategy, so pre-existing work is never overwritten.
- Optional tools **only if actually needed and approved**: Node.js, a package manager, a browser/Playwright test environment, Caveman, Codebase Memory MCP, or Mnemopi support.

**Do not run unknown repository installers, package lifecycle scripts, migrations, network probes, or paid model tests merely because an installation prompt mentions them.** Inspect their side effects and request approval where required.

### 3.2 Fresh installation procedure

1. **Obtain the whole distribution.** Make `WEBTEAM_MASTER_PROMPT.md`, `commands/`, and `skills/` accessible to the OMP session. Supplying only the Master Prompt is insufficient for its exact companion-file installation contract.
2. **Launch OMP in the intended authorized location** and instruct it to read and carry out [`WEBTEAM_MASTER_PROMPT.md`](WEBTEAM_MASTER_PROMPT.md). File attachment and workspace access methods depend on your OMP setup.
3. **Allow read-only environment discovery first.** It should identify OMP version/profile, real configuration schema, existing agents/skills/commands, model/provider inventory, Git state, tools and effective permissions.
4. **Complete the one-time Global interview.** Select installation scope, model provider, safe model-routing policy, optional integrations, memory/Auto-Learn, optional council/fallback, quality-loop policy, permissions, and Agent Hub display preference.
5. **Review the proposed plan.** Confirm paths, changes, risk controls, budget, collisions, backups and rollback. Do not approve blind overwrites of unrelated files.
6. **Install in checkpoints.** Generate substantive 16-agent definitions and domain skills; install exact command and bundled Designer and Backend skill files; merge supported configuration changes carefully; record a manifest of completed and blocked stages.
7. **Run static and observed verification.** Test actual discovery and a harmless delegated `task`, not just file existence or a successful YAML parse. Optional functionality is separately tested only when approved.
8. **Receive an evidence-based handoff.** Require exact changed paths, results, known limitations, unresolved approval decisions and a reproducible resume/rollback path.

**Suggested request to OMP:**

```text
Read WEBTEAM_MASTER_PROMPT.md and its companion commands/ and skills/
directories. First inspect the active OhMyPi runtime and existing setup.
Present an installation plan, required user choices, permission impacts,
backups, and model/provider costs before modifications. Install only
approved components; then run the required observed WebTeam orchestration
smoke tests. Report PASS_VERIFIED, PARTIAL_VERIFIED, BLOCKED, or FAIL
with evidence rather than assuming installation success.
```

If a companion directory is missing, the correct behavior is to mark the corresponding stage **BLOCKED** and request access to the canonical files—not fabricate 23 replacement commands or claim the specialized skills were installed.

### 3.3 One-time installation decisions

| Decision | Recommended starting point | Why it matters |
|---|---|---|
| Placement | Global reusable agents/commands/skills; project-local requirements | Prevents cross-project identity and data leakage |
| Default model | User-selected provider, verified model/alias | Avoids invented names or silent provider changes |
| Effort routing | Adaptive by agent/task complexity | Limits wasted reasoning/context |
| Cross-provider fallback | `OFF` or consent-first `ASK` | Keeps cost and data egress under user control |
| Multi-model deliberation | `OFF`/`ASK` unless specifically warranted | Most tasks do not justify a council |
| Memory | Project-scoped Mnemopi if supported and approved | Separates project knowledge from global policies |
| Auto-Learn | Supervised; block unreviewed global skill promotion | Managed skills may live outside project scope |
| Native continuous Loop | **OFF**; bounded verification policy `ASK` | Prevents runaway retries/cost/side effects |
| External integrations | Opt-in, version/capability/permission checked | A configured MCP is not necessarily available to subagents |
| Subagent display | Optional `full` pinned roster + live preview | Helps observe actual work without changing routing |
| Project governance | Preserve existing data, Git state and Design DNA | Avoids destructive “setup” surprises |

These are recommended policies, **not assumed OMP-native enum values or automatically enforceable controls**. The bootstrap must translate approved policy to the actual runtime syntax and mark unimplemented restrictions explicitly.

### 3.4 Upgrading an existing installation

This distribution does **not** include upgrade-specific prompts. For an existing WebTeam, use the same Master Prompt with instructions to **inventory, compare, back up, merge only missing or approved changes, and revalidate**, without reinstalling or replacing working models, Memory, Auto-Learn or project docs. Resolve same-name commands/skills with diff review rather than overwriting automatically. A successful static diff is not the final runtime smoke test.

## 4. Global versus project architecture

**Global WebTeam defines how engineering work is performed.** Its agent roles, reusable skills, routing logic, baseline verification and security policies are cross-project tools.

**Project WebTeam defines what this application is.** It owns requirements, implementation facts, approved visual language, stack decisions, routes, data constraints, quality baselines, open issues, and a specific backlog. It may narrow or specialize Global behavior, but must not silently weaken Global security or provider permissions.

### Monorepo and working-directory hazard

OMP project **context instruction discovery** and project **settings discovery** may follow different rules. In particular, a nearer `.omp/` may shadow parent instructions, while `config.yml` lookup can depend on the launched working directory. Do **not** assume launching OMP from `apps/web/` sees the same project instructions or config as launching from repository root.

Verify both cases when relevant:

```text
repo/.omp/AGENTS.md
repo/.omp/config.yml
repo/apps/web/.omp/            # if present, may affect effective discovery
```

Use the intended repository root or an explicit, non-contradictory local pointer to authoritative project docs. Inspect the **effective** context, not a guessed path. Do not copy project-specific secrets or business facts into global instructions.

### Decision and document precedence

- User-approved product/security decisions override proposals.
- Fresh source and verified test evidence outrank stale unverified memories.
- Existing Design DNA remains protected until a legitimate redesign decision.
- Third-party reference code or documentation is **untrusted input**, not operating authority.
- Every exception should have an owner, reason, scope and review/expiry condition.

## 5. Team structure and ownership

WebTeam contains exactly **16 permanent specialized agents**, not 16 different default model sessions running at all times.

| Agent | Specialist role | Owns / primary artifacts |
|---|---|---|
| `webteam-orchestrator` | Engineering Director / coordination | Intake, difficulty/risk, task charters, routing, approval gates, roadmap and delivery evidence |
| `webteam-product` | Product Manager / Business Analyst | `PRODUCT.md`, actors, roles, user journeys, measurable acceptance criteria |
| `webteam-designer` | Principal Product Designer / Art Director | `DESIGN.md`, Design DNA, visual direction, typography, tokens and interaction contracts |
| `webteam-architect` | Principal Software Architect | `ARCHITECTURE.md`, `TECH_STACK.md`, ADRs, module and trust boundaries |
| `webteam-frontend` | Principal Frontend Engineer | Responsive React/SolidJS UI, data-aware components, typed routes/forms and frontend tests |
| `webteam-backend` | Principal Backend Engineer | Fastify services, Zod contracts, authentication/authorization and API tests |
| `webteam-database` | Database Architect | SQLite/MongoDB models, migration strategy, indexes, integrity and restore planning |
| `webteam-security` | Application Security Engineer | Threat modeling, tenancy/authorization validation, dependency and secrets risk |
| `webteam-qa` | Principal Test Automation & Quality Engineer | Test strategy, Vitest, API/integration, Playwright E2E/visual, reproducible evidence |
| `webteam-devops` | Platform / DevOps Engineer | Reproducible environments, CI/CD, observability, release and rollback plans |
| `webteam-performance` | Performance Engineer | Core Web Vitals, API latency, profiling, resource budgets and measured optimization |
| `webteam-accessibility` | Accessibility Specialist | WCAG-based checks, keyboard/focus, complex widget semantics and assistive-tech evidence |
| `webteam-reviewer` | Independent Senior Reviewer | Risk-ranked code/design review and independent quality-gate assessment |
| `webteam-researcher` | Technical Researcher | Primary-source research, dependency decisions, licensing and provenance |
| `webteam-documentation` | Technical Writer | Onboarding, API docs, knowledge organization, changelogs and runbooks |
| `webteam-integration` | Integration Engineer | OAuth/API/webhooks, idempotency, timeouts/retries, events and external contracts |

### Who actually coordinates?

- **Preferred:** WebTeam's Orchestrator governs web-development work and dispatches specialists through OMP's real delegation mechanism.
- **Supported fallback:** if nested `MAIN → orchestrator → specialist` delegation is not allowed, the **MAIN OMP session** coordinates and calls specialists directly.
- **Not acceptable:** claiming that a specialized agent worked on a task simply because the prompt mentioned its name.

Natural-language requests are the primary interface. Users normally **do not need to name agents**. For example, “Improve the customer table, preserve our Design DNA, and add E2E tests” should be classified and dispatched to relevant Designer/Frontend/QA roles—not all 16.

### Delegation examples

| Request | Commonly relevant owners | Typical verification |
|---|---|---|
| Fix a minor CSS spacing bug | Frontend; Designer if tokens change | Targeted visual and component check |
| Add role-based access control | Product, Architect, Backend, Security, QA; relevant Frontend/Database | Unauthorized-path tests and contract checks |
| Build a dense operations dashboard | Product, Designer, Frontend, Accessibility, QA; Backend/Database if needed | Real metric contracts, responsive/browser evidence |
| Improve a slow data query | Database, Backend, Performance | Profile, query plan, p95 before/after |
| Add an external payment/webhook provider | Integration, Backend, Security, QA | Signature/replay/idempotency tests, approval gates |
| Review release readiness | QA, Security, DevOps, Reviewer | CI evidence, rollback readiness, unresolved risks |

**Conflict rule:** assign one implementation owner per overlapping path; delegate read-only independent review in parallel; reconcile conflicting findings through evidence, project decisions, and user approval when needed.

## 6. Specialist skills and context efficiency

The Master Prompt mandates a broad professional skill catalog across Orchestrator, Product, Designer, Architecture, Frontend, Backend, Database, Security, QA, DevOps, Performance, Accessibility, Reviewer, Research, Documentation, Integration, and shared engineering methods. These skills must be **real, discoverable `SKILL.md` files with substantial procedures**, not merely a list of names in an agent prompt.

An adequate skill documents:

- purpose, activation triggers **and exclusions**;
- prerequisites, inputs and ownership;
- step-by-step method with examples/recipes and tool constraints;
- expected outputs and acceptance criteria;
- security cautions, common failure modes, escalation and rollback;
- tests and evidence required for a credible Definition of Done;
- local reference files, if any, via existing relative paths.

Install and smoke-test a skill individually. OMP discovery may not recursively find nested skill directories; references below a skill are intended for **on-demand reading**, not automatic scanning. Unknown `autoloadSkills` references can silently result in an absent capability. Avoid duplicate competing skills for the same concept.

### Context-efficient execution

1. Discover relevant project paths and docs before reading entire repositories.
2. Activate only the **few relevant** agent skills and, for Designer, only the matching page/component reference sections.
3. Pass narrowly scoped task charters: target paths, constraints, acceptance criteria, permitted tools, budget and expected evidence.
4. Reuse trustworthy search/index metadata before full-file reads; verify any index results against live source.
5. Apply high effort only where the task and risk justify it, and separate parallel read-only analysis from a single authorized writer.
6. Use bounded verification cycles; do not nest councils, provider fallback and Loop into uncontrolled multiplicative cost.

## 7. Models, reasoning effort, fallback and deliberation

WebTeam can operate with **one approved model**. Optional multiple models/providers can improve particular hard tasks, but are not a prerequisite for the team.

### Primary-provider onboarding and routing

During Global installation, **first** ask the user to select the primary provider; **then** inventory the models actually exposed and credential-ready on that provider. Verify selector syntax, aliases, tool support, context metadata and thinking/effort settings with the installed OMP version. Do not hard-code a hypothetical provider/model combination. An existing alias such as `deepseek-flash` is honored only when it actually resolves.

Illustrative role policy—not an OMP configuration file:

| Workload | Starting effort tendency | Escalate when |
|---|---|---|
| Documentation, targeted research and status | Low | Complex ambiguities, high-risk source analysis |
| UI/UX critique, frontend/backend and QA implementation | Medium | Difficult architecture, debugging or complex cross-cutting UX |
| Architecture, security and orchestration | High | Exceptional, consequential uncertainty warrants maximum supported effort |
| Narrow follow-up on an already isolated failure | Low/Medium | Evidence shows repeated failure to resolve |

The Master Prompt defines per-role baselines and adaptive C1–C5 task rules. Translate desired policy to the **real** provider and OMP controls; for example, OMP task effort hints may use `lo`, `med`, `hi`, while some providers expose different `defaultThinkingLevel` or reasoning mappings. Do not write unsupported keys or force a made-up context window.

### Cross-provider fallback (optional)

Fallback addresses model/provider **availability or task compatibility**, not independent design review. Its permitted mode is governed separately from the default model and any council. Recommended starting mode is OFF or ASK:

- **OFF:** do not switch away from the approved primary route.
- **ASK:** explicitly pause and obtain authorization before a new provider receives data or incurs cost; an automatic inherited route that switches silently is **not** ASK.
- **AUTO:** only when every executable fallback route—including inherited/session/child/extension paths—can be technically constrained to approved providers, data classifications, tools and budgets.

The Orchestrator must check whether a failed operation already produced side effects before retrying. Never replay payments, emails, migrations, production writes or other non-idempotent actions after an ambiguous timeout.

### Multi-model deliberation (optional)

Deliberation is separate from fallback. Use model diversity sparingly for significant architecture decisions, high-impact design tradeoffs, complex security reviews, and disputed technical evidence:

| Mode | Meaning | Typical use |
|---|---|---|
| `OFF` | No extra independent model review | Routine work |
| `CHALLENGE` | Bounded independent alternative/critique | Difficult but contained decisions |
| `COUNCIL` | Multiple approved independent perspectives and evidence-based arbitration | Exceptional high-stakes disputes |

The user may opt into an **ASK-before-panel** governance policy. Panel participants are temporary decision roles, **not extra permanent WebTeam agents**. Use independent candidate proposals, explicit dissent, independent tests where possible, and a decision log for consequential choices. Never mistake majority vote or self-reported confidence for ground truth.

### Cost and privacy controls

Specify per-task model call/effort, tool, token or budget limits when enforceable; otherwise use clearly described policy limits and observe actual consumption if exposed. Include **subagents, retries, fallback, councils, browser tests and Loop** in one overall task budget. Obtain approval before new providers receive private code, screenshots, prompts, log contents or external integrations. A document rule without runtime enforcement is `prompt-only`, not a proven security boundary.

## 8. Project onboarding and documentation

### 8.1 New application

Use the native command:

```text
/webteam_create_project "School Management System"
```

Or give a natural-language request. Orchestrator should interview progressively about:

1. product goals, intended users, roles/permissions, workflows, MVP and non-goals;
2. repository root, current code, Git policy, runtime and package manager;
3. frontend framework, design references, languages, brand, accessibility and target devices;
4. backend, data storage, authentication, integrations and operational constraints;
5. inherited model/memory policies, approved costs and data-sharing rules;
6. tests, CI/CD, hosting, recovery/rollback and release criteria.

Avoid repeated giant questionnaires. Record each consequential choice as **confirmed, accepted default, proposed/provisional, rejected or blocked**. Do not scaffold an approved architecture while a blocking product/data/security decision remains unresolved.

### 8.2 Adopt an existing repository

```text
/webteam_adopt_project "/path/to/existing-app"
```

**Discovery comes before edits.** Inspect Git state, manifest and framework versions, routes, UI implementation, design tokens, APIs, data models, tests, deployment files, current documentation and project instructions. Extract **Design DNA** and **Engineering DNA** from verified sources; label conflicting or uncertain findings with confidence. Produce a preservation/adoption plan and only then request approval for project-scoped document changes or refactoring. Do not reset Git, overwrite established design, run unreviewed scripts, or re-scaffold the application.

### 8.3 Project document contract

Documents are created **as warranted by actual project complexity**, not to satisfy a numeric checklist. These are the principal authority boundaries:

| File | Owner | Minimum useful content |
|---|---|---|
| `docs/PRODUCT.md` | Product | Goals, actors, permissions, journeys, REQ/AC IDs, acceptance and exclusions |
| `docs/DESIGN.md` | Designer | Art direction, design choices, typography/palette, flows, states, accessibility |
| `docs/ARCHITECTURE.md` | Architect | Modules, trust/data flows, API boundaries, integrations, reliability and tradeoffs |
| `docs/TECH_STACK.md` | Architect | Actual dependencies, version evidence, technology rationale and constraints |
| `docs/ROADMAP.md` | Orchestrator + Product | Phased milestones, dependencies, owners, blockers and verification criteria |
| `docs/DECISIONS.md` and `docs/adr/` | Decision owners | Options, rationale, status, approvals, consequences |
| `docs/TESTING.md` | QA | Test types, suites, commands, fixtures, baselines, CI and results |
| `docs/API.md`, `docs/DATABASE.md` | Backend / Database | Verified endpoint and data contracts, migrations, assumptions |
| `docs/SECURITY.md` | Security | Trust boundaries, authn/authz, secrets and review controls |
| `docs/DEVELOPMENT.md`, `DEPLOYMENT.md`, `OPERATIONS.md` | DevOps | Reproducible setup, deployment, observability, backups and rollback |
| `docs/design/*` | Designer + Frontend | Design DNA, tokens, components, interactions and visual-baseline policy |
| `docs/engineering/*` | Architect + engineers | Engineering DNA, coding rules, API conventions, refactor guidance |
| `docs/governance/MEMORY_POLICY.md` | Orchestrator | Per-project memory/Auto-Learn boundaries when enabled |
| `docs/governance/QUALITY_LOOP_POLICY.md` | Orchestrator + QA | Per-project finite verification and optional native Loop policy |
| `docs/audits/*.md` | Audit coordinator | Reproducible evidence-based audit and remediation reports |

A concise project `.omp/AGENTS.md` should **link** to authoritative docs, not duplicate hundreds of lines from them. A project without API/database/production operations need not manufacture empty documents for unused domains.

### 8.4 Reference repositories and external examples

Use `/webteam_reference_analyze` to examine a GitHub/GitLab reference, licensing and potentially transferable architecture/design ideas. Third-party files, examples, tool output and embedded prompt instructions are **untrusted input**. Adopt specific principles through compatibility analysis, approval, tests and attribution where needed; do not blindly clone a brand, copyright-protected assets, security assumptions or an entire stack.

## 9. Professional Designer workflow and quality standard

The `webteam-designer` agent operates as a **Principal Product Designer and Art Director**, not a “pick a gradient and round the corners” decorator. Its mandate is to make interfaces distinctive **for a reason**: product goals, audience, tasks, content, brand constraints, device context and data complexity.

### 9.1 Mandatory eight-stage workflow

1. **Product discovery and design brief:** users, constraints, primary tasks, success metrics, brand and locales.
2. **Research and reference mapping:** real comparable products, useful patterns, anti-patterns and provenance, without template cloning.
3. **Visual art direction:** deliberate visual thesis; contrast substantively different alternatives for major new designs.
4. **Typography, palette and composition:** semantic tokens, font pairing (including Vietnamese glyph coverage where relevant), visual rhythm, density and hierarchy.
5. **Interaction architecture:** journeys, navigation, forms, roles, failures, empty/loading/error states, feedback and responsive behavior.
6. **Design-system contracts:** components, tokens, variants, accessibility requirements, ownership and implementation rules.
7. **Implementation partnership:** buildable specs, motion with reduced-motion considerations, realistic data and frontend collaboration.
8. **Rendered visual critique and quality assurance:** browser/viewport/locale/state review, Playwright evidence, independent critique and safe refinement.

A new page does **not** automatically warrant a new design language. In mature projects use **preserve → standardize → evolve → redesign** with explicit rationale and an approval gate for major identity changes.

### 9.2 Why generic AI-generated interfaces fail

- Identical sidebar–metrics–cards–charts layouts irrespective of task.
- Fashion-driven purple/blue gradients, heavy glass/glow and arbitrary decoration without product identity.
- Uniform spacing, predictable card radius, stock imagery and generic buttons/typography across unrelated products.
- False KPI figures, placeholder-heavy content, awkward labels and no meaningful information architecture.
- Decorative charts with undefined units, data freshness, comparison basis or drill-down.
- Screenshots captured only in the default happy state, with no mobile, error, empty, dense or keyboard review.
- Subjective “looks modern” scores unsupported by actual UI/browser evidence.

WebTeam addresses these through **product-specific information hierarchy, editorial craft, real content, semantic tokens, individual page design, explicit component behavior and verified interaction states**. Novelty is not a license to break familiar controls or WCAG targets.

### 9.3 Sixteen bundled Designer skills

Every entry below is a real [`SKILL.md`](skills/) in this distribution, not just a name mentioned in the Master Prompt.

| Skill | Specialized responsibility |
|---|---|
| [`webteam-design-direction-and-taste`](skills/webteam-design-direction-and-taste/SKILL.md) | Art direction, product-specific creative thesis and critique |
| [`webteam-research-and-reference-transfer`](skills/webteam-research-and-reference-transfer/SKILL.md) | Reference research and responsible transfer without cloning |
| [`webteam-visual-identity-systems`](skills/webteam-visual-identity-systems/SKILL.md) | Brand-relevant palette, surfaces, icons and semantic tokens |
| [`webteam-typography-art-direction`](skills/webteam-typography-art-direction/SKILL.md) | Font selection/pairing, hierarchy, editorial rhythm and language coverage |
| [`webteam-layout-composition-and-rhythm`](skills/webteam-layout-composition-and-rhythm/SKILL.md) | Proportions, hierarchy, whitespace, optical alignment, responsive composition |
| [`webteam-information-dense-dashboard`](skills/webteam-information-dense-dashboard/SKILL.md) | Task-driven KPIs, dashboards, data-density ergonomics, honest visualization |
| [`webteam-landing-and-marketing-experience`](skills/webteam-landing-and-marketing-experience/SKILL.md) | Editorial storytelling, credible proof, conversion actions |
| [`webteam-auth-profile-settings-ux`](skills/webteam-auth-profile-settings-ux/SKILL.md) | Login/logout, recovery, account/profile/preferences, trustworthy states |
| [`webteam-tables-lists-and-cards`](skills/webteam-tables-lists-and-cards/SKILL.md) | DataTable, lists/cards, filtering, bulk operations and content density |
| [`webteam-interaction-motion-feedback`](skills/webteam-interaction-motion-feedback/SKILL.md) | Functional feedback, meaningful motion, reduced-motion behavior |
| [`webteam-content-realism-and-localization`](skills/webteam-content-realism-and-localization/SKILL.md) | Authentic microcopy, realistic states, locale readiness |
| [`webteam-design-system-evolution`](skills/webteam-design-system-evolution/SKILL.md) | Preserving and evolving components/tokens without accidental rebranding |
| [`webteam-uiux-design-critique`](skills/webteam-uiux-design-critique/SKILL.md) | Evidence-led design critique; separate objective defects from taste |
| [`webteam-ui-visual-e2e-qa`](skills/webteam-ui-visual-e2e-qa/SKILL.md) | Deterministic Playwright interaction, screenshots and review |
| [`webteam-page-experience-patterns`](skills/webteam-page-experience-patterns/SKILL.md) | On-demand page blueprints for 22 page families |
| [`webteam-component-interaction-contracts`](skills/webteam-component-interaction-contracts/SKILL.md) | On-demand contracts for 38 component families |

#### Page-specific UX catalog: 22 pattern families

The [`PAGE_BLUEPRINTS.md`](skills/webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md) reference covers additional patterns for search/filter/results, record details and master–detail, comparison, CRUD and multi-step workflows, onboarding, administration/permissions, approval queues, calendars/booking, collaboration/messages/notifications, Kanban, activities, file management and versioning, CMS/editors, analytics and reports, developer/API consoles, AI-assisted workflows, billing/checkout, maps, and offline/error/maintenance/incident states. **The canonical reference contains the exact P01–P22 definitions**; read the matching section for the current surface instead of flattening the catalog into a generic dashboard template.

#### Component catalog: 38 pattern families

The [`COMPONENT_CATALOG.md`](skills/webteam-component-interaction-contracts/references/COMPONENT_CATALOG.md) and [`ACCEPTANCE_MATRICES.md`](skills/webteam-component-interaction-contracts/references/ACCEPTANCE_MATRICES.md) define behavior for complex navigational, filtering, form, data, status and authoring components: menus, breadcrumbs, tabs, command palette, combobox, date-range picker, validation, OTP, uploads, dialogs, drawers, toasts, popovers/tooltips, tables/grids/treegrids, charts, editors, scheduling, selection and more.

A valid **component interaction contract** identifies:

1. intended task and rationale for selecting this control;
2. information hierarchy, semantic tokens, responsive layout and truncation/overflow behavior;
3. applicable default/loading/empty/error/success/disabled/selected/unauthorized states;
4. pointer, keyboard, focus, screen-reader and touch behavior;
5. long text/large datasets, localization, permissions and error recovery;
6. measurable acceptance checks, tests and reviewer responsibility.

Read **only the applicable P/C sections** to keep prompts and context proportionate.

### 9.4 Designer quality gates

Review at least: product distinction, task hierarchy, composition, typography, palette and surface semantics, component craft, real data/copy, interaction completion, accessibility and responsive reliability. Record each meaningful finding with **route, viewport, affected state, evidence, severity, user impact, minimal repair, test and confidence**.

- **No running browser?** Static critique only; visual quality `NOT_RUN` or `UNVERIFIED`.
- **No actual user evidence?** Mark aesthetic assumptions clearly; do not invent user preference statistics.
- **Existing design system?** Preserve its intended invariants; request approval for identity-breaking changes.
- **Accessibility?** Automated checks help, but manual keyboard/assistive-tech testing is still necessary where applicable.
- **Visual baselines?** Never silently replace screenshots to make a regression pass.

## 10. Professional Backend Engineering: Production Grade

The Backend specialist is a **Principal Backend Engineer**, not merely a Fastify route generator. The extension includes **14 task-activated Backend engineering skills plus one reference router (15 `SKILL.md` files)** and seven companion manuals, sourced from the actual distribution. It requires domain invariants, typed API contracts, object/property/tenant authorization, transactional integrity, failure-safe side effects, observability, focused testing and migration-aware releases. Existing frameworks other than Fastify remain valid; the stack defaults are preferences, never reasons for unsolicited rewrites.

### 10.1 The 15 bundled backend skills

| Bundled skill | Responsibility |
|---|---|
| [`webteam-backend-domain-architecture`](skills/webteam-backend-domain-architecture/SKILL.md) | Business capabilities, modular architecture, invariants and boundaries |
| [`webteam-backend-api-contract-engineering`](skills/webteam-backend-api-contract-engineering/SKILL.md) | Request/response schemas, OpenAPI compatibility, pagination and API evolution |
| [`webteam-backend-fastify-typescript-engineering`](skills/webteam-backend-fastify-typescript-engineering/SKILL.md) | Fastify encapsulation, validators, serializers, Node/TS lifecycle and safe config |
| [`webteam-backend-authz-multitenancy`](skills/webteam-backend-authz-multitenancy/SKILL.md) | Session/OAuth where applicable, fine-grained permissions and tenant boundaries |
| [`webteam-backend-data-protection-inputs`](skills/webteam-backend-data-protection-inputs/SKILL.md) | Input complexity, SSRF, injection, sensitive output and log protection |
| [`webteam-backend-persistence-consistency`](skills/webteam-backend-persistence-consistency/SKILL.md) | Transactions, concurrency, indexes, migration expand/contract |
| [`webteam-backend-async-workflows`](skills/webteam-backend-async-workflows/SKILL.md) | Queues, outbox/inbox, idempotency, background jobs and replay |
| [`webteam-backend-reliability-engineering`](skills/webteam-backend-reliability-engineering/SKILL.md) | Deadlines, bounded retries/jitter, backpressure, graceful shutdown |
| [`webteam-backend-observability-sre`](skills/webteam-backend-observability-sre/SKILL.md) | Metrics, traces, redacted logs, SLI/SLO and operations |
| [`webteam-backend-performance-engineering`](skills/webteam-backend-performance-engineering/SKILL.md) | Measured p95/p99, query profiling, cache correctness, capacity |
| [`webteam-backend-testing-quality`](skills/webteam-backend-testing-quality/SKILL.md) | Fastify inject, auth/tenant negatives, API contracts, race/fault tests |
| [`webteam-backend-external-integrations`](skills/webteam-backend-external-integrations/SKILL.md) | OAuth providers, inbound webhooks, retries, secrets and provider failures |
| [`webteam-backend-files-realtime-search`](skills/webteam-backend-files-realtime-search/SKILL.md) | Upload/download, streaming, SSE/WebSockets, safe search |
| [`webteam-backend-production-readiness`](skills/webteam-backend-production-readiness/SKILL.md) | Release safety, restores, version support and operational readiness |
| [`webteam-backend-engineering-reference`](skills/webteam-backend-engineering-reference/SKILL.md) | Load only the matching reference documents and capability blueprints |

### 10.2 Reference manuals, loaded on demand

The router links seven authored sources under [`skills/webteam-backend-engineering-reference/references/`](skills/webteam-backend-engineering-reference/references/):

1. [`API_CONTRACT_PLAYBOOK.md`](skills/webteam-backend-engineering-reference/references/API_CONTRACT_PLAYBOOK.md) — HTTP semantics, request/response schema, errors and client compatibility.
2. [`SECURITY_ABUSE_CASES.md`](skills/webteam-backend-engineering-reference/references/SECURITY_ABUSE_CASES.md) — object/property/tenant authorization matrix, abuse tests, OAuth and privacy.
3. [`DATA_CONSISTENCY_PATTERNS.md`](skills/webteam-backend-engineering-reference/references/DATA_CONSISTENCY_PATTERNS.md) — race control, transactions, safe migrations and durable idempotency.
4. [`ASYNC_RELIABILITY_PATTERNS.md`](skills/webteam-backend-engineering-reference/references/ASYNC_RELIABILITY_PATTERNS.md) — outbox/inbox, jobs, webhooks, timeouts/retries.
5. [`FASTIFY_NODE_RECIPES.md`](skills/webteam-backend-engineering-reference/references/FASTIFY_NODE_RECIPES.md) — Fastify hooks/encapsulation, schemas, TS and process lifecycle.
6. [`OPERATIONS_AND_TEST_MATRIX.md`](skills/webteam-backend-engineering-reference/references/OPERATIONS_AND_TEST_MATRIX.md) — operational SLO evidence, CI/contract/authz/chaos tests.
7. [`BACKEND_CAPABILITY_BLUEPRINTS.md`](skills/webteam-backend-engineering-reference/references/BACKEND_CAPABILITY_BLUEPRINTS.md) — **B01–B24**, covering identity, roles, search, billing, scheduling, uploads, queues, webhooks, realtime, reports, AI endpoints and more.

These reference materials are **not automatically injected wholesale** into every backend task. Select one or two relevant skills and only matching reference headings, while preserving existing project choices and observed facts.

### 10.3 Typical backend implementation flow

1. **Discover evidence:** read actual API code, consumers, DB/store, deployment versions, permissions, tests and uncommitted changes; mark uncertain facts.
2. **Define contract:** actor/action/resource, data sensitivity, invariant, request+response schema, error/status behavior, side effects and failure mode.
3. **Choose minimal architecture:** prefer a modular monolith and store/provider patterns already justified by requirements. Avoid speculative brokers, microservices and event sourcing.
4. **Implement safely:** authz server-side at object and property level, guard transactions and unknown write outcomes, bound I/O, preserve backward compatibility and test migrations off production.
5. **Verify adversarially:** negative permissions, duplicate writes, two-writer races, exhausted resources, partial network failure and real response serialization when relevant.
6. **Report evidence:** tests actually executed, observed cost/latency only, residual risk, rollout/rollback, owner approvals for consequential changes.

### 10.4 `/webteam_backend`: report, plan and bounded safe fix

Run from the intended project root after checking OMP command discovery:

```text
/webteam_backend --mode=report --scope=all --depth=deep --roadmap=on
/webteam_backend --mode=plan --scope=api,auth,data
/webteam_backend --mode=report --scope=async --routes=/api/jobs
/webteam_backend --mode=fix --scope=api --max-fixes=3
/webteam_backend --mode=fix --scope=all --dry-run
```

- **`report`** (default): read-only application inspection, write an evidence-based Markdown report under `docs/audits/`, list `BE-*` findings and optional separate capability roadmap.
- **`plan`**: additionally write ordered `P0–P3` work packages with API/migration compatibility, required tests, owners and rollback. No source edits.
- **`fix`**: implement only a few **already approved, reversible local corrections**, and verify the changed scope. The flag does **not** authorize production writes, security policy changes, destructive migrations, payment operations, secret rotations, provider changes or deployment. Those always need separate approval.

The command is a native **prompt-expander**, not an executable test framework. It does not by itself prove that `webteam-backend` was called; observe actual native `task` delegation and tool output. Its report must distinguish `PASS_VERIFIED`, `PARTIAL_VERIFIED`, `FAIL`, `BLOCKED`, `NOT_RUN` and `NOT_APPLICABLE` rather than asserting compliance.

### 10.5 Professional standards and versioning

- **OWASP ASVS 5.0.0** and API Security Top 10 (2023) inform specific abuse tests; an audit is not a security certification.
- **RFC 9457** provides Problem Details for HTTP APIs; **RFC 9700** provides OAuth 2.0 security best current practices when OAuth is used.
- **Fastify** compiles application-provided JSON Schemas and recommends response schemas; do not compile untrusted schemas or place DB I/O into initial validators.
- **OpenAPI 3.2.0** exists, but generators may support only earlier versions: verify actual tool compatibility.
- **OpenTelemetry JavaScript** tracing/metrics are stable; the logging SDK maturity and selected semantic conventions should be checked before adopting them.
- **Node production version** should be an active/maintenance LTS compatible with project dependencies; verify lifecycle status at execution time.

Backend owns service code. **Database** owns schema/migration design, **Security** the independent threat/permission review, **QA** independent test evidence, **Integration** provider contracts, **Performance** measurement, **DevOps** deployment and operations, and **Reviewer** consequential independent diff review. Respect single-writer ownership.

## 11. Technical stack and implementation standards

The preferred baseline is a starting point, **not a blanket instruction to install every library**.

| Area | Typical option | Selection guidance |
|---|---|---|
| Language/runtime | TypeScript, Node.js | Verify versions, deployment/runtime constraints |
| Backend framework | Fastify | Typed, modular APIs, service boundaries, hooks/encapsulation |
| Validation | Zod | Runtime boundary validation and coherent contracts |
| Formatting/lint | Biome | One compatible, consistent project policy |
| Frontend | Vite + React **or** SolidJS | Choose one based on project context and requirements |
| Client libraries | Appropriate TanStack packages when needed | Router/Query/Table/Form/Virtual only if justified |
| Database | SQLite **or** MongoDB | Choose based on query/transaction model, scale and operations |
| Tests | Vitest, Fastify `inject`, Playwright | Unit, component, integration, API and UI evidence |
| UI implementation | Semantic HTML, CSS/design tokens, justified accessible primitives | Design identity, states, keyboard support, actual content |
| Delivery | Suitable CI, containers and observability | Reproducible environments, least privilege, rollback |

Major choices belong in `TECH_STACK.md`/ADRs. Prefer maintainable modular structure over speculative microservices; confirm existing contracts before changing frameworks or persistence.

### Engineering expectations

- Explicit server-side authn/authz; never trust client-provided role or tenancy boundaries.
- Safe inputs, bounded resource usage, consistent errors and structured redacted logs.
- Reversible migrations with tested restore paths when data is involved.
- Typed API and database boundaries, idempotent external actions and observability.
- Async UI state correctness: loading, empty, partial, retry, error, stale, unauthorized and success.
- Responsive and accessible interactions across representative real devices/viewports.
- Dependency and license review before introducing third-party code or assets.

## 12. Testing strategy and evidence-based quality gates

`webteam-qa` owns the overall quality strategy and harness; code authors contribute tests but cannot independently certify critical changes without appropriate review. Quality is **built during implementation**, not appended at the end.

| Layer | Representative techniques | Evidence required |
|---|---|---|
| Unit | Vitest functions, guards, validators and core business rules | Commands/results, assertions and negative paths |
| Component | React/SolidJS interaction tests | User-visible state, keyboard, errors and validation |
| API | Fastify `inject`, schema and auth tests | Request/response contract, errors, ownership/tenancy |
| Integration | Disposable DB, contracts, workers, external mocks | Boundaries, data integrity, retries/idempotency |
| End-to-end | Playwright critical user journeys | Accessible flow completion, relevant fixtures and browsers |
| Visual | Playwright screenshot comparisons | Pinned browser/OS/fonts/viewport/data/locale/theme |
| Security | Relevant SAST/review and permission tests | Attack-surface coverage and limitations |
| Accessibility | Automated scans **plus** appropriate manual keyboard/AT checks | Specific WCAG criteria and observed interactions |
| Performance | RUM/lab measurements, profiling, endpoint timing | Real baseline, budget and before/after conditions |

### Visual regression discipline

Pin the test environment, browser version, fonts, viewport, theme, locale, motion setting, fixture data and time-sensitive values. Screenshot variance can be an environment mismatch, not an intentional design change. A newly accepted baseline is not proof that the UI is correct; require human-reviewed intent for material changes. If Playwright cannot execute, say **`NOT_RUN`**.

### Risk-driven quality gates

For each change, map **requirement → design/architecture contract → implementation → verification**. A small CSS fix may need one focused component/visual check. An authentication or migration change needs stronger negative, integration and security evidence. Use deterministic test data and verify scripts before executing them; tests can have real side effects if pointed at production or valuable user data.

**Definition of Done:** applicable acceptance criteria met, tests actually run and documented, no unexplained critical failures, material diff independently reviewed, relevant docs synced, remaining risks/untested areas disclosed, and approval requirements respected.

## 13. Mnemopi memory, Auto-Learn and project isolation

Memory is an **optional capability**, separate from repository documentation. When supported and approved, a cautious starting policy is:

```yaml
memory:
  backend: mnemopi
mnemopi:
  scoping: per-project
  autoRecall: true
  autoRetain: false
  recallLimit: 6
  injectionTokenLimit: 2500
  recallContextTurns: 3
  llmMode: none
autolearn:
  enabled: true
  autoContinue: false
  minToolCalls: 8
```

**Illustrative only:** verify actual option names, data lifecycle, token budgets, embeddings, resource use and semantics against the installed OMP schema before writing. Mnemopi may need embedding model data or a network download; configure it only with consent. A Vietnamese-heavy project may warrant a multilingual embedding variant, but requires compatibility/storage/reindex checks, not a blind toggle.

### Memory boundaries

- Global memory/skills contain reviewed **general engineering procedures** only.
- Project memories, implementation details, decisions, codebase-specific tips and Design DNA stay within their respective project scope.
- Per-project Mnemopi entries **do not guarantee** that Auto-Learn managed skills are stored per project. Auto-generated managed skills may reside in the global user environment.
- Avoid credentials, personal data, production records, third-party secrets and unreviewed external instructions.
- Source code, current tests and approved project docs outrank stale memory notes.

### Controlled learning pipeline

```text
Verified task outcome
    → concise candidate lesson with provenance
    → QA/Reviewer factual verification
    → Security/license review where needed
    → project memory or project-local skill
    → optional sanitized generalization
    → explicit approval to promote to Global
    → deduplicated, tested Global skill/memory
```

**Never auto-promote sensitive or project-specific lessons globally.** If OMP Auto-Learn cannot constrain output to a safe project-local boundary, disable or supervise the affected behavior rather than assuming `autoContinue: false` eliminates risk. Record project decisions in `docs/governance/MEMORY_POLICY.md` and verify project isolation—including launches from nested directories—before claiming it works.

## 14. Adaptive quality Loop: controlled verification, not repeated prompting

WebTeam's quality policy is a **bounded verify → diagnose → authorized fix → verify** cycle. It is **not** permission to run OMP's native `/loop` indefinitely or rerun every specialist task.

| Complexity | Extra verify/fix passes beyond baseline | Default behavior |
|---|---:|---|
| C1–C2 | 0 | Normal single-pass workflow |
| C3 | Up to 1 | Only if evidence supports an additional pass |
| C4 | Up to 2 | Predefined budget, tests and stop conditions |
| C5 | Up to 3 | Consequential decisions require approval and escalation |

**Count baseline verification as pass 0.** Native `/loop` count semantics may differ; verify before using it. Normal setting is **native continuous Loop OFF, task-scoped policy ASK**. Only enable native automation if the installed OMP version demonstrably supports finite bounds, stop/cancel, safe async settlement and non-idempotent-operation protection in a disposable test.

The bootstrap should create `webteam-adaptive-quality-loop` and `webteam-loop-evidence-evaluator` as real skills. Each extra pass needs a changed hypothesis and fresh reproducible evidence, not mere dissatisfaction. Stop on PASS, no progress, regression, risk/permission conflict, exhausted budget, deadline, or unreliable runtime control. A retry or model fallback **does not reset** the pass counter; do not nest model councils, fallback and repeated tools into runaway cost.

Use `/webteam_quality_loop` to propose or run an appropriately approved bounded cycle. No Loop may approve its own destructive operation, provider change, production deployment, snapshot re-baseline or Global memory promotion.

## 15. Optional runtime integrations

### Caveman — `JuliusBrussee/caveman`

If installed and compatible with the active OhMyPi runtime, Caveman can assist with focused investigation, edits or task workflows. Verify the actual extension, exposed capabilities, health, current permissions and interactions with existing orchestration before use. Do not assume OpenCode-oriented instructions work in OMP, or accidentally create a second autonomous multi-agent hierarchy.

### Codebase Memory MCP — `DeusData/codebase-memory-mcp`

When connected and approved, a code graph/index may help discover symbols, dependencies, references and implementation impact. Scope indexes to the authorized project, check freshness and exclusions, and confirm returned facts against actual code. **MCP tools may be visible/additive to subagents even when a prompt says “read only”; verify effective privileges.** Do not index secrets or neighboring projects automatically.

### Browser and test tooling

Use the actual available browser, Playwright installation and configured safe environments. Screenshots, visual comparisons, app launches, test fixtures and paid services may require explicit authorization. Optional tool absence is reported clearly; it is not a reason to fabricate test evidence.

### Integration readiness checklist

- Package/connector is installed, compatible, accessible and authorized.
- Effective subagent tools and credentials are constrained by the host runtime.
- Network/data egress and index scope are approved.
- Runtime smoke test is harmless and recorded.
- Failure falls back to a documented native/manual workflow, not invented tool output.

## 16. Native slash command reference

OMP Markdown slash commands are **prompt expanders**. They are not executable scripts, formal CLI parsers, tool-permission boundaries or guaranteed agent launchers. The command filename supplies the slash name; `$ARGUMENTS` is inserted as **untrusted text**. The MAIN session interprets documented flags, enforces authorizations and delegates through OMP's actual `task` tool when available.

Global commands are typically installed under the **active** user-profile `commands/` directory; project commands under `<project>/.omp/commands/`. Discover the real OMP rules and collision precedence before installing. Keep **one flat file per command**.

### All 24 commands

| Command | Purpose and default safety | Canonical file |
|---|---|---|
| `/webteam_create_project` | Progressive new-project onboarding and docs; consent before scaffolding | [`webteam_create_project.md`](commands/webteam_create_project.md) |
| `/webteam_adopt_project` | Evidence-based existing-repository adoption; discovery first | [`webteam_adopt_project.md`](commands/webteam_adopt_project.md) |
| `/webteam_status` | Read-only project status, blockers and current verified work | [`webteam_status.md`](commands/webteam_status.md) |
| `/webteam_plan` | Dependency-aware plan and acceptance criteria; no code by default | [`webteam_plan.md`](commands/webteam_plan.md) |
| `/webteam_implement` | Implement scoped, authorized features with relevant specialists | [`webteam_implement.md`](commands/webteam_implement.md) |
| `/webteam_design_audit` | Read-only Design DNA extraction, preservation and consistency review | [`webteam_design_audit.md`](commands/webteam_design_audit.md) |
| `/webteam_uiux` | Deep visual/UX and component audit, plan or bounded fix | [`webteam_uiux.md`](commands/webteam_uiux.md) |
| `/webteam_backend` | Backend, API, authz/data, reliability/security audit with report, plan or bounded safe fixes | [`webteam_backend.md`](commands/webteam_backend.md) |
| `/webteam_architecture_audit` | System boundaries, contracts, reliability and migration risks | [`webteam_architecture_audit.md`](commands/webteam_architecture_audit.md) |
| `/webteam_security_audit` | Risk-ranked security analysis, no intrusive testing by default | [`webteam_security_audit.md`](commands/webteam_security_audit.md) |
| `/webteam_audit` | Full-project evidence-backed report, remediation plan, bounded safe fixes | [`webteam_audit.md`](commands/webteam_audit.md) |
| `/webteam_test` | Risk-selected unit/component/API/integration/E2E checks | [`webteam_test.md`](commands/webteam_test.md) |
| `/webteam_visual_test` | Deterministic Playwright screenshot/visual evaluation | [`webteam_visual_test.md`](commands/webteam_visual_test.md) |
| `/webteam_review` | Independent diff/code/design review | [`webteam_review.md`](commands/webteam_review.md) |
| `/webteam_reference_analyze` | Analyze external Git references, provenance, license and adoption risk | [`webteam_reference_analyze.md`](commands/webteam_reference_analyze.md) |
| `/webteam_memory_review` | Mnemopi/Auto-Learn boundaries, quality and isolation review | [`webteam_memory_review.md`](commands/webteam_memory_review.md) |
| `/webteam_models_audit` | Verify model roles, default provider, fallback and council policy | [`webteam_models_audit.md`](commands/webteam_models_audit.md) |
| `/webteam_quality_loop` | Govern finite evidence-based verify/fix passes | [`webteam_quality_loop.md`](commands/webteam_quality_loop.md) |
| `/webteam_docs_sync` | Detect inconsistencies among code, product, design and tests | [`webteam_docs_sync.md`](commands/webteam_docs_sync.md) |
| `/webteam_healthcheck` | Consented, harmless observed orchestration/delegation smoke tests | [`webteam_healthcheck.md`](commands/webteam_healthcheck.md) |
| `/webteam_release_check` | Release readiness assessment **without automatic deployment** | [`webteam_release_check.md`](commands/webteam_release_check.md) |
| `/webteam_monitor` | One-shot read-only subagent activity/Agent Hub visibility snapshot | [`webteam_monitor.md`](commands/webteam_monitor.md) |
| `/webteam_agents` | Read-only 16-agent discovery/model/skill inventory | [`webteam_agents.md`](commands/webteam_agents.md) |
| `/webteam_help` | Explain command usage and applicable workflow | [`webteam_help.md`](commands/webteam_help.md) |

### Useful everyday command examples

```text
/webteam_help
/webteam_create_project "Attendance and School Equipment Management"
/webteam_adopt_project "/path/to/current-app"
/webteam_status
/webteam_plan "Add granular user permissions and audit history"
/webteam_implement "Add the approved permission matrix and tests"
/webteam_test "API authorization and teacher dashboard"
/webteam_visual_test "/dashboard"
/webteam_review "Current uncommitted diff"
/webteam_docs_sync
/webteam_release_check "staging"
```

**Commands are optional entry points.** The same intentions can be expressed in natural language. Agent routing must still be verified through observed delegation, not assumed from a command name.

## 17. Comprehensive project audit

`/webteam_audit` performs risk-driven coverage across product fit, architecture, frontend, UI/UX, backend, database, security/privacy, accessibility, testing, performance, operations, integrations/AI and documentation. A full-scope audit **must disclose what could not be examined**.

### Modes and common commands

| Mode | Source code | Markdown report | Remediation planning | Feature roadmap |
|---|---|---|---|---|
| `report` | Read-only by default | Required | Prioritized recommendations | On by default |
| `plan` | Read-only by default | Required | Sequenced, dependency-aware implementation plan | Off unless requested |
| `fix` | Bounded approved local changes only | Required with fix ledger | Required | Off unless requested |

```text
/webteam_audit --mode=report --scope=full --depth=standard --roadmap=on
/webteam_audit --mode=plan --scope=security,backend --depth=deep
/webteam_audit --mode=fix --scope=frontend --max-fixes=3 --budget=normal
```

### Supported argument contract

| Option | Valid values | Default / critical behavior |
|---|---|---|
| `--mode` | `report`, `plan`, `fix` | `report` |
| `--scope` | `full` or applicable listed domain(s) | `full`; `full` is risk-driven, not guaranteed exhaustive coverage |
| `--depth` | `quick`, `standard`, `deep` | `standard`; deep does not authorize intrusion or high-cost jobs |
| `--roadmap` | `on`, `off` | On in report; off in plan/fix |
| `--output` | Safe new `docs/audits/*.md` path | Generated new report filename; no overwrite, traversal or escaping symlinks |
| `--max-fixes` | Integer 1–20 | 5 for fix; issue count, **not** Loop iterations |
| `--budget` | `small`, `normal`, `extended` | `normal`; advisory effort label, not a hard provider charge cap |

Read the [canonical command contract](commands/webteam_audit.md) for exact domains and validation rules. Markdown does not enforce these parameter types; the running OMP agent must validate arguments before work.

### Report contract

Each mode produces **one redacted Markdown report inside the authorized repository's `docs/audits/`**, if safe writing is permitted. It must include an executive decision/limitations, scope and methods, evidence ledger with observed results, domain coverage, prioritized findings and detailed reproduction, risk register, phased remediation, optional feature roadmap, fix ledger for `fix`, residual risk and decisions still needed.

Use clear IDs such as `AUD-001` and priorities `P0–P4`. Separate **confirmed defects, hypotheses, missing evidence and strategic product opportunities**. A “GO” release recommendation or passing subset of checks is **not** a security certification.

### Fix-mode protections

A request explicitly using `--mode=fix` permits **reasonable reversible local fixes within the specified repository and approval rules**, not unrestricted self-modification. It does **not** authorize production requests, schema/data destruction, secret changes, purchases, provider reconfiguration, Git push/commit, deployment, security bypasses or silent screenshot-baseline updates. One writer owns a path; verify each material change with relevant tests and independent review. If a safe report path cannot be written, state the blocker—do not claim the file exists.

## 18. Dedicated UI/UX quality and remediation

`/webteam_uiux` applies the advanced Designer skills and matching P01–P22/C01–C38 contracts to **rendered user experience, not merely CSS formatting**. It complements, but does not replace, other audits:

- `/webteam_design_audit`: discover and preserve project Design DNA (usually read-only).
- `/webteam_visual_test`: observed Playwright screenshots and UI interactions.
- `/webteam_audit`: broad full-stack health including design as one domain.
- `/webteam_uiux`: specialist visual language, page/task hierarchy, interaction behavior, component contracts, responsive states, and safe remediation.

```text
/webteam_uiux --mode=report --scope=all --depth=deep
/webteam_uiux --mode=plan --scope=route --pages=/dashboard,/users --style=preserve
/webteam_uiux --mode=fix --scope=route --pages=/dashboard --style=preserve --max-fixes=3
/webteam_uiux --mode=report --scope=component --component=DataGrid --roadmap=on
```

### Key options

| Option | Valid values / meaning |
|---|---|
| `--mode=report|plan|fix` | Audit; prepare a change plan; or execute bounded authorized fixes |
| `--scope=all|route|component` | Whole app, selected routes, or selected component |
| `--pages=<routes>` | Comma-separated route list, validated within authorized app |
| `--component=<name>` | Specific named component |
| `--depth=quick|deep` | Targeted static or deeper visual/interaction review |
| `--style=preserve|evolve|redesign` | `preserve` default; identity-breaking redesign requires explicit approval |
| `--reference=<URL>` | Design inspiration for analysis, **not automatic cloning** |
| `--roadmap=on|off` | Optional improvement roadmap |
| `--output=<safe-path>` | Markdown file within authorized project, default `docs/audits/UIUX_AUDIT_<date>.md` |
| `--max-fixes=N` | Default 3, normally capped at 5 absent further approval |
| `--budget=<cap>` | User-defined spending/effort limit; runtime enforcement must be verified |
| `--dry-run` | Produce a proposed plan/report only, including in fix mode |

Inspect the [canonical UI/UX command](commands/webteam_uiux.md) for validation nuances. Results should cover typography, brand, density, interactions, roles/states, layout composition, mobile, long text and locale expansion, accessibility and screenshots where actually available. Preserve intentional design system constraints. A subjective preference alone is not a severity-one defect, and a static review cannot honestly certify pixel quality.

## 19. Day-to-day operational playbooks

### Plan → implement → verify → review

```text
/webteam_plan "Create approval workflow for purchase requests"
/webteam_implement "Implement the approved purchase approval workflow"
/webteam_test "Approval workflow, unauthorized actions and failure paths"
/webteam_review "Current change set"
/webteam_docs_sync
```

An effective plan identifies dependency ordering, one source writer per area, acceptance criteria, risk and needed test owners. The Orchestrator chooses relevant agents and records remaining work honestly.

### Preserve design when improving a mature product

```text
/webteam_design_audit "/dashboard and /users"
/webteam_uiux --mode=plan --pages=/dashboard,/users --style=preserve
/webteam_visual_test "/dashboard and /users"
```

Obtain approval before broad theme rewrites, changing primary navigation structure, replacing design tokens or rebaselining screenshots.

### Investigate a failing feature

```text
/webteam_status
/webteam_test "Failing route or API"
/webteam_review "Suspected defect area"
/webteam_quality_loop "Bounded verify-fix-verify for the confirmed failure"
```

Require a reproducible failure before repeated repair. Stop after no progress rather than spending more tokens on near-identical retries.

### Preparing a release

```text
/webteam_audit --mode=report --scope=full --roadmap=off
/webteam_release_check "staging"
```

The release check does not deploy. Production writes and external operations remain human-approval-gated.

## 20. Agent visibility, routing and health checks

### Which agents are installed versus actually running?

These are **different questions**:

| Question | Best interface | What it proves |
|---|---|---|
| Which of the 16 definitions exists and is discoverable? | `/webteam_agents --mode=verify --scope=all` | Static roster/discovery/model readiness where inspectable |
| Which subagents are currently active? | **`Alt+A` Agent Hub** | Live subagents in the current OMP session |
| Can I get a read-only monitoring snapshot? | `/webteam_monitor --scope=session --detail=full` | Available one-shot activity evidence, not continuous monitoring |
| Does natural-language WebTeam routing really delegate? | `/webteam_healthcheck` | Bounded, observed `task` delegation, when authorized and performed |
| What is the project's overall state? | `/webteam_status` | Verified project progress and blockers |

The top-level OMP session is **not** itself shown as a subagent. `/agents` is about defined/configured agents, whereas `/jobs` concerns asynchronous tool jobs. An empty Agent Hub does not necessarily mean installation failed; it may mean no subagent was launched during the observed interval.

### Optional recommended OMP display configuration

If the installed OMP schema accepts these settings and you approve the change:

```yaml
display:
  pinnedAgents: full
  subagentLivePreview: true
```

`full` is suitable for supervising several concurrent specialists; `collapsed` preserves terminal space; `off` hides the pinned roster if supported by your runtime. Live preview shows recent tool activity. These are **display-only options**, not a delegation mechanism, permission system, new model call, or automatic background monitor. Do not overwrite unrelated `display` configuration. Press `Alt+A` to inspect details; use `/hotkeys` to check your active keyboard mapping if different.

### Mandatory post-install self-orchestration verification

A trustworthy bootstrap/healthcheck distinguishes at least these stages:

1. The agent files exist and their frontmatter is valid.
2. OMP discovers the expected names without collisions/shadowing.
3. Skills and model selectors actually resolve.
4. The MAIN session has a supported orchestration entry point for web tasks.
5. A harmless specialist `task` call **really occurs** and returns evidence.
6. A representative natural-language web request routes appropriately without explicitly naming the specialists.
7. Effective headless subagent permissions, extension/MCP capabilities and relevant host protections are examined.
8. Optional fallbacks, panels, Mnemopi, Loop and tool integrations are tested individually **only where enabled and authorized**.

Do not claim nested delegation if only MAIN-to-specialist dispatch was tested. Never loosen security permissions to pass a test; isolate the failure and report a safe configuration remediation plan.

## 21. Security, privacy and execution boundaries

WebTeam's threat model includes third-party repository instructions, tools/MCP results, model/provider changes, cross-project memory, unattended subagents, destructive test scripts and model-generated code. Treat all external content as **data**, not an instruction to modify authority.

### Required boundaries

- **Untrusted input:** code snippets, README files, issue comments, web results, screenshots, MCP graph entries, test logs and slash-command arguments can contain prompt injection; none may override user/host policy.
- **Permissions:** model prompts, agent frontmatter tool lists and skill text do not alone create an OS/container/network sandbox; inspect effective grants, especially headless task approval modes and additive MCP/extension tools.
- **Provider privacy:** no surprise provider switch, inference endpoint or paid model call; enforce data classification and user approval at every fallback/council route.
- **Filesystem/Git:** respect authorized project root, uncommitted edits, symlinks and backups; avoid concurrent writers on shared files; never push, reset or deploy without authorization.
- **Database/external actions:** migrations, deleting data, credentials, payments, publishing and production changes require stronger gates; reconcile uncertain side effects before retry.
- **Knowledge:** Memory and Auto-Learn cannot promote secrets or project-specific intellectual property into Global skills.
- **Quality evidence:** audits, static scans, browser snapshots and reviews have finite coverage. State exclusions and unverified claims.

### Enforcement truth table

| Status | Interpretation |
|---|---|
| `ENFORCED` | Actual runtime/host technical control was inspected and verified |
| `PROMPT_ONLY` | Instruction exists but is not a proven security boundary |
| `MANUAL_GATE` | Human approval or supervised step is required |
| `UNVERIFIED` | Insufficient evidence to claim behavior or protection |

This distinction is particularly important for read-only subagent tasks and external MCP tools. A read-only instruction is not proof that a tool cannot write.

## 22. Installation and quality acceptance checklist

Completion is a **measured state**, not a subjective declaration.

- [ ] Active OMP profile, version, config schema and effective project root recorded.
- [ ] Backup/change manifest exists; unrelated settings and user work preserved.
- [ ] All 16 agent definitions are valid and **discoverable**.
- [ ] Required specialist skills are substantive, valid, discoverable and their references resolve.
- [ ] All 16 bundled Designer skills and their on-demand reference assets are present; all 15 bundled Backend skills and seven references are present.
- [ ] All **24 native commands** are discoverable, do not collide unexpectedly and at least one expands correctly.
- [ ] Primary model/alias resolves; actual model routing and optional effort mapping checked.
- [ ] Optional fallback, council, Mnemopi, Auto-Learn and integrations validated **only if enabled and approved**.
- [ ] Natural-language routing and harmless real `task` delegation observed (or correctly reported blocked).
- [ ] Effective tool/MCP permissions and relevant isolation tested to available authority.
- [ ] New/adopted project documents agree with observed project reality and approved decisions.
- [ ] Applicable tests and visual evidence actually run, with failures and `NOT_RUN` clearly marked.
- [ ] Risk, remaining work, costs if observable, decisions required and rollback instructions handed over.

### Outcome vocabulary

| Result | Meaning |
|---|---|
| `PASS_VERIFIED` | Observed against the actual OMP runtime/tooling with supporting evidence |
| `PARTIAL_VERIFIED` | Some layers or dimensions verified; remaining scope explicitly identified |
| `BLOCKED` | Prevented by missing access, companion files, permissions, tools or approval |
| `FAIL` | A checked invariant or observed behavior failed |
| `NOT_RUN` / `UNVERIFIED` | Not executed/observed; **never** substitute for a pass |

Static Markdown/frontmatter/ZIP checks count as **document integrity** only. They cannot prove agent runtime behavior, real accessibility, deployed security, or that all bugs are fixed.

### What a good handoff contains

1. Completed and incomplete installation/checkpoint stages.
2. Exact files created/modified and scope, with backup/rollback locations.
3. Agents actually invoked, resolved model routes and tools actually used, if observable.
4. Real commands run, exit statuses, browser settings and test evidence.
5. Known limitations, unresolved high-risk findings and required approvals.
6. Token/cost/time usage **when actually measured**; otherwise unknown.
7. The next small verified task or project-start command.

## 23. Operator guidance and common questions

**Must I mention a specific agent each time?** Usually no. Request the desired outcome in plain language; the Orchestrator or verified MAIN fallback routes specialists according to task scope. If routing has not yet been tested, use `/webteam_healthcheck` before relying on it.

**Does running a slash command automatically start a subagent?** No. Markdown commands expand prompts. Specialist invocation depends on active OMP delegation tools and routing policy.

**Does the package install every listed specialized skill immediately?** Not by extracting it. The 16 Designer and 15 Backend skills are physically bundled; other specialist skills and agent definitions must be created and verified during bootstrap.

**Can I use only one DeepSeek or other model?** Yes, as long as it resolves, supports required tools, and is allowed by policy. Councils and cross-provider fallback are optional.

**Will all 16 agents run on every request?** No. Dispatching every specialist would waste tokens, increase overlap and often reduce quality.

**Can it automatically fix every audit finding?** No. `fix` is bounded, evidence-led and approval-constrained. Some defects require product decisions, manual testing, environment access or high-risk changes that must remain proposed.

**Will automatic Loop make the UI look better?** Not reliably. Additional passes help when there is specific failing test/browser evidence; subjective repeated prompting without a bounded design critique often yields inconsistent aesthetics and higher cost.

**Can WebTeam guarantee WCAG compliance or production security?** No. It targets relevant WCAG/OWASP practices, tests only what is accessible/authorized, and reports coverage and limitations; formal compliance requires appropriate broader assessment.

## 24. Troubleshooting

| Symptom | Likely cause / safe response |
|---|---|
| Slash commands not listed | Wrong active profile/path, nested directory, stale reload, command collision or unsupported native discovery; inspect OMP command inventory |
| Command expands but no specialist appears | Prompt expansion is not `task` dispatch; inspect MAIN orchestration and tool availability |
| Agent exists but is not used | Discovery, `spawns`, task-depth, role alias or routing policy issue; run bounded `/webteam_healthcheck` |
| Agent Hub is empty | No subagent running, different session, hidden pinned roster or delegation not yet reached; use `Alt+A` and observed task evidence |
| `/webteam_agents` shows definitions but execution fails | Model may not resolve, credentials/tool permissions may be missing, or headless child restrictions differ; distinguish static and runtime states |
| Unknown Designer/Backend skill | Missing/invalid `SKILL.md`, wrong directory, broken references or stale discovery; verify canonical files and actual load |
| Model uses unexpected provider | Audit fallback inheritance, role mapping and per-task overrides; stop unapproved data egress |
| Mnemopi recalls another project's context | Pause sharing, verify effective root/scoping and nested path behavior; don't claim isolation without a two-project test |
| Auto-Learn writes user-global managed skills | Managed skill storage differs from memory scope; disable uncontrolled promotion and apply review/project-local workflow |
| Caveman or Codebase Memory MCP not callable | Integration not installed/connected, tool permission mismatch or stale index; fall back to approved source inspection |
| Playwright screenshots are flaky | Browser/OS/fonts/time/locale/fixtures/viewports vary; fix environment before comparing, never blindly update baselines |
| UI looks template-like despite passing tests | UX craft requires human/product judgment, truthful content, alternatives and rendered art-direction critique; use `/webteam_uiux` |
| Quality Loop fails to stop | Turn native Loop off; resume only a supervised finite verify–fix–verify cycle after confirming stop behavior |
| `/webteam_audit` gives chat summary but no file | Missing write scope, invalid or colliding path, tool failure; mark report not saved, resolve safe-write blocker |
| Report claims security/quality success with little evidence | Treat uncovered domains as UNVERIFIED, validate applicable areas and revise conclusions |
| Monorepo uses wrong instructions/config | Context and settings may resolve differently by cwd; inspect effective profile and nearest `.omp`, test root and nested paths |
| Setup stopped halfway | Use stage manifest/backups and continue from last verified checkpoint; never rerun destructive setup blindly |

## 25. Maintenance and change management

- Review model/provider availability, OMP schema, command collisions, tool grants and integration compatibility after relevant runtime changes.
- Review project docs, Design DNA and test baselines when the product actually changes; never rebrand solely because a new UI trend exists.
- Re-run `/webteam_healthcheck` after substantive routing changes, agent installation, provider/permission changes or major project relocation.
- Periodically review Mnemopi scope, stale knowledge, Auto-Learn generated skills and global promotions.
- Keep lessons, ADRs and roadmap updates concise and attributable; avoid multiple conflicting sources of truth.
- Do not install untrusted third-party extensions or blindly paste external prompt instructions into agent files.
- Maintain backups, provenance and a clear rollback strategy for configuration and application changes.

## 26. Standards and further reading

These references are **guidance for applicable work**, not a declaration that the project conforms to them:

- [OhMyPi source and documentation](https://github.com/can1357/oh-my-pi) — runtime behavior must be verified against the installed version.
- [OhMyPi native command discovery](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/slash-command-internals.md) and [task-agent discovery](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/task-agent-discovery.md) — version-specific implementation references.
- [OhMyPi Agent Hub](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/agent-hub.md) — monitoring concepts, validate active hotkeys/settings.
- [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) — reproducible visual testing and baseline management.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — accessibility goals and interaction patterns.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) and [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) — security risk and verification frameworks.
- [Web Vitals](https://web.dev/articles/vitals) — user-perceived performance metrics and measurement considerations.
- [Caveman](https://github.com/JuliusBrussee/caveman) and [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp) — optional integration sources; examine trust and OMP compatibility before activation.

---

### Recommended first workflow

**For a fresh installation:** provide the Master Prompt and all companion files, authorize the requested setup stages, validate actual runtime discovery/delegation and optional controls, then create your first project.

**For an existing application:** adopt the repository without overwriting its identity, establish a verified product/design/engineering baseline, and work through scoped plans, tests, reviews and documentation updates.

**For a mature project seeking quality improvements:** run `/webteam_audit --mode=report --scope=full` for overall engineering health or `/webteam_uiux --mode=report --scope=all --depth=deep` for professional UI/UX craft. Review evidence and approve a bounded plan before fixes.

**The goal is not the largest agent team or the most commands called. It is the smallest justified set of specialists producing a verifiable, distinctive, secure and maintainable result.**

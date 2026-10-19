# WebTeam Enterprise R10.1 — OhMyPi Installation, Operation and Upgrade Guide

**Release:** R10.1, audited · **Language:** English · **Target:** OhMyPi (OMP) · **Team:** 16 specialists + WebTeam Orchestrator

**New team:** [`WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R10_REVISED.md`](./WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R10_REVISED.md)  
**Existing R6 → Memory + Loop:** [`WEBTEAM_R6_TO_R10_UPGRADE_PROMPT_REVISED.md`](./WEBTEAM_R6_TO_R10_UPGRADE_PROMPT_REVISED.md)  
**Existing R6/R9/R10 with Memory already installed → Loop only:** [`WEBTEAM_EXISTING_INSTALL_LOOP_ONLY_UPGRADE_PROMPT.md`](./WEBTEAM_EXISTING_INSTALL_LOOP_ONLY_UPGRADE_PROMPT.md)  
**Existing R6 → Memory only:** [`WEBTEAM_R6_MEMORY_ONLY_UPGRADE_PROMPT_REVISED.md`](./WEBTEAM_R6_MEMORY_ONLY_UPGRADE_PROMPT_REVISED.md)  
**Vietnamese guide:** [`README_VI.md`](./README_VI.md) · **Audit:** [`WEBTEAM_R10_REVISED_AUDIT_REPORT.md`](./WEBTEAM_R10_REVISED_AUDIT_REPORT.md)

> These documents contain **installation instructions**, not an installed WebTeam. Runtime configuration, MCP permissions, actual model discovery, memory isolation, Loop cancellation and cost must be verified in the user's **installed** OMP. Run **exactly one** installation/upgrade path according to the situation. Do not re-bootstrap an existing team.

## Recommended R10.1 defaults

- **Global/Project:** install reusable agents/skills once; keep PRODUCT.md, DESIGN.md, ARCHITECTURE.md, memory and project-specific rules isolated per repository.
- **Memory:** optional consented `mnemopi` with `scoping: per-project`, `autoRetain: false`; Auto-Learn `autoContinue: false`, review-first, and enforce project-local output of learned skills or use supervised manual learning. Do not override an existing approved working setup.
- **Model routes:** first ask which primary provider to use, then discover its real model catalog; fallback and multi-model deliberation are separate consented features. No provider changes during a Loop.
- **Quality Loop:** `ASK` policy; continuous native Loop **OFF**. C1/C2: zero extra passes; C3: up to one; C4: up to two; C5: up to three only with risk approval. Use native `/loop` only after version-specific cap/stop/steering/async smoke tests; otherwise use manually orchestrated finite passes.
- **Tool safety:** Caveman and Codebase Memory are optional and need readiness checks; prompts cannot enforce OS/container or MCP tool restrictions. No unapproved production writes, memory promotion, payment or destructive actions.

The example `loop.mode: prompt` is only a **native loop mode preference**, not an enable switch or a WebTeam `ASK/AUTO` setting. If your current OMP version cannot guarantee safe native stopping, use the manual quality-cycle fallback.

## 1. What Is WebTeam?

**WebTeam** is a multi-agent engineering organization for professional, modern web application development. Its objective is not simply to generate code, but to own a disciplined delivery lifecycle:

**Requirements discovery → Technology decisions → Product design → Implementation → Testing → Independent review → Security → Approved deployment → Maintenance and improvement.**

The preferred backend stack is **Node.js + Fastify + TypeScript + Zod + Biome**; the preferred database is **SQLite or MongoDB**; and the preferred frontend stack is **Vite + TypeScript + React or SolidJS + TanStack + Zod + Biome**. Additional dependencies should be selected for specific technical reasons, not installed indiscriminately because they are popular.

WebTeam provides **16 specialist roles**, but ordinary tasks should invoke only a small, relevant subset. `webteam-orchestrator` interprets requests, chooses specialists, defines boundaries, coordinates reviews, and reports results. The project owner retains authority over consequential decisions.

## 2. Two Levels: Global WebTeam and Project WebTeam

| Level | Responsibility | Scope |
|---|---|---|
| **Global WebTeam** | The 16 agents, shared expertise, advanced skills, operational policies, model/routing rules, and project bootstrap workflows | Reused across many repositories |
| **Project WebTeam** | Product requirements, Design DNA, architecture, model restrictions, coding conventions, tests, ADRs, and roadmap | Belongs to one application |

Illustrative layout (OMP must verify the effective locations and supported configuration schema):

```text
~/.omp/agent/
  agents/
    webteam-orchestrator.md
    webteam-product.md
    ... (16 agent definition files)
  skills/
    design-master-workflow/SKILL.md
    webteam-deliberation-routing/SKILL.md
    playwright-visual-regression/SKILL.md
    ...
  config.yml
  webteam/                    # optional supporting policies/docs; not assumed recursive agent discovery

my-project/
  .omp/
    AGENTS.md
    RULES.md                  # only when useful and supported by installed OMP
    config.yml                # only if project overrides are justified
  docs/
    PRODUCT.md
    DESIGN.md
    ARCHITECTURE.md
    TECH_STACK.md
    ROADMAP.md
    DECISIONS.md
    TESTING.md
    design/                   # Design DNA, tokens, components, visual baselines
    engineering/              # Engineering DNA, coding/API conventions
    references/               # external repository analysis
    deliberations/            # redacted records of important model deliberations
  apps/                       # if a monorepo was selected
  packages/                   # only if necessary
```

### Can WebTeam agents live in their own subdirectory?

OMP commonly discovers `agents/*.md` **directly**; it should not be assumed to recursively scan `agents/webteam/*.md`. During bootstrap, the installer asks whether you prefer a dedicated subdirectory. Use that layout only if the installed OMP version demonstrates successful discovery and spawning. The safer default is flat, consistently prefixed `agents/webteam-*.md` files. An OMP extension/package can provide a more self-contained distribution, but its installation and discovery behavior must be verified.

## 3. The 16 WebTeam Agents

| # | Agent | Core responsibilities | Typical activation |
|---|---|---|---|
| 01 | `webteam-orchestrator` | Coordination, onboarding, planning, task/effort routing, multi-model council, escalation, quality gates | Entry point for project-level web work |
| 02 | `webteam-product` | Requirements engineering, user journeys, permissions, testable acceptance criteria | New features, domain logic, scope changes |
| 03 | `webteam-designer` | Eight-stage UI/UX workflow, design system, palettes, font pairing, anti-AI-slop, visual QA | New interfaces, design changes, Design DNA analysis |
| 04 | `webteam-architect` | System boundaries, modular design, ADRs, reliability, technical tradeoffs | Platform decisions, architecture, cross-module refactoring |
| 05 | `webteam-frontend` | React/SolidJS, Vite, TanStack, type-safe forms, accessibility, design-to-code | UI development, state, routing |
| 06 | `webteam-backend` | Fastify, Node.js, TypeScript, Zod, authorization, API lifecycle, observability | APIs, services, business logic, authentication |
| 07 | `webteam-database` | SQLite/MongoDB, schema, indexing, transactions, migrations, backup/restore | Data model, queries, schema transitions |
| 08 | `webteam-security` | Threat modeling, access control, tenant isolation, OWASP, supply chain | Sensitive data, permissions, high-risk changes |
| 09 | `webteam-qa` | Vitest unit/component/API/integration tests, Playwright E2E and visual regression | Test strategy, bug regression, release verification |
| 10 | `webteam-devops` | Reproducible environments, CI/CD, containers, monitoring, rollback, runbooks | CI, deployment, operations |
| 11 | `webteam-performance` | Core Web Vitals, profiling, API/database latency, caching, performance budgets | Slow interfaces, load and latency requirements |
| 12 | `webteam-accessibility` | WCAG 2.2 AA, keyboard/focus, screen readers, inclusive UX | Interactive UIs, forms, dialogs, dashboards |
| 13 | `webteam-reviewer` | Independent diff review, correctness, contracts, architectural drift | Changes requiring independent review |
| 14 | `webteam-researcher` | Official documentation, provider/model capabilities, reference repositories, licenses | Technology/model/API evaluation |
| 15 | `webteam-documentation` | Docs as code, API docs, project memory, onboarding, runbooks | Durable technical documentation |
| 16 | `webteam-integration` | OAuth, webhooks, external APIs, retries, idempotency, provider connectivity | Service, AI API, email, payment integration |

**Sixteen agents do not mean sixteen simultaneous models.** An agent is a professional role. Several agents may use the same model, and the Orchestrator should only dispatch the roles required by the task.

## 4. Key Skills and Capabilities

### 4.1 Product, Architecture, and Engineering

WebTeam discovers and formalizes requirements, generates product documentation, establishes coherent architecture, develops API contracts and ADRs, preserves conventions found in actual source code, and manages migrations, security, and enforceable coding standards.

### 4.2 Designer: Eight-Stage Professional Workflow

1. Product Context & Discovery.
2. Research & Reference Analysis.
3. Art Direction & Visual Identity.
4. Palette & Typography Engineering.
5. UX Architecture & Interaction Planning.
6. Design System & Component Specifications.
7. Design-to-Code Collaboration & Motion.
8. Visual QA, Anti-AI-Slop & Refinement.

Project decisions are recorded in `docs/DESIGN.md`, design tokens, and component contracts. The team must only claim that a screen has been visually verified when it has actually inspected browser output or screenshots using available tools.

### 4.3 QA, Vitest, and Playwright

Testing is selected according to the change's risk and scope:

- **Unit tests:** Vitest, isolated domain behavior, fixtures, controlled mocks, fake timers, and edge cases.
- **Component tests:** React/SolidJS Testing Library, interactive states, form validation, and accessible behaviors.
- **API tests:** Fastify `inject()`, Zod schemas, authentication/authorization, contracts, and negative cases.
- **Integration tests:** service ↔ database ↔ API behavior, migrations, and tenant/data isolation.
- **End-to-end tests:** Playwright, critical user journeys, sign-in, navigation, and cross-browser coverage where justified.
- **Visual regression:** Playwright `toHaveScreenshot()`, desktop/mobile baselines, reviewed diffs, and controls for font/OS/browser variance.
- **Regression and CI gates:** reproduce real defects, add prevention tests, and enforce risk-proportionate gates.

**Never accept updated visual snapshots solely to turn a failing test green.** Designer and QA must evaluate whether the visual change was intentional.

### 4.4 Learning from Existing Projects and External Source Code

- `webteam-project-design-dna`: discovers actual UI identity, semantic colors, spacing, typography, and component variants.
- `webteam-engineering-dna`: identifies conventions, module boundaries, APIs, and testing patterns.
- `webteam-design-preservation`: protects UI contracts, behavior, and visual baselines.
- `webteam-reference-repository-intelligence`: examines GitHub/GitLab repositories with pinned revisions, license, security, and compatibility analysis.
- `webteam-standards-evolution`: proposes controlled improvements with an impact assessment, regression plan, and ADRs.

External repository analysis defaults to **Learn Only**. It does not authorize copying source code or rewriting the target project.

## 5. Multi-Model Deliberation (Introduced in R4; Retained in R6)

Multi-model deliberation means **independent proposals and evidence-based criticism from distinct model routes** for important decisions. It is not a requirement to call multiple models for every prompt.

### Three Deliberation Levels

| Mode | When to use it | Behavior |
|---|---|---|
| **OFF** | Disabled or straightforward work | Normal specialist execution, tests, and reviews |
| **CHALLENGE** | Significant uncertainty or correctness risk | Model A proposes; independently selected Model B challenges and seeks counterexamples |
| **COUNCIL** | High-stakes architecture, authorization, or migration decisions | Usually 2–3 independent approved routes; bounded debate, testing, and Orchestrator arbitration |

At initial installation, WebTeam must ask:

- Whether deliberation should be available, and whether invocation is **OFF / ASK / AUTO** within an approved policy. **ASK** is the recommended initial setting.
- Which models/providers are approved for the Primary, Proposer, Critic, and optional Specialist roles.
- What kinds of decisions justify independent deliberation and the maximum calls/rounds/cost for a decision.
- Whether source code or internal documents may be sent to each provider. Secrets must be excluded.
- Whether to enable continuous Advisor/WATCHDOG operation. This is **independent** of deliberation and is not required for council sessions.

OMP may expose `modelRoles`, per-task model selectors, custom agents, and `advisor`/`WATCHDOG`; installed-version support must be checked. **A model list such as `model: [A, B]` typically represents fallback order, not two independent opinions.** A council requires distinct actual model invocations. Continuous Advisor supervision is not itself a deliberation council.

### Deliberation Process

```text
Risk/uncertainty justifies deliberation
  → Orchestrator frames a narrow question, evidence packet, privacy and cost limits
  → Model A and Model B analyze INDEPENDENTLY, without seeing each other's conclusions
  → Bounded criticism and rebuttal (normally one round)
  → QA/Security/Architect test claims against code and evidence
  → Orchestrator documents the evidence-based conclusion and dissent
  → User approves consequential decisions when required
  → One implementation owner modifies code and executes relevant tests
  → Save a redacted ADR/deliberation record
```

**Do not decide by simple majority vote.** Correctness evidence, security, and product requirements take precedence. Competing agents must not write to the same working tree at the same time. If only one usable model route exists, use an explicitly named single-model review rather than claiming independent multi-model consensus.

### Adding More Models Later

The Orchestrator may **propose**, but must not autonomously enable, additional model providers. A `MODEL_ADDITION_PROPOSAL` must identify the need, verified alternatives, capability/price/privacy implications, smoke tests, and a rollback strategy. Model registration, credentials, and paid inference require appropriate approval.

## 5B. Provider-First Discovery, Cross-Provider Fallback, and Per-Agent Optimization (R6)

R6 distinguishes three independent mechanisms:

1. **Primary routing:** select a suitable model for each agent from the approved default provider.
2. **Runtime fallback:** switch when a model/provider is unavailable under a verified, approved fallback policy.
3. **Multi-model deliberation:** intentionally obtain independent evaluations for a difficult decision.

Enabling one mechanism never silently enables another. Cross-provider fallback is disabled unless explicitly approved.

### 5B.1 Required Questions, in Order, During Initial Installation

1. **Ask for the default provider FIRST.** Show provider identities discovered in OMP (for example, DeepSeek, OpenAI, or a configured local/custom provider). Do not automatically assume DeepSeek. `deepseek-flash` is a candidate only when the user selects the matching provider and OMP verifies the alias.
2. **Only after provider selection, inspect that provider's model catalog.** Capture actual selectors, authentication and availability, reasoning/effort support, context/output limits, tools, vision, pricing when known, and operational status. Save a complete discovered snapshot when feasible, but present a concise shortlist for selection.
3. **Ask about fallback separately:** **OFF** (no cross-provider switch), **ASK** (confirm each cross-provider switch; recommended initially), or **AUTO** (use only previously approved providers/models, data classes, and cost constraints).
4. **If fallback is enabled, ask which alternate provider(s) are allowed and in what order; only then discover their models.** Do not enumerate or activate all providers indiscriminately.
5. **Ask permission to transmit project material and incur costs for each approved provider.** A provider may be authorized for public code but not private code, personal data, or sensitive logs.
6. **Only then address multi-model deliberation, Caveman, Codebase Memory MCP, agent placement, and other options** specified by the master prompt. Fallback consent does not imply consent for a council.
7. Preview the final routing/configuration diff and obtain required approval before applying it. Do not run paid test inference without permission.

### 5B.2 Bootstrap Skills for Model Routing

The R6 master prompt requires real OMP-discoverable `SKILL.md` implementations for:

- `webteam-primary-provider-onboarding`
- `webteam-model-capability-profiling`
- `webteam-agent-model-optimizer`
- `webteam-cross-provider-fallback`
- `webteam-effective-routing-audit`
- `webteam-model-compatibility-smoke-tests`
- `webteam-provider-routing-evolution`

These skills are loaded for setup, model failures, and approved policy changes—not for every ordinary coding task.

### 5B.3 Model Profiles for All 16 Agents

Each agent receives an **Agent Model Profile** identifying its primary provider/model, ordered approved fallback routes, supported thinking level, task context/compaction policy, required tool abilities, Caveman/Codebase Memory access, privacy classification, failure behavior, and verification evidence.

Architect/Orchestrator/Security may benefit from strong reasoning; Researcher/Documentation may prioritize cost and latency; Designer/Accessibility may require screenshot or vision capabilities for certain tasks; Frontend/Backend/QA require reliable tool use. Selection is based on verified capabilities rather than model reputation alone.

**Caveman and Codebase Memory are not installed “inside” individual models.** They are OMP/runtime/agent integrations. WebTeam verifies the selected model route's tool-calling compatibility and the agent's actual available tools before enabling a workflow. Fallback does not trigger a full repository reindex by default.

### 5B.4 Illustrative Native OMP Configuration

OMP documentation describes `retry.modelFallback`, `retry.fallbackChains`, `retry.fallbackRevertPolicy`, and `modelRoles`, subject to installed-version verification. **The following model selectors are placeholders and MUST NOT be copied unchanged into production configuration:**

```yaml
# Illustration only. Use actual, verified selectors and valid keys for your OMP version.
modelRoles:
  webteam_primary: "PRIMARY_PROVIDER/PRIMARY_MODEL"
  webteam_review: "PRIMARY_PROVIDER/REVIEW_MODEL:medium"
retry:
  modelFallback: true
  fallbackRevertPolicy: cooldown-expiry
  fallbackChains:
    webteam_primary:
      - "FALLBACK_PROVIDER/FALLBACK_MODEL:medium"
    webteam_review: []
```

Do not invent fallback keys such as `retry.fallbackChains.agent:webteam-qa`. Agent-specific routing must use the actual subagent model ordering and/or overrides supported by the installed OMP version. **An agent's candidate model array is not necessarily a closed allowlist:** effective routing may inherit more general retry chains, including `provider/*` and `default` entries.

**OFF must really mean OFF.** An unapproved provider must not receive project data through an inherited fallback chain. Do not damage other agents' shared global configuration to enforce that restriction; use an isolated OMP profile or another native enforced boundary when necessary. A prompt policy alone is not a hard network/permission boundary.

### 5B.5 Runtime Scenarios

| Situation | Required behavior |
|---|---|
| Primary returns a retryable 429, timeout, or outage | Check effective chain, approved data transfer and cost; ASK requests authorization, AUTO stays within approved limits |
| No eligible fallback | Report the blocker or propose a model; never silently choose an unapproved one |
| Fallback has a smaller context window | Produce a compact but sufficient context handoff; stop if a safe transfer is impossible |
| Fallback lacks required tools or vision | Do not proceed with a tool/screenshot-dependent step; ask for another approved route or change in scope |
| Migration or side-effectful operation is in progress | Inspect state before retrying; never blindly replay non-idempotent actions |
| Council participants resolve to the same model via fallback | Do not count them as independent votes; correct the panel or report insufficient diversity |
| Task is difficult but the primary model is healthy | Escalate effort or propose deliberate review; difficulty alone is not an outage-fallback trigger |

### 5B.6 Auditing or Changing Model Routes Later

Request an audit without allowing immediate changes:

```text
Audit all WebTeam model routes. Show which primary and fallback models
all 16 agents actually resolve to, supported reasoning levels,
effective context limits, tool compatibility, fallback privacy,
and the health status of Caveman and Codebase Memory MCP.
Propose improvements only; ask before modifying provider configuration.
```

Or propose a limited new fallback:

```text
Propose a new cross-provider fallback for Security and Architect only.
Discover candidates only after I approve the alternate provider.
Compare verified capabilities and costs; do not activate any route
until I approve the final per-agent model matrix.
```

The Orchestrator should produce a `MODEL_ROUTING_CHANGE_PROPOSAL`, compare before/after behavior, audit all affected agent profiles, obtain approval, record the change, and verify or roll back its activation. Never autonomously enable a new paid provider.

## 6. Installing Global WebTeam with the Master Prompt

### 6.1 Prerequisites

1. Install OhMyPi and verify that its `omp` executable works.
2. Have at least one available OMP provider/model, or be prepared to authenticate safely when installation asks. **You choose the default provider**; DeepSeek is not mandatory. Retain `deepseek-flash` only if that provider/alias is selected and verified.
3. Allow appropriate read/write access to the OMP configuration area, with backups or Git available for existing configuration.
4. **Never paste API keys into prompts, Markdown files, or source control.** Use OMP/provider authentication facilities.
5. Understand the network, code execution, installation, privacy, and indexing implications before enabling Caveman or Codebase Memory.

Check commands against the installed CLI; representative commands may include:

```bash
omp --version
omp models
omp models find deepseek       # example only; replace with the selected provider/model
omp config list --json
omp config path
```

`omp config path` and other example syntax might differ across versions. If a command is unsupported, consult `omp --help` and the installed command's `--help` output instead of guessing.

### 6.2 Launch OMP and Submit the Master Prompt

Start OMP from a safe working directory. Provide the full contents of [`WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R10_REVISED.md`](./WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R10_REVISED.md) with the instruction:

> Execute this WebTeam Enterprise R6 bootstrap prompt in my active OhMyPi environment. First inspect the installed runtime, ask the mandatory global installation questions, preserve existing configuration, and implement and verify actual agents, skills, and policies. Do not create a web application yet.

If your OMP session cannot read the Markdown file directly, paste the master prompt text into the session. Do not assume every OMP version supports a particular file-import command.

### 6.3 Mandatory Global Installation Onboarding

The installer must ask the following questions before it modifies configuration:

| Question | Choices / recommendation |
|---|---|
| Agent file location | `agents/webteam/` only if discovery is verified; **flat `agents/webteam-*.md`** is safest |
| **Default provider (ASK FIRST)** | You choose DeepSeek, OpenAI, custom/local, etc.; only then enumerate models from that provider |
| Models for the 16 primary agent routes | Select from the verified catalog; `deepseek-flash` is optional and must actually resolve |
| Cross-provider fallback | **OFF / ASK / AUTO**; ASK is recommended initially |
| Fallback providers/models | Inspect candidates only after you approve each fallback provider; verify effort, context, tools and cost |
| Fallback data permissions | Approve code/data types and cost scope for each provider |
| Multi-model deliberation | **ASK** recommended; OFF and approved AUTO are also supported |
| Council model/provider selection | Use genuinely available and authorized OMP model routes |
| Code/document sharing | Approve separately per provider; never send credentials or secrets |
| Inference limits | Number of calls, rounds, time budget, and monetary ceiling when enforceable |
| Advisor/WATCHDOG | **OFF** unless explicitly requested |
| Caveman | Yes/No; inspect before installing, install only with approval |
| Codebase Memory MCP | Yes/No; verify actual OMP connectivity, privacy, and index scope |
| Agent subdirectory/package | Ask preference; keep flat files if recursive discovery is unsupported |
| External installers/provider setup | Require prior disclosure and approval of material effects |

If only one model works, council policies can remain configured but unverified/inactive. If a selected required integration fails its smoke test, dependent setup must stop and offer remediation or an explicitly approved skip—not silently claim success.

### 6.4 Caveman and Codebase Memory MCP

Verify current upstream documentation before installing:

- **Caveman:** <https://github.com/JuliusBrussee/caveman>. It may provide an OMP-native installer. Review the current installer and revision before executing remote code.
- **Codebase Memory MCP:** <https://github.com/DeusData/codebase-memory-mcp>. Provides codebase graph retrieval. Verify index scope/freshness, effective OMP MCP visibility, and exclusions for `.env`, secrets, and private data.

The Orchestrator must avoid duplicate plugin/crew orchestration, perform health checks **within the effective OMP session**, and assign only supported agent-specific policies. Large graph indexing is not warranted for every minor edit.

### 6.5 Expected Bootstrap Results

- All 16 `webteam-*` agents exist and are discoverable through OMP.
- Relevant specialist skills are real, valid `SKILL.md` files with supporting material, not just skill names.
- The chosen primary provider resolves; all 16 model profiles have effective effort/context/tool policies and explicitly approved or disabled fallback behavior.
- Deliberation OFF/ASK/AUTO policy is recorded separately from fallback; approved role selectors resolve.
- Selected plugins/MCP integrations work or are explicitly classified as blocked/unverified.
- A smoke-test report includes actual commands, results, paths created, and remaining limitations.
- No application project is created unless the user separately requests one.

## 7. Initializing a New Web Application

### 7.1 Example Request

```text
I want to create a new web application using WebTeam.
Start the new-project onboarding process.
Help me choose React or SolidJS, SQLite or MongoDB,
repository structure, design language, provider/model policy,
security, testing, deployment, and CI.
After my decisions are confirmed, generate real PRODUCT.md,
DESIGN.md, ARCHITECTURE.md, TECH_STACK.md, TESTING.md and ROADMAP.md.
Do not fabricate requirements or make paid/destructive changes without approval.
```

### 7.2 Expected Workflow

The Orchestrator works through grouped questions: product and audience → repository/runtime → backend/database → frontend/design → inherited or narrowed primary/fallback/council rules → testing/deployment. After confirmation, Product creates `PRODUCT.md`; Designer creates `DESIGN.md`; Architect creates `ARCHITECTURE.md`; QA creates `TESTING.md`; DevOps creates operational guidance; and Orchestrator coordinates `ROADMAP.md`, cross-document validation, and approved implementation.

Not every optional field deserves a separate question. WebTeam should recommend sensible defaults and ask for input only where missing information materially affects product, architecture, permissions, cost, or delivery.

### 7.3 Example: School Management Application

```text
Build a Vietnamese school-management web application.
Use Fastify, TypeScript, Zod, Biome, SQLite initially,
and React + Vite + TanStack. I prefer a calm, highly usable
enterprise design. Ask me about roles, teacher workflows,
and report permissions. Reuse global WebTeam and its skills.
Use multi-model CHALLENGE mode only for permission design,
data migrations, or unresolved architectural tradeoffs,
within my approved model/provider policy.
```

## 8. Adopting an Existing Repository

Start OMP in the existing repository and request:

```text
Use WebTeam to adopt this existing repository safely.
Do not scaffold a new application or redesign it.
Inspect the implemented architecture and design conventions.
Run Project Design DNA and Engineering DNA discovery.
Create or reconcile the project documentation with the actual code.
Preserve current behavior, existing tokens and component APIs.
Present significant improvements and ask before migrations.
```

The expected output distinguishes **facts verified in code** from assumptions; captures evidence-backed standards, Design DNA, Engineering DNA, inconsistencies, and testable improvement plans. Existing projects must **not** be blindly rewritten to match a new template.

## 9. Learning from GitHub or Another Reference Repository

```text
Analyze this repository as an external reference:
https://github.com/OWNER/REPOSITORY
Mode: Learn Only.
Pin the revision, inspect architecture, UI/design system,
code quality, dependencies, license and security implications.
Compare it with my current project and suggest transferable ideas.
Do not execute downloaded scripts or copy code without approval.
```

After analysis you may approve **Selective Adoption** (adapt suitable patterns) or **Guided Migration** (planned transition). WebTeam records source/revision, permissions and license, compatibility analysis, test plan, and rollback approach. It must not copy protected branding or assets without authorization.

## 10. Requesting a Multi-Model Decision Review

```text
Use WebTeam's approved multi-model CHALLENGE/COUNCIL protocol
for the tenant authorization architecture in this repository.
Have at least two genuinely distinct approved model routes
produce independent proposals before revealing conclusions.
Ask a security specialist to produce counterexamples.
Evaluate with real contract and permission tests,
record dissent, and ask me to approve any consequential change.
Do not let competing models write to the same files.
```

If a second model is unavailable, the Orchestrator must disclose that limitation, propose authorized options, or run a truthfully labeled single-model review.

## 11. Model Roles, Reasoning Effort, and Context

Review **Section 5B** and select/verify the primary provider and fallback routes before editing model configuration. The following example concerns **deliberation roles**, which must be coordinated with the runtime's native fallback policy.

OMP may support role aliases and per-task overrides; confirm the exact syntax in the installed build. The example is **illustrative** and its placeholders must not be copied as working selectors:

```yaml
# Illustration only. Replace with verified selectors and OMP-supported settings.
modelRoles:
  webteam_primary: PROVIDER/PRIMARY_MODEL
  webteam_critic: PROVIDER/CRITIC_MODEL
  webteam_specialist: PROVIDER/OPTIONAL_THIRD_MODEL
# Do not turn on always-on Advisor unless requested.
advisor:
  enabled: false
```

An agent's `model: "@webteam_primary"` may resolve through an alias if the installed runtime supports it. WebTeam policy names `low`, `medium`, `high`, and `max` do **not** necessarily correspond one-to-one with provider API values. OMP may expose coarse per-task effort hints such as `lo|med|hi`; validate the effective behavior of each selected model rather than assuming a setting worked.

**Context policy:** Do not invent 128K/256K/1M capacities. Use verified provider/model limits, task-focused retrieval, concise handoffs, and progressive skill loading. Codebase Memory, if enabled, assists navigation; it does not replace checking source files or running tests.

## 12. Security, Privacy, and Approval Boundaries

Obtain the owner's approval before:

- Switching providers, using paid services, or exceeding approved inference limits.
- Sending proprietary code, restricted data, or internal materials to newly authorized external providers.
- Installing extensions, MCP servers, or installers with material system/network privileges.
- Changing major architecture or database decisions; executing destructive migrations.
- Deleting important files, deploying to production, or committing/pushing changes without authorization.
- Replacing an established application's visual identity or design system.

Never expose credentials in documentation, logs, graph indexes, model handoffs, or prompts. Distinguish **native tool permissions** from **policies written in prompts**. A prompt is neither a hard sandbox nor an enforceable spending cap.

## 13. Everyday Task Lifecycle

- **Small CSS defect:** Frontend handles it, runs proportionate checks, and does not invoke a model council.
- **New API:** Product/Backend develop contract and implementation; QA verifies Fastify/Zod behavior; Security participates when risk warrants.
- **Important UI:** Designer's eight stages → Frontend implementation → Accessibility/QA → browser and screenshot review.
- **Risky migration:** Database/Architect/Security/QA coordinate; use CHALLENGE/COUNCIL only when genuine uncertainty justifies it.
- **Cross-module bug:** Orchestrator may use healthy Codebase Memory to locate dependencies, verifies source, assigns one writer, and runs regression tests.

Each completed task should report actual changed files, executed commands/tests and their results, remaining unverified claims, approvals needed, and next actionable steps.

## 14. Updating, Managing, and Uninstalling WebTeam

### 14.1 Updating Global WebTeam

Run a newer master prompt with an **upgrade-in-place** instruction: detect the installed version, back up files, preview a diff, update only WebTeam-owned files, and preserve unrelated user settings. Recheck agent/skill discovery and model routes after upgrading.

### 14.2 Changing Models or Inference Limits

Ask the Orchestrator to show the model registry and a proposal before making edits. After approval, update routing, verify effective selectors/effort/retry chains/data permissions, and log the change. The entire team does not have to switch models together.

### 14.3 Disabling Deliberation or Advisor

Set WebTeam deliberation to `OFF` in the appropriate global/project policy. Disable any separately enabled native Advisor using the OMP mechanism actually supported by that version (for example, a verified `/advisor off` command or supported `advisor.enabled` setting). These are independent controls.

### 14.4 Uninstalling

Back up first. Build a manifest of files created by WebTeam; remove only WebTeam-owned agents, skills, metadata, and settings. Do not delete shared `.omp/` directories, MCP servers, provider settings, or project documentation without knowing whether other tooling relies on them. Caveman and Codebase Memory removal must be a separate, approved operation.

## 15. Troubleshooting

| Symptom | Likely issue to investigate | Safe resolution |
|---|---|---|
| `webteam-orchestrator` is missing | Wrong path/profile, undiscovered subdirectory, invalid agent frontmatter | Inspect effective OMP directory, discovery and spawn; fall back to flat `agents/webteam-*.md` |
| Fallback switches to an unauthorized provider | Inherited `default` chain, model-specific rule, `provider/*` wildcard, or task override | Suspend cross-provider fallback, audit effective routes, consider an isolated OMP profile, request approval before shared-config changes |
| Fallback cannot use Caveman/CBM | Model tool protocol, missing subagent permissions, unhealthy MCP/index | Inspect effective tool exposure and perform safe probes; do not treat tools as intrinsic model features |
| Model alias cannot resolve | Unregistered provider/model, missing auth, wrong role override or selector | Check `omp models`, effective config, and exact selector |
| “Two-model debate” produces one model's result | Ordered fallback `[A,B]` or runtime fallback mistaken for independent calls | Make separately routed task calls, log resolved model identities, check retry rules |
| Council is too costly | Always-on Advisor or an unbounded panel | Prefer OFF/ASK, limit participants/rounds, apply approval and cost gates |
| Advisor duplicates Caveman/Reviewer review | Multiple automatic review loops | Choose one review owner; enable continuous Advisor only when beneficial |
| Codebase Memory misses relationships | Stale index, wrong branch/scope, invisible tool | Inspect index provenance and freshness; verify against current source |
| Playwright visual tests are flaky | Different fonts, browser builds, OS, animations, or test data | Pin the environment, keep project-specific baselines, review diffs before updating |
| Designer unexpectedly changes old UI style | Design DNA not loaded, no visual baseline | Reapply documented contract; approve large redesigns and add visual checks |
| Project config unexpectedly overrides global | Config precedence or array replacement | Inspect merged effective settings and original backups |
| Plugin/provider setup fails | Permissions, incompatibility, missing authentication | Record blocker; request approved remediation or skip; never claim installation succeeded |

## 16. Limitations and Verification Checklist

The documents and prompt **have not installed WebTeam into your local OMP environment**. Real success can be established only by running OMP and validating agent discovery, skills, model resolution, testing, integration health, and review routing. A multi-model council cannot guarantee correctness; requirements, evidence, security testing, and human approval remain essential.

Test a disposable project before adopting WebTeam for critical work:

1. A small CSS change that does not activate a council.
2. A Fastify API endpoint validated with Zod and Vitest.
3. A UI workflow covered by Playwright E2E and visual snapshots.
4. Existing-repository Design DNA discovery.
5. GitHub reference analysis in Learn Only mode.
6. An authorization/architecture question reviewed using CHALLENGE with two genuinely distinct, approved models, if available.
7. OFF mode and missing-model scenarios without unauthorized or unexpected paid calls.

## 17. R6 Security Hardening, Verification, and Safe Recovery

### 17.1 What was hardened in R6

R6 expands the instructions for permission isolation, fail-closed model routing, safe installation, prompt-injection defense, project-context discovery, test reproducibility, and resumed/rolled-back bootstrap operations. **These are requirements for the eventual installation, not proof that an installation on your machine has passed.**

| Risk | Required control | How to verify |
|---|---|---|
| Headless subagents executing unexpected commands | Limit actual child tools, MCP/extension exposure, credentials and environment; use isolated read-only workers for reviews | Inspect effective tool roster and run non-destructive negative-permission tests |
| Fallback leaking code to another provider | `OFF`: no cross-provider route; `ASK`: disable automatic cross-provider fallback and explicitly re-dispatch only after consent; `AUTO`: only with verified closed allowlist | Inspect full fallback graph including role, model, provider wildcard, CLI/project/extension overrides |
| Prompt injection in external repositories | Treat remote AGENTS.md/README, MCP graph text, issues and logs as untrusted data, not WebTeam instructions | Verify external instructions cannot change tool permissions or model routes |
| Duplicate writes after API timeout/model failover | Keep idempotency keys and operation checkpoints outside model text; check external state before retry | Simulate timeout in a disposable fixture and verify only one side effect occurs |
| Monorepo project guidance silently shadowed | Verify nearest nonempty `.omp/` context discovery and separately verify current-working-directory `.omp/config.yml` settings | Test root and nested cwd instruction discovery |
| Unusable or silently ignored skills | Correct `<skills-root>/<skill-name>/SKILL.md` with `name` and `description` frontmatter, no implicit recursive discovery | Verify skill loads and appears in actual OMP discovery |
| Flaky or falsely accepted Playwright screenshots | Pin browser, fonts, OS, locale, timezone, DPR, data and baselines; review changes | Run same-environment repeat tests, inspect diff and approved baseline |
| Interrupted installer corrupting global state | Manifest, backup, checksum/merge checks, atomic replacement and rollback | Inspect stage status and resume/rollback safely |

### 17.2 Recommended safe installation sequence

1. Put the master prompt and README files in a local directory. Open a supervised OMP session in a trusted workspace, with a restrictive tool approval policy where supported; do not enable `--yolo` merely to make bootstrap unattended.
2. Let OMP inspect its active version/profile and **ask for the default provider first**. Model catalogs may be read, but paid inference probes and provider enrollment require authorization.
3. Choose cross-provider fallback separately. Start with `ASK` for private or cost-sensitive projects; this must **not** enable an uncontrolled native automatic switch. Choose multi-model council separately, usually `ASK`.
4. Review agent-directory placement, Caveman and Codebase Memory installation plans, user-level file changes and external code downloads. Approve only the specific operations you trust.
5. Verify each batch: definitions parse, all agents/skills are discoverable, effective tools satisfy restrictions, each chosen model resolves, and authorized smoke tests behave correctly.
6. Require an installation manifest, evidence table, real remaining blockers and rollback instructions. Do not consider `partial_verified` equivalent to fully installed.

### 17.3 If something fails

**Provider route unexpectedly changed:** stop task execution, disable automatic fallback for that task or use an isolated provider-limited profile, inspect `retry.fallbackChains`, agent model arrays, `task.agentModelOverrides`, active session/project overrides and extension hooks; require new consent before retrying.

**Reviewer has a write/exec/MCP mutation tool:** do not give it sensitive source or credentials; remove access by enforceable tool policy/isolation and repeat the probe. Simply saying “read-only” in its agent prompt is insufficient. OMP subagents may execute headlessly under permissive approval settings.

**Nested project ignores standards:** inspect its nearest nonempty `.omp` context directory; remember settings may load only from the process cwd `.omp/config.yml`. Supply a local context pointer, correct the launch directory or add a supported scoped override; then re-test both context and effective settings.

**Installation stops halfway:** use the manifest/checkpoint, inspect which files were actually written, reconcile any changed user config before resuming, and restore only WebTeam-owned changes if rolling back. Never delete unrelated agents or integrations.

**Playwright screenshots vary:** first inspect environment drift (fonts/browser/OS/timezone/data), not the baseline itself. Never mass-accept snapshot updates as a substitute for review.

### 17.4 What has and has not been verified

The R6 package can be checked statically for Markdown structure, paths and cross-file links. It **cannot** verify the user's actual OMP version, installed integrations, account model access, paid routing, sandbox strength or production behavior without execution on that machine. Consult `WEBTEAM_R10_REVISED_AUDIT_REPORT.md` for confirmed fixes and remaining environment-dependent gates.

## 18. References

- [OhMyPi repository](https://github.com/can1357/oh-my-pi)
- [OMP task-agent discovery](https://github.com/can1357/oh-my-pi/blob/main/docs/task-agent-discovery.md)
- [OMP task tool and per-item model selection](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md)
- [OMP model configuration](https://github.com/can1357/oh-my-pi/blob/main/docs/models.md)
- [OMP retry, fallback chains, and settings precedence](https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md)
- [OMP provider authentication and discovery](https://github.com/can1357/oh-my-pi/blob/main/docs/providers.md)
- [OMP Advisor / WATCHDOG](https://github.com/can1357/oh-my-pi/blob/main/docs/advisor-watchdog.md)
- [Caveman](https://github.com/JuliusBrussee/caveman)
- [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)
- [Vitest](https://vitest.dev/guide/)
- [Playwright](https://playwright.dev/docs/writing-tests)
- [Playwright visual testing](https://playwright.dev/docs/test-snapshots)

---

**Operational recommendation:** Choose the primary provider first. Keep `deepseek-flash` only if that provider and alias are verified. Start with cross-provider fallback set to **ASK** where desired, allow only verified models, use one model for ordinary tasks, set multi-model deliberation to **ASK**, and invoke independent models only when the stakes justify their cost. Resolve decisions with tests and evidence and retain user approval for consequential changes.


---

## Mnemopi Profile and R6 In-Place Upgrade

For a **fresh installation**, use `WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R10_REVISED.md`. If an **existing R6** team needs only memory governance, use `WEBTEAM_R6_MEMORY_ONLY_UPGRADE_PROMPT_REVISED.md`; if it needs both Memory and Loop, use `WEBTEAM_R6_TO_R10_UPGRADE_PROMPT_REVISED.md`; if Memory is already set up, use `WEBTEAM_EXISTING_INSTALL_LOOP_ONLY_UPGRADE_PROMPT.md`. Mnemopi is a native OhMyPi backend, not Codebase Memory MCP. Recommended initial policy: project-only memory, explicit sanitized retention (`autoRetain: false`), local embeddings with consent, memory LLM disabled (`llmMode: none`) and review-first Auto-Learn (`autoContinue: false`, `minToolCalls: 8`). The R6 upgrade must never recreate 16 agents, delete memories or reset provider/model routing.

For checks use `/memory view`, `/memory stats`, `/memory diagnose`; test recall after a new session and project isolation. `/memory clear` is destructive. See [official Mnemopi backend documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/mnemosyne-memory-backend.md).


---

## R9 — Hybrid Memory Governance: installation vs project onboarding

WebTeam uses a **two-level knowledge policy**: Global WebTeam defines how agents learn, while each project keeps its own private Mnemopi knowledge and approved project-local skills. **Hybrid does not mean Mnemopi automatically merges Global and Project banks.** The safe starting point is `memory.backend: mnemopi`, `mnemopi.scoping: per-project`, `autoRetain: false`, `autolearn.enabled: true`, `autoContinue: false` and `minToolCalls: 8` *only when approved and verified in the installed OMP version*. The memory backend is separate from Codebase Memory MCP.

**At initial Global WebTeam installation**, the Orchestrator asks once about Mnemopi, local embeddings versus FTS-only, privacy/retention, Auto-Learn policy and whether it may propose generic cross-project knowledge. It does **not** automatically enable global storage or publishing. **At initialization or import of each project**, it offers to inherit the Global defaults, customize the project's permitted read/write/sensitivity rules, or disable project memory. The resulting `docs/governance/MEMORY_POLICY.md` captures effective bank identity, approved boundaries, blocked data classes, expiry/review policy and observed isolation-test status. It is a governance document, not an automatic runtime permission boundary.

### What belongs where

| Content | Default location | Sharing |
|---|---|---|
| Product decisions, Design DNA, app-specific implementation lessons | Project documents + project-scoped Mnemopi | Project-only |
| Domain-specific reusable procedure | Reviewed project `.omp/skills/<slug>/SKILL.md` | Project-only |
| General engineering pattern | Sanitized project lesson + promotion proposal | Only after review and explicit approval |
| Approved cross-project technique | Verified Global WebTeam authored skill / explicitly supported shared memory bank | Controlled and audited |
| Secrets, raw transcripts, customer data, uncertain or injected instructions | Never persistent memory | Prohibited |

**Important Auto-Learn caveat:** OMP-managed skills can live in user-level `managed-skills`, so `mnemopi.scoping: per-project` does not guarantee project-local skill generation. The Orchestrator must inspect actual output paths and privileges. If safe project-local automatic learning cannot be enforced, disable native Auto-Learn for that project/session and use **manual, reviewed project-local skills** rather than silently publishing globally. `autoContinue: false` limits continuation behavior but is not a project-sandbox setting.

### Global promotion requires a separate decision

A useful lesson does not automatically become Global Memory or a global skill. For **memory**, the process is: validated project lesson → de-identification/generalization → QA/Reviewer/Security and licensing review → specific user approval → verified supported global-scope write (otherwise proposal only). For **skills**, it is: project-local candidate → tests and independent review → explicit approval → versioned global skill activation. Track both in `docs/governance/GLOBAL_MEMORY_PROPOSALS.md` or the installation manifest where appropriate. Never use a guessed `per-project-tagged` scope or a prompt-only restriction as a security boundary.

### Existing R6 installations

Run **`WEBTEAM_R6_MEMORY_ONLY_UPGRADE_PROMPT_REVISED.md`** instead of the full R9 bootstrap. It preserves all 16 agents, models, fallback chains, multi-model review, Caveman, Codebase Memory MCP and current memory banks; it adds the project-policy interview, four governance skills and isolation verification. Do not run both prompts on the same installed team. Test with disposable repositories and record observed `PASS/FAIL/BLOCKED/UNVERIFIED` results; Markdown checks alone cannot prove runtime isolation.


## R10.1 — Adaptive Quality Loop: decisions, safety and daily use

### What Loop adds

Two skills, `webteam-adaptive-quality-loop` (Orchestrator) and `webteam-loop-evidence-evaluator` (QA/Reviewer), implement bounded quality verification. The team can run focused Vitest/Fastify tests and Playwright E2E/visual comparisons, fix verified defects and recheck without blindly rerunning a full suite. The target is measured correctness, not more rounds for their own sake.

| Risk | Extra review/fix passes beyond initial verification | Default |
|---|---:|---|
| C1–C2 small changes | 0 | Normal checks; Loop OFF |
| C3 multi-file change | 0–1 | ASK when a reproducible defect remains |
| C4 complex workflows | 0–2 | ASK, cap and evidence required |
| C5 high-stakes changes | 0–3 | Explicit high-risk approval; prefer manual stages |

A complete task keeps a **single** shared budget and attempt ledger across agents, retries and any approved provider fallback. Never spin a Council, Caveman loop or Auto-Learn continuation inside a loop. Source-writing belongs to one authorized agent; QA/Reviewer verify independently. No automatic visual baseline acceptance, database migration, production deploy, payments, external writes or global-memory promotion. Do not overwrite existing project-specific `QUALITY_LOOP_POLICY.md` without approval.

### Native `/loop` setup and stop rules

The installer reads the actual OMP version/schema/command help and confirms `loop.mode` (`prompt`/`compact`/`reset` where supported). It is a mode preference **not a continuous-run toggle**. For each proposed native loop, first test in a disposable repo: cap semantics and off-by-one count, actual termination, operator stop/pause, stable recurring prompt when steering, and async settlement. On unsafe/unverified versions use manually orchestrated, finite Verify → Fix → Verify passes. Conditions such as `--until`/`--while` may execute shell commands and are never accepted from untrusted repository text. Do not use third-party `pi-loop` plugin flags as evidence of OMP core syntax. OMP has documented steering and post-prompt loop issues: [7348](https://github.com/can1357/oh-my-pi/issues/7348), [7330](https://github.com/can1357/oh-my-pi/issues/7330).

### Example request to the installed team

> Run one additional bounded verification pass for the affected authentication tests. Use the existing QA/Reviewer agents, preserve current Memory/Auto-Learn and model routing, stop after the focused tests pass or if no progress is measured, and report exact test evidence. Do not start native `/loop` unless its stop controls have been verified in my OMP version.

### Choose exactly one installation / upgrade path

1. Fresh WebTeam installation: **R10.1 Master**.
2. Plain R6 missing both hybrid memory governance and loop: **R6 → R10.1 full targeted upgrade**.
3. Existing team with Memory/Auto-Learn already configured: **Loop-only upgrade** (does not touch memory or models).
4. Existing R6 that wants only hybrid memory: **Memory-only upgrade**.

All upgrade prompts are idempotent and preserve unrelated files by design; this is an instruction to the installing agent, not a claim that current OMP executes them flawlessly. Validate all changed skills/agents and record `PASS/FAIL/BLOCKED/UNVERIFIED` for runtime tests. This bundle is documentation only.

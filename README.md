# WebTeam Enterprise for OhMyPi

A reusable, multi-agent software engineering organization for designing, building, testing, auditing, deploying (with approval), and maintaining modern web applications.

**This package is a complete installation specification plus 20 native OhMyPi slash-command templates.** It is not pre-installed software, an extension binary, a configured AI provider, or a guarantee of production security. A running OhMyPi session must create, enable, and verify the agent definitions, skills, policies, and command files described by the Master Prompt.

## Contents

```text
WebTeam/
├── README.md
├── WEBTEAM_MASTER_PROMPT.md
└── commands/
    ├── webteam_create_project.md
    ├── webteam_adopt_project.md
    ├── webteam_audit.md
    └── ... 17 additional commands (20 total)
```

There are **no migration prompts, legacy releases, or alternate-language documents** in this distribution. The standalone Markdown templates in `commands/` are authoritative for slash-command behavior; the Master Prompt defines how to install and coordinate them.

## 1. What WebTeam does

WebTeam is a role-based workflow for engineering a web application with high professional standards and measurable results. It covers product discovery, interface art direction, design systems, frontend/backend implementation, database architecture, security, quality assurance, accessibility, integrations, operations, performance, code review, documentation, and technical research.

Key characteristics:

- **16 specialist agents**, coordinated by `webteam-orchestrator` where OMP's effective runtime permits; the main session coordinates directly when nested delegation is unsupported.
- **Two-level architecture:** reusable Global WebTeam plus per-repository Project WebTeam specifications and configuration.
- **Native slash commands:** 20 reusable Markdown commands for project creation, adoption, inspection, audit, testing, and delivery.
- **Project-aware onboarding:** questions about the repository, product, requirements, frontend/backend/database, design, testing, deployment, and AI model routing.
- **Professional design:** the complete eight-stage design workflow, Design DNA, palettes, font pairing, accessibility, interaction specification, design tokens, and anti-generic-UI checks.
- **Engineering tests:** Vitest, component and Fastify API tests, integration and contract checks, Playwright E2E, visual regression, and CI quality gates.
- **Evidence-first project audit:** `/webteam_audit` writes a project Markdown report, prioritized repair plan, and optional future feature roadmap; it can implement tightly bounded safe fixes when explicitly requested.
- **Adaptive reasoning:** role-specific primary models, per-task effort, optional approved cross-provider fallback, and optional independent multi-model deliberation.
- **Mnemopi memory:** project-scoped knowledge, explicit promotion gates, and reviewed Auto-Learn/skill improvement where supported.
- **Caveman and Codebase Memory MCP:** optional integrations used only when installed, healthy, permitted, and suitable for the specialist/task.
- **Bounded quality cycles:** finite verify–fix–verify passes; continuous native Loop stays off unless version-specific safety controls are demonstrated.

### Preferred technology baseline

| Layer | Preferred technologies | Decision rule |
|---|---|---|
| Backend | Node.js, Fastify, TypeScript, Zod, Biome | Re-evaluate only for a specific requirement |
| Database | SQLite or MongoDB | Choose by data model, concurrency, deployment, transaction semantics, and operations |
| Frontend | Vite, TypeScript, **React or SolidJS**, Zod, TanStack, Biome | Select one framework after onboarding; add TanStack libraries when needed |
| Validation | Vitest, Playwright, browser/integration tools | Risk-driven, reproducible, environment-safe |
| UI | Project-specific CSS/design-token and component choices | Maintain a coherent and accessible design system |

The team does not install every suggested library or launch every specialist for each request.

## 2. Architecture and 16 agents

| Agent | Responsibility | Representative output |
|---|---|---|
| `webteam-orchestrator` | Requirements intake, planning, difficulty classification, task dispatch, cost and risk gates, delivery | Task charters, delegation evidence, roadmap |
| `webteam-product` | Product discovery, user journeys, permissions and measurable acceptance criteria | `docs/PRODUCT.md` |
| `webteam-designer` | UI/UX art direction, design-system engineering, existing Design DNA preservation | `docs/DESIGN.md`, tokens, visual rules |
| `webteam-architect` | Software architecture, technical boundaries, contracts and ADRs | `docs/ARCHITECTURE.md`, ADRs |
| `webteam-frontend` | React/SolidJS UI, TanStack, validated forms, responsive and accessible components | Browser-facing application code |
| `webteam-backend` | Fastify API/service implementation, typed schemas, server-side authorization | APIs, services and tests |
| `webteam-database` | SQLite/Mongo modeling, indexing, migrations, backup and restore | Schema/model/migration strategy |
| `webteam-security` | Threat modeling, authorization and tenancy, supply chain, privacy, secure defaults | Security evidence and findings |
| `webteam-qa` | Unit, component, API, integration, Playwright E2E, visual-regression and release tests | Reproducible tests and test reports |
| `webteam-devops` | Development environments, CI/CD, observability, releases and rollback | CI configuration and runbooks |
| `webteam-performance` | Core Web Vitals, p95/p99 latency, profiling and budgets | Measured performance reports |
| `webteam-accessibility` | WCAG 2.2 AA design target, keyboard, focus, screen-reader behavior | Accessibility findings and fixes |
| `webteam-reviewer` | Independent risk-ranked review of diffs and evidence | Actionable review findings |
| `webteam-researcher` | Verified technical documentation, framework models, source/license analysis | Evidence-backed technical options |
| `webteam-documentation` | Docs-as-code, project knowledge, API and operational documentation | Consistent durable docs |
| `webteam-integration` | Third-party APIs, OAuth, webhooks, retry/idempotency and realtime connectivity | Safe integration contracts/tests |

**Agent discovery does not prove orchestration.** After installation, WebTeam must observe a representative natural-language request being routed to the correct specialist via OMP's actual `task` interface. The main session is allowed to act as coordinator if nested agent dispatch is unavailable; it must not claim that a nested agent call occurred if it did not.

### Global and project files

A typical layout is:

```text
~/.omp/agent/                       # example only; verify current profile
  agents/webteam-*.md               # 16 globally reusable roles, flat files
  skills/<skill-name>/SKILL.md      # load relevant skills on demand
  commands/webteam_*.md             # 20 flat Markdown commands
  config.yml                        # only approved, verified settings

my-app/
  .omp/AGENTS.md                     # project entry point and instructions
  .omp/config.yml                    # only supported project overrides
  docs/PRODUCT.md
  docs/DESIGN.md
  docs/ARCHITECTURE.md
  docs/TECH_STACK.md
  docs/ROADMAP.md
  docs/DECISIONS.md
  docs/TESTING.md
  docs/design/                      # project-specific Design DNA
  docs/engineering/                 # Engineering DNA and conventions
  docs/governance/MEMORY_POLICY.md  # when project memory is configured
  docs/audits/                      # comprehensive audit reports
```

The real OMP discovery rules depend on version, active profile, current working directory, and nested `.omp` directories. Native commands and native agent files normally use flat `*.md` discovery; do not put them into attractive but unrecognized subfolders. When launching from monorepo subdirectories, inspect both effective context instructions and effective project settings, which need not follow identical lookup rules.

## 3. Prerequisites and safe installation

You need an installed OhMyPi with access to the intended local files, an approved model provider with credentials configured **outside tracked project files**, and permission to configure your agent profile. For specialist smoke tests, you may also need a disposable project and a working shell/test environment.

The native command behavior documented here was checked against OhMyPi **v18.12.2**. Other installations must inspect their actual schema and command precedence instead of assuming every setting or extension is available. Documentation: [OhMyPi repository](https://github.com/can1357/oh-my-pi), [slash command internals](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/slash-command-internals.md), [task-agent discovery](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/task-agent-discovery.md).

### First installation

1. Download/extract this package to a trusted directory. Review the command files and Master Prompt before using them with an AI coding agent.
2. Launch OMP in an authorized working directory; confirm its version (`omp --version`) and actual profile/config roots using installed documentation or supported commands.
3. Supply the complete `WEBTEAM_MASTER_PROMPT.md` to your OMP session **and make the companion `commands/` directory readable to that session**. Request: “Implement this WebTeam installation specification; first inspect the installed runtime and ask me for the required setup choices.”
4. Answer the compact installation interview: effective agent file placement, **primary model provider first**, usable models, optional additional provider(s) for fallback, optional council, Caveman/Codebase Memory, Mnemopi/Auto-Learn, quality-loop policy and global command scope.
5. Review the proposed settings, downloads, access permissions, approximate cost implications and file manifest before granting installation authorization. Credentials belong in a supported secure environment, not in Markdown or Git.
6. Allow OMP to create all 16 agent definitions, actual `SKILL.md` files, approved model mappings, supporting policies, and command files. A named skill without a discoverable `SKILL.md` is not installed.
7. Require runtime validation: effective discovery, model resolution, real `task` delegation, safe default routing, command expansion, and optional integration health. A static file check alone is **not** a successful install.
8. Restart/reload OMP when required by the installed runtime; run `/webteam_healthcheck` and `/webteam_help`. Review the results before using WebTeam for critical work.

**Existing working OMP settings must be preserved.** The installer should back up touched files, merge minimally, avoid duplicate extensions and report where effective restrictions are merely instructions rather than enforced tool permission boundaries.

### Are model fallback and councils mandatory?

No. You can use one approved model throughout. For a multi-provider setup, select the primary provider **before** discovering its model catalog; explicitly opt in to each fallback provider and the classifications of source code permitted to cross provider boundaries. Fallback handles operational availability failures; **multi-model deliberation** intentionally obtains independent advice on difficult decisions. They are separate features, not equivalent retry policies. Default recommendation: **ASK** for provider changes, cross-provider fallback, and expensive council invocations; never silently incur charges or transfer private repository contents.

### Optional Caveman and Codebase Memory MCP

If you opt in, the OMP installer should check compatibility, exact active profile, existing installation, command/tool availability, data handling, and smoke-test before enabling task-specific use. Do not install a duplicate extension/server, index private secrets, or assume all subagents have identical tools. Caveman is a workflow helper, not a replacement orchestrator; Codebase Memory MCP is an index to guide source navigation, not the authoritative source of correctness.

## 4. Project onboarding and everyday use

Once installation has been **verified**, you usually do **not** need to name a specialist. A normal request such as “Add teacher permissions and tests without changing our Design DNA” should be routed through the WebTeam policy; only necessary specialists are called. Slash commands are helpful explicit workflow triggers when more structure is useful.

### Create a new project

From the intended working directory in OMP:

```text
/webteam_create_project "School Management Platform"
```

The onboarding process should establish target users, workflows, MVP features, localization, repository root, frontend (React vs SolidJS), Fastify backend, SQLite vs MongoDB, design direction, authentication, deployment constraints, tests, approved provider/model routing, and any narrower memory/privacy policy. The Orchestrator coordinates generation of **project-specific** PRODUCT/DESIGN/ARCHITECTURE/TECH_STACK/ROADMAP/DECISIONS and relevant QA/security documents. Proposed consequential choices are reviewed with you before implementation.

Do not generate boilerplate `DESIGN.md` and label it “validated”. The designer performs the eight-stage workflow and documents approved palettes, font pairs, semantic tokens and component behaviors. Record incomplete choices explicitly as provisional.

### Adopt an existing codebase

```text
/webteam_adopt_project "/work/existing-school-app"
```

Adoption starts with read-only source and configuration inspection. It discovers how the application actually works, reconstructs **Design DNA** and **Engineering DNA**, identifies gaps between source and docs, and proposes improvements without overwriting current architecture, existing user changes, component contracts or branding. Reference repository URLs are analyzed for permitted transferable ideas, not blindly copied.

### Typical development session

```text
/webteam_status
/webteam_plan "Add role-based access for teachers"
/webteam_implement "Implement the approved teacher permission plan"
/webteam_test "Authentication and authorization"
/webteam_visual_test "Dashboard layouts"
/webteam_review "Changes since the last approved baseline"
```

Project artifacts are the durable authority; recalled memory is advisory and can be stale. Avoid requesting an entire-agent council for every isolated change. Run checks proportionate to risk, and require an independent review for sensitive work.

## 5. Complete list of 20 slash commands

All command names are slash commands **inside OMP chat**, not terminal shell commands. Their Markdown bodies are loaded as prompts. The main session interprets arguments and uses actual permitted OMP tools/agents; a command file cannot independently enforce access control.

| Command | Purpose |
|---|---|
| `/webteam_create_project` | New application onboarding and project documentation |
| `/webteam_adopt_project` | Safe takeover of an existing repository |
| `/webteam_status` | Project status, blockers and routing health |
| `/webteam_plan` | Scope and stage a feature without coding |
| `/webteam_implement` | Implement approved, bounded functionality |
| `/webteam_audit` | Full evidence-based audit, remediation plan and optional safe fixes |
| `/webteam_design_audit` | Design DNA, UI consistency and visual/design system review |
| `/webteam_architecture_audit` | System structure, contracts and architecture decisions |
| `/webteam_security_audit` | Targeted security, privacy, authorization and dependency review |
| `/webteam_test` | Unit/component/API/integration/E2E tests according to risk |
| `/webteam_visual_test` | Playwright visual regression, responsive UI validation |
| `/webteam_review` | Independent code and test-evidence review |
| `/webteam_reference_analyze` | Inspect external Git repositories for suitable reusable ideas |
| `/webteam_memory_review` | Mnemopi scope, recall, lesson retention and Auto-Learn review |
| `/webteam_models_audit` | Effective primary/fallback/council routing and permissions |
| `/webteam_quality_loop` | Supervised, bounded quality repair cycles |
| `/webteam_docs_sync` | Synchronize approved project documents with real implementation |
| `/webteam_healthcheck` | Verify discovery, routing, delegation and tool availability |
| `/webteam_release_check` | Release readiness assessment, no automatic deployment |
| `/webteam_help` | Command discovery and usage help |

Native discovery generally looks in the **flat** directory `~/.omp/agent/commands/*.md` (or the real active profile) and project `.omp/commands/*.md`. Exact precedence and collisions require verification. The source package's `commands/` directory is not automatically discoverable until its files are installed to the effective OMP location.

## 6. Comprehensive project audit: `/webteam_audit`

This workflow is meant for mature, evidence-based project review, not a superficial one-paragraph assessment. It reviews applicable dimensions: product completeness, architecture and contracts, frontend and design, accessibility, backend/API, database, security/privacy, automated tests, performance, operations, third-party integrations, and documentation.

Reference targets include the **OWASP Top 10:2025** awareness categories, relevant **OWASP ASVS 5.0.0** verification controls, **WCAG 2.2 AA** where applicable, and the technologies actually deployed. Using these references does not mean the project has passed a formal certification.

### Three operating modes

| Mode | What happens | Product source edits? |
|---|---|---|
| `report` (default) | Broad audit, one Markdown report, prioritized findings and optional feature roadmap | No |
| `plan` | Audit plus detailed dependency-aware fixes, owners, tests and rollback plan | No |
| `fix` | Audit, create plan, then fix a bounded number of confirmed, safe, reversible local issues | Yes, within approvals |

Examples:

```text
/webteam_audit
/webteam_audit --mode=report --scope=full --depth=standard --roadmap=on
/webteam_audit --mode=plan --scope=security,backend --depth=deep --roadmap=off
/webteam_audit --mode=fix --scope=full --max-fixes=3 --budget=normal
/webteam_audit --mode=report --scope=accessibility --output=docs/audits/accessibility-review.md
```

Supported argument contract (interpreted **by the agent**, not validated by a native CLI parser):

| Parameter | Allowed values | Default |
|---|---|---|
| `--mode` | `report`, `plan`, `fix` | `report` |
| `--scope` | `full` or supported domain(s) | `full` |
| `--depth` | `quick`, `standard`, `deep` | `standard` |
| `--roadmap` | `on`, `off` | `on` for report; `off` for plan/fix |
| `--output` | Safe new relative Markdown path inside `docs/audits/` | Unique dated report |
| `--max-fixes` | Integer `1..20`; only used for fix | `5` |
| `--budget` | `small`, `normal`, `extended` | `normal` |

**Report location:** `docs/audits/WEBTEAM_AUDIT_<date>_<unique>.md` by default. Every mode creates one authoritative Markdown report containing executive findings, scope/limitations, coverage matrix, exact checks/outcomes, stable issue IDs with evidence, risk prioritization, remediation plan, conditional feature roadmap, and (in fix mode) before/after validation of changed files.

The command never treats `--mode=fix` as permission to deploy, delete data, run destructive migrations, change primary providers, weaken tests, rebaseline screenshots without review, push Git commits, or write to production. High-risk findings become approval-gated proposals. The audit may report checks as **SKIPPED, BLOCKED or UNVERIFIED**; these are not passing scores. Observed outputs, revisions and source paths are more important than artificial numerical ratings.

**Roadmap vs defects:** Findings identify broken or risky existing behavior. The optional feature roadmap recommends future functionality based on actual product needs. New features are not implicitly authorized by the audit, including in `fix` mode.

### Distinguish related commands

- `/webteam_audit` reviews the whole project or selected domains and produces a consolidated report.
- `/webteam_security_audit` is a narrower security assessment.
- `/webteam_design_audit` inspects design consistency and Design DNA.
- `/webteam_healthcheck` assesses **WebTeam itself** (configuration, discovery, routing and delegation), not application security or business correctness.

## 7. Design quality and visual safety

WebTeam's designer must follow all eight steps:

1. Product context and requirements discovery.
2. Relevant visual/product research and reference analysis.
3. Art direction and visual identity design.
4. Semantic palette and intentional typography/font pairing.
5. UX information architecture and interactive states.
6. Versionable design tokens, components and `DESIGN.md` specifications.
7. Frontend integration and meaningful motion (including reduced motion).
8. Actual browser/screenshot visual QA, anti-generic-design review and refinement.

For existing projects, preserve established conventions unless an improvement has evidence, impact assessment and approval. Playwright visual baselines must be generated and compared in a controlled environment (font, OS/browser and viewport differences matter). Don't automatically approve snapshot updates just to pass tests.

## 8. Testing and quality gates

The QA agent owns test strategy and reliable test infrastructure, not all implementation work. Unit tests focus on critical logic and boundary conditions, component tests cover interactive states, Fastify `inject()` tests cover API behavior, integration tests cover data and contract boundaries, and Playwright covers critical browser flows. Visual regression protects meaningful UI surfaces. Use fixtures, deterministic data, isolated databases, controlled clocks and reliable cleanup.

Before describing a feature as complete, report which checks were actually executed, their exact results, remaining risks and the limitations of the environment. A missing test run is not a pass. For high-impact changes, obtain independent review and test authn/authz, tenant boundaries, migrations or recovery as applicable.

## 9. Models, fallback, councils and cost efficiency

WebTeam asks for your **primary provider first** and discovers its actual available models, context/output limits, tool support, reasoning capabilities and rate/budget characteristics. It then asks **separately** whether you want fallback to other providers and multi-model deliberation.

- **Primary routing:** assign models and thinking levels by actual agent workload and tested model capabilities. `deepseek-flash` can be an initial alias when it really exists; do not replace verified user aliases with guessed IDs.
- **Fallback:** handles eligible model availability failures; can cross providers **only with advance approval and an enforceable route/data allowlist**. It must not be used as a backdoor to send private code elsewhere.
- **Deliberation:** optional OFF / CHALLENGE / COUNCIL workflows for difficult, consequential choices, with independent evaluations, evidence arbitration, cost cap and a single implementation writer.
- **Context:** use focused retrieval and handoff packets; task working-context budgets are not arbitrary increases to model capacity. Verify actual provider/OMP context limits.
- **Effort:** Low/Medium for routine work, High for architecture/security complexity, Max only when supported and justified. OMP task effort hints may use different syntax than agent thinking levels.

A useful starting policy is `ASK` for costly fallback/council decisions. Do not create nested deliberation inside automatic loops. Report cost only if it is genuinely measured or based on a documented estimator with assumptions.

## 10. Mnemopi memory and Auto-Learn

The preferred governance model is **Global procedures + project-scoped knowledge**. Ask global technical preferences once during team setup; for each newly initialized or adopted project, ask whether to inherit that approved policy or narrow it. Record the answer in `docs/governance/MEMORY_POLICY.md`.

If the installed OMP schema supports these settings, an initial example is:

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

Do not assume this example applies unchanged to every OMP version. Confirm the actual config and available local embedding requirements. `per-project` memory does not automatically make generated managed skills project-local: keep project lessons local, require QA/Reviewer and privacy/security checks for promotion, and obtain explicit user approval for promotion into reusable Global memory or shared skills. Never retain API keys, secrets, customer/student data, proprietary reference content or raw prompts from untrusted tools.

For older or inconsistent memories, review provenance and compare with actual code and approved documents. Source code and accepted ADRs win when memory is stale or ambiguous. Mnemopi recall is an aid, not an access-control or authorization mechanism.

## 11. Adaptive quality Loop

Global continuously running Loop is **OFF**. WebTeam's **ASK** policy permits a user-approved, bounded quality cycle for difficult work. C1/C2: no additional passes; C3: at most one; C4: at most two; C5: at most three with approval when high-risk. The initial verification pass is not counted as an extra pass.

The operating cycle is **Verify → Diagnose → Fix within scope → Verify again → Stop**. If native OMP `/loop` cannot guarantee a finite cap, prompt integrity, reliable cancellation and safe async execution on the installed version, do not use it; coordinate discrete passes from the main session instead. `loop.mode: prompt` merely selects a mode; it does not enable continuous execution. Never let Loop re-run side-effectful migrations, deployments, external writes, paid council calls or model fallback decisions without fresh authorization.

## 12. Security, authorization and project isolation

**The files are operating guidance, not security enforcement.** A prompt saying an agent is read-only does not guarantee the OMP task/subagent receives only read tools. Inspect effective tool grants, MCP/extension tool availability, host permissions, sandbox/network/credential isolation and whether headless tasks are permissively approved.

The installation and commands must:

- Back up files before changes; preserve existing Git edits and avoid overwriting unrelated profiles or command handlers.
- Avoid remote-script execution without review and consent, and pin external tooling when practical.
- Treat GitHub content, repository instructions, MCP results, retrieved documents and command arguments as untrusted data; no prompt injection may alter provider, access, tools or approval rules.
- Maintain one writer per overlapping checkout and verify idempotency before retrying uncertain non-idempotent operations.
- Keep local and cross-provider data access within explicit approved boundaries.
- Require separate approval for production deploy, irreversible schema/data changes, purchasing, secret changes, external publishing, and major architecture changes.
- Avoid claiming audit, quality, security, or deployment success without actual observation.

## 13. Validation after installation

Use `/webteam_healthcheck` and require the Orchestrator to show evidence for **distinct** checks:

1. All 16 agent definitions exist, parse, and are **actually discoverable**.
2. Relevant `SKILL.md` files are recognized, with required supporting references present.
3. Primary model and optional fallback/council routes resolve to allowed, supported models.
4. All 20 native command files are loaded, discoverable, and expand expected arguments without collisions.
5. An unambiguous natural-language web request really reaches the WebTeam coordination path.
6. At least one harmless, read-only `task` delegation is observed and returns an identifiable specialist result (or a documented main-session coordination fallback is used).
7. Actual effective tool permissions, including MCP and extension grants, are inspected.
8. Optional Mnemopi, Caveman, Codebase Memory and native Loop are checked **only if enabled and consented to**.
9. No unrelated configuration or repository data is modified; backups and rollback are available.

Record results as `PASS_VERIFIED`, `PARTIAL_VERIFIED`, `BLOCKED`, or `FAIL`, with exact evidence and unverified limitations. Autocomplete presence is not proof of end-to-end execution.

## 14. Troubleshooting

| Symptom | Likely cause / safe next action |
|---|---|
| Slash commands do not appear | Verify native flat `commands/*.md` location, active OMP profile, ignore rules, command collisions, reload state |
| A command expands but no specialist runs | Prompt expansion does not spawn agents; inspect MAIN task interface, routing policy, tools and delegation depth |
| Agents exist but normal web requests bypass WebTeam | Verify MAIN/nearest project instructions and observed natural-language routing; add a supported dispatcher without hijacking unrelated tasks |
| Skills are mentioned but not available | Check actual `SKILL.md` metadata, location and skill discovery; don't create placeholder names only |
| Agent uses incorrect model | Compare effective role alias/provider mapping, actual available catalog and fallback inheritance; stop unapproved cross-provider routes |
| Mnemopi recalls wrong project | Check effective project root, scoping, nested cwd, autoRecall and memory bank; halt sharing until isolation is tested |
| Auto-Learn creates global skill unexpectedly | Do not assume `per-project` scopes managed skills; disable unsafe automatic publication and use reviewed project-local output |
| Playwright visual diffs vary between machines | Fix browser/OS/font/viewport/test fixtures and rebaseline only after visual review |
| Loop does not stop safely | Disable native automation; use supervised finite verify–fix–verify with bounded budget |
| `/webteam_audit` returns only chat text | Check verified repository path and safe report permissions; do not claim saved report, resolve safe-write blocker |
| Audit says no vulnerabilities but few tests ran | Treat uncovered areas as UNVERIFIED, rerun applicable checks with consent and revise findings |
| Caveman or CBM tools cannot be called | Verify actual native OMP plugin/MCP connection and capabilities; use focused source inspection if authorized |

## 15. Limitations, cost and responsibility

- Model outputs can be wrong, and a 16-agent team cannot replace real testing, human product decisions, infrastructure security, or professional audits when required.
- Every subagent, fallback, council and verification loop can add tokens, runtime and cost. There is no reliable universal “token savings” claim. Use task complexity, bounded tools and actual measurements.
- Some setup steps, credentials, network installers, production tests, visual screenshots, live model calls, and OS permission changes require access that a standalone prompt cannot grant.
- A static Markdown lint pass proves only document consistency, **not** OMP runtime security, privacy isolation, or production readiness.
- Audit reports are bounded, point-in-time assessments, not security or accessibility certifications. Known unknowns must be explicit.

## 16. External references

- [OhMyPi source and user documentation](https://github.com/can1357/oh-my-pi)
- [OMP native command discovery](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/slash-command-internals.md)
- [OMP task agents](https://github.com/can1357/oh-my-pi/blob/v18.12.2/docs/task-agent-discovery.md)
- [Playwright visual comparison guidance](https://playwright.dev/docs/test-snapshots)
- [OWASP Top 10:2025](https://top10.owasp.org/2025/)
- [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Caveman](https://github.com/JuliusBrussee/caveman)
- [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)

---

**Start with the Master Prompt for a fresh WebTeam installation. After it is genuinely installed and validated, use natural-language requests or the native commands. Use `/webteam_audit` when you need a consolidated evidence-backed audit and a repair/feature roadmap, and use `/webteam_healthcheck` when you need to validate WebTeam itself.**

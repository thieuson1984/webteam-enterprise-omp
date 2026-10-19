# Product Capability Blueprints — 12 professional scenarios

Each entry is a **reviewable workflow contract**, not a recipe to execute automatically. Read selectively by case.

Status classification: `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED`, `NOT_APPLICABLE`.

## PRD01 — Outcome-driven discovery and problem framing
- **When applicable:** A proposed feature is not linked to a specific user problem or measurable business outcome.
- **Analysis and design sequence:** Define target user, job-to-be-done, critical journey, constraints, baseline and outcome metric. Build a concise opportunity tree: outcome → observed problems → solution hypotheses → smallest experiments. Separate needs observed in interviews/analytics from assumptions; explain opportunity cost of not solving each problem.
- **Deliverable:** A one-page opportunity brief, numbered hypotheses HYP-*, research gaps, falsifiable success/kill criteria, opportunity→requirements trace.
- **Professional anti-pattern:** Reject fake user interviews, invented market statistics and output-only success such as number of screens shipped.
- **Acceptance evidence:** Product and QA agree success measurements and leading/lagging guardrails; Designer validates journeys.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD02 — User research, triangulation and evidence calibration
- **When applicable:** Persona, problem priority or usability assumption depends on unclear or biased evidence.
- **Analysis and design sequence:** Select ethical methods: contextual inquiry, task interview, prototype usability, support-ticket analysis, moderated/unmoderated tests, and quantitative funnels. Document sample and recruitment bias; get consent; protect transcripts. Triangulate observations with product logs and domain experts. Use evidence tags VERIFIED/INFERRED/PROPOSED/UNKNOWN with dates and confidence.
- **Deliverable:** Research plan, scripts, provenance ledger, insight→decision table, bias/risk notes and follow-up questions.
- **Professional anti-pattern:** Never impersonate a user study, synthesize fake quotes or treat a few anecdotes as population-level proof.
- **Acceptance evidence:** Evidence sources retraceable; confidence appropriate; accessibility and underserved user segments considered.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD03 — Market, alternatives and differentiated positioning
- **When applicable:** Strategic direction depends on competing alternatives, pricing or product positioning.
- **Analysis and design sequence:** Frame competitors and non-product alternatives against buyer/user jobs. Collect authorized, dated public evidence for capabilities/prices; build comparison against outcome, workflow friction and total adoption cost. Identify credible differentiators that implementation can sustain; distinguish parity, advantage and non-goals.
- **Deliverable:** Alternatives matrix, positioning hypothesis, differentiation evidence, strategic assumptions and validation plan.
- **Professional anti-pattern:** Never claim current vendor price from memory; never use copied competitor brand assets or confidential source.
- **Acceptance evidence:** Each proposed differentiator has a user reason, cost implication and testable claim.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD04 — Functional requirements, quality attributes and acceptance engineering
- **When applicable:** Vague user request, cross-functional dependency or contract change needs unambiguous requirements.
- **Analysis and design sequence:** Map actors, permissions, inputs, output, invariants, exceptions, lifecycle, locale, data sensitivity and nonfunctional constraints. Assign REQ/AC identifiers, Given–When–Then examples including forbidden flows; express latency/reliability/accessibility thresholds only with rationale and baseline. Trace outcome→opportunity→REQ→design/API/data→test.
- **Deliverable:** Prioritized REQ/AC specification, assumptions, exclusions, role matrix and QA-ready traceability table.
- **Professional anti-pattern:** Reject acceptance phrases like modern, intuitive or enterprise grade without observable criteria.
- **Acceptance evidence:** QA can write tests; Architect and Database can identify exact affected contracts.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD05 — Business process modeling and policy state machines
- **When applicable:** An approval, booking, enrollment, inventory, payment or multi-actor workflow has nontrivial states.
- **Analysis and design sequence:** Model actors, command/query permissions, state graph, legal transitions, ownership, concurrent actions, escalation, audit events and expiry. Identify invariants, boundary cases, cancel/reverse behavior and compensations. Keep business rules separate from UI display state.
- **Deliverable:** Workflow sequence, state transition table, policy decisions, business glossary, sample scenarios and failure cases.
- **Professional anti-pattern:** Do not equate UI disabled controls with server authorization; avoid implicit state transitions and hidden magic statuses.
- **Acceptance evidence:** Security verifies denial scenarios, Backend validates state transitions, Database enforces persistence constraints.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD06 — Outcome roadmapping, RICE/WSJF alternatives and capacity tradeoffs
- **When applicable:** Backlog growth or competing features need an explicit sequencing decision.
- **Analysis and design sequence:** Classify mandatory controls, customer pain, enablers and experiments; score relative reach/impact/confidence/effort only when estimates exist, otherwise use qualitative impact×risk with uncertainty. Sequence dependency-aware now/next/later hypotheses and decision checkpoints. Separate feature opportunity roadmap from mandatory defect/incident remediation.
- **Deliverable:** Prioritized backlog, decision log, milestone assumptions, dependency map and outcome-linked roadmap.
- **Professional anti-pattern:** Never launder made-up RICE numbers into facts or let stakeholder title override explicit risk.
- **Acceptance evidence:** Roadmap has measurable decision gates and clear uncertainty, not unconditional date promises.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD07 — Product analytics, experimentation and instrumentation contracts
- **When applicable:** Feature value, funnel, retention or release impact must be measured.
- **Analysis and design sequence:** Define north-star support metrics only where meaningful; specify event naming/properties, privacy categories, identity stitching, deduplication, retention and instrumentation owner. For experiments define unit of randomization, exposure, guardrails, sample assumptions, stopping rule and bias. Provide observational fallback when A/B is unsuitable.
- **Deliverable:** Metric dictionary, event specification, dashboard questions, experiment preregistration and data-quality checks.
- **Professional anti-pattern:** Do not claim statistical significance without analysis; prohibit unapproved tracking, PII-rich event payloads and dark patterns.
- **Acceptance evidence:** Database and Backend verify data contracts; QA tests event correctness and consent; data availability confirmed.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD08 — Information architecture, content strategy and localization
- **When applicable:** Complex navigation, terminology, Vietnamese/localized workflows or error messages are present.
- **Analysis and design sequence:** Use domain vocabulary, clear information scent, task-based nav, content hierarchy and progressive disclosure. Define terminology glossary; include long labels, localized dates/numbers, pluralization, RTL if applicable, accessible microcopy and recovery-oriented error messages.
- **Deliverable:** Information map, glossary, content matrix, microcopy examples, locale test cases and content ownership.
- **Professional anti-pattern:** Avoid decorative filler, translation-only internationalization and inconsistent words for the same entity.
- **Acceptance evidence:** Designer and Accessibility review comprehension, localization and responsive truncation.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD09 — Trust, privacy, responsible AI and consent by design
- **When applicable:** Sensitive personal data, child/student information, AI outputs or high-consequence recommendations are implicated.
- **Analysis and design sequence:** Map sensitive categories, purposes, legal constraints to verify, consent/notice, retention/deletion/access requests, auditability and human review. For AI features distinguish generated/inferred facts, failure modes, explainability, automation bias and user override.
- **Deliverable:** Data-use map, trust requirements, consent flows, failure/human-escalation criteria and acceptance tests.
- **Professional anti-pattern:** Do not infer legal compliance or deploy AI decisions impacting users without authorized review.
- **Acceptance evidence:** Security/Database check retention and access controls, QA verifies refusal/recovery and user notice.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD10 — Stakeholder alignment, decisions and change control
- **When applicable:** Conflicting requests, strategic assumptions or approval ownership are ambiguous.
- **Analysis and design sequence:** Identify decision-maker, consulted roles, impacted users, alternatives, decision deadline and reversibility. Maintain assumption/decision/risk logs with source and date. Define change impact on scope, test, privacy, migrations and release. Raise high-stakes gaps instead of silently selecting a path.
- **Deliverable:** Decision register, stakeholder map, RACI-like ownership, open questions and change-impact summary.
- **Professional anti-pattern:** No silent scope creep or unauthorized commitment of people, cost or delivery dates.
- **Acceptance evidence:** All approvals are attributable and related implementation artifacts reference decisions.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD11 — Commercial policies, entitlement and lifecycle UX contracts
- **When applicable:** Subscriptions, billing, licensing, quotas, trials, refunds or usage metering are in scope.
- **Analysis and design sequence:** Separate product policy from provider mechanics. Specify pricing/plan entitlements, grace periods, renewals, failed payment transitions, proration assumptions, invoices, regional tax questions and reconciliation requirements. Validate jurisdiction/provider specifics before coding.
- **Deliverable:** Entitlement state machine, policy table, audit events, exception scenarios and acceptance suite.
- **Professional anti-pattern:** Never invent tax rules, store sensitive payment credentials or let frontend grant entitlements.
- **Acceptance evidence:** Backend and Database test idempotent billing events, reconciliation and authorization.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## PRD12 — Product release criteria, adoption and feedback loops
- **When applicable:** A release requires user acceptance, rollout or learning after shipping.
- **Analysis and design sequence:** Review acceptance tests, operational readiness, legal/trust issues, documentation, support capacity, enablement, measurement and rollback/feature flags. Define launch cohorts, qualitative feedback and rollback triggers. Evaluate observed outcomes post-release and update roadmap.
- **Deliverable:** Go/no-go packet, release communication, training and support plan, post-release learning review.
- **Professional anti-pattern:** Do not declare shipped=successful; no automatic production rollout or baseline shifts.
- **Acceptance evidence:** QA/DevOps/Security attest relevant gates, Product owns outcome follow-up.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

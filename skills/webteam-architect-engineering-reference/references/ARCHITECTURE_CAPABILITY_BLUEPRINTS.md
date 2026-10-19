# Architect Capability Blueprints — 12 professional scenarios

Each entry is a **reviewable workflow contract**, not a recipe to execute automatically. Read selectively by case.

Status classification: `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED`, `NOT_APPLICABLE`.

## ARC01 — Architecture drivers, quality-attribute scenarios and fitness
- **When applicable:** An architectural decision lacks explicit load, latency, availability, security or evolution constraints.
- **Analysis and design sequence:** Elicit measurable quality-attribute scenarios: stimulus, environment, response and measure. Rank by business criticality and change likelihood. Compare simplest viable options with tradeoffs across reliability, security, cost, team topology and complexity. Convert high-risk assumptions to spikes and tests.
- **Deliverable:** Architectural drivers matrix, option tradeoff, rejected alternatives, decision criteria and validation tasks.
- **Professional anti-pattern:** Do not substitute microservices/Kubernetes diagrams for measured requirements or prescribe an unverified SLO.
- **Acceptance evidence:** Product verifies scenarios; QA turns key quality requirements into executable or observable checks.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC02 — Bounded contexts and evolutionary modular monolith
- **When applicable:** Domain logic bleeds across modules or a system is splitting/merging services.
- **Analysis and design sequence:** Find cohesive business capabilities, ownership and transaction boundaries. Define allowed dependency directions, public module interfaces, anti-corruption layers, cycles policy and extraction criteria. Default to modular monolith unless independent scaling/deployment/data ownership justify distribution.
- **Deliverable:** Context map, component responsibility table, interface contract, architecture tests and extraction trigger.
- **Professional anti-pattern:** Avoid shared-everything libraries, distributed transactions by default and architecture astronautics.
- **Acceptance evidence:** Reviewer checks import boundaries; Database verifies ownership of writes, Backend API contracts.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC03 — C4 views, ADRs and decision provenance
- **When applicable:** Stakeholders need to understand current versus proposed system.
- **Analysis and design sequence:** Produce context/container/component views only at useful fidelity; label trust boundaries, data stores, owners, protocols, deployment environments and revision. Add sequence diagrams for complex failure paths. Write ADR as status, context, decision, alternatives, consequences, evidence and re-evaluation trigger.
- **Deliverable:** AS-IS/TO-BE diagrams, ADR and drift register tied to real source paths.
- **Professional anti-pattern:** Do not invent components or turn C4 into mandatory code-level UML detail; diagrams are snapshots not proof.
- **Acceptance evidence:** Cross-check diagrams against repo manifests/routes and representative runtime topology.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC04 — Architecture fitness functions and governance-as-code
- **When applicable:** Architecture is documented but not enforced or drifts over releases.
- **Analysis and design sequence:** Translate key invariants into buildable static/dynamic checks: import boundaries, forbidden dependencies, API compatibility, module ownership, secret-free config, database contract smoke tests, release budgets and dependency update gates. Assign threshold, owner, CI mode and exception process.
- **Deliverable:** Fitness function matrix, executable-test candidates, CI evidence map, waiver log.
- **Professional anti-pattern:** Avoid brittle golden metrics with no baselines or CI jobs that require production credentials.
- **Acceptance evidence:** QA runs representative tests; false positives and migration exceptions are documented.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC05 — API/event integration architecture and compatibility
- **When applicable:** Contracts evolve across frontend/backend, partners or asynchronous consumers.
- **Analysis and design sequence:** Map producers/consumers, data classification and versioning. Define compatibility windows, schema evolution, deprecation policy, idempotency, retry/ordering guarantees, reconciliation and contract-test ownership. Isolate third-party protocols behind adapters.
- **Deliverable:** Context contract map, versioning/deprecation ADR, consumer matrix, negative-path tests.
- **Professional anti-pattern:** Avoid breaking contract changes without migration or believing queues guarantee exactly-once side effects.
- **Acceptance evidence:** Backend, Integration, Database and QA verify contracts and schema compatibility.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC06 — Distributed systems, consistency and failure models
- **When applicable:** Multiple services or data stores require cross-boundary coordination.
- **Analysis and design sequence:** State consistency requirements, failure model, duplicate delivery, clock assumptions, retry safety, transaction/outbox or saga boundaries and compensation semantics. Compare transactional single-store implementation first; justify distributed design only when necessary.
- **Deliverable:** Consistency matrix, failure sequence diagrams, recovery/idempotency contracts, cost and operational risk.
- **Professional anti-pattern:** No fictitious exactly-once behavior, unbounded retries or implicit cross-service atomicity.
- **Acceptance evidence:** Backend/Database/QA test duplicate, reorder, crash-after-commit and partial failure.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC07 — Reliability, SLOs, capacity and graceful degradation
- **When applicable:** Service availability, resilience or timeouts are critical.
- **Analysis and design sequence:** Establish service-level indicators from actual user journeys. Design bounded timeouts, retry budgets, backpressure, bulkheads only when warranted, graceful shutdown and graceful degradation. Define RTO/RPO with business approval and recovery rehearsals.
- **Deliverable:** SLI/SLO proposal, dependency failure matrix, runbook outlines, recovery validation and cost implication.
- **Professional anti-pattern:** No arbitrary 99.99% target or retry storm; do not declare backups good without restore test.
- **Acceptance evidence:** DevOps/QA validate outage simulations and alert signals, Product accepts user impact.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC08 — Trust boundaries, threat modeling and privacy architecture
- **When applicable:** Data crosses tenants, service boundaries or external providers.
- **Analysis and design sequence:** Inventory assets, actors, entry/egress points, trust zones and data classes. Use STRIDE-like prompts where useful. Evaluate authz ownership, identity propagation, SSRF/injection risks, key/secrets management, data minimization and auditability.
- **Deliverable:** Threat/data-flow diagrams, prioritized mitigations, abuse-case tests and unresolved policy approvals.
- **Professional anti-pattern:** Never treat CDN/VPC/HTTPS as a substitute for object-level authorization.
- **Acceptance evidence:** Security approves threat plan; Backend and Database enforce controls independently.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC09 — Storage selection, data ownership and reporting topology
- **When applicable:** SQL, document store, eventing, search or analytics choices are under consideration.
- **Analysis and design sequence:** Compare access patterns, constraints, consistency, scale, ops cost, backup/recovery, migration and team knowledge. Prefer one operational source of truth; define derived views, reporting freshness and reconciliation separately. Use SQLite/MongoDB/PostgreSQL where justified, not brand preference.
- **Deliverable:** Data topology ADR, ownership and change-data flows, synchronization checks, extraction criteria.
- **Professional anti-pattern:** Reject premature polyglot persistence and undocumented dual-write pipelines.
- **Acceptance evidence:** Database signs off transaction and migration design; Backend/QA check application contracts.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC10 — Performance architecture, workload modeling and cost
- **When applicable:** High latency, cloud cost or scaling limits influence architecture.
- **Analysis and design sequence:** Define realistic workload mix, burst and growth assumptions. Model bottlenecks across network, DB, CPU, caching and external APIs. Measure current p95/p99/throughput before caching/sharding; include operator cost and complexity in options.
- **Deliverable:** Capacity model, performance-budget hypotheses, benchmark plan and cost risk table.
- **Professional anti-pattern:** No vendor cost estimate without a dated quote or measurement; no caching sensitive responses without scope control.
- **Acceptance evidence:** Performance/Database/DevOps jointly validate representative workloads.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC11 — Strangler modernization, migrations and legacy preservation
- **When applicable:** Existing project must migrate frameworks, schemas or deployment architecture without downtime.
- **Analysis and design sequence:** Inspect actual system, freeze invariants, inventory dependencies, plan incremental seams, dual compatibility windows, expand/contract DB changes, rehearsal, feature flags and rollback/roll-forward. Define irreversible boundaries and approvals.
- **Deliverable:** Phased migration ADR, dependency graph, test coverage holes, go/no-go and backout steps.
- **Professional anti-pattern:** No big-bang rewrite by default, destructive migration or autonomous production cutover.
- **Acceptance evidence:** Database/Backend/QA/DevOps check mixed-version traffic and recovery paths.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## ARC12 — Deployment, runtime boundaries and supply-chain architecture
- **When applicable:** Build/release environments or deployment topology are architecturally significant.
- **Analysis and design sequence:** Plan environment separation, config/secret contracts, immutable artifacts, provenance/lockfile, health/readiness, IaC ownership, least-privileged identities and observability. Keep local/CI parity proportionate. Define failures at deploy and rollback boundaries.
- **Deliverable:** Deployment view, release contract, health and secret policy, runbook/test expectations.
- **Professional anti-pattern:** Never assume an OMP prompt can grant deployment rights; no speculative service mesh.
- **Acceptance evidence:** DevOps/security review, QA exercises deployment-like failure in safe fixture.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

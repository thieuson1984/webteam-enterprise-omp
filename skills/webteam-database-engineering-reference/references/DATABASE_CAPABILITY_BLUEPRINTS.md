# Database Capability Blueprints — 14 professional scenarios

Each entry is a **reviewable workflow contract**, not a recipe to execute automatically. Read selectively by case.

Status classification: `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED`, `NOT_APPLICABLE`.

## DBD01 — Access-pattern-first relational/document modeling
- **When applicable:** New data model, schema refactor or unexpected query complexity.
- **Analysis and design sequence:** Start from entities, lifecycle and actual reads/writes, cardinality, growth, consistency and access control. Pick normalization/denormalization based on invariants; specify keys, optionality, uniqueness, domain types, referential actions, document embedding/reference limits and archival.
- **Deliverable:** Schema/collection design, entity cardinality table, query-to-index map, invariants and data dictionary.
- **Professional anti-pattern:** Avoid arbitrary ORM-first models, redundant columns without reconciliation or premature document embedding.
- **Acceptance evidence:** Backend validates domain semantics; Product confirms lifecycle; QA checks invalid writes.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD02 — SQLite durability, integrity and concurrency practice
- **When applicable:** The deployed datastore is SQLite or migration to SQLite is proposed.
- **Analysis and design sequence:** Verify SQLite build, connection lifecycle, foreign_keys enforcement, WAL suitability, busy_timeout and writer contention. Evaluate checkpointing and hosting constraints; avoid WAL on unsupported network filesystem. Use transaction mode deliberately; test concurrent writes. Confirm backup via online Backup API/VACUUM INTO as appropriate and restoration to isolated file.
- **Deliverable:** SQLite operational profile, pragma verification plan, migration guard, contention tests and restore runbook.
- **Professional anti-pattern:** Do not claim WAL makes writes fully parallel; do not copy only the main db file during active WAL operation.
- **Acceptance evidence:** QA reproduces contention/restore; DevOps owns storage and backup scheduling.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD03 — MongoDB documents, validation, atomicity and indexes
- **When applicable:** Document data access, embedding, schema changes or query perf in MongoDB.
- **Analysis and design sequence:** Select embedding/reference by bounded aggregates, write contention, document size and query shapes. Use validator/schema versioning with staged rollout; unique/compound indexes backed by workload. Distinguish single-document atomicity from multi-document transactions and verify deployment capabilities.
- **Deliverable:** Collection schemas and examples, relationship decision table, index workload map, transaction applicability and migration plan.
- **Professional anti-pattern:** No assumption that denormalization is universally better or that multi-document transactions are free.
- **Acceptance evidence:** QA validates validator failures, duplicates, retry behavior and index regressions.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD04 — PostgreSQL constraints, MVCC, RLS and indexing
- **When applicable:** PostgreSQL is selected or existing SQL reliability issues appear.
- **Analysis and design sequence:** Choose proper column types and constraints; understand MVCC/isolation and lock contention. Use RLS only after validating session/role setup, ownership bypass, FORCE policy needs and tenant test matrix. Profile real SQL with EXPLAIN (ANALYZE) only in safe environment; assess index build/migration locking.
- **Deliverable:** Schema/role design, isolation decision, RLS policies and negative tests, measured plan and migration safety notes.
- **Professional anti-pattern:** Never assume RLS replaces service authz or test dangerous queries against production by default.
- **Acceptance evidence:** Security crosschecks tenant policy; Backend preserves session-scoped tenant context.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD05 — Expand/contract migrations, data backfills and compatibility
- **When applicable:** Schema changes affect deployed users, old app versions or large datasets.
- **Analysis and design sequence:** Write additive change first, dual-compatible reads/writes if needed, staged backfill with checkpoint/verification, contract/cleanup only after consumers migrated. Check locks, size, downtime and rollback/roll-forward. Test against a representative disposable copy, not real production credentials.
- **Deliverable:** Migration sequence, approval gates, compat matrix, backfill resume logic, restore and verification queries.
- **Professional anti-pattern:** No unapproved destructive DDL, production migrations or fake zero-downtime guarantees.
- **Acceptance evidence:** DevOps schedules deploy steps; QA confirms old/new compatibility; Backend implements readers.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD06 — Transactions, race conditions and business invariants
- **When applicable:** Duplicate records, lost updates, stock counters, reservations or money-like balances are involved.
- **Analysis and design sequence:** Identify invariant and transaction boundary. Select uniqueness constraints, conditional updates, isolation/locking, optimistic versions, idempotency keys, safe retries after serialization/deadlocks. Exercise crash/timeout-after-commit and duplicate message behaviors.
- **Deliverable:** Consistency contract, concurrency timeline, isolation decision, race matrix and tests.
- **Professional anti-pattern:** Avoid check-then-insert without constraint, assuming exactly-once delivery, blind retry on non-idempotent operations.
- **Acceptance evidence:** Backend owns command orchestration; QA runs two-client race and replay cases.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD07 — Query planning, indexes and workload-based tuning
- **When applicable:** Slow queries, cardinality growth, data grids, exports and reports.
- **Analysis and design sequence:** Collect sanitized query shapes/frequency/data scale, benchmark with representative data. Analyze plans, N+1, sort/filter pagination, index coverage and selectivity; measure write amplification and storage cost. Set regression thresholds from real baseline.
- **Deliverable:** Top-query inventory, explain evidence, index tradeoffs, measured before/after and rollback.
- **Professional anti-pattern:** Never claim indexes universally improve performance; no production ANALYZE/EXPLAIN side-effects without policy.
- **Acceptance evidence:** Performance validates p95 throughput; Backend confirms pagination contracts.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD08 — Tenant-aware partitioning, authorization and data sharing
- **When applicable:** Multi-tenant users, organizations, schools or cross-tenant data access exists.
- **Analysis and design sequence:** Document tenancy model, tenant identifiers, access contexts, row/document predicate rules, elevated/admin exceptions, caches, exports, search indexes and background jobs. Combine application authz with database least privilege/RLS when available; test denial by swapping actor and tenant IDs.
- **Deliverable:** Tenant data-flow map, access matrix, query guardrails, negative tests and threat exceptions.
- **Professional anti-pattern:** Do not trust client tenant_id; no global admin connection as default request role.
- **Acceptance evidence:** Security signs off cross-tenant threat cases; QA tests list/get/update/export/search leakage.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD09 — Backup, PITR, restore tests and disaster recovery
- **When applicable:** System holds valuable records or claims recovery objectives.
- **Analysis and design sequence:** Elicit data loss/outage tolerance (RPO/RTO). Inventory base backups, journals/oplog/WAL/replica snapshots, encryption, offsite storage, key recovery, access separation and expiration. Perform isolated restore drill; reconcile checksums/counts and application smoke tests.
- **Deliverable:** Recovery plan, backup coverage and key custody, restore evidence template, failure drill calendar.
- **Professional anti-pattern:** A successful backup job is not proof of restorability; never execute restores over real production.
- **Acceptance evidence:** DevOps owns automation, QA validates restored behavior, Product approves tolerances.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD10 — Classification, retention, deletion, legal holds and audit provenance
- **When applicable:** Sensitive records, retention limits or user deletion requests affect storage.
- **Analysis and design sequence:** Map data purposes and classification, data subject references, retention clocks, pseudonymization, deletion propagation to caches/backups/exports, legal hold exclusions, audit log minimization and consent changes. Differentiate policies from verified jurisdictional requirements.
- **Deliverable:** Data inventory, retention/deletion matrix, audit schema, privacy approval needs and tests.
- **Professional anti-pattern:** Do not promise deletion from immutable backups without established lifecycle and policy; never expose PII in samples.
- **Acceptance evidence:** Product owns policy, Security validates threat/privacy, DevOps backup lifecycle.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD11 — Outbox/inbox, CDC, sync and derived data correctness
- **When applicable:** App writes DB and sends notifications, events, search updates or analytics together.
- **Analysis and design sequence:** Define durable commit point; use transactional outbox only where supported and needed, idempotent consumers, dedupe keys, replay windows and reconciliation. Clarify ordering and eventual-consistency UI impact. CDC is not a universal shortcut; consider retention and schema compatibility.
- **Deliverable:** Event/data contract, delivery semantics, recovery diagram, reconciliation queries and failure injection tests.
- **Professional anti-pattern:** No blind dual-write, unsupported exactly-once claims or replay without side-effect validation.
- **Acceptance evidence:** Backend/Integration implement consumer contracts, QA simulates crash-after-commit.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD12 — Reporting/search/analytics data architecture
- **When applicable:** Dashboards, data tables, full-text search, exports or historical reports need special access paths.
- **Analysis and design sequence:** Separate operational queries from analytics/exports where load warrants; define source of truth, freshness, row-level visibility, pagination, index/search semantics and consistency. Audit expensive aggregation and PII access; design stable snapshots for exports.
- **Deliverable:** Query/report contract, data freshness SLA, derived view model and authorization test cases.
- **Professional anti-pattern:** Do not suggest a separate warehouse/search engine before workload evidence; no unbounded export by default.
- **Acceptance evidence:** Product confirms business definitions, Frontend owns data-grid UX, Security tests exports.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD13 — Database operational monitoring, capacity and regressions
- **When applicable:** Growth, outages, locks, connection saturation or unstable performance.
- **Analysis and design sequence:** Track pool occupancy, locks/wait time, slow queries, checkpoint/replication lag as applicable, disk/IO, backup age and migration drift. Use safe cardinality and redacted query metadata; design meaningful alerts and response runbooks.
- **Deliverable:** Operational dashboard spec, metrics dictionary, capacity forecast assumptions and alert actions.
- **Professional anti-pattern:** Avoid logging raw SQL parameters/PII and alarms without defined owners.
- **Acceptance evidence:** DevOps/Performance validate signals and alert thresholds against observed baselines.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

## DBD14 — Data quality, representative fixtures and property testing
- **When applicable:** Database model changes require verification beyond happy-path CRUD.
- **Analysis and design sequence:** Build synthetic privacy-safe fixtures for zero/null/duplicate/large/unicode/locale/multitenant/race conditions. Test FK/unique/check/validator behavior, migrations up/down or roll-forward, idempotency, consistency and restores. Use property-based tests for invariants when cost-effective.
- **Deliverable:** Data test matrix, fixture policy, migration rehearsal outputs and evidence-linked defects.
- **Professional anti-pattern:** Never seed production from test harness or mark migration verified without execution.
- **Acceptance evidence:** QA owns harness/evidence; Database owns invariant correctness and test data boundaries.
- **Negative-case challenge:** What breaks when inputs are wrong, ownership changes, dependencies fail or two actors operate concurrently? Document one actual test or an explicitly unrun test.
- **Handoff:** exact contract/owner/approval; never assign all 16 agents by default.

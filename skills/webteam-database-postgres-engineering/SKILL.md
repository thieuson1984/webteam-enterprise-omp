---
name: webteam-database-postgres-engineering
description: "PostgreSQL constraints, MVCC, RLS and indexing. Apply selectively when postgreSQL is selected or existing SQL reliability issues appear."
---

# PostgreSQL constraints, MVCC, RLS and indexing

**Owner:** `webteam-database`. **Activation:** PostgreSQL is selected or existing SQL reliability issues appear. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Choose proper column types and constraints; understand MVCC/isolation and lock contention. Use RLS only after validating session/role setup, ownership bypass, FORCE policy needs and tenant test matrix. Profile real SQL with EXPLAIN (ANALYZE) only in safe environment; assess index build/migration locking.

## Mandatory work products

Schema/role design, isolation decision, RLS policies and negative tests, measured plan and migration safety notes. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Security crosschecks tenant policy; Backend preserves session-scoped tenant context. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Never assume RLS replaces service authz or test dangerous queries against production by default. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- PostgreSQL MVCC and isolation: https://www.postgresql.org/docs/current/mvcc.html
- PostgreSQL RLS: https://www.postgresql.org/docs/current/ddl-rowsecurity.html

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

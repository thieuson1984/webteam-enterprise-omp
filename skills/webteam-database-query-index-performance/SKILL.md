---
name: webteam-database-query-index-performance
description: "Query planning, indexes and workload-based tuning. Apply selectively when slow queries, cardinality growth, data grids, exports and reports."
---

# Query planning, indexes and workload-based tuning

**Owner:** `webteam-database`. **Activation:** Slow queries, cardinality growth, data grids, exports and reports. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Collect sanitized query shapes/frequency/data scale, benchmark with representative data. Analyze plans, N+1, sort/filter pagination, index coverage and selectivity; measure write amplification and storage cost. Set regression thresholds from real baseline.

## Mandatory work products

Top-query inventory, explain evidence, index tradeoffs, measured before/after and rollback. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Performance validates p95 throughput; Backend confirms pagination contracts. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Never claim indexes universally improve performance; no production ANALYZE/EXPLAIN side-effects without policy. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- Use relevant, verified engine documentation from `webteam-database-engineering-reference` for the *actual* selected database.

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

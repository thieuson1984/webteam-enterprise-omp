---
name: webteam-database-reporting-search
description: "Reporting/search/analytics data architecture. Apply selectively when dashboards, data tables, full-text search, exports or historical reports need special access paths."
---

# Reporting/search/analytics data architecture

**Owner:** `webteam-database`. **Activation:** Dashboards, data tables, full-text search, exports or historical reports need special access paths. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Separate operational queries from analytics/exports where load warrants; define source of truth, freshness, row-level visibility, pagination, index/search semantics and consistency. Audit expensive aggregation and PII access; design stable snapshots for exports.

## Mandatory work products

Query/report contract, data freshness SLA, derived view model and authorization test cases. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Product confirms business definitions, Frontend owns data-grid UX, Security tests exports. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Do not suggest a separate warehouse/search engine before workload evidence; no unbounded export by default. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- Use relevant, verified engine documentation from `webteam-database-engineering-reference` for the *actual* selected database.

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

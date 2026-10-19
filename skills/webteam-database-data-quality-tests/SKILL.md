---
name: webteam-database-data-quality-tests
description: "Data quality, representative fixtures and property testing. Apply selectively when database model changes require verification beyond happy-path CRUD."
---

# Data quality, representative fixtures and property testing

**Owner:** `webteam-database`. **Activation:** Database model changes require verification beyond happy-path CRUD. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Build synthetic privacy-safe fixtures for zero/null/duplicate/large/unicode/locale/multitenant/race conditions. Test FK/unique/check/validator behavior, migrations up/down or roll-forward, idempotency, consistency and restores. Use property-based tests for invariants when cost-effective.

## Mandatory work products

Data test matrix, fixture policy, migration rehearsal outputs and evidence-linked defects. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

QA owns harness/evidence; Database owns invariant correctness and test data boundaries. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Never seed production from test harness or mark migration verified without execution. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- Use relevant, verified engine documentation from `webteam-database-engineering-reference` for the *actual* selected database.

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

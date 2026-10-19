---
name: webteam-database-transaction-concurrency
description: "Transactions, race conditions and business invariants. Apply selectively when duplicate records, lost updates, stock counters, reservations or money-like balances are involved."
---

# Transactions, race conditions and business invariants

**Owner:** `webteam-database`. **Activation:** Duplicate records, lost updates, stock counters, reservations or money-like balances are involved. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Identify invariant and transaction boundary. Select uniqueness constraints, conditional updates, isolation/locking, optimistic versions, idempotency keys, safe retries after serialization/deadlocks. Exercise crash/timeout-after-commit and duplicate message behaviors.

## Mandatory work products

Consistency contract, concurrency timeline, isolation decision, race matrix and tests. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Backend owns command orchestration; QA runs two-client race and replay cases. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Avoid check-then-insert without constraint, assuming exactly-once delivery, blind retry on non-idempotent operations. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- Use relevant, verified engine documentation from `webteam-database-engineering-reference` for the *actual* selected database.

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

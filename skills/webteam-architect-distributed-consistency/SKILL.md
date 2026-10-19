---
name: webteam-architect-distributed-consistency
description: "Distributed systems, consistency and failure models. Apply selectively when multiple services or data stores require cross-boundary coordination."
---

# Distributed systems, consistency and failure models

**Owner:** `webteam-architect`. **Activation:** Multiple services or data stores require cross-boundary coordination. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

State consistency requirements, failure model, duplicate delivery, clock assumptions, retry safety, transaction/outbox or saga boundaries and compensation semantics. Compare transactional single-store implementation first; justify distributed design only when necessary.

## Mandatory work products

Consistency matrix, failure sequence diagrams, recovery/idempotency contracts, cost and operational risk. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Backend/Database/QA test duplicate, reorder, crash-after-commit and partial failure. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

No fictitious exactly-once behavior, unbounded retries or implicit cross-service atomicity. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- C4 architecture communication: https://c4model.com/
- AWS Well-Architected tradeoff framework (not an AWS requirement): https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

---
name: webteam-architect-reliability-operability
description: "Reliability, SLOs, capacity and graceful degradation. Apply selectively when service availability, resilience or timeouts are critical."
---

# Reliability, SLOs, capacity and graceful degradation

**Owner:** `webteam-architect`. **Activation:** Service availability, resilience or timeouts are critical. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Establish service-level indicators from actual user journeys. Design bounded timeouts, retry budgets, backpressure, bulkheads only when warranted, graceful shutdown and graceful degradation. Define RTO/RPO with business approval and recovery rehearsals.

## Mandatory work products

SLI/SLO proposal, dependency failure matrix, runbook outlines, recovery validation and cost implication. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

DevOps/QA validate outage simulations and alert signals, Product accepts user impact. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

No arbitrary 99.99% target or retry storm; do not declare backups good without restore test. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

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

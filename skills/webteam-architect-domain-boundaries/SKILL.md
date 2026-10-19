---
name: webteam-architect-domain-boundaries
description: "Bounded contexts and evolutionary modular monolith. Apply selectively when domain logic bleeds across modules or a system is splitting/merging services."
---

# Bounded contexts and evolutionary modular monolith

**Owner:** `webteam-architect`. **Activation:** Domain logic bleeds across modules or a system is splitting/merging services. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Find cohesive business capabilities, ownership and transaction boundaries. Define allowed dependency directions, public module interfaces, anti-corruption layers, cycles policy and extraction criteria. Default to modular monolith unless independent scaling/deployment/data ownership justify distribution.

## Mandatory work products

Context map, component responsibility table, interface contract, architecture tests and extraction trigger. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Reviewer checks import boundaries; Database verifies ownership of writes, Backend API contracts. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Avoid shared-everything libraries, distributed transactions by default and architecture astronautics. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

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

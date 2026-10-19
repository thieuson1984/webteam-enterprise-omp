---
name: webteam-architect-architecture-drivers
description: "Architecture drivers, quality-attribute scenarios and fitness. Apply selectively when an architectural decision lacks explicit load, latency, availability, security or evolution constraints."
---

# Architecture drivers, quality-attribute scenarios and fitness

**Owner:** `webteam-architect`. **Activation:** An architectural decision lacks explicit load, latency, availability, security or evolution constraints. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Elicit measurable quality-attribute scenarios: stimulus, environment, response and measure. Rank by business criticality and change likelihood. Compare simplest viable options with tradeoffs across reliability, security, cost, team topology and complexity. Convert high-risk assumptions to spikes and tests.

## Mandatory work products

Architectural drivers matrix, option tradeoff, rejected alternatives, decision criteria and validation tasks. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Product verifies scenarios; QA turns key quality requirements into executable or observable checks. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Do not substitute microservices/Kubernetes diagrams for measured requirements or prescribe an unverified SLO. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

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

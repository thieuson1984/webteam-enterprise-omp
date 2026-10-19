---
name: webteam-architect-fitness-functions
description: "Architecture fitness functions and governance-as-code. Apply selectively when architecture is documented but not enforced or drifts over releases."
---

# Architecture fitness functions and governance-as-code

**Owner:** `webteam-architect`. **Activation:** Architecture is documented but not enforced or drifts over releases. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Translate key invariants into buildable static/dynamic checks: import boundaries, forbidden dependencies, API compatibility, module ownership, secret-free config, database contract smoke tests, release budgets and dependency update gates. Assign threshold, owner, CI mode and exception process.

## Mandatory work products

Fitness function matrix, executable-test candidates, CI evidence map, waiver log. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

QA runs representative tests; false positives and migration exceptions are documented. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Avoid brittle golden metrics with no baselines or CI jobs that require production credentials. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

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

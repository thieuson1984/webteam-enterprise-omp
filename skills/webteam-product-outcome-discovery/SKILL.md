---
name: webteam-product-outcome-discovery
description: "Outcome-driven discovery and problem framing. Apply selectively when a proposed feature is not linked to a specific user problem or measurable business outcome."
---

# Outcome-driven discovery and problem framing

**Owner:** `webteam-product`. **Activation:** A proposed feature is not linked to a specific user problem or measurable business outcome. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Define target user, job-to-be-done, critical journey, constraints, baseline and outcome metric. Build a concise opportunity tree: outcome → observed problems → solution hypotheses → smallest experiments. Separate needs observed in interviews/analytics from assumptions; explain opportunity cost of not solving each problem.

## Mandatory work products

A one-page opportunity brief, numbered hypotheses HYP-*, research gaps, falsifiable success/kill criteria, opportunity→requirements trace. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Product and QA agree success measurements and leading/lagging guardrails; Designer validates journeys. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Reject fake user interviews, invented market statistics and output-only success such as number of screens shipped. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- ISO/IEC 25010:2023 quality model: https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/07/81/78176.html
- Evidence-driven discovery/opportunity trees: https://www.producttalk.org/opportunity-solution-trees/

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

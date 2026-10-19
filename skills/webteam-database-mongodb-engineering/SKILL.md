---
name: webteam-database-mongodb-engineering
description: "MongoDB documents, validation, atomicity and indexes. Apply selectively when document data access, embedding, schema changes or query perf in MongoDB."
---

# MongoDB documents, validation, atomicity and indexes

**Owner:** `webteam-database`. **Activation:** Document data access, embedding, schema changes or query perf in MongoDB. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Select embedding/reference by bounded aggregates, write contention, document size and query shapes. Use validator/schema versioning with staged rollout; unique/compound indexes backed by workload. Distinguish single-document atomicity from multi-document transactions and verify deployment capabilities.

## Mandatory work products

Collection schemas and examples, relationship decision table, index workload map, transaction applicability and migration plan. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

QA validates validator failures, duplicates, retry behavior and index regressions. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

No assumption that denormalization is universally better or that multi-document transactions are free. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- MongoDB modeling: https://www.mongodb.com/docs/manual/data-modeling/embedding/
- MongoDB indexes/validation: https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/create-indexes/

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

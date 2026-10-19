---
name: webteam-database-backup-recovery
description: "Backup, PITR, restore tests and disaster recovery. Apply selectively when system holds valuable records or claims recovery objectives."
---

# Backup, PITR, restore tests and disaster recovery

**Owner:** `webteam-database`. **Activation:** System holds valuable records or claims recovery objectives. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Elicit data loss/outage tolerance (RPO/RTO). Inventory base backups, journals/oplog/WAL/replica snapshots, encryption, offsite storage, key recovery, access separation and expiration. Perform isolated restore drill; reconcile checksums/counts and application smoke tests.

## Mandatory work products

Recovery plan, backup coverage and key custody, restore evidence template, failure drill calendar. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

DevOps owns automation, QA validates restored behavior, Product approves tolerances. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

A successful backup job is not proof of restorability; never execute restores over real production. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- Use relevant, verified engine documentation from `webteam-database-engineering-reference` for the *actual* selected database.

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

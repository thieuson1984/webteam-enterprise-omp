---
name: webteam-database-privacy-lifecycle
description: "Classification, retention, deletion, legal holds and audit provenance. Apply selectively when sensitive records, retention limits or user deletion requests affect storage."
---

# Classification, retention, deletion, legal holds and audit provenance

**Owner:** `webteam-database`. **Activation:** Sensitive records, retention limits or user deletion requests affect storage. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Map data purposes and classification, data subject references, retention clocks, pseudonymization, deletion propagation to caches/backups/exports, legal hold exclusions, audit log minimization and consent changes. Differentiate policies from verified jurisdictional requirements.

## Mandatory work products

Data inventory, retention/deletion matrix, audit schema, privacy approval needs and tests. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Product owns policy, Security validates threat/privacy, DevOps backup lifecycle. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Do not promise deletion from immutable backups without established lifecycle and policy; never expose PII in samples. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- OWASP database privileges: https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

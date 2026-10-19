---
name: webteam-database-tenant-isolation
description: "Tenant-aware partitioning, authorization and data sharing. Apply selectively when multi-tenant users, organizations, schools or cross-tenant data access exists."
---

# Tenant-aware partitioning, authorization and data sharing

**Owner:** `webteam-database`. **Activation:** Multi-tenant users, organizations, schools or cross-tenant data access exists. Do not preload unrelated skills. Use the current project's approved facts, not hypothetical defaults.

## Method and professional judgment

Document tenancy model, tenant identifiers, access contexts, row/document predicate rules, elevated/admin exceptions, caches, exports, search indexes and background jobs. Combine application authz with database least privilege/RLS when available; test denial by swapping actor and tenant IDs.

## Mandatory work products

Tenant data-flow map, access matrix, query guardrails, negative tests and threat exceptions. Every substantial claim must carry a source path/reference, observation or explicit assumption; assign owner and evidence status. Track constraints, unknowns, scope exclusions and downstream impacts.

## Collaboration contract

Security signs off cross-tenant threat cases; QA tests list/get/update/export/search leakage. Delegate only when a real task crosses that role's ownership; orchestrator limits tool access, token budget and concurrent writers. Product sets intent; Architect sets structure; Database sets persistence invariants; Backend implements application use cases; Security reviews authorization and privacy; QA provides executed evidence.

## Failure modes and guardrails

Do not trust client tenant_id; no global admin connection as default request role. Avoid gratuitous technology, fabricated user evidence, unverified compliance or migration promises. Never run unknown scripts, touch production systems, promote project data to global memory, change model/provider or execute destructive writes as a side effect of advice. Require explicit approval for irreversible or privacy-sensitive work.

## Acceptance and escalation

1. Identify the scope and real repository revision; record evidence quality as `VERIFIED`, `INFERRED`, `PROPOSED`, `BLOCKED` or `NOT_APPLICABLE`.
2. Produce the work products above, with testable acceptance conditions and an explicit owner.
3. Name at least one realistic negative, failure or boundary scenario, and a verification method.
4. Escalate high-impact decisions, changes to policy/brand, production data or costly infrastructure before executing them.
5. Close with what was tested **in reality**, what was merely analyzed, and unresolved dependencies.

## Selective sources

- OWASP database privileges: https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html

*These sources are guidance, not claims of certification or runtime validation. Verify applicability and current engine versions.*

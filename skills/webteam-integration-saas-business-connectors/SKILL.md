---
name: webteam-integration-saas-business-connectors
description: "Business SaaS and Enterprise Connector Engineering; a targeted professional workflow with evidence and safe validation."
---

# Business SaaS and Enterprise Connector Engineering

**Owner:** `webteam-integration`. Optional skill: load only when a relevant task is present; it does not grant execution rights.

## Trigger and problem definition

A product exchanges customers, orders, documents, payments or account records with approved SaaS and enterprise platforms.

## Inputs

- Actual code paths and current repository revision, confirmed use cases, affected users and approval boundary.
- Current schemas or UI contracts, permissions/tenant rules, error behavior, existing tests and expected side effects.
- Safe development or sandbox environments, representative synthetic fixtures and bounded time/cost budget.

## Professional execution workflow

1. **Discover:** verify current behavior from code/tests; separate `OBSERVED`, `INFERRED`, `NOT_RUN` and `BLOCKED` evidence.
2. **Formalize contract:** specify actors, allowed actions, state invariants, source-of-truth, normal/error/empty and degraded behavior.
3. **Design solution:** Inventory supported APIs and tenant scope; map canonical IDs, object ownership, field semantics, consent, paging, rate limits, retries and reconciliation. Use sandbox and least-scoped credentials.
4. **Edge cases:** include negative authorization, old/new schema, long/empty content, lost response, duplicate delivery, concurrency, cancellation and recovery when applicable.
5. **Verify:** choose the cheapest reliable unit/contract/API/Playwright/manual-assistive tests warranted by risk; only execute on approved isolated resources.
6. **Handoff:** cite source paths, outcomes, remaining risk, affected owner, proposed patch, independent reviewer and rollback plan.

## Acceptance criteria

- Supported connectors are versioned, least-privilege, testable and reversible.
- No unapproved production writes, external API calls, credential exposure, cross-tenant access or silent changes to previously approved behavior.
- Findings explain confidence, severity, measured result versus hypothesis, and realistic next verification step.

## Coordination

Architect defines system boundaries; Product confirms business semantics; Backend builds adapters; Database owns stored state; Security reviews credentials and cross-tenant access; QA proves contracts.

## References

Load the corresponding domain's `engineering-reference` skill and only the relevant blueprint or acceptance matrix entry. Select official W3C WAI/WCAG, Playwright, OpenAPI, AsyncAPI, provider or platform standards based on the actual project requirements; do not claim a test or service integration ran unless observed.

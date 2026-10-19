---
name: webteam-integration-schema-evolution-and-mapping
description: "Cross-System Schema Evolution and Mapping; a targeted professional workflow with evidence and safe validation."
---

# Cross-System Schema Evolution and Mapping

**Owner:** `webteam-integration`. Optional skill: load only when a relevant task is present; it does not grant execution rights.

## Trigger and problem definition

Message or API schemas evolve, external fields diverge or old/new consumers deploy independently.

## Inputs

- Actual code paths and current repository revision, confirmed use cases, affected users and approval boundary.
- Current schemas or UI contracts, permissions/tenant rules, error behavior, existing tests and expected side effects.
- Safe development or sandbox environments, representative synthetic fixtures and bounded time/cost budget.

## Professional execution workflow

1. **Discover:** verify current behavior from code/tests; separate `OBSERVED`, `INFERRED`, `NOT_RUN` and `BLOCKED` evidence.
2. **Formalize contract:** specify actors, allowed actions, state invariants, source-of-truth, normal/error/empty and degraded behavior.
3. **Design solution:** Version schemas and mapping rules, classify compatible and breaking changes, handle unknown fields and numeric precision, replay past payloads, validate dual-version rollout and deprecation.
4. **Edge cases:** include negative authorization, old/new schema, long/empty content, lost response, duplicate delivery, concurrency, cancellation and recovery when applicable.
5. **Verify:** choose the cheapest reliable unit/contract/API/Playwright/manual-assistive tests warranted by risk; only execute on approved isolated resources.
6. **Handoff:** cite source paths, outcomes, remaining risk, affected owner, proposed patch, independent reviewer and rollback plan.

## Acceptance criteria

- Old and new supported clients have measured compatibility or approved migration.
- No unapproved production writes, external API calls, credential exposure, cross-tenant access or silent changes to previously approved behavior.
- Findings explain confidence, severity, measured result versus hypothesis, and realistic next verification step.

## Coordination

Architect defines system boundaries; Product confirms business semantics; Backend builds adapters; Database owns stored state; Security reviews credentials and cross-tenant access; QA proves contracts.

## References

Load the corresponding domain's `engineering-reference` skill and only the relevant blueprint or acceptance matrix entry. Select official W3C WAI/WCAG, Playwright, OpenAPI, AsyncAPI, provider or platform standards based on the actual project requirements; do not claim a test or service integration ran unless observed.

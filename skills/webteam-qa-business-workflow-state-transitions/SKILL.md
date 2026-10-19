---
name: webteam-qa-business-workflow-state-transitions
description: "Business Workflow and State-Transition Verification; a targeted professional workflow with evidence and safe validation."
---

# Business Workflow and State-Transition Verification

**Owner:** `webteam-qa`. Optional skill: load only when a relevant task is present; it does not grant execution rights.

## Trigger and problem definition

Test approvals, CRUD lifecycle, order/case status, workflow invariants, role transitions and retries across frontend, API and persistence.

## Inputs

- Actual code paths and current repository revision, confirmed use cases, affected users and approval boundary.
- Current schemas or UI contracts, permissions/tenant rules, error behavior, existing tests and expected side effects.
- Safe development or sandbox environments, representative synthetic fixtures and bounded time/cost budget.

## Professional execution workflow

1. **Discover:** verify current behavior from code/tests; separate `OBSERVED`, `INFERRED`, `NOT_RUN` and `BLOCKED` evidence.
2. **Formalize contract:** specify actors, allowed actions, state invariants, source-of-truth, normal/error/empty and degraded behavior.
3. **Design solution:** Model actors and authorized transitions; verify forbidden transitions, cancellation, rollback, stale versions, concurrent actions, audit events and notifications; cross-check product acceptance.
4. **Edge cases:** include negative authorization, old/new schema, long/empty content, lost response, duplicate delivery, concurrency, cancellation and recovery when applicable.
5. **Verify:** choose the cheapest reliable unit/contract/API/Playwright/manual-assistive tests warranted by risk; only execute on approved isolated resources.
6. **Handoff:** cite source paths, outcomes, remaining risk, affected owner, proposed patch, independent reviewer and rollback plan.

## Acceptance criteria

- Every critical transition has positive/negative evidence and no duplicate side effects.
- No unapproved production writes, external API calls, credential exposure, cross-tenant access or silent changes to previously approved behavior.
- Findings explain confidence, severity, measured result versus hypothesis, and realistic next verification step.

## Coordination

Product defines requirements; Backend, Frontend and Database own implementation; Integration owns external contracts; Security, Accessibility and Reviewer independently validate applicable risks.

## References

Load the corresponding domain's `engineering-reference` skill and only the relevant blueprint or acceptance matrix entry. Select official W3C WAI/WCAG, Playwright, OpenAPI, AsyncAPI, provider or platform standards based on the actual project requirements; do not claim a test or service integration ran unless observed.

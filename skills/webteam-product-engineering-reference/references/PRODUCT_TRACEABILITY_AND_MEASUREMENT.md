# Product Traceability, Metrics and Readiness

## Traceability matrix (example columns)

| Outcome ID | User/problem evidence | REQ ID | AC ID | UX design | API/data | Tests | Metric | Approval |
|---|---|---|---|---|---|---|---|---|
| OUT-001 | customer-interview reference / unverified | REQ-001 | AC-001 | user journey | affected contract | QA-001 | baseline/event | product owner |

Every ID must point to a real artifact when one exists. Explicitly mark unlinked proposals as `UNVERIFIED`; never fabricate executed research or impact.

## Example acceptance story

- Given a student record belongs to School A, when a School B teacher requests it, then the server returns the approved denial response and reveals no record existence or PII.
- Given an enrollment request is submitted twice with the same idempotency key, when both requests finish, then at most one durable enrollment is created; API status follows documented idempotency semantics.
- Given an accessible localized UI, when a Vietnamese name is very long or contains diacritics, labels remain comprehensible and screen-reader relationships persist.

## Outcome measurement protocol

1. Name the beneficiary and behavior, not only a UI click or screen count.
2. Establish measurement feasibility and an observed or explicitly unknown baseline.
3. Define numerator/denominator, time window, segmentation, guardrails and data owner.
4. Map events to minimization/consent and test duplicate/missing events.
5. Distinguish causation from correlation; use ethically designed experiments when possible.
6. Schedule outcome review and deprecate low-value work rather than adding endless features.

## Product → engineering handoff

Product owns requirements and policy; Architect records important technical choices; Database and Backend ensure persistence/authorization semantics; Designer owns usability; QA owns acceptance verification; Product judges outcome after release. Resolve conflicting specifications before implementation. Clear business rules should not be "fixed" by changing one database enum in isolation.

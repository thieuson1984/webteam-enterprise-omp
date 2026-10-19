# QA — Acceptance and Evidence Matrix

This is a review template, not a claim of compliance or a runtime test. Mark only the checks relevant to the product and repository.

## Separate evidence status dimensions

| Check | Applicable? | Requirement/actor | Observed evidence | Run result | Owner | Residual risk |
|---|---|---|---|---|---|---|
| Critical business/user journey | yes/no | REQ/AC ID | test/source reference | PASS / FAIL / NOT_RUN / BLOCKED | named | explicit |
| Invalid, unauthorized, cross-tenant | yes/no | action/object | negative result | PASS / FAIL / NOT_RUN / BLOCKED | named | explicit |
| Delayed, duplicate, offline or failure | yes/no | invariant | sandbox/stub trace | PASS / FAIL / NOT_RUN / BLOCKED | named | explicit |
| Data ownership and source of truth | yes/no | producer/consumer | contract and mapping | PASS / FAIL / NOT_RUN / BLOCKED | named | explicit |
| Assistive technology/manual UX | yes/no | page/widget | AT/browser + result | PASS / FAIL / NOT_RUN / BLOCKED | named | explicit |
| Release rollback, regression | yes/no | change request | actual approved test | PASS / FAIL / NOT_RUN / BLOCKED | named | explicit |

## Release stop conditions

- Confirmed high-risk defect impacting security, durable data integrity or accessibility of essential workflow with no accepted mitigation.
- Critical test evidence missing or failed and no informed accountable signoff.
- Product/source mutation outside approved environment or command scope.
- External provider interaction requiring credentials, spend, tenant data transfer or production write without approval.
- An agent declares a compliance/safety certification based on text or one automated tool alone.

## Severity and reproducibility

Record finding IDs, affected role/tenant, environment, revision, steps, actual vs expected behavior, evidence paths, responsible code owner, proposed fix, tests and rollback. Preserve original failures, do not silently regenerate snapshots or mark an unexecuted gate PASS.

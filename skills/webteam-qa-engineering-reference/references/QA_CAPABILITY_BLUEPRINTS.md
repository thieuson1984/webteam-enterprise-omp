# Principal Test Automation and Quality Engineer — Capability Blueprints

Apply only to relevant product features; do not infer that unused domains exist. Each entry is a workflow, not proof of implementation.

## Q01 — Risk-based Test Strategy

**Activate when:** Risk and change impact vary across roles, business flows, tenant isolation and operational environments.

**Workflow:** Assess impact × likelihood × detectability, prioritize critical journeys and irreversible side effects, choose unit/contract/E2E proportions.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Each high-risk requirement has identified tests, owner and real evidence.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q02 — Requirements and Invariant Traceability

**Activate when:** Acceptance or requirements are incomplete or scattered.

**Workflow:** Trace REQ/AC → actor/permission → domain invariant → implementation path → executable test → actual result.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Critical behavior is mapped to coverage or explicitly blocked.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q03 — Deterministic Test Data and Environments

**Activate when:** Tests are flaky because of state leakage, clock, locale or shared accounts.

**Workflow:** Use seeded isolated data, frozen clocks where feasible, stable IDs, synthetic privacy-safe fixtures, per-test cleanup.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Failures reproduce locally and in CI without touching production.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q04 — Unit and Component Test Engineering

**Activate when:** Business calculations, domain parsers and UI state transitions need fast checks.

**Workflow:** Test behavior/observable outputs and boundaries, not brittle implementation details; include negative and error states.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Failures signal true contract regressions and are deterministic.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q05 — API and Consumer/Provider Contract Verification

**Activate when:** Clients and services deploy at different speeds.

**Workflow:** Validate request/response schemas, errors, pagination, authorization, idempotency and version compatibility; use approved contract tooling.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Consumers and providers pass compatibility gates or documented migration.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q06 — Playwright Business Journey Automation

**Activate when:** A user flow spans auth, forms, navigation and API outcomes.

**Workflow:** Use accessible locators, isolated sessions, seeded data, multi-browser trace and realistic empty/error/retry states.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Critical journeys verified on supported browsers with trace provenance.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q07 — Visual and Responsive Regression Governance

**Activate when:** Layout, dense views or theme changes risk regressions.

**Workflow:** Control browser/font/time/data/viewport; test high zoom, overflow, large content; require independent baseline approval.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Visual changes are explainable and approved; no silent baseline regeneration.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q08 — Business Workflow and State-Transition Verification

**Activate when:** Approvals, lifecycle statuses, queues or multi-step forms encode complex business rules.

**Workflow:** Test allowed/forbidden transitions, workflow timeouts, approval chains, cancellation, partial save and compensation, idempotent replay and audit trail.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Unauthorized or duplicate transitions cannot change business outcome.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q09 — Concurrency and Transaction Invariant Testing

**Activate when:** Multiple writers update same resource or share a constraint.

**Workflow:** Test stale versions, simultaneous updates, constraint conflicts, timeout-after-commit and duplicate requests.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** No double side effects, silent lost update or undetected conflict.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q10 — Resilience and Fault Simulation

**Activate when:** Network or dependency outages affect customer workflows.

**Workflow:** Inject sandbox timeouts, late/out-of-order events, lost acknowledgements, restarts and retry storms; test bounded recovery.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Recovery is observable, safe and reproducible without production load.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q11 — Event and Integration Verification

**Activate when:** Webhooks, queues and SaaS adapters can drift or replay.

**Workflow:** Test signature validation, schema versions, duplicate/out-of-order events, callback failure, auth rotation, rate limiting and reconciliation.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** External contracts verified with stubs and versioned fixtures.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q12 — Security and Tenant Negative Test Suites

**Activate when:** Roles and tenant boundaries protect sensitive resources.

**Workflow:** Test actor × action × object × tenant, stale sessions, BOLA, BFLA, CSRF where applicable and server-side denial.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Unauthorized paths proven denied with non-destructive tests.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q13 — CI Quality Gates and Flakiness Analysis

**Activate when:** CI tests are unreliable or too costly.

**Workflow:** Classify flakes by time/network/data/race and keep evidence; sharding and minimal retries must not mask defects.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** CI health and quarantines tracked with owner and expiry.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Q14 — Release Quality, UAT and Evidence Handoff

**Activate when:** Deployment decision needs objective release and business acceptance.

**Workflow:** Summarize coverage, blocked tests, migration contracts, rollback evidence, known defects and accountable signoff.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Release readiness reported as PASS/FAIL/BLOCKED/NOT_RUN with proof.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Cross-domain anti-patterns

- Treating a template workflow as the actual product requirement.
- Marking scanner, document, or prompt execution as proof tests passed.
- Performing production mutations to satisfy a command.
- Loading the entire blueprint catalog into one task rather than the relevant headings.

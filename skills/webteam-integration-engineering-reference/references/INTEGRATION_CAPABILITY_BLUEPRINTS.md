# Principal Enterprise Integration Engineer — Capability Blueprints

Apply only to relevant product features; do not infer that unused domains exist. Each entry is a workflow, not proof of implementation.

## I01 — System Boundaries and Canonical Data Contracts

**Activate when:** Multiple software platforms use inconsistent identifiers, formats and semantics.

**Workflow:** Map producer/consumer, source of truth per field, canonical IDs, units and time semantics, transformation loss.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Boundaries and reconciliation invariants are explicit.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I02 — API/GraphQL/gRPC Compatibility Engineering

**Activate when:** Internal and external consumers deploy independently.

**Workflow:** Use actual supported protocol, versioned request/response/event schemas, compatibility tests, deprecation and pagination.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Approved consumers remain compatible or have migration.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I03 — Integration Identity, Secrets and Trust

**Activate when:** Data crosses customer/tenant/service boundaries.

**Workflow:** Use scoped OAuth/service identities, mTLS only if warranted, audit, secret rotation and tenant ownership.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Unauthorized access denied with redacted evidence.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I04 — Secure Webhooks and Callbacks

**Activate when:** Provider callbacks can replay or arrive late.

**Workflow:** Validate signed raw payload, time tolerance, replay protection, idempotent processing and bounded retries.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Duplicate callback does not duplicate business effect.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I05 — Event Brokers and Messaging Semantics

**Activate when:** Async systems reorder or redeliver messages.

**Workflow:** Define at-least-once realities, ordering scopes, outbox/inbox, dead letters and correlation IDs.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Recovery is idempotent and observable.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I06 — Long-running Integration Workflows

**Activate when:** Cross-system workflows span multiple irreversible actions.

**Workflow:** Use durable state machine, saga compensation when possible, manual intervention for irreversible stages.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Partial completion can be detected and remediated.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I07 — Synchronization, CDC and Reconciliation

**Activate when:** Copies of records drift.

**Workflow:** Specify writer authority, cursor, conflict policy, replay windows and reconciliation audit.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** No silent overwrites or unexplained drift.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I08 — Business SaaS and Enterprise Connector Engineering

**Activate when:** CRM, identity, payment, document or ERP platforms need stable connectors.

**Workflow:** Document provider scopes, IDs, object mappings, rate limits, changes, sandbox tests and owner.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Connector changes are compatible and reversible.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I09 — External System Boundaries and Data Ownership

**Activate when:** Integrations handle proprietary, personal or regulated content.

**Workflow:** Map legal/data owner, classification, recipient, trust boundary, consent, retention, residency and failure owner.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** No silent data exfiltration or unidentified authoritative source.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I10 — Provider Sandboxes, Stubs and Contract Tests

**Activate when:** Provider integration is costly, slow or unavailable in tests.

**Workflow:** Construct deterministic stub fixtures; verify auth, paging, timeouts, expired tokens, status mapping and drift.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Contract tests run without production dependencies.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I11 — Cross-System Schema Evolution and Mapping

**Activate when:** Schema or business field changes break consumers.

**Workflow:** Version schemas and mapping, classify compatible/breaking changes, handle unknown fields, precision and replay.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Old/new consumers pass migration contract checks.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I12 — Offline Sync and Store-and-Forward

**Activate when:** Browser/mobile software may temporarily lose connectivity.

**Workflow:** Specify local persistence, conflict detection, deduplication, resumable upload and state freshness.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Reconnection does not silently lose or overwrite data.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I13 — Batch Files, EDI and ETL Interfaces

**Activate when:** Data import/export is file-based or periodic.

**Workflow:** Validate encoding, file schema, checksums, partial batches, quarantine and replayable reports.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Invalid rows are isolated and reported; replays are safe.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I14 — Realtime Status and Notifications

**Activate when:** User-facing state depends on streaming data or notifications.

**Workflow:** Define freshness, permissions, subscriptions, retry, backpressure, duplicate suppression and accessibility announcements.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Stale/unknown state is clearly indicated and safely handled.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## I15 — Integration Operations, Monitoring and Runbooks

**Activate when:** Connectors fail in production and need owned recovery.

**Workflow:** Define metrics, alert thresholds, retries, DLQ, reconciliation job, emergency disable and runbook owner.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Recovery has traceable actions and escalation path.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Cross-domain anti-patterns

- Treating a template workflow as the actual product requirement.
- Marking scanner, document, or prompt execution as proof tests passed.
- Performing production mutations to satisfy a command.
- Loading the entire blueprint catalog into one task rather than the relevant headings.

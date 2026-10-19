# Backend Capability Blueprints — domain-specific production behavior

**Use selectively.** Each B-pattern describes a capability and likely failure modes, not a template every project must implement. Preserve existing architecture/approved technology. `webteam-backend` owns service correctness; coordinate with specialist owners on their surfaces. Every blueprint requires actor/tenant trust, state transitions, DTO contract, error contract and tests.

## B01 — User identity and sessions
**Contract:** account identifier, auth assurance, session lifetime/rotation, recovery/revocation, device logout and rate limits. **Adversarial tests:** user enumeration, wrong audience, expired/forged tokens, revoked membership, concurrent password changes. **Avoid:** home-grown token cryptography.

## B02 — Organization / tenant management
**Contract:** tenant context derived from authenticated server facts, membership invite lifecycle, admin transfer and account removal rules. **Tests:** IDOR/BOLA on read/write/export/search and last-admin race. **Avoid:** trust `tenantId` from request body.

## B03 — User permissions and policy evaluation
**Contract:** actor × action × resource × property, policy exception/expiration, deny semantics and delegated admin authority. **Tests:** horizontal/vertical escalation, stale policy cache, simultaneous role revoke. **Avoid:** client-side role checks as security.

## B04 — CRUD with business state machines
**Contract:** allowed status transitions, per-state commands, invariants, version conflicts, audit trail. **Tests:** invalid transition, unauthorized state, conflict under two writers. **Avoid:** one unrestricted PATCH of every field.

## B05 — Search, filters, exports
**Contract:** query syntax, allowlisted sort fields, per-tenant counts, page limits, export scope/expiry, data staleness and PII policy. **Tests:** unauthorized aggregate, huge filter, stable pagination, missing permission. **Avoid:** exporting more than list UI allows.

## B06 — Reports and analytics aggregation
**Contract:** metric formula, event/source, freshness window, timezone, late updates, exact/estimated labeling, privacy scope. **Tests:** grouped tenant isolation, time boundary/DST, duplicate events, empty dataset. **Avoid:** fake 'live' counts.

## B07 — Inventory / reservations / allocations
**Contract:** available count, reservation expiry, atomic allocation, cancellation and idempotent payment/booking effect. **Tests:** racing final unit, double submit, cancellation after commit. **Avoid:** check-then-write without atomicity.

## B08 — Scheduling and calendar
**Contract:** local time vs UTC, timezone database, recurrence, DST gaps/overlaps, overlap policy and participant permissions. **Tests:** conflicting bookings, timezone conversion, expired slot, recurring exception. **Avoid:** treating date string as unambiguous UTC instant.

## B09 — File upload/preview/download
**Contract:** object ownership, size/type safety, quarantine/scanning if needed, retention, signed links, privacy audit. **Tests:** polyglot file, unauthorized retrieval, stale signed link, huge stream. **Avoid:** arbitrary uploads into executable web root.

## B10 — Notifications and messaging
**Contract:** category, recipient/tenant, preference/unsubscribe, template locale, durable event and delivery status. **Tests:** duplicate send after worker crash, denied recipient, provider timeout. **Avoid:** emit email before DB commit without reconciliation.

## B11 — Approval workflows / audit trail
**Contract:** initiator/approver separation, state transitions, immutable evidence vs mutable projections, delegation, expiry. **Tests:** self-approval forbidden, stale status, duplicate approval, tamper resistance. **Avoid:** audit history as editable business row.

## B12 — Payment and subscription state
**Contract:** money as exact decimal/minor units, provider authority, idempotency key, webhook replay/dedupe, ledger/reconciliation. **Tests:** payment succeeds but callback lost, duplicate charge protection, refund concurrency. **Avoid:** interpreting redirect URL as payment proof.

## B13 — External sync/import jobs
**Contract:** cursor/checkpoint, immutable source IDs, conflict ownership, provenance, outbox update and bounded batch. **Tests:** partial batch, duplicate feed, vendor 429, resume checkpoint. **Avoid:** destructive full re-import on every error.

## B14 — Webhooks / inbound events
**Contract:** provider authenticity, signature body semantics, replay window, tenant mapping, durable ACK, DLQ. **Tests:** forged/replay/out-of-order messages. **Avoid:** same-handler long blocking business transaction.

## B15 — Outbound API clients
**Contract:** credentials/scopes, timeout/retry layer, budget, provider error map, request trace. **Tests:** 401/429/503, timeout-after-write, circuit trip/restore. **Avoid:** logging tokens or retrying permanent 4xx.

## B16 — Background workers and scheduled jobs
**Contract:** schedule/trigger, idempotency, lease/lock, concurrency, delay, cancellation, backlog owner. **Tests:** worker lost mid-job, schedule overlap, poison message. **Avoid:** infinite polling.

## B17 — Real-time notifications (SSE/WebSocket)
**Contract:** authenticate connection and channel subscriptions, backpressure, resume offset, token revocation and event order. **Tests:** switch tenant channel, expired auth, reconnect gap. **Avoid:** broadcast all tenants.

## B18 — Feature flags and progressive rollout
**Contract:** flag owner, targeting source, default/fail behavior, client/DB compatibility, retirement. **Tests:** flag OFF/ON, rollout midway during migration. **Avoid:** permanent flags accumulating forever.

## B19 — Configuration and administration
**Contract:** role-scoped settings, sensitive vs public config, versioning and audit, validation before persistence. **Tests:** malicious defaults, privilege change, dynamic reload failure. **Avoid:** editing runtime env files over HTTP.

## B20 — Tenant-safe caching
**Contract:** cache key includes effective principal/tenant/policy constraints; TTL and invalidation; negative caching; encryption where needed. **Tests:** role revoked, tenant switch, stale replica, cold start. **Avoid:** caching protected response under shared public key.

## B21 — Full-text search / indexing
**Contract:** ingestion latency, access filter before or inside index, reindex pipeline, relevance transparency, delete compliance. **Tests:** indexed but now revoked, stale delete, injection-like query and giant regex. **Avoid:** treating search index as security boundary.

## B22 — AI/model-backed API endpoints (only if product needs it)
**Contract:** provider/model allowlist and egress consent, PII classification, request budgets/quotas, prompt-injection threat boundary, retrieval authorization, output validation, timeout/fallback. **Tests:** adversarial retrieved text, tenant leak attempt, provider outage and over-budget refusal. **Avoid:** hidden provider switching and untrusted model output as authorized commands.

## B23 — Account deletion / data export
**Contract:** owner identity verification, legal hold/retention policy, async export delivery, eventual deletion propagation and backups. **Tests:** unauthorized deletion, idempotent repeated requests, partial remote cleanup, revocation during export. **Avoid:** instant 'all copies deleted' promise without evidence.

## B24 — Operations and incident endpoints
**Contract:** liveness vs readiness vs deep diagnostics, safe status, privilege protection, release/drain behavior. **Tests:** dependency outage, secret not reflected, pod termination, alert routing. **Avoid:** unauthenticated internal config dump.

## Required output per used blueprint
`Capability ID · user/business goal · API contracts · permissions/tenant matrix · state transitions · consistency requirements · performance/SLO if specified · failure cases · auth abuse tests · exact backend owners · implementation acceptance tests · rollout/rollback. `

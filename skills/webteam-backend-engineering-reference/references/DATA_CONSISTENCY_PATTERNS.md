# Database consistency and safe evolution recipes

## D1 — Invariant-to-storage mapping
Start from data definitions and business rule, not table naming. For each write list all rows/documents touched, expected isolation, required uniqueness, data owner and observable side effects. Mark application-only vs storage-enforced constraints. Ask `webteam-database` to validate store-specific capabilities. SQLite and MongoDB differ in transaction, indexing and write semantics; do not paste SQL advice unadapted.

## D2 — Concurrent updates
- **Optimistic concurrency:** record a version/timestamp (with correct granularity) and conditionally update; if count=0 return conflict and show reconciliation path. Test two actors reading same version.
- **Atomic invariant updates:** use transaction/constraint/conditional update for balances, inventory, last-admin removal, permission changes and reservations. A check-before-write without atomicity is race-prone.
- **Long-running operations:** never hold DB transaction open during arbitrary network calls; use outbox/saga/compensation where transaction cannot include remote side effect. Compensation is not equivalent to rollback and may be impossible.
- **Isolation:** choose consistency semantics explicitly for replicas, caching, read-your-writes, aggregates and external events. Explain unavoidable staleness.

## D3 — Migration protocol (expand/contract)
1. Inspect deployed app versions, schema, lock behavior, backup and restore evidence.
2. Add backwards-compatible nullable column/index or new collection fields with safe defaults; preserve old readers/writers.
3. Backfill in bounded idempotent batches with checkpointing; measure locks, CPU and write load; no unapproved live runs.
4. Update application reads/writes behind feature or capability detection; test mixed app versions during rolling deployments.
5. Enforce stronger constraints after data validity is demonstrated; remove old fields **only** after all old clients/apps retired and rollback plan revised.
6. Rehearse both forward recovery and backups/restore on disposable environment; identify irreversible boundaries.

## D4 — Idempotency state machine
Recommended conceptual states: `UNSEEN -> IN_PROGRESS -> COMMITTED` (with `FAILED_RETRYABLE`, `FAILED_FINAL`, and defined expiration/cleanup policy). Scope key to actor+operation+payload hash. Lock or compare-and-swap concurrent same-key requests. Persist response metadata or a durable operation resource so timeout-after-commit does not execute twice. A duplicate request must return same logical result or a documented in-progress/conflict response.

## D5 — Query and index performance
- Profile representative cardinality and distribution; inspect EXPLAIN/query plans, sort/filter combinations, hot paths and transaction time.
- Enforce tenant scopes in predicates and cache keys; examine compound-index order and pagination stability.
- Be careful with index maintenance/write amplification and backfill lock duration; set operational budgets.

## D6 — Required tests
Two simultaneous writers, same idempotency key concurrency, commit then connection timeout, transaction rollback on failure, old/new schema app compatibility, realistic restore, cross-tenant aggregate, bulk partial failure, index correctness under query variants.

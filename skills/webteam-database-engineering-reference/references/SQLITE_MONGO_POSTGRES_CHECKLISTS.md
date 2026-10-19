# Datastore-Specific Professional Checklists

## SQLite

- Verify actual `PRAGMA foreign_keys` on **every application connection**; never assume it is enabled universally. Check `PRAGMA foreign_key_check` in a safe copy when relevant.
- Decide WAL vs rollback journal with tested hosting/storage assumptions; WAL readers and writer concurrency are **not** parallel writers, and checkpoint/recovery need consideration.
- Configure `busy_timeout` appropriately, avoid long-lived write transactions, measure contention; distinguish in-memory/dev databases from production durability.
- Use online backup API or correctly coordinated backup technique; test restore with sidecar WAL consistency, not a naked copy of a live file.
- Measure `EXPLAIN QUERY PLAN`, indices and constraints using a representative copy. Verify runtime SQLite version and driver behavior.

## MongoDB

- Model by aggregate boundaries and read/write patterns; embed only bounded cohesive data, reference large/changing/many-to-many data when appropriate.
- Enforce validators, unique indexes and schema versioning; document limitations with nested arrays and multi-key indexes.
- Single-document writes are atomic, but multi-document invariants require deliberate transaction or redesign; confirm replica set/cluster and driver support.
- Design indexes from `explain()` on representative synthetic data; too many indexes increase write cost; inspect TTL/retention and change-stream permissions if used.
- Test cross-tenant reads, aggregation, exports, retries, duplicate webhooks and schema compatibility.

## PostgreSQL (where selected)

- Use normalized constraints and precise types; evaluate isolation and MVCC concurrency for actual invariant, not simply set SERIALIZABLE everywhere.
- RLS is defense in depth, not a replacement for application authorization: check role bypass, table ownership, `FORCE ROW LEVEL SECURITY` and session scoping.
- Create/replace indexes with measured migration-lock and write impact; compare query plans from a disposable representative dataset.
- Test deadlock/serialization retries carefully and ensure retried transaction is safe.
- Verify backup/PITR tooling, replication topology and recovery drills before claiming readiness.

## Selection rule

Keep the selected project datastore and its documented requirements. Do **not** introduce PostgreSQL into an existing SQLite/MongoDB system merely because advanced enterprise examples mention it. The architect and database owner must justify a new engine by access patterns, constraints, ops burden and approved migration scope.

Official documentation: https://www.sqlite.org/pragma.html ; https://www.sqlite.org/wal.html ; https://www.sqlite.org/backup.html ; https://www.mongodb.com/docs/manual/data-modeling/embedding/ ; https://www.postgresql.org/docs/current/mvcc.html

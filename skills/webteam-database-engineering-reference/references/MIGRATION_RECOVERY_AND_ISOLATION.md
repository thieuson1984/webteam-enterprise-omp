# Data Migration, Recovery and Tenant Isolation

## Safe schema change protocol

1. Identify engine/version/deployment, writers/readers, active jobs and mixed-version compatibility.
2. Snapshot test fixtures without PII; establish realistic row/collection counts and index shapes.
3. Plan expand → deploy compatible readers/writers → backfill (batched, resumable, checksummed) → observe → contract later.
4. For critical data define recovery point/time (RPO/RTO) with Product and DevOps; prove backup restore to an isolated target before irreversible steps.
5. Separate schema rollback from data rollback; a reverse DDL cannot restore lost or transformed information.
6. Require independent approval for destructive DDL, cross-tenant movement, production data modification, backup deletion and production operations.

## Concurrency and consistency test matrix

| Fault/event | Expected invariant | Minimum safe test |
|---|---|---|
| Two concurrent creates | unique business key | parallel requests, database unique constraint |
| Read-modify-write conflict | no silent lost update | version/conditional update and conflict response |
| Timeout after commit | retry-safe result | same idempotency key, replay |
| Worker crash after commit | durable processing intent | outbox recovery or appropriate equivalent |
| Mixed app versions | backward-compatible reads/writes | old/new contract fixture |
| Tenant token swap | no cross-tenant leakage | actor × tenant × route negative matrix |
| Restore from backup | consistent accessible state | isolated restore + smoke tests + data counts |

## Security and privacy

Use least-privilege service identities; keep human emergency rights separate. Encrypt sensitive backups and manage keys independently. Document retention, deletion propagation and lawful exceptions as policy decisions, not generic automatic instructions. Never connect an audit command to production credentials without explicit authorization.

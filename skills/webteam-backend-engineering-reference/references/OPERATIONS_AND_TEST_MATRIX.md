# Backend production readiness, SRE and testing matrix

## O1 — Evidence levels
`STATIC_OBSERVED` = code/config reviewed, `TEST_EXECUTED` = actual command+exit/logs, `RUNTIME_OBSERVED` = monitored service with exact environment/time, `NOT_RUN` = not measured, `BLOCKED` = prerequisite absent. Never label security/privacy compliance as certified by this matrix.

## O2 — Coverage by capability
| Capability | Minimal acceptance evidence | Higher-risk verification |
|---|---|---|
| HTTP input/output | status, malformed JSON, schema, content type, over-posting | contract diff, fuzz/property inputs, large payload |
| Authentication | missing/expired credential, cookie flags, issuer/audience | session fixation, OAuth redirect attacks, revocation race |
| Authorization | subject/action/object/property/tenant matrix | cross-tenant lists, aggregate/export/stream access, role change race |
| Persistence | unit + real disposable DB integration, constraint tests | two-writer races, fail mid-transaction, migration rehearsal |
| Async/jobs | retry and dedupe fixture | crash after commit/before ACK, DLQ/replay/access tests |
| Integrations | sandbox status mapping, timeout, 429 | signing key rotation, forged/replayed webhook, cost/effect bound |
| Performance | representative baseline p50/p95/p99 and error rate | sustained load, cache invalidation and CPU/heap profile |
| Observability | redacted request ID, trace/metric sample | PII negative test, alert drill, cardinality audit |
| Operations | readiness/liveness/graceful shutdown, version support | restore drill, incident/tabletop, rolling deploy compatibility |
| Abuse prevention | body/rate/query size caps | tenant-isolation negative testing, SSRF fixture, upload quarantine |

## O3 — SLI/SLO worksheet
- **Critical journey:** e.g. create attendance record, export equipment report, or API authentication; do not invent product journey if not established.
- **SLI:** successful eligible requests / eligible attempts; p95 end-to-end latency; job age, backlog and dedup error; DB saturation. Define windows and exclusions.
- **SLO:** product-approved target and budget; `TBD` until approved/observed. Do not announce '99.9%' based only on code.
- **Alert:** symptom, impact, owner, threshold, runbook link, mute/escalation plan. Favor burn-rate alerts where supported, avoid alerting on random traffic spikes without error impact.

## O4 — Safe telemetry contract
- Use HTTP route **templates** as low-cardinality attributes (`/users/:id`), not full raw paths, emails, user IDs, tenant IDs or bearer tokens in metric label sets.
- Structured logs: timestamp, severity, service/version, request/trace ID, safe operation code, result class and duration. Never include raw Authorization/Cookie headers or sensitive bodies.
- OpenTelemetry JavaScript traces and metrics are stable; logs SDK maturity and semantic conventions must be checked against installed releases. Exporters and sampling can fail: instrument tests should detect missing telemetry.
- Trace an example request across API → DB/outbox → worker with sampling/redaction. Never fabricate traces from intended design.

## O5 — Readiness checklist
- [ ] Supported Node and dependency security policy; lockfile reproducibility and provenance.
- [ ] Database migration expand/contract and restore plan rehearsed or marked NOT_RUN.
- [ ] Secrets injection, permission boundaries, network egress and logging redaction verified.
- [ ] Runtime request/worker concurrency, shutdown and connection pool limits.
- [ ] Real unit/integration/contract/authz/concurrency testing outcomes.
- [ ] Monitored critical journeys and owner-approved SLO; alert/runbook or explicit risk exception.
- [ ] Canary/rollback/forward plan and release owner approval for production changes.
- [ ] No outstanding critical/high risk left unacknowledged by authorized owner.

## O6 — Quality assessment rubric
For each domain assign `PASS_VERIFIED`, `PARTIAL_VERIFIED`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, or `NOT_RUN` with evidence path and confidence. Severity based on user/asset impact and exposure, not number of files. Prioritize correctness/security/data loss above cosmetic lint preferences. A passing CI alone does not prove all tests, access paths or operational readiness.

Sources: https://opentelemetry.io/docs/languages/js/ · https://opentelemetry.io/docs/specs/semconv/http/http-spans/ · https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_mitigate_interaction_failure_limit_retries.html

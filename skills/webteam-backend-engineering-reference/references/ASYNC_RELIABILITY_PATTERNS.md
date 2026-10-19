# Async, integration and failure-tolerant backend patterns

## R1 — Delivery guarantees truth table
| Boundary | Common reality | Required design |
|---|---|---|
| Client → API | Client may retry after lost response | Durable operation ID, idempotency and reconciliation |
| Database → broker | Crash between commit and publish | Transactional outbox if event publication must follow transaction |
| Broker → worker | At-least-once, duplicates and reordered events | Dedupe/inbox, idempotent effects, ordering assumptions recorded |
| Worker → external provider | Timeout may hide completed side effect | Provider idempotency key/read-back reconciliation; no blind replay |
| Incoming webhook | Provider duplicates, delay, replay and burst | Raw-body auth, event ID dedupe, fast durable ACK, bounded workers |
| Long-running job → UI | Progress may be stale or delayed | Explicit status resource, retry/cancel, failure visibility, retention |

Exactly-once *business effect* may be approximated with durable idempotency and transactional boundaries; never promise exactly-once *network delivery* without a proven end-to-end protocol.

## R2 — Timeout/retry budget
- Define per-request deadline; propagate cancellation to downstream HTTP/db calls where possible. Reserve time for cleanup and response.
- Distinguish transient 429/503/network from permanent 400/401/403/validation errors. Retry only where idempotent or safely deduplicated.
- Use **one** retry owner per dependency boundary; exponential backoff with jitter, maximum attempts, maximum elapsed time, 429 Retry-After when relevant. Account for built-in SDK retries so wrapper retries do not multiply.
- Cap queue depth, in-flight concurrency, open connections and payload size; shed load with coherent error handling instead of indefinite buffering.

## R3 — Webhook hardening
1. Look up verified provider docs for signature algorithm and **exact raw bytes** to be signed. Do not invent one algorithm for all providers.
2. Validate event age/timestamp, dedupe event ID, verify tenant/target mapping, store received state and schedule processing durably before ACK as appropriate.
3. Isolate effect execution in idempotent worker; handle at-least-once and out-of-order events.
4. Provide operator replay/poison-message handling with permissions and audit trail; limit retention of raw payloads.
5. Test forged signature, replay, rotated key, provider throttling, duplicate invoices and crash-after-commit.

## R4 — Failure exercises (nonproduction)
- DB commit succeeds; broker enqueue fails; restart attempts delivery.
- Worker processes event and crashes before ACK; event reappears and must not repeat side effect.
- External API request times out after provider accepted write; reconcile first.
- Queue consumer slows to zero: time-in-queue SLI and backpressure alarms work.
- Graceful shutdown on SIGTERM while HTTP requests and workers are active.

## R5 — Exceptions and escalation
If backend cannot prove safe replay, do **not** enable retry or automatic quality-loop replay for mutations. Escalate external money movement, account deletion, billing reconciliation and production recovery to the authorized human.

Sources: https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_mitigate_interaction_failure_limit_retries.html · https://www.rfc-editor.org/rfc/rfc9110

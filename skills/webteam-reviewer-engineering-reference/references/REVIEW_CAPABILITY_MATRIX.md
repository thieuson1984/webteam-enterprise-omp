# Reviewer Capability Matrix

| Surface | Question that can fail | Minimal proof | Mandatory partner when material |
|---|---|---|---|
| Product and domain | Does changed behavior match user intent and state transitions? | REQ/AC + concrete boundary examples | Product |
| Architecture | Is it placed in correct module without expanding coupling? | affected boundary and ADR | Architect |
| Frontend/UX | Does it preserve Design DNA and functional interactions? | screenshot states + actual interaction | Designer/Frontend |
| Accessibility | Can a keyboard and assistive-tech user operate it? | manual keyboard/focus/screen-reader notes | Accessibility |
| Backend/API | Are validation, status/error contracts and compatibility intact? | schema diff + contract tests | Backend/Integration |
| Database | Is migration safe under live data and version overlap? | migration rollback/backfill and synthetic rehearsal | Database/DevOps |
| Security | Are object and tenant permissions checked at server boundary? | negative role tests + threat scenario | Security |
| Reliability | Are duplicate, stale and concurrent events safe? | concurrency/fault tests | Backend/QA |
| Performance | Is p95/p99 or memory worse under comparable load? | baseline and remeasure | Performance |
| Quality | Would tests detect the actual regression? | meaningful assertions + run output | QA |
| Ops | Can this safely deploy, monitor and revert? | health/runbook and approval | DevOps |

Risk C1–C5 influences depth, **not reviewer independence**. A simple lint/comment-only change may use a light review; an auth/financial/data-migration change requires matching specialist assurance. No absence of evidence may be promoted to PASS.

## Review sequence

1. Pin base/head revision; inspect requested diff, full touched units, callers and downstream contracts.
2. Enumerate behavior changes and key counterexamples, preserving existing user changes.
3. Confirm tests and line-level findings with independent evidence.
4. Separate security/domain blockers from style nits and feature suggestions.
5. Re-review only changed fixes plus impacted neighbors; re-run affected checks.

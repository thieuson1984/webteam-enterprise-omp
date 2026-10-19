# Architecture Fitness Functions, Reliability and Evolution

## Representative fitness functions

| Quality driver | Enforceable check | Evidence | Gate/owner |
|---|---|---|---|
| Boundary isolation | import/dependency direction and forbidden cross-module calls | architecture unit tests on actual files | Architect/Reviewer |
| API compatibility | OpenAPI/consumer contract comparison | executed contract tests on old/new schemas | Backend/QA |
| Data migration safety | mixed-version compatibility and repeatable, resumable backfill | disposable DB test, row counts/checksums | Database/QA |
| Tenant isolation | actor×tenant negative test across list/get/update/export | executed authorization matrix | Security/QA |
| Reliability | p95/p99 + failure-mode tests based on agreed journey | measured workload and safe fault injection | DevOps/Performance |
| Deployment safety | rollback or roll-forward, health/readiness and configs | staging drill (not production by default) | DevOps/QA |

## Quality attribute scenario template

`When [stimulus], in [operating condition], [component/user journey] must [measurable response], verified by [method], with [known constraints]`.

No numerical threshold should be invented solely to look enterprise grade. Start with observed baseline or an approved SLO hypothesis.

## ADR template

`Status`, `Context/evidence`, `Business driver`, `Options`, `Decision`, `Tradeoffs and rejected alternatives`, `Security/privacy implications`, `Migration compatibility`, `Cost/operations`, `Fitness test`, `Owner`, `Review/expiry trigger`.

## Failure and release discipline

- Analyze partial failure, retries/idempotency, timeouts, capacity limits and coordinated outages.
- Preserve user-visible behavior before changing boundaries. Split migrations into independently reversible phases.
- A failure injection test should operate on a safe fixture, not on production credentials or third-party systems without authorization.
- An architecture review is not a green light for autonomous deployment or a security certification.

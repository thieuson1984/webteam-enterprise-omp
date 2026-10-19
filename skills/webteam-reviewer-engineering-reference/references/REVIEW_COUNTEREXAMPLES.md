# Counterexample and Regression Playbook

Select only tests that apply. Show expected, actual, test fixture, timing and ownership.

- **Permissions:** cross-tenant resources, deleted/disabled accounts, stale role cache, bulk mutations and IDOR.
- **Transactions:** simultaneous updates, unique conflicts, timeout-after-commit, partial writes, isolation variations and rollback.
- **Messages/webhooks:** duplicate/out-of-order deliveries, missing signature, event version drift, retries and reconciliation.
- **Frontend:** asynchronous stale state, lost focus, screen reader updates, long localized strings, mobile reflow and error recovery.
- **Security/privacy:** log-redaction regression, secrets in telemetry, trust-boundary bypass and unsafe deserialization.
- **API:** removed enum/value, changed nullability, 2xx↔4xx semantics, pagination order, missing cursor and schema evolution.
- **Operational:** deploy with old worker, stale cache, partial rollout, rollback and feature flag disabled state.
- **Testing:** mock asserts its own setup, non-deterministic fixture, baseline auto-accept and pass-at-different-commit.

**Method:** build one plausible minimal counterexample, prefer deterministic local reproduction, request domain specialist verification if unsupported, then stop. No live exploitation or unapproved load/fault injection.

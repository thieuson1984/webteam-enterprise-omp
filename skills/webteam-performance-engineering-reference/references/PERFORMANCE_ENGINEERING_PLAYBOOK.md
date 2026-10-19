# Performance Engineering Playbook — production-grade decision and evidence

**Authoritative scope:** This is reusable technical guidance. It does not override project architecture, approved model/tool policies, or live OMP capabilities. Read the relevant subsection only. Separate `MEASURED`, `OBSERVED`, `INFERRED`, `NOT_RUN`, and `NOT_APPLICABLE`.

## Standards and evidence provenance

- [Web Vitals](https://web.dev/articles/vitals)
- [React Compiler](https://react.dev/learn/react-compiler/introduction)
- [OpenTelemetry JavaScript status](https://opentelemetry.io/docs/languages/js/)
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Measurement-first performance engineering protocol

### Metric definitions and source of truth

Core Web Vitals field targets currently described by web.dev: LCP <=2.5 s, INP <=200 ms, CLS <=0.1 at p75, segmented by mobile/desktop. A Lighthouse lab score is not field evidence. Lab protocol must pin hardware/emulation, browser, network, cold/warm cache, fixtures and repeat count. For API and jobs distinguish p50/p95/p99, throughput, error rate, queue lag, resource saturation and test sample uncertainty.

```text
Journey: create invoice with 1,000-item account
Environment: staging mirror, fixed commit/seed, controlled synthetic tenants
Profile: N simultaneous users, rising stages + pause + recovery
Measure: end-to-end duration p50/p95/p99, API latency, DB query time,
         worker lag, CPU, memory, error rate, correctness checks
Stop: explicit time/traffic ceiling, error threshold, owner approval
```

### Performance attribution

Start with a real slow journey and response-time decomposition: DNS/TLS/edge, TTFB, service auth/serialization, DB, downstream, client bundle, input handling, layout/paint. Verify where time goes before changing code. A cache should have an explicit authorized-data key, invalidation plan and correctness test. Database indexes require representative cardinality plus write/load tradeoff and DBA approval.

### Browser optimization protocol

Measure LCP resource or critical paint path, long tasks and INP attribution. Check bundle transfer/execution, images/font loading, hydration timing, event work, layout thrashing and CLS causes. Lazy-load non-critical routes/resources where justified but never lazily defer the true LCP element. Profile React/Solid components before memoization or virtualization. Protect focus/keyboard and actual product behavior in every comparison.

### Load and capacity testing boundary

Only execute bounded load or soak tests in explicitly approved safe environments. Get capacity and rate authorization; stop on SLA degradation or unanticipated side effects. Avoid striking production or third-party endpoints. No made-up simulation output: if a tool is missing, document the exact repeatable test plan instead.

### Observability maturity

Use supported OTel JS instrumentation where appropriate: tracing and metrics have stable components; logs are development status and browser instrumentation is experimental per official JS documentation. Mark those limitations. Correlate traces and metrics using high-cardinality controls and redaction; quantify instrumentation overhead before adopting broadly.

### Success proof

A fix passes only with matched before/after tests, preserved business correctness and security constraints, repeatable measurements, documented tradeoffs and rollback. Do not reduce server validation, request authentication, tenant scoping, data freshness or error handling for faster benchmarks.


## Reversible implementation workflow

1. Baseline real behavior / establish a precise gap and target outcome.
2. Record ownership, existing user changes, touched files, anticipated data/security effects and approvals.
3. Compare at least one simpler alternative and explicitly reject unnecessary infrastructure, tool purchases, new packages or frameworks.
4. Make the smallest authorized local change with a single implementation owner; avoid concurrent edits to shared files.
5. Run real tests, capture outputs, check privacy/accessibility/business semantics and compare objective before/after evidence.
6. Request independent QA/reviewer verification proportionate to risk; escalate unknowns, blocking approvals or production effects.
7. Report residual issues, updated contract/docs, evidence links and rollback. Never falsely label tests, scans, monitoring or deployments as completed.

## State and uncertainty labels

| Status | What it means |
|---|---|
| `OBSERVED` | Verified in source or direct tool output, with path/version or artifact ID |
| `MEASURED` | Actual run using documented environment, inputs and method |
| `INFERRED` | Reasoned hypothesis not yet independently demonstrated |
| `NOT_RUN` | Relevant test or measurement omitted, with explicit reason |
| `BLOCKED` | Missing tool/permission/environment/decision |
| `NOT_APPLICABLE` | Excluded because the real project has no such surface |

## Cross-agent handoff

Lead: `webteam-performance`. Partners only when justified: webteam-frontend (rendering), webteam-backend (API), webteam-database (query plan), webteam-architect (system design), webteam-devops (infra budgets), webteam-qa (repeatable regression). No tool or reference grants production access; do not send project data to new providers without authorization.

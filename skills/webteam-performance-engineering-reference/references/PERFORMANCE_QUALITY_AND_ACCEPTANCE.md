# Performance Quality & Acceptance Matrices

Map requirements and accepted risk to tests. Execute only within authorized repository and environments. **No unsupported claim of security certification, accessibility compliance, speed improvement or production readiness.**

| Quality surface | Failure case to verify | Evidence-producing method | Owner(s) |
|---|---|---|---|
| Web Vitals | LCP/INP/CLS regression by cohort | RUM p75 when available, otherwise labeled lab | Performance/Frontend |
| Interaction | Long tasks, render thrash, slow event | Browser profile at fixed device | Performance/Frontend |
| Bundle/assets | Huge chunk, bad cache headers, image priority | Build analyzer + controlled waterfall | Performance/Frontend/DevOps |
| Client memory | Subscriptions, detached DOM, timers | Heap snapshots across repeat navigation | Performance/Frontend |
| API latency | p95/p99, error and throughput mismatch | Trace breakdown + staged load | Performance/Backend |
| Database | Query plan, lock/pool saturation | Controlled EXPLAIN & realistic fixtures | Performance/Database |
| Caching | Stale data, cross-tenant key, stampede | Cold/warm + authorization negative test | Performance/Security/Backend |
| Capacity | Burst, overload, queue lag, recovery | Authorized rate-bounded load/soak | Performance/DevOps/QA |

## Finding / remediation record template

```yaml
id: "<domain>-001"
status: observed | inferred | not_tested | not_applicable | blocked
severity: blocker | high | medium | low | improvement
confidence: high | medium | low
source: "path:line or tool run artifact"
impact: "specific user, privacy or system behavior"
reproduction: "safe steps + environment; never paste secrets"
root_cause: "reasoned root cause vs symptom"
proposal: "minimal option, alternative and tradeoff"
owner: "one authorized agent"
verification: "test, inputs, actual result, remaining gap"
rollback: "reversal of changes and data considerations"
approval: "not needed | pending | explicit owner and decision"
```

## Severity and fix governance

- `BLOCKER`: confirmed exposed exploit or loss/corruption of critical data/service; immediately escalate to user and Security/DevOps; no unattended fix.
- `HIGH`: significant reproducible security/business/availability impact; independent approval/review before sensitive rollout.
- `MEDIUM`: bounded issue with reproducible effect; plan controlled remediation, explicit test and review.
- `LOW`: local reversible non-sensitive defect, eligible for bounded `fix` only when user requested it.
- `IMPROVEMENT`: maintainability/usability/perf opportunity; no fabricated severity or automatic rewrite.
- Findings without sufficient evidence are hypotheses; severity depends on actual context, not labels alone.

## Definition of done

- [ ] Scope and applicable dimensions reconciled with real code and approved user goal.
- [ ] Findings have exact evidence source and no exposed secrets.
- [ ] Baselines/negative test cases are reproducible and actual test status disclosed.
- [ ] No permissions, cloud/production state, model costs, design DNA or public contracts changed outside approval.
- [ ] Rollback, residual risk, independent reviewer and QA outcome documented.

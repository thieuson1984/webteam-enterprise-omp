# Security Quality & Acceptance Matrices

Map requirements and accepted risk to tests. Execute only within authorized repository and environments. **No unsupported claim of security certification, accessibility compliance, speed improvement or production readiness.**

| Quality surface | Failure case to verify | Evidence-producing method | Owner(s) |
|---|---|---|---|
| Access control | Cross-role, object, property, tenant, export | Automated synthetic negative auth tests | Security/Backend/QA |
| Authentication | Fixation, reset link replay, logout invalidation | Controlled session lifecycle integration | Security/Backend/QA |
| Injection | HTML/SQL/NoSQL/URL trust boundaries | Parameterized/sanitized sink tests | Security/Frontend/Backend |
| Business abuse | Replays, quota bypass, enumeration, SSRF | Local abuse-case fixtures | Security/Backend/Product |
| Supply chain | Unpinned change, vulnerable transitive dep | SCA/SBOM + evaluated reachability | Security/DevOps |
| Privacy & logs | PII/secrets leaks, retention violations | Synthetic events + sampling/redaction audit | Security/Database/DevOps |
| Tools/agents | Untrusted prompt via repo/MCP/web, exfil | Benign prompt-injection fixture + permission check | Security/Orchestrator |
| Incident readiness | Revocation, backup integrity, containment | Staging tabletop; approvals required | Security/DevOps/Reviewer |

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

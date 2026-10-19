# Reviewer finding and decision standard

## Scope declaration
Repository, branch/commit, base/head, changed files, task requirements, inspected call chains, running tests and exclusions. Treat unstaged/untracked changes as user-owned. Worktree must remain unmodified in read-only modes.

## Findings
```
ID: RV-001
Disposition: CONFIRMED | LIKELY | HYPOTHESIS | PREFERENCE
Severity: CRITICAL | HIGH | MEDIUM | LOW | NIT
Confidence: HIGH | MEDIUM | LOW
Location: path:line (verified at reviewed revision)
Claim: specific incorrect behavior
Trigger: minimal feasible scenario
Evidence: code + executed test/trace if any
Impact: affected users/data/security/reliability
Fix: smallest safe change; code owner
Verify: deterministic test or observation
Dependencies: specialist review/approval
```

Only material confirmed or strong likely defects block; hypotheses prompt targeted verification; preferences never block. Critical security issues require Security specialist and responsible human decision; reviewer cannot unilaterally deploy or waive controls. Findings must survive counterexample review. Deduplicate by root cause. Assign risk weighting based on the project's documented criticality, not invented probabilities.

## Final verdict
- PASS: inspected scope is acceptable and required evidence is present; list residual accepted risks.
- CHANGES_REQUESTED: blocking findings remain, each evidenced.
- UNVERIFIED: material evidence or independent reviewer unavailable.
- BLOCKED: permission, source, tests or required approvals prevent assessment.

Independent review means separate author/reviewer role and unaltered code; same underlying model may not supply strong independence. Record actual model/provider if verified, otherwise state unknown. Never approve own code.

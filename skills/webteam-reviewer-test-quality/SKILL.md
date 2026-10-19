---
name: webteam-reviewer-test-quality
description: "Test Adequacy and Evidence Review for risk-calibrated independent WebTeam change review"
---

# Test Adequacy and Evidence Review

## Activate
Load this skill only when a current diff, requested review, or project risk implicates: tests as reliable observations, not declarations. Do not auto-load every Reviewer skill. The reviewer has no code-write authority by default and must never claim to be independent when reviewing its own authored output.

## Procedure
1. Confirm authorized repository, effective project policy, exact source revision, base revision, scope and user acceptance criteria. Preserve working-tree changes.
2. Acquire relevant code, call sites, requirements and test evidence, avoiding unrelated repositories or confidential exports.
3. Build acceptance-to-test traceability; inspect assertion strength, fixtures, isolation, flaky conditions, negative cases, unauthorized access, failure injection and mocks; distinguish test source from executed test result; do not change snapshot baselines to silence failures.
4. Validate each suspected bug against actual reachable behavior; mark unreproduced paths as hypotheses, not proven defects.
5. Rank findings by impact and realistic likelihood; avoid style-only blocking comments. Require exact path/line when inspected, otherwise label location unverified.
6. Hand remediation to a distinct owning implementer; send serious uncertainty to the appropriate domain agent; do not silently edit, execute untrusted scripts or authorize production actions.
7. Re-evaluate only the changed evidence after remediation and give an honest verdict.

## Output contract
Coverage gaps by risk; commands actually run, exit codes and limitations.

For every blocking finding include **ID, severity, confidence, file/line, observed code fact, triggering scenario, user/business impact, minimal fix, verification method and reviewer status**. Report what was not inspected and what tests were not run. Do not infer proof from a tool description.

## Failure modes
Equating passing CI with complete correctness, inventing coverage from file names.

## References
Google Engineering Practices code review standards; OWASP Code Review Guide for relevant security cases. Use project policies and current documented standards first. Optional local checklists are loaded on demand.

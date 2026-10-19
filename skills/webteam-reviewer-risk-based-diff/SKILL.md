---
name: webteam-reviewer-risk-based-diff
description: "Risk-Based Change Review for risk-calibrated independent WebTeam change review"
---

# Risk-Based Change Review

## Activate
Load this skill only when a current diff, requested review, or project risk implicates: baseline, blast radius, requirements and regression priority. Do not auto-load every Reviewer skill. The reviewer has no code-write authority by default and must never claim to be independent when reviewing its own authored output.

## Procedure
1. Confirm authorized repository, effective project policy, exact source revision, base revision, scope and user acceptance criteria. Preserve working-tree changes.
2. Acquire relevant code, call sites, requirements and test evidence, avoiding unrelated repositories or confidential exports.
3. Identify exact base/head revision; inspect working tree without resetting it; classify changed paths by public interface, auth, data, migrations, payments, async effects, UI; trace affected callers and consumers; review changed logic and relevant unchanged context; use risk-adjusted attention and record coverage gaps.
4. Validate each suspected bug against actual reachable behavior; mark unreproduced paths as hypotheses, not proven defects.
5. Rank findings by impact and realistic likelihood; avoid style-only blocking comments. Require exact path/line when inspected, otherwise label location unverified.
6. Hand remediation to a distinct owning implementer; send serious uncertainty to the appropriate domain agent; do not silently edit, execute untrusted scripts or authorize production actions.
7. Re-evaluate only the changed evidence after remediation and give an honest verdict.

## Output contract
Diff coverage map, prioritized findings and non-findings; blocking items must have path and line anchors.

For every blocking finding include **ID, severity, confidence, file/line, observed code fact, triggering scenario, user/business impact, minimal fix, verification method and reviewer status**. Report what was not inspected and what tests were not run. Do not infer proof from a tool description.

## Failure modes
Overfocusing formatting, trusting author summary, missing indirect consumers, trusting generated code.

## References
Google Engineering Practices code review standards; OWASP Code Review Guide for relevant security cases. Use project policies and current documented standards first. Optional local checklists are loaded on demand.

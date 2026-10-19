# Evidence-led product discovery and delivery

## First principles

Begin from who experiences the problem, what task fails today, its frequency/severity and the desired behavioral outcome. Record evidence provenance, sampling bias, persona/permissions, current workaround, constraints and ethical data handling. Separate validated fact from inference. Avoid inventing personas, interview findings or product metrics. Prioritize the least expensive observation or experiment capable of invalidating a costly assumption. Decompose requirements into requirement IDs, measurable acceptance conditions and negative paths before roadmap commitments. Product owns intent and problem fit, not infrastructure choices.

## Decision evidence matrix

| Field | Required content |
|---|---|
| Scope & revision | Actual project root, Git revision, relevant service/data boundaries |
| Stakeholder/user journey | Confirmed actors, goals, permissions and failure impact |
| Invariants/quality | Measurable or testable requirements, explicit unknowns |
| Alternatives | At least a lowest-complexity viable option when consequential |
| Evidence | Real source lines, test command/result, dated source, or labeled assumption |
| Tradeoffs | Delivery cost, learning/coupling risk, security/privacy, operational load |
| Verification | Test, measurement or experiment that can falsify proposal |
| Release/change control | Owner, reversibility, approval requirement and rollout strategy |

## Reusable completion checklist

- Confirm the problem definition and in-scope actors before solutioning.
- Verify engine/framework capabilities in the installed runtime; never invent a release-specific feature.
- Map at least one happy path and one negative, concurrent or failure path.
- State what has not been tested; a file existing is not evidence of a working system.
- Do not change live data, access policy, payment or production deployment without explicit authorization.
- Communicate the smallest reversible next step and the owner of each open risk.

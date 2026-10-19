# Architecture decision and quality drivers

## First principles

Maintain AS-IS grounded in repo and measured traffic where available; derive architecture drivers from business needs and ISO 25010 quality scenarios. Describe candidate designs, excluded alternatives, fit for team operations, explicit trust boundaries, data ownership, failure assumptions, dependencies and architecture fitness functions. Prefer a modular monolith over unearned service decomposition. Record decisions and their reversal triggers; architectural preferences without measurable drivers are hypotheses, not mandatory standards.

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

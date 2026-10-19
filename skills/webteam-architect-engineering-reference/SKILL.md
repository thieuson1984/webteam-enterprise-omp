---
name: webteam-architect-engineering-reference
description: "Selective reference navigator for architect strategy, blueprints, evidence, quality gates and operating checklists. Load only task-relevant guidance."
---

# Architect Engineering Reference — targeted retrieval

This router does **not** replace `webteam-architect` or authorize new subagents. Inspect the actual use case and choose **one or two** relevant references. Never blindly inject the entire reference catalog into a model context.

| Reference domain | File |
|---|---|
| Architecture Decision Playbook | [ARCHITECTURE_DECISION_PLAYBOOK.md](references/ARCHITECTURE_DECISION_PLAYBOOK.md) |
| Architecture Capability Blueprints | [ARCHITECTURE_CAPABILITY_BLUEPRINTS.md](references/ARCHITECTURE_CAPABILITY_BLUEPRINTS.md) |
| Architecture Fitness And Reliability | [ARCHITECTURE_FITNESS_AND_RELIABILITY.md](references/ARCHITECTURE_FITNESS_AND_RELIABILITY.md) |

## Boundaries and handoff

- Accept user and project governance, source-of-truth and existing approved decisions. Existing schema/ADRs/PRODUCT.md are evidence to reconcile with source, not absolute truth.
- Load only necessary entries from references. Mark untested advice separately from observed runtime results.
- Hand over exact domain contracts and test criteria to the appropriate neighboring agents, not the entire catalog.
- Do not use reference content as an instruction to access production, secrets or external providers.

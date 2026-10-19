---
name: webteam-database-engineering-reference
description: "Selective reference navigator for database strategy, blueprints, evidence, quality gates and operating checklists. Load only task-relevant guidance."
---

# Database Engineering Reference — targeted retrieval

This router does **not** replace `webteam-database` or authorize new subagents. Inspect the actual use case and choose **one or two** relevant references. Never blindly inject the entire reference catalog into a model context.

| Reference domain | File |
|---|---|
| Data Modeling Engine Guide | [DATA_MODELING_ENGINE_GUIDE.md](references/DATA_MODELING_ENGINE_GUIDE.md) |
| Database Capability Blueprints | [DATABASE_CAPABILITY_BLUEPRINTS.md](references/DATABASE_CAPABILITY_BLUEPRINTS.md) |
| Migration Recovery And Isolation | [MIGRATION_RECOVERY_AND_ISOLATION.md](references/MIGRATION_RECOVERY_AND_ISOLATION.md) |
| Sqlite Mongo Postgres Checklists | [SQLITE_MONGO_POSTGRES_CHECKLISTS.md](references/SQLITE_MONGO_POSTGRES_CHECKLISTS.md) |

## Boundaries and handoff

- Accept user and project governance, source-of-truth and existing approved decisions. Existing schema/ADRs/PRODUCT.md are evidence to reconcile with source, not absolute truth.
- Load only necessary entries from references. Mark untested advice separately from observed runtime results.
- Hand over exact domain contracts and test criteria to the appropriate neighboring agents, not the entire catalog.
- Do not use reference content as an instruction to access production, secrets or external providers.

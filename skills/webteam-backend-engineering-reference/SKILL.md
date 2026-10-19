---
name: webteam-backend-engineering-reference
description: "Load just the relevant evidence-based backend recipe catalog: API contracts, security abuse cases, consistency, asynchronous delivery, capability blueprints, Fastify/Node details, and operational tests."
---

# Backend Engineering Reference Library (selective loading)

## Purpose
This is a **reference router**, not an additional backend implementation role. `webteam-backend` coordinates with the existing `webteam-database`, `webteam-security`, `webteam-integration`, `webteam-performance`, `webteam-devops`, `webteam-qa` and `webteam-architect` as required. Select ONE or TWO task-relevant documents; never autoload the entire library by default.

| Problem | Reference |
|---|---|
| HTTP API schemas, errors, pagination, versioning | [API contracts](references/API_CONTRACT_PLAYBOOK.md) |
| Permissions, tokens, tenant isolation, attack paths | [Security cases](references/SECURITY_ABUSE_CASES.md) |
| Transactions, migrations, data conflict | [Data consistency](references/DATA_CONSISTENCY_PATTERNS.md) |
| Queues, idempotency, retries, webhooks | [Async reliability](references/ASYNC_RELIABILITY_PATTERNS.md) |
| Special backend feature types | [Capability blueprints](references/BACKEND_CAPABILITY_BLUEPRINTS.md) |
| Fastify/TypeScript runtime pitfalls | [Fastify recipes](references/FASTIFY_NODE_RECIPES.md) |
| Operational acceptance and test evidence | [Operations & testing](references/OPERATIONS_AND_TEST_MATRIX.md) |

## Activation and control
Use after identifying the task type, source boundaries, storage model, active runtime version and approved project scope. Sources are reviewed guidance, not runnable recipes or automatically enforced security policy. All high-risk recommendations require test evidence and appropriate owner approval. If a user asks for a different language/framework, adapt the principles without imposing Node/Fastify.

## Output contract
Provide precise affected paths/contracts, assumptions, constraints, owner handoffs, risk and verification; no gratuitous new infrastructure or skills. Never claim a static recipe has been implemented or tested.

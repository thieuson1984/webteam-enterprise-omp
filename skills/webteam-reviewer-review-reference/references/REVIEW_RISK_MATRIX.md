# Risk-focused review matrix

| Change surface | Must inspect | Specialist |
|---|---|---|
| Identity, tenant policy, secrets | object-level checks, negative tests, logs | Security |
| API and typed schema | consumer compatibility, validation and errors | Backend |
| Schema, index, migration | live-version safety, rollback and integrity | Database |
| Async jobs, payment, side effects | retries, idempotency, ordering, partial failures | Backend + Integration |
| UI navigation, forms, design tokens | interaction states, browser regression, accessibility | Designer + Accessibility + QA |
| Caching, queries and concurrency | correctness and baseline load measurement | Performance |
| Deployment/config | secrets, rollback, rollout, health | DevOps |
| Product semantics | accepted user stories, requirements and metrics | Product |

## Review budget
C1 trivial scope: author self-check may suffice when policy permits. C2 low-risk: lightweight diff inspection. C3: one independent Reviewer pass. C4: one independent Reviewer plus needed domain specialist. C5: independent Reviewer and Security/QA or relevant specialists with explicit risk owner. Review is not automatic multi-model council. One bounded re-review after fix; further loops require reason and approval. Never run multiple reviewers on the same diff without a distinct mandate.

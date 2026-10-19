# Failure Handling, Approval and Budget

- **Approval boundary:** model/provider egress, external network, untrusted script execution, production deploy, data migration, credential access, purchases, changing brand direction and global skill/memory promotion. No slash command or headless subagent may grant these implicitly.
- **Failure classes:** ordinary deterministic failure, model/tool incompatibility, transient rate limit, blocked access, uncertain side effect, provider outage, failed test or inconsistent child results. Choose remedy by class.
- **Idempotent retries:** after uncertain write, reconcile actual state and idempotency key first. Never replay non-idempotent action because response was lost.
- **Budget:** task-wide shared caps across all agents, deliberate model council, provider fallback, native/custom loop, test reruns and prompts. Escalate before overruns. Do not assume higher effort or more agents always improves correctness.
- **Escalation brief:** concise evidence, impact, tried options, recommendation, reversible alternatives, required decision and cost. If user does not approve, stop without silently changing plans.
- **Stop conditions:** no authority, unknown external side effect, critical test blocked, two ineffective hypotheses, failed dependency, conflicting requirements, leaked secret risk, overlapping writers, insufficient independent verification.

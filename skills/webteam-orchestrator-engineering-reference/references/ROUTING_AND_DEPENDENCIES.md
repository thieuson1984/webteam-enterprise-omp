# Routing, Capability and DAG Playbook

1. **Preflight:** OMP version/profile, source root, closest `.omp` directory, `task` tool, discoverable agents, effective spawns and recursion depth, tool policy, actual model roles. Do not assume a nested orchestrator agent can delegate.
2. **Classify:** C1 trivial (MAIN-only often appropriate); C2 local (one domain owner); C3 medium (owner + QA/Reviewer as needed); C4 cross-domain (DAG + independent checks); C5 high stakes (explicit approval + multiple specialized gates).
3. **Pick minimum expert set:** Project constraints and changed surfaces determine selected agents. Never fan out to all 16 merely for appearances. Allow domain specialist skip only with reason.
4. **Task DAG:** define node ID, dependencies, owner, writer paths, output contract, safe read tools, accepted proof, token/cost cap, stop and rollback condition.
5. **Batch:** only disjoint read-only tasks or isolated writers. Defer integration and review until actual child completion and source revisions have reconciled.
6. **Topology fallback:** if `MAIN → webteam-orchestrator → specialist` is blocked by effective spawn/depth/tools, MAIN performs orchestration and dispatches verified specialists directly; no recursive workaround or implicit security enlargement.
7. **Reconcile:** check interface assumptions across Product/Architect/Database/Backend/Frontend/Integration before release; update canonical requirement and evidence ledger once.

One writer per file/worktree. Reviewers never approve their own changes. Every provider and MCP side effect requires actual runtime permission and user authorization.

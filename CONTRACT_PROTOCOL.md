# WebTeam Structured Contract Protocol v1

Opt-in protocol for typed WebTeam handoffs. It changes **how** work is assigned and verified, not
the 16-agent roster, model roles, fallbacks, memory or tool authorization.

## Artifacts

- `.omp/contracts/schemas/`: `task.v1`, `result.v1`, `result.omp`, `verification.v1`, `review.v1`.
- `.omp/contracts/tools/validate_contracts.py`: schema + handoff + canonical digest.
- `.omp/contracts/tools/verify_artifact_links.py`: cross-field digest/revision/evidence links.
- `.omp/contracts/governance/state_machine.json`: transition guards (policy, not an extension).
- Agent and command files contain an **opt-in** contract-handoff/preflight section.

## Flow

1. **Plan:** Orchestrator freezes objective, AC IDs, scope, revision, dependencies and budget.
2. **Preflight:** validate the Task Contract and recompute its canonical SHA-256; compare
   `source.repo_revision` with `git rev-parse HEAD`; reject identity/scope/dependency mismatch.
3. **Dispatch:** native OMP `task` with the complete `outputSchema` **object** and
   `schemaMode: "strict"`. A read-only task needs an enforced read-only runtime, not a prompt claim.
4. **Result:** the child returns `webteam.result.v1` (or `verification.v1`/`review.v1`) with exact
   task ID, input digest, revision, real `path:line` evidence and `NOT_RUN` for unexecuted tests.
5. **Verify:** local schema/handoff/cross-field checks, then independent QA and Reviewer.
6. **Accept:** only the Orchestrator/human gate may accept; a schema PASS and
   `SUBMITTED_FOR_VERIFY` are not acceptance.

## Hard stops

Wrong task ID/agent/digest/revision; path outside scope; `READ_ONLY` with changed paths; `PASS`
without evidence; missing/duplicate acceptance IDs; unresolvable evidence; unresolved CRITICAL/HIGH
blocker; unapproved external side effect; uncertain replay of a side effect.

## Limits

- A canonical digest is an integrity check, not a signature; an actor who can rewrite both task
  and result defeats it.
- Schema validation is syntactic. Business correctness needs source inspection, tests and
  independent review.
- Command files are prompt expansions, not enforcement. Put enforceable gates in the dispatcher,
  validator or CI.
- Tool lists restrict built-ins, not an OS sandbox.

## Rollback

- **Project/source install:** restore modified files from the P13 migration backup recorded in
  `SOURCE_MIGRATION_REPORT.md`.
- **Live installed agent directory:** restore the 23 agent/command files from the P14
  pre-deployment backup recorded in `P14_DEPLOYMENT_REPORT.md`, and remove the added
  `~/.omp/agent/CONTRACT_PROTOCOL.md`. Do not delete unrelated agents/commands, `config.yml`,
  `AGENTS.md`, memory/session data or the codebase-memory agents.
- Never use destructive Git reset/clean.

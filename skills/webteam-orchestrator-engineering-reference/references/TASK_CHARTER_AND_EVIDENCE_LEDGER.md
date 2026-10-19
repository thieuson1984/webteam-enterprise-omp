# Task Charter and Evidence Ledger

## Charter

`TASK-ID`, user outcome, known requirements and confirmed authority, repo revision/dirty state, in-scope/out-of-scope, selected skills, risk C1–C5, owner/reviewer, task DAG, allowed providers/model/effort, tool/net/write limits, budget, acceptance gates, expected artifact, failure/stop condition.

## Child handoff envelope

A short context packet with exact target files, project docs/ADRs, requirements, ownership, sensitive-data restrictions, timeouts, maximum attempts, test selection and evidence format. Avoid forwarding transcript dumps or requiring another full repository index. Assign exactly one writer per file.

## Evidence ledger

| Node | Owner | Revision | Observed result | Checks actually run | Reviewer | Decision/approval | Remaining risk |
|---|---|---|---|---|---|---|---|

Statuses: `NOT_STARTED`, `RUNNING`, `BLOCKED`, `FAILED`, `PASS_VERIFIED`, `UNVERIFIED`. A subagent saying "completed" is not enough; record the diff, outputs and tests at matching revision. Unknown or blocked items are not silently removed after compaction.

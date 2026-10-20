# WebTeam rollout instructions — paste into an authorized OMP pilot session

You are operating an existing WebTeam installation. Implement a **phased contract-first communication pilot**, NOT a full team reinstall.

Constraints:
- Never modify global OMP config via `omp config set` during the pilot. Use verified project-local overlay/profile.
- Before any write: inspect exact active OMP version, current working directory, config scope, installed agents, skills, tools, task topology and agent permission policies. Back up target files. Treat existing user files as authoritative; do not overwrite without reviewing diffs.
- Read `ANALYSIS_VI.md`, `IMPLEMENTATION_GUIDE_VI.md`, `schemas/`, `governance/state_machine.json`, and test fixtures from the local WebTeam Contract Protocol starter kit at the user-specified accessible path.
- First run the deterministic validator suite. If it fails, report the findings and stop.
- Initially pilot only with `webteam-orchestrator`, `webteam-backend`, `webteam-qa`, `webteam-reviewer`, using synthetic non-sensitive read-only tasks; do not modify any other agent. Prefer main-session direct delegation if nesting is not supported.
- For each pilot subagent dispatch, validate the task envelope BEFORE `task`; use strict native `outputSchema` only if the active OMP exposes and supports it. Verify the actual structured-output validation status, not the existence of any artifact.
- After completion, validate canonical result schema, identity, digest, repo revision, allowed paths, ACs and test evidence. Require truly independent QA/Reviewer checks before Orchestrator accepts the task.
- Never allow an agent to mark its own change ACCEPTED. Never retry external side effects blindly or broaden providers, tools or approval modes to make a smoke test pass.
- Gather observed metrics (time/tokens when available, valid output ratio, misunderstanding rework, false completion, out-of-scope edits), compare to baseline and write a redacted pilot report. Missing data is UNVERIFIED, never estimated PASS.
- Stop after the 4-agent pilot and provide a go/no-go assessment. Do **not** roll out to the other 12 agents without explicit approval for the next stage.

Required deliverables:
1. Effective configuration/topology evidence and pre-change backups.
2. Task/Result/Review/Verification schema test results and failed-case reproduction.
3. At least one native `task` call observed or an explicit BLOCKED reason.
4. An honest, redacted `results/pilot-evaluation.md` and prioritized corrections.
5. Proposed changes for the next rollout stage, with cost, data boundaries and rollback plan.

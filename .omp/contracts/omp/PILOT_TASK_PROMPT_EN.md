# Paste into the running OMP *pilot session* (after setup); do not run against production.

Run one **read-only** native `task` delegation to `webteam-backend` using the real OMP tool available in this session. Use a validated synthetic task contract supplied below or load `.omp/contracts/examples/task.valid.json` after confirming the path is mounted and accessible. The goal is a native structured-output smoke test, not implementation.

Mandatory checks before dispatch:
1. Confirm current working directory and active effective `task.structured`/`task.batch` config. If not supported or unavailable, stop and report.
2. Confirm `webteam-backend` exact agent name is discoverable, is permitted by spawn policy, and can complete a read-only task. Confirm model/provider route and effective child tools; do not raise privileges.
3. Compute/verify `input_sha256` with `python3 .omp/contracts/tools/validate_contracts.py hash --file .omp/contracts/examples/task.valid.json`. Do not guess or fabricate SHA-256.
4. Keep this test synthetic. No repository edits, network calls, credentials, account operations or third-party side effects.
5. If the native tool is batch mode, provide the required non-empty `context` and one `tasks[]` item. Each item must include `agent`, `task`, `solutionSpace`, `schemaMode: strict`, and `outputSchema` **as the JSON object** read from `.omp/contracts/schemas/result.omp.schema.json` (not as a file path string). If flat mode is active, use its verified flat shape instead.
6. Ask the agent to return all Result Envelope fields. It must use `SUBMITTED_FOR_VERIFY` at most, not `ACCEPTED`; for unexecuted checks, use `NOT_RUN`; if insufficient context, use `NEEDS_CLARIFICATION`.
7. Inspect the actual task result: agent ID, status, resolved model if available, structured validation status, and saved artifact. Never infer validation success from `.json` existence. Do not mark a passed OMP call as semantically verified.
8. Save a redacted local pilot report including exact OMP/tool observations, timing/tokens when available, output schema validation, code validator result and next action. Avoid copying user or repository secrets.

After the result is written to a local JSON file, run:
`python3 .omp/contracts/tools/validate_contracts.py handoff --task .omp/contracts/examples/task.valid.json --result <actual-result.json>`

Do not auto-fix a failing strict schema by expanding tools or altering provider routing. Report failure and do not broaden rollout until resolved.

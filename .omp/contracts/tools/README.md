# WebTeam contract tools

`validate_contracts.py` — canonical schema and handoff checks:
`check`, `hash`, `handoff`, `suite`. It validates JSON Schema, task/result identity, canonical
SHA-256, READ_ONLY scope, acceptance IDs and declared test evidence. It does **not** execute tests
or prove semantic correctness.

`verify_artifact_links.py` — cross-field links the schema-only check omits:
verification/result digests, observed revision, checked acceptance IDs, `VERIFIED` preconditions and
resolvable `path:line` evidence in verification/review artifacts.

Requirements: Python 3 and `jsonschema` (`requirements.txt`). Run from the repository root:

```bash
python3 .omp/contracts/tools/validate_contracts.py suite
python3 .omp/contracts/tools/validate_contracts.py check --kind result --file <result.json>
python3 .omp/contracts/tools/validate_contracts.py handoff --task <task.json> --result <result.json> --repo .
python3 .omp/contracts/tools/verify_artifact_links.py --task <task.json> --result <result.json> \
  --verification <qa.json> --review <review.json>
```

Limits: `handoff` compares declared paths with Git status; pre-existing workspace changes can
produce warnings. A PASS is not acceptance. Read [CONTRACT_PROTOCOL.md](../../../CONTRACT_PROTOCOL.md).

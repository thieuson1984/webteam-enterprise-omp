#!/usr/bin/env python3
"""Cross-field WebTeam protocol checks missing from schema-only validation.

Verifies deterministic links between Task, Result, Verification and Review artifacts:
canonical digests, task/agent/revision identity, acceptance IDs, VERIFIED preconditions and
resolvable `path:line` evidence. It does not prove semantic correctness.
"""
import argparse, importlib.util, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
V = ROOT / ".omp/contracts/tools/validate_contracts.py"
spec = importlib.util.spec_from_file_location("validator", V)
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

def load(p): return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def line_exists(ref):
    m = re.fullmatch(r"([^:\\]+):(\d+)(?:-\d+)?", ref)
    if not m: return False
    p, n = m.group(1), int(m.group(2))
    if not v.safe_path(ROOT, p): return False
    f = ROOT / p
    return f.is_file() and 1 <= n <= len(f.read_text(encoding="utf-8").splitlines())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True); ap.add_argument("--result", required=True)
    ap.add_argument("--verification"); ap.add_argument("--review")
    a = ap.parse_args()
    if not a.verification and not a.review:
        print("FAIL no verification/review supplied; 0 cross-field artifacts checked")
        return 2
    task, result = load(a.task), load(a.result)
    errors = []
    if a.verification:
        ver = load(a.verification)
        if ver["task_id"] != task["task_id"]: errors.append("verification task_id mismatch")
        if ver["input_sha256"] != v.digest(task): errors.append("verification input_sha256 mismatch")
        if ver["result_sha256"] != v.digest(result): errors.append("verification result_sha256 mismatch")
        if ver["observed_revision"] != result["reported_revision"]:
            errors.append("verification observed_revision mismatch")
        if set(ver["checked_acceptance_ids"]) != set(task["origin"]["acceptance_ids"]):
            errors.append("verification checked_acceptance_ids mismatch")
        if ver["decision"] == "VERIFIED":
            if not ver["independent"]: errors.append("VERIFIED without independent=true")
            if ver["failed_checks"]: errors.append("VERIFIED with failed_checks")
            if not ver["confirmed_evidence_refs"]: errors.append("VERIFIED without confirmed evidence")
        for ref in ver["confirmed_evidence_refs"]:
            if not line_exists(ref): errors.append(f"unresolvable confirmed evidence {ref}")
    if a.review:
        rev = load(a.review)
        if rev["task_id"] != task["task_id"]: errors.append("review task_id mismatch")
        if rev["reviewer"] != "webteam-reviewer": errors.append("review reviewer mismatch")
        if rev["source_revision"] != result["reported_revision"]: errors.append("review source_revision mismatch")
        for f in rev["findings"]:
            if f["line"] is not None and not line_exists(f"{f['path']}:{f['line']}"):
                errors.append(f"unresolvable review finding {f['id']} {f['path']}:{f['line']}")
    checked = []
    if a.verification: checked.append("verification")
    if a.review: checked.append("review")
    for e in errors: print("FAIL", e)
    if not errors:
        print("PASS cross-field checks executed: " + ", ".join(checked))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())

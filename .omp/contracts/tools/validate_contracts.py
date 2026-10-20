#!/usr/bin/env python3
"""Local, deterministic WebTeam contract checks. Does not invoke OMP/models or modify repositories."""
import argparse, fnmatch, hashlib, json, os, pathlib, re, subprocess, sys
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS = {'task':'task.v1.schema.json','result':'result.v1.schema.json','review':'review.v1.schema.json','verification':'verification.v1.schema.json','omp':'result.omp.schema.json'}

def load(path):
    with open(path, encoding='utf-8') as f: return json.load(f)

def canonical(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')

def digest(data): return hashlib.sha256(canonical(data)).hexdigest()

def validate(kind, data):
    schema = load(ROOT/'schemas'/SCHEMAS[kind]); Draft202012Validator.check_schema(schema)
    errors=sorted(Draft202012Validator(schema).iter_errors(data),key=lambda e: [str(x) for x in e.path]);
    return [f"{('/'.join(map(str,e.absolute_path)) or '/')}: {e.message}" for e in errors]

def valid_rel(path):
    if not isinstance(path,str) or not path or '\\' in path or path.startswith('/') or '\x00' in path: return False
    segments=path.split('/')
    return not any(seg in ('', '.', '..') for seg in segments) and not re.match(r'^[A-Za-z]:',path)

def pattern_match(path, pat):
    # Supports repo-relative globs such as src/**, src/auth/**, foo/*.ts.
    if pat.endswith('/**') and path.startswith(pat[:-3] + '/'):
        return True
    return fnmatch.fnmatchcase(path,pat)

def safe_path(root,path):
    if not valid_rel(path): return False
    base=root.resolve(); target=(base/path).resolve(strict=False)
    return target == base or base in target.parents

def get_repo_files(repo):
    try:
        v=subprocess.run(['git','-C',str(repo),'status','--porcelain=v1','-z','--untracked-files=all'],capture_output=True,check=True)
    except (subprocess.CalledProcessError,FileNotFoundError): return None
    parts=v.stdout.decode('utf-8','replace').split('\x00'); changed=[]
    for part in parts:
        if not part: continue
        if len(part)<4: continue
        # For renames, record displayed path. This is a conservative check; production should parse rename destinations and old paths.
        changed.append(part[3:])
    return changed

def check_handoff(task,result,repo=None):
    errors=[]; warns=[]
    errors += ['TASK '+e for e in validate('task',task)]
    errors += ['RESULT '+e for e in validate('result',result)]
    if errors:return errors,warns
    for field,left,right in [('task_id',task['task_id'],result['task_id']),('agent',task['assigned_agent'],result['agent']),('repo_revision',task['source']['repo_revision'],result['reported_revision']),('input_sha256',digest(task),result['input_sha256'])]:
        if left!=right:errors.append(f'MISMATCH {field}: task identity/revision/digest not preserved')
    expected=set(task['origin']['acceptance_ids']); got=[a['id'] for a in result['acceptance']]
    if set(got)!=expected or len(got)!=len(set(got)):errors.append('Acceptance IDs must match input exactly, once each')
    changed=result['changed_paths']; scope=task['scope']; allow=scope['allowed_paths']; exclude=scope['excluded_paths']
    if scope['change_policy']=='READ_ONLY' and changed:errors.append('READ_ONLY task reports changed files')
    for p in changed:
        if not valid_rel(p):errors.append(f'Unsafe changed path {p!r}')
        elif (not any(pattern_match(p,g) for g in allow) or any(pattern_match(p,g) for g in exclude)):errors.append(f'Changed path outside approved scope: {p}')
    if result['status']=='SUBMITTED_FOR_VERIFY' and result['blockers']:warns.append('Submitted with blockers; ensure explicit triage')
    if result['status']=='SUBMITTED_FOR_VERIFY' and not result['evidence_refs']:warns.append('No evidence supplied: cannot accept outcome')
    for t in result['tests']:
        if t['status']=='PASS' and not t['evidence_ref']:errors.append(f"Test {t['name']} marked PASS without evidence_ref")
        if t['status']=='NOT_RUN':warns.append(f"Test not run: {t['name']}")
    if repo:
        base=pathlib.Path(repo)
        if not base.is_dir():errors.append('Repository path is missing')
        else:
            for p in changed:
                if not safe_path(base,p):errors.append(f'Changed path escapes repository: {p}')
            dirty=get_repo_files(base)
            if dirty is None:warns.append('Cannot inspect git status: not a Git repository?')
            else:
                extra=[p for p in dirty if p not in changed]
                if extra:warns.append(f'Workspace has changes not declared in result: {extra[:10]} (could predate task; compare snapshots)')
                for p in dirty:
                    if valid_rel(p) and ((not any(pattern_match(p,g) for g in allow)) or any(pattern_match(p,g) for g in exclude)):
                        errors.append(f'Workspace has out-of-scope change: {p}')
    return errors,warns

def main():
    p=argparse.ArgumentParser(description='WebTeam JSON and semantic contract validator')
    sub=p.add_subparsers(dest='cmd',required=True)
    q=sub.add_parser('check');q.add_argument('--kind',choices=SCHEMAS,required=True);q.add_argument('--file',required=True)
    q=sub.add_parser('hash');q.add_argument('--file',required=True)
    q=sub.add_parser('handoff');q.add_argument('--task',required=True);q.add_argument('--result',required=True);q.add_argument('--repo')
    q=sub.add_parser('suite')
    args=p.parse_args()
    try:
        if args.cmd=='check':
            es=validate(args.kind,load(args.file));print('\n'.join(es) if es else f'PASS {args.kind} schema');return 1 if es else 0
        if args.cmd=='hash':print(digest(load(args.file)));return 0
        if args.cmd=='handoff':
            es,ws=check_handoff(load(args.task),load(args.result),args.repo)
            for e in es:print('FAIL',e)
            for w in ws:print('WARN',w)
            if not es:print('PASS structural + deterministic handoff checks; human evidence verification still required')
            return 1 if es else 0
        if args.cmd=='suite':
            ex=ROOT/'examples';good=['task.valid.json','result.valid.json','review.valid.json','verification.valid.json']
            kinds=['task','result','review','verification']
            for f,k in zip(good,kinds):
                e=validate(k,load(ex/f));assert not e,(f,e)
            assert validate('result',load(ex/'result.invalid.json'))
            e,w=check_handoff(load(ex/'task.valid.json'),load(ex/'result.valid.json'))
            assert not e,e
            evil=load(ex/'result.valid.json');evil['input_sha256']='0'*64
            e,w=check_handoff(load(ex/'task.valid.json'),evil);assert any('input_sha256' in x for x in e),e
            evil=load(ex/'result.valid.json');evil['changed_paths']=['secret.txt']
            e,w=check_handoff(load(ex/'task.valid.json'),evil);assert any('READ_ONLY' in x or 'scope' in x for x in e),e
            evil=load(ex/'result.valid.json');evil['tests'][0]['status']='PASS';evil['tests'][0]['evidence_ref']=None
            e,w=check_handoff(load(ex/'task.valid.json'),evil);assert any('without evidence' in x for x in e),e
            print('PASS 4 valid schema fixtures, invalid schema fixture, and 3 negative handoff cases')
            return 0
    except (OSError,ValueError,AssertionError) as e:
        print('FAIL',e,file=sys.stderr);return 1

if __name__=='__main__':sys.exit(main())

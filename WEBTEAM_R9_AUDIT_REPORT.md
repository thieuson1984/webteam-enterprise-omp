# WebTeam R9 — Hybrid Memory Governance Audit

## Scope
Source: installed deliverables R8 and R6-to-Mnemopi upgrade prompt. This is a **static-document audit**, not an OMP runtime validation.

## Findings and resolutions

| Finding | Severity | R9 remedy |
|---|---|---|
| Per-project memory onboarding lacked a required documented policy | High | Mandatory `docs/governance/MEMORY_POLICY.md` plus inherit/customize/off interview |
| Memory promotion to Global conflated with managed skill promotion | High | Separate permission- and capability-gated memory and skill pipelines |
| Native Auto-Learn could emit user-global managed skills from project context | High | Verify output placement; fail closed, use reviewed project-local skills if containment unavailable |
| `per-project` YAML mistaken for proven isolation | High | Runtime bank identity and two-repository negative tests, with evidence |
| Project preferences could be unenforceable against user-global settings | High | Discover effective scoping, isolate via supported profile or disable operation |
| Cross-project reference/memory injection and sensitive knowledge promotion | High | Sanitization, provenance/license/security review, owner approval per candidate |
| Incomplete learning lifecycle | Medium | Candidate states, aging, invalidation, audit trail, source freshness |
| Repeated first-time setup questions on every project | Medium | Split global install vs per-project policy decisions |
| Risk of wiping installed R6 agents/config | High | Dedicated targeted R6 upgrade prompt, no re-bootstrap or destructive migrations |

## Document checks
- Source R8 preserved and appended with authoritative 15C R9 governance overlay.
- R6 upgrade prompt kept as an in-place operation with a mandatory R9 addendum.
- English/Vietnamese README extended consistently.
- ZIP contents and SHA256 hashes validated in build.

## Environment-dependent tests still required
1. Actual installed OMP version, config schema and profile precedence.
2. Project bank identity and cross-project memory isolation in separate sessions.
3. Auto-Learn generated skill placement and write permissions.
4. Actual supported Global/shared write path before any approved promotion.
5. Tool permission enforcement for specialist subagents.
6. Caveman, Codebase Memory MCP and fallback/council regressions.

**No claim of production-runtime verification is made.**

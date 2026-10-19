# WebTeam Enterprise R10.1 — Security, Compatibility and Quality Audit

**Scope:** Static/document-level audit of the prior R10 Master Prompt, the prior combined R6→R10 upgrade prompt, the previously published R6→R9 memory-only upgrade prompt, and both README documents. A new self-contained Loop-only upgrade is included in this reviewed bundle. Review date: **2026-10-19**.

## Executive result

**Document-level status: PASS with runtime gates outstanding.** The latest reviewed outputs are consistent about the intended upgrade route, safety precedence and bounded quality iteration. **No claim is made that the user's OMP runtime has been probed or is free of implementation vulnerabilities.** Some controls depend on OMP version, available tools/permissions, provider approvals, shell isolation, and actual cancellation behavior; these remain **UNVERIFIED** until tested on the user's machine.

## Files produced

| File | Purpose |
|---|---|
| `WEBTEAM_ENTERPRISE_OMP_MASTER_PROMPT_R10_REVISED.md` | Full R10.1 new-install bootstrap, retaining sixteen-agent functionality and historical feature contracts with corrected precedence and Loop rules |
| `WEBTEAM_R6_TO_R10_UPGRADE_PROMPT_REVISED.md` | Consolidated standalone upgrade for R6 lacking hybrid memory governance and/or adaptive Loop |
| `WEBTEAM_EXISTING_INSTALL_LOOP_ONLY_UPGRADE_PROMPT.md` | Targeted Loop-only upgrade for an existing team already running Memory/Auto-Learn |
| `WEBTEAM_R6_MEMORY_ONLY_UPGRADE_PROMPT_REVISED.md` | Optional revised Memory-only upgrade for R6 without Loop changes |
| `README.md` and `README_VI.md` | English and Vietnamese updated usage guidance with a four-route decision tree |
| `WEBTEAM_R10_REVISED_AUDIT_REPORT.md` | This report, audit findings, coverage and limitations |

## Findings and corrections

| ID | Priority | Prior issue | Correction in R10.1 | Status |
|---|---|---|---|---|
| A01 | High | Master R10 header still labeled R7; older R8/R9 guidance looked simultaneously authoritative | Correct revision and explicit precedence: Section 15B Mnemopi settings, 15C isolation/governance, 16A–G quality loops, 17 hardening | Document fixed |
| A02 | High | Earlier Memory examples recommended `local` even after Mnemopi-first R8/R9 | Removed conflicting local *default* example; keep LOCAL as explicitly consented fallback, Mnemopi per-project recommended only after schema/privacy verification | Document fixed |
| A03 | High | Combined R6→R10 prompt mechanically concatenated R6→R9 and Loop changes; misleading old title and repeated or unnecessary memory migration risk | Replaced with staged standalone R6→R10.1 upgrade, capability inventory/idempotence, skip healthy Mnemopi, and one approval-gated Loop path | Document fixed |
| A04 | Critical | No isolated Loop-only upgrade; running combined upgrade could change already-working memory/model setup | Added standalone Loop-only upgrade with explicit **allowlist and denylist**, before/after diff, no memory/model changes, rollback | Document fixed; runtime diff unverified |
| A05 | High | `/loop` mode confused with auto-activation; OFF/ASK/AUTO might be treated as native config keys | Explicitly distinguish native `loop.mode` from WebTeam policy states; no invented `loop.enabled` or `webteam.loopPolicy` keys | Document fixed |
| A06 | High | Baseline QA check versus *additional* loop passes was inconsistently counted | Baseline pass 0; C1/C2=0, C3≤1, C4≤2, C5≤3 **extra** passes. Runtime submission count must be verified for off-by-one | Document fixed; runtime count unverified |
| A07 | Critical | Natural-language stop or unspecified `/loop` commands might be mistaken for enforceable limits | Native only after actual command/cap/cancel/steering/async smoke tests; fail closed to finite supervised passes | Document fixed; runtime safety unverified |
| A08 | High | Loop shell predicates could execute untrusted repository-supplied commands | Fixed, non-destructive, user-authorized predicates; verify exit-code semantics and cap; no arbitrary interpolation of untrusted text | Document fixed; runtime command policy unverified |
| A09 | Critical | Native loop plus nested Caveman/Council/fallback/Auto-Learn could multiply calls, bypass budget and repeat dangerous side effects | Single controller/writer, shared budget across retries/providers, no global promotion or side-effect replay, stop on ambiguity | Document fixed; host enforcement unverified |
| A10 | High | Auto-Learn managed skills can be global although Mnemopi bank is project-scoped | Explicit output-path check; project-local reviewed skills or disable unsafe auto-learning with approval; separate memory and skill promotion | Document fixed; project isolation unverified |
| A11 | High | Read-only agent tool lists may not prevent inherited MCP/extension writes | Effective tool and host-boundary verification, no prompt-only sandbox claims; critical review in supervised parent if needed | Document fixed; permissions unverified |
| A12 | Medium | README linked outdated R7/R8 installation routes, duplicated R9 guidance | New R10.1 entrypoints, updated routing text, removed duplicate R9 sections, separate Loop-only usage | Document fixed |
| A13 | Medium | Visual tests could be made green by updating snapshots | Deterministic Playwright baselines, independent review, ban on automatic baseline acceptance | Document fixed; actual UI tests unverified |
| A14 | High | Async work and steering can make native Loop unsafe, with upstream issue reports | Version-specific probe, no unattended native Loop when unsafe or unverified, bounded manual alternative | Document fixed; upstream bug status depends on installed version |
| A15 | Medium | Future project onboarding could rerun global setup or overwrite user decisions | Global interview once; project policy inheritance/override only; minimal idempotent updates, preserved app docs | Document fixed |

## Deliberately retained functionality

The R10.1 Master Prompt preserves all sixteen specialist roles, eight-stage Designer workflow/anti-AI-slop, Global/Project WebTeam, React/SolidJS and Node/Fastify, data and security specialists, Vitest/Fastify/Playwright/visual testing, Design DNA/Engineering DNA, external repository intelligence, provider-first inventory, cross-provider fallback, multi-model deliberation, optional Caveman/Codebase Memory MCP, Mnemopi, controlled Auto-Learn, and project-specific knowledge promotion policy. It **does not** install or upgrade third-party tools as part of a Loop-only upgrade.

## Evidence hierarchy

- **Static verified:** file bytes exist, UTF-8 readable, Markdown fences balanced, required coverage strings and references present, package integrity and relative links checked, no forbidden installation step in the Loop-only scope, documented upgrade routes clearly separated.
- **Not runtime verified:** OMP agent/skill parsing and discovery; specific installed `/loop` syntax, cap, stop, steering or async behavior; effective MCP permissions; provider and model fallback; Mnemopi bank isolation; Auto-Learn user-level managed-skill output; actual browser snapshots; costs/tokens; idempotency under real API failures.
- **Fail-closed operational recommendation:** keep native looping OFF until a disposable environment demonstrates a finite cap and reliable operator stop; choose ASK and manually bounded QA passes. Never silently change approved memory/fallback/model settings for a Loop-only upgrade.

## User-side verification checklist

1. Run `omp --version`, `omp config path` and inspect the installed settings schema in the correct profile. Do not publish any credential values.
2. Confirm project-specific `.omp` discovery, actual agents/skills and effective model roles/fallbacks in the intended cwd.
3. Take approved configuration snapshots before applying **one** selected upgrade prompt.
4. With synthetic data, verify QA/Reviewer tool rights, test fixtures, Mnemopi isolation (if touched), and that no managed skills leak globally.
5. Test native Loop only if the installed version exposes and safely enforces an iteration limit and stop. Include off-by-one counting, one-off steering, background task settlement and stop on a fixed predicate. Do not deliberately hang production sessions.
6. Inspect actual changed files and effective settings after the upgrade; confirm all out-of-scope settings are unchanged.
7. Record commands, exit codes, OMP version, task/pass budget, model routes and **observed** token/cost usage; record failed/unrun cases as `FAIL/BLOCKED/UNVERIFIED`, never PASS by inference.

## Primary references

- OMP settings and scope: https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md
- Task agents, model and effort behavior: https://github.com/can1357/oh-my-pi/blob/main/docs/task-agent-discovery.md
- Task execution and tool exposure: https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md
- OMP extension lifecycle: https://github.com/can1357/oh-my-pi/blob/main/docs/extensions.md
- Loop steering issue #7348: https://github.com/can1357/oh-my-pi/issues/7348
- Loop pending post-prompt work issue #7330: https://github.com/can1357/oh-my-pi/issues/7330

**Bottom line:** All *identified document-level* conflicts in this review have been addressed. No static review can guarantee that every runtime vulnerability or implementation defect in OMP or installed third-party extensions has been eliminated; test and enforce the listed gates locally before relying on unattended automation.

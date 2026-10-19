# WebTeam Enterprise R10.2 — Post-Installation Routing Audit (Document Review)

**Review date:** 2026-10-19  
**Scope:** R10.1 master/README, R6 full targeted upgrade, dedicated new post-install verification; no actual user OMP runtime attached.  
**Document status:** PASS (static consistency and package checks).  
**Runtime status:** UNVERIFIED (must be established by the installed OhMyPi session).

## Significant findings and corrections

| ID | Severity | Finding in previous revision | R10.2 response |
|---|---|---|---|
| A01 | High | Agent discovery could be mistaken for proof of generic-request automatic dispatch | Adds a fresh-main-session natural-language routing probe with observed task tracing; clear UNVERIFIED state if impossible |
| A02 | High | The phrase “default Orchestrator” could imply a hardwired dispatcher, which normal Markdown instructions do not create | Distinguishes main-session WebTeam dispatcher from explicitly spawned `webteam-orchestrator`; documents two valid topologies |
| A03 | High | Task agent may be discovered but unspawnable due to depth, disabledAgents or spawn allowlist | Adds effective policy checks plus a real bounded specialist spawn test (supported batch/flat schema) |
| A04 | Critical | Headless subagents may auto-approve execution; “read-only” prose is not a tool sandbox | Enforces read-only-first, inspection of effective tools including MCP/extension, no destructive denial probes, restrict/disable unsafe role when unverifiable |
| A05 | Medium | Monorepo `.omp` discovery can shadow project context | Checks nearest effective context/root vs nested worktree and repairs only with scoped consent |
| A06 | High | Install success could be declared after static validation alone | Requires observed S01/S02 for PASS_VERIFIED and accurately reports BLOCKED/PARTIAL/UNVERIFIED otherwise |
| A07 | Medium | No minimal repair/rollback path after a routing failure | Adds evidence-based defect tickets, targeted backups, single-writer and bounded retest rules |
| A08 | High | Smoke tests might invoke paid provider fallback, multi-model, Loop or Caveman unexpectedly | Single small approved budget; hold smoke test if fallback/extra calls cannot be controlled |
| A09 | Medium | Post-install checks not a durable reusable skill | Requires `webteam-self-orchestration-audit` skill, with selective loading and validated SKILL.md |
| A10 | Medium | Existing R6→R10 upgrade omitted fresh-session routing proof | R6→R10.2 upgrade now includes a post-upgrade routing validation gate without reinstalling agents |

## Verification performed here

- Checked **all sixteen** agent names remain in the integrated Master Prompt.
- Checked the R10.2 installation stage invokes the new Section 18 post-install process before declaring verified completion.
- Checked the standalone audit includes D01–D12 inventory, S01–S04 runtime observations, consented repair and rollback.
- Checked static Markdown code-fence balance and relative links for shipped files.
- Checked both English and Vietnamese README documents link to the standalone audit and use the R10.2 master.
- Checked R6→R10.2 upgrade remains narrowly scoped and does not assume already-installed Memory/Loop must be rewritten.
- Checked final ZIP entries against the SHA-256 manifest.

## Runtime checks still required (cannot be completed by editing Markdown)

1. Effective OMP build/version/profile/config roots, model-role and fallback resolution.
2. Native `task` availability, `task.batch` setting, real parent spawn policy and recursion depth.
3. Main-session natural-language dispatch to an actual WebTeam agent, with task trace or Agent Hub evidence.
4. Actual nested Orchestrator delegation **or** tested main-session direct specialist topology.
5. Effective headless child tool restrictions, third-party MCP/extension tool availability, and lack of unauthorized side effects.
6. Non-destructive fixture completion, async cleanup, model cost, provider/data permissions, and no active Loop/Council at the end.
7. Re-run after any approved fix and record exact observed failure/success evidence.

**Limits:** The prompt can request repairs, but cannot force the OMP runtime to adopt routing or hard security controls it does not support. Tests in a synthetic repo do not prove the absence of every runtime vulnerability. A configured skill/AGENTS.md is a behavioral convention, not a hard-coded message interception mechanism.

## Upstream reference points checked

- [OMP task agent discovery](https://github.com/can1357/oh-my-pi/blob/main/docs/task-agent-discovery.md)
- [OMP task tool](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md)
- [OMP context discovery](https://github.com/can1357/oh-my-pi/blob/main/docs/context-files.md)
- [OMP skills](https://github.com/can1357/oh-my-pi/blob/main/docs/skills.md)
- [OMP tool approval/subagents](https://github.com/can1357/oh-my-pi/blob/main/docs/approval-mode.md)

These are upstream references, not proof that the user's particular installed build supports every setting shown.

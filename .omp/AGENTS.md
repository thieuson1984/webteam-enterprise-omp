# WebTeam Enterprise builder repository

This repository is the source distribution for the WebTeam for OhMyPi installation. It is **not**
the SMS monorepo.

## Scope precedence

- The installed team is canonical at `~/.omp/agent/`: 16 agents, 35 commands, and the WebTeam skill
  catalog.
- Source copies live in `agents/`, `commands/`, and `skills/`. Preserve parity with the installed
  copies unless a change explicitly targets the source distribution.
- Standalone ancestor `AGENTS.md` discovery is disabled for this project by `.omp/config.yml`
  (`disabledProviders: [agents-md]`). Do not apply the SMS monorepo rules from
  `/home/sontt/Documents/AGENTS.md` here.
- The global WebTeam routing policy in `~/.omp/agent/AGENTS.md` still applies when this repository
  is used for web engineering work.

## Working rules

- No package manifest or test harness is defined here. Verify structural changes directly: parse
  frontmatter, count agents and skills, and compare `agents/` and `commands/` with the installed
  copies.
- Do not edit `~/.omp/agent/` from this repository unless the task explicitly targets the installed
  team; keep a timestamped backup and revalidate when it does.
- Preserve existing uncommitted changes. Do not commit or push without explicit instruction.

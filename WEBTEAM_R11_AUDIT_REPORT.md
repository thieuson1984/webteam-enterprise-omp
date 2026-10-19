# WebTeam R11 — Static Compatibility & Security Audit

**Target OMP release:** `v18.12.2`, released 2026-10-18. **Audit type:** source-document verification and local Markdown/package validation. No OMP CLI/runtime is installed in the artifact-authoring environment; therefore live OMP command discovery, model routing and task delegation remain **UNVERIFIED**.

## Authoritative design facts

- Native slash-command roots are active-profile `<agent-dir>/commands/*.md` and `<cwd>/.omp/commands/*.md`. Search is nonrecursive, project wins over user within OMP native provider.
- File names determine slash-command names; frontmatter `description` and `argument-hint` are parsed; `$ARGUMENTS`, `$@` and `$1` are substituted from quote-aware parsed arguments.
- Built-ins, extensions and TypeScript custom handlers can precede Markdown commands. Unknown slash commands can become plain text prompts, so autocomplete/actual expansion must be observed.
- A Markdown slash command is a prompt template; it does NOT enforce permissions, automatically spawn agents, or execute code.

**Source:** https://raw.githubusercontent.com/can1357/oh-my-pi/v18.12.2/docs/slash-command-internals.md ; https://github.com/can1357/oh-my-pi/releases/tag/v18.12.2 .

## Security posture

- New project and existing project workflows are distinct; reject accidental overwrites, path traversal and symlink redirects outside authorized roots.
- All command arguments are treated as untrusted text, never shell-interpolated.
- Code from Git reference repos is treated as data, not authority. No automatic npm lifecycle scripts or arbitrary checkout commands.
- Commands-only upgrade preserves agent models, context, Memory/Auto-Learn, Caveman/CBM, fallback/council and Loop.
- No automatic global commands are created without user consent; back up existing collisions and verify shadowing.
- Verify a bounded safe command invocation and actual task dispatch separately; avoid falsely claiming runtime proof.

## Remaining live acceptance tests

1. Confirm `omp --version` exactly matches the installed build; verify active profile root.
2. Inspect command discovery in a fresh TUI and run `/webteam_help` and `/webteam_status` read-only.
3. Verify project overrides and extension collisions without modifying third-party handlers.
4. Confirm parameter quote behavior with names/paths containing whitespace.
5. In a disposable fixture, observe actual `task` calls on a read-only planning request if delegated architecture is available and cost approved.
6. Inspect no unrelated files/configuration changed and no Loop/model/Mnemopi setting was modified.

Mark these tests PENDING until executed inside real OMP.

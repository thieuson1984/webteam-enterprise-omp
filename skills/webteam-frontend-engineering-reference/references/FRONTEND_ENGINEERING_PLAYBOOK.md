# Frontend Engineering Playbook — production-grade decision and evidence

**Authoritative scope:** This is reusable technical guidance. It does not override project architecture, approved model/tool policies, or live OMP capabilities. Read the relevant subsection only. Separate `MEASURED`, `OBSERVED`, `INFERRED`, `NOT_RUN`, and `NOT_APPLICABLE`.

## Standards and evidence provenance

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [React Compiler (optional, verify)](https://react.dev/learn/react-compiler/introduction)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Web Vitals](https://web.dev/articles/vitals)

## Frontend decision architecture

### Browser/route data contract example

A search page has URL state (`?q=&sort=&cursor=`), server state (typed API result), view state (selected row, dialog) and security policy (server). Map each to its owner. Route reload, back/forward, logout, failed fetch and locale change must not produce contradictory data. Data keys should include tenant/account identity and authorization context where required; clear them on identity change.

```ts
// Illustrative TypeScript contract; adapt to actual project framework and server schema.
type PageState<T> =
  | { kind: 'loading' }
  | { kind: 'ready'; items: T[]; nextCursor?: string }
  | { kind: 'empty' }
  | { kind: 'forbidden' }
  | { kind: 'error'; requestId?: string; canRetry: boolean };
```

Prefer an explicit state model to a pile of booleans (`isLoading && isError && data`). Guard runtime input with shared or generated schema only when verified against the deployed API. A generic 401 refresh interceptor must not create redirect/retry storms; use bounded refresh coordination and fail closed.

### Component engineering strategy

- Split controlled data/behavior from visual presentation when it makes tests/ownership clearer; avoid abstractions simply to satisfy a folder hierarchy.
- Design system covers semantic tokens, variants, density, all interaction states and real content lengths. A new component must specify focus, names, keyboard behavior and responsive constraints.
- For data grids define server-sort/filter semantics, selection scope, stable row identities, revalidation after mutation, explicit empty/error states. Virtualization is a performance tradeoff and can damage accessibility; test the exact implementation.
- Use actual product flows (not aesthetic-only screenshots) for login, forms, dashboards, settings and critical navigation. Use no invented business metrics.

### Browser and route verification ladder

1. Contract smoke: parse successful/error API fixture, distinguish unauthorized/error/empty.
2. Component: keyboard and state transitions under slow/deferred requests.
3. Route: navigation, direct linking, refresh, logout/login return-to safe URL.
4. Visual: approved screenshots at representative desktop/mobile widths, real empty/loading/error states, reduced motion.
5. Security/observability: verified redaction, no accidental credentials, correct tenant change behavior.

### Project stack compatibility

React, SolidJS, Vite, TanStack, CSS frameworks, SSR and hydration are choices, not mandatory bundles. Determine the installed version before referencing APIs. React Compiler can reduce manual memoization when configured correctly, but only adopt with supported toolchain and profiled value. Prefer native HTML where feasible. Generate no test-success claims from code reasoning alone.


## Reversible implementation workflow

1. Baseline real behavior / establish a precise gap and target outcome.
2. Record ownership, existing user changes, touched files, anticipated data/security effects and approvals.
3. Compare at least one simpler alternative and explicitly reject unnecessary infrastructure, tool purchases, new packages or frameworks.
4. Make the smallest authorized local change with a single implementation owner; avoid concurrent edits to shared files.
5. Run real tests, capture outputs, check privacy/accessibility/business semantics and compare objective before/after evidence.
6. Request independent QA/reviewer verification proportionate to risk; escalate unknowns, blocking approvals or production effects.
7. Report residual issues, updated contract/docs, evidence links and rollback. Never falsely label tests, scans, monitoring or deployments as completed.

## State and uncertainty labels

| Status | What it means |
|---|---|
| `OBSERVED` | Verified in source or direct tool output, with path/version or artifact ID |
| `MEASURED` | Actual run using documented environment, inputs and method |
| `INFERRED` | Reasoned hypothesis not yet independently demonstrated |
| `NOT_RUN` | Relevant test or measurement omitted, with explicit reason |
| `BLOCKED` | Missing tool/permission/environment/decision |
| `NOT_APPLICABLE` | Excluded because the real project has no such surface |

## Cross-agent handoff

Lead: `webteam-frontend`. Partners only when justified: webteam-designer (design contracts), webteam-accessibility (independent accessibility), webteam-backend (API), webteam-qa (test evidence), webteam-security (trust boundaries), webteam-performance (measurement). No tool or reference grants production access; do not send project data to new providers without authorization.

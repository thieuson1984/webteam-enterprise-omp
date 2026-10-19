# Frontend capability blueprints — practical selection catalog

Select a **single relevant** entry rather than loading the entire document. Each entry applies conditionally; identify `NOT_APPLICABLE` features. Baseline and evidence must be real. The table and skills are reference artifacts, not automatically executed tools.

**Source standards (verify applicability and versions):**
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [React Compiler (optional, verify)](https://react.dev/learn/react-compiler/introduction)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Web Vitals](https://web.dev/articles/vitals)

## FE01 — Frontend architecture, route ownership and component/API boundaries
- **Trigger:** feature boundaries, complex client modules, monorepo UI.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Map routes, domain boundaries, shared UI and API ownership. Keep domain policy out of reusable view components.
- **Contract/design:** Choose module boundaries by use-case and independent change rate; document import directions, shared dependencies and circular dependency checks.
- **Bounded change:** Build a route/feature ownership matrix and protect page-load/error/layout boundaries; do not invent framework changes.
- **Verification including negative cases:** Test representative end-to-end journeys and architecture import checks, plus smallest module-level fixture.
- **Evidence to hand off:** Architecture map, boundary decisions, dependency graph and acceptance evidence.
- **Reject:** Cross-feature singletons, context-provider pyramids, globally mutable client state, speculative microfrontends.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE02 — Typed server/client contracts and failure semantics
- **Trigger:** API client change, forms, paginated data, contract drift.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Identify authoritative server schema and actual consumers; treat TypeScript runtime casts as untrusted.
- **Contract/design:** Validate boundary values, discriminated server errors, 401/403/404/409/422/429 and privacy redaction; preserve intentional null versus absent.
- **Bounded change:** Specify typed request cancellation, retries only for safe operations, cursor invalidation, API compatibility and conflict UX.
- **Verification including negative cases:** Use mocked success/error/timeout/unauthorized fixtures and contract tests against server schema.
- **Evidence to hand off:** Typed contract diff, error-state matrix, consumer tests and backward-compatibility notes.
- **Reject:** Assuming generated SDK is authoritative without checking deployed server, implicit any, silent error swallowing.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE03 — Navigation, deep links, route guards and recovery
- **Trigger:** router, nested layout, auth redirect, multi-step workflow.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Model route hierarchy, user journey entry/exit and canonical URL ownership; ensure direct refresh works.
- **Contract/design:** Separate UI hiding from backend authorization, and implement return-to paths only from allowlisted internal routes.
- **Bounded change:** Preserve focus/scroll semantics, history navigation, language, search params and meaningful 404/403 flows.
- **Verification including negative cases:** Test deep links, reload, logout/login redirects, back-forward, route loaders and error boundaries.
- **Evidence to hand off:** Route contract, navigation state diagram, inaccessible-path tests and keyboard checks.
- **Reject:** Open redirects, broken nested layouts, client-only authorization, inaccessible route transitions.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE04 — Async server-state lifecycle and cache consistency
- **Trigger:** TanStack Query, realtime, mutation, offline, stale data.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Inventory query keys, mutation ownership and refetch invalidation; distinguish server data from local UI state.
- **Contract/design:** Specify stale/fresh TTL relative to business risk; handle aborts, race conditions, optimistic updates and rollback.
- **Bounded change:** Use idempotency/ETags or versions for conflicting edits; prevent tenant/user caches crossing sessions.
- **Verification including negative cases:** Test slow responses, out-of-order completion, 409 conflicts, failed retries and logout cache reset.
- **Evidence to hand off:** Async state chart, query-key scheme, invalidation map, race tests.
- **Reject:** Fire-and-forget mutations, stale secrets in cache, unbounded retries, excessive global stores.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE05 — Enterprise forms, schemas and complex task workflows
- **Trigger:** CRUD, wizard, dirty form, bulk editor.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Inventory field validation, dependencies, server errors, permissions, autosave and loss-of-work risk.
- **Contract/design:** Design schema alignment between frontend and server, multi-step persistence, disabled/submitting/success states.
- **Bounded change:** Use accessible label/description/error semantics, safe destructive confirmations and focus on first invalid field.
- **Verification including negative cases:** Test partial failure, draft restore, double submit, localization, slow networks and concurrent edits.
- **Evidence to hand off:** Field/step state matrix, error copy, validation contracts, tests.
- **Reject:** Frontend-only validation, accidental double-submit, silently discarded unsaved changes.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE06 — Accessible component behavior and keyboard engineering
- **Trigger:** dialog, listbox, combobox, table, complex navigation.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Select native HTML first; refer to WAI-ARIA APG only for custom composite components.
- **Contract/design:** Specify keyboard map, roving tab stops or activedescendant, focus trap/return, names/descriptions and announcement strategy.
- **Bounded change:** Preserve contrast, zoom/reflow, reduced motion, touch targets and translated content behavior.
- **Verification including negative cases:** Run axe-style automated checks PLUS manual keyboard/focus and screen-reader scenarios on real UI.
- **Evidence to hand off:** Interaction contract, WCAG 2.2 evidence, keyboard and assistive technology test notes.
- **Reject:** ARIA without behavior, trapped focus, div-as-button, snapshots claimed as accessibility proof.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE07 — High-density data grids, filters and virtualized views
- **Trigger:** DataTable, treegrid, large list, pagination.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Start with actual user tasks, column priority, sort/filter semantics and visible row/selection counts.
- **Contract/design:** Choose pagination, virtualization and sticky headers only when data size and use-cases justify; maintain semantic access.
- **Bounded change:** Specify bulk action selection rules, persisted filters, permissions, empty/loading/error/partial states and export.
- **Verification including negative cases:** Test 10k-row synthetic workloads if relevant, keyboard table access, screen-reader semantics and selection during pagination.
- **Evidence to hand off:** Grid state machine, query/filter contract, density budget and realistic fixtures.
- **Reject:** Infinite scroll without recovery, virtual rows lacking accessibility, fake counts, silently misapplied bulk actions.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE08 — Resilient UI error boundaries and offline behavior
- **Trigger:** SPAs, flaky APIs, PWAs, critical workflows.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Classify fatal vs recoverable errors, offline-read behavior, timeout/cancel distinction and safe retries.
- **Contract/design:** Specify full-page, route, and component isolation, actionable recovery copy and event correlation identifiers.
- **Bounded change:** Protect drafts and pending requests; require explicit offline cache/data handling and no unauthorized stale exposure.
- **Verification including negative cases:** Test forced network-off, 500, timeout, stale response, client crash and restart; verify graceful degradation.
- **Evidence to hand off:** Failure taxonomy, recovery specification, manual failure test evidence.
- **Reject:** Blank screens, retry loops, caching private records without approval, offline promises unsupported by stack.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE09 — Frontend rendering, bundle and hydration engineering
- **Trigger:** large bundle, slow interaction, React or Solid bottlenecks.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Measure field/lab signal and profile before change; identify user action and execution hot path.
- **Contract/design:** Inspect route-level code splitting, image/fonts, bundle chunks, main-thread long tasks and hydration boundaries.
- **Bounded change:** Apply framework-supported optimization only after measurement; React Compiler is opt-in and version-verified, not universal.
- **Verification including negative cases:** Compare reproducible profiles/bundle diff at same environment and rerun interaction + visual regression.
- **Evidence to hand off:** Before/after trace, bundle summary, risk and measured metrics.
- **Reject:** Blind memoization, shipping extra dependencies to optimize negligible work, hydration mismatches.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE10 — Design-to-code precision and token/component governance
- **Trigger:** shared components, design-system migration, branded UI.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Derive tokens from approved DESIGN.md and screenshot evidence, keeping semantic roles separate from raw colors.
- **Contract/design:** Build bounded component APIs and variants; use actual data, content hierarchy, states and product brand.
- **Bounded change:** Enforce responsive layouts, focus, hover, disabled, error, density and dark mode only when supported.
- **Verification including negative cases:** Run visual diffs with approved baselines across real viewports; flag brand changes for Designer approval.
- **Evidence to hand off:** Token→component map, variants, screenshots, Designer signoff.
- **Reject:** Inventing palette on each page, giant prop soup, auto-accepting screenshots, generic AI template polish.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE11 — Internationalization, Vietnamese content and formatting correctness
- **Trigger:** multilingual product, Vietnamese, dates, numeric data.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Map locales, business timezone, fallback semantics, actual glyph and font coverage.
- **Contract/design:** Use safe localization of dates/numbers/currency/pluralization; preserve semantic values independent from display strings.
- **Bounded change:** Support lengthy translated labels, RTL when relevant, responsive overflow and localized validation copy.
- **Verification including negative cases:** Test vi-VN and another locale in real UI including forms, tables, sorting and screen reader labels.
- **Evidence to hand off:** Locale contract, content/fallback checklist and visual/functional evidence.
- **Reject:** String concatenation localization, ambiguous dates, truncated Vietnamese diacritics.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE12 — Browser-side privacy and threat boundaries
- **Trigger:** tokens, CSP, SSRF links, embeds, untrusted HTML.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Define trust boundary for URLs, HTML, file previews, browser storage and cross-origin messages.
- **Contract/design:** Use safe renderers, output encoding, CSP/Trusted Types as compatible, CSRF defense per session design and token discipline.
- **Bounded change:** Ensure logout clears session-scoped caches, telemetry excludes secrets, redirect targets are safe, third-party embeds are reviewed.
- **Verification including negative cases:** Test malicious fixtures, script sink paths, CORS/CSRF expectations and tenant switch; Security co-sign required.
- **Evidence to hand off:** Browser attack surface list, exploit regression tests, approved controls.
- **Reject:** Disabling CSP to fix a widget, storing long-lived secrets carelessly, client-side checks as only security.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE13 — Component, integration and visual quality in CI
- **Trigger:** frontend release, regression, flaky UI tests.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Map journeys to component behavior, API contract, routing, a11y, visual and E2E coverage.
- **Contract/design:** Use deterministic fixtures, isolated clocks, stable selectors, realistic error responses and reproducible Playwright viewports.
- **Bounded change:** Define code ownership and CI gates, quarantine flaky tests with ticket rather than hiding failures.
- **Verification including negative cases:** Run actual commands; report count, failure, screenshot diff review and NOT_RUN gaps.
- **Evidence to hand off:** Test pyramid map, flaky-test plan, executed command evidence.
- **Reject:** Snapshot spam, global mocks that bypass contracts, auto-updated golden images.
- **Partner/owner:** `webteam-frontend` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## FE14 — SSR/CSR trade-offs
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Do not assume SSR is desirable: measure SEO/TTFB/hydration/state cost, choose based on actual delivery system.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## FE15 — Frontend feature flags
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Evaluate flag data safety, telemetry privacy, cleanup and stale-flag fallbacks; never rely on flags as authz.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## FE16 — Realtime reconnection
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Specify last-seen sequence, backoff, replay/idempotency and UI staleness; test intermittent connectivity.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## FE17 — Charts/maps interaction
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Ensure source credibility, scale/units, accessible text equivalents and low-end-device memory budget.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## FE18 — File previews/downloads
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Validate MIME/size server-side, sanitize untrusted previews, revoke blob URLs and track permission failures.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.


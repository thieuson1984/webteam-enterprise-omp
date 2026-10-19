---
name: webteam-ui-visual-e2e-qa
description: "Verify UI/UX via Playwright interaction and visual tests with deterministic fixtures, meaningful baselines, accessibility evidence and safe repairs."
---

# webteam-ui-visual-e2e-qa

## Purpose and activation
Verify UI/UX via Playwright interaction and visual tests with deterministic fixtures, meaningful baselines, accessibility evidence and safe repairs.

**Activate when:** UIUX audit/fix, design-system changes, new critical pages, responsive/layout regressions, major component changes.

**Required inputs:** Target route/viewport/state matrix, approved expected visuals, deterministic seed/fixture, browser/server tool availability and test budget.

## Professional workflow
1. Prepare trusted test environment; verify app startup and no production or private-data dependence. Use seeded fixture data and agreed test accounts.
2. Capture major breakpoints, both themes if supported, locale expansion, error/empty/loading states and long-record extremes; include interaction screenshots after controls settle.
3. Use Playwright `toHaveScreenshot()` only when runner and stable reference snapshots exist; disable or normalize animation, clocks, network variability, fonts and other nondeterminism.
4. Check layout overflows, clipping, occluded menus/modals, sticky headers, focus order, keyboard/hover parity, touch, zoom/reflow, reduced motion and semantic labels.
5. Attach screenshot names, diff location, test command, environment/browser and actual results; do not assert a visual check ran without an artifact.
6. Review diffs by impact; only the authorized implementation agent repairs code, QA writes tests and Reviewer confirms intentional baseline changes.
7. Run a bounded verification cycle; stop when criteria met, no progress, budget expired or user approval needed. Never invoke native `/loop` without runtime-safe stop verification.

## Extended page/component regression coverage
When a project uses these flows, select relevant contracts from `webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md` and `webteam-component-interaction-contracts/references/ACCEPTANCE_MATRICES.md`. For complex components prioritize keyboard and async transitions (Escape/focus restoration, grid sort/filter/select semantics, date DST, file failure/retry, role denial, modal lifecycle), not only screenshot comparison. Test representative state and viewport combinations using risk-based pairwise coverage; do not exhaustively multiply all states unless justified. Never mark manual assistive-technology checks PASS from an automated accessibility scan alone.

## Known anti-patterns
Blind screenshot updates; non-deterministic screenshots treated as product regressions; exclusively desktop testing; passing after skipping tests; browser work on production.

## Deliverables
Visual coverage matrix, reproducible test commands, screenshot/diff evidence, defect status and approvals.

## Quality gate / Definition of Done
Critical routes and states checked in verified environment; intentional visual changes documented and unwanted regressions resolved.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving ui visual e2e qa, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

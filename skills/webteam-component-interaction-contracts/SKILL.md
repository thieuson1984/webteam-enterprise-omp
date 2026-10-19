---
name: webteam-component-interaction-contracts
description: "Specify and verify production-ready interaction, responsive, accessibility, data and visual contracts for complex interface components: navigation, menus, forms, dialogs, grids, filters, charts, editors, file uploads, calendars and more."
---

# WebTeam — Component Interaction Contracts

## When to use
Use when designing, implementing or auditing shared UI primitives or complex widgets, especially when appearance looks polished but real behavior is incomplete. Read ONLY the relevant family in [Component Catalog](references/COMPONENT_CATALOG.md) (`skill://webteam-component-interaction-contracts/references/COMPONENT_CATALOG.md`), then apply [Acceptance Matrices](references/ACCEPTANCE_MATRICES.md) for consequential interactions. Do not load the whole component catalog into routine tasks.

## Responsibility
`webteam-designer` authors component intent/appearance and behavior contract. `webteam-frontend` implements using proven native semantics/accessible primitives. `webteam-accessibility` validates keyboard and AT behavior; `webteam-qa` verifies states and regression; `webteam-security` reviews auth/privacy-sensitive widgets; `webteam-reviewer` independently challenges impactful changes.

## Component contract, mandatory fields
- **Role and selection rationale:** why button vs link, combobox vs native select, table vs grid, modal vs page; avoid needless custom widgets.
- **Anatomy:** slots/labels/helper text/icons/required markers/actions, visual priority, min/max text and data extremes.
- **Variants:** semantic role (primary/secondary/destructive/subtle), sizes and density, themes and color meaning.
- **States:** default/hover/pressed/focus-visible/selected/expanded/disabled/loading/error/success/readonly and asynchronous transitions, as relevant.
- **Interaction:** pointer, touch, keyboard keys, Escape behavior, focus entry/exit/restore, outside-click behavior and effect on page scroll.
- **Data:** input/output types, server truth, search/filter/sort logic, loading/race conditions, pagination, optimistic rollback, empty/partial/error.
- **Responsive:** stacking, progressive disclosure, overflow strategy, touch size, landscape/zoom, text expansion.
- **A11y:** semantic HTML first; ARIA only where necessary; accessible name/description, announcements, contrast and reduced motion. Follow relevant APG **pattern** rather than casually attaching `role=grid` or `role=menu`.
- **Verification:** component tests, keyboard journey, focus and error behavior, visual viewport screenshot, accessibility check and manual review where required.

## Component decision principles
1. Use native HTML semantics unless custom widget complexity earns its maintenance and testing cost.
2. Distinguish **navigation**, **command/action**, **selection**, **status** and **disclosure**—do not style them into indistinguishable pills.
3. Visual polish comes from consistent spacing, optical alignment, type metrics, surface layers, icon style and purposeful density, not extra shadows/gradients.
4. No hover-only essential controls; no color-only status meaning; no disappearing focus ring; no fake success toasts for failed requests.
5. For complex `grid`, `tree`, `combobox`, `dialog`, `menu`, `tabs` patterns, document actual keyboard and focus contract aligned to APG and test it. Static screenshot inspection is never enough.
6. Shared component changes trigger a cross-route impact inventory and visual regression review; do not silently replace approved baselines.

## Output
Create a short `Component Contract` (component ID/name; scenarios; anatomy; states; keyboard/AT; responsive; styling/token mapping; API/data; edge cases; acceptance tests; owners). Prefer amending the project's component registry or `docs/DESIGN.md`; never generate a redundant design system for every feature.

## References
- W3C WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/patterns/
- WCAG 2.2 target-size and focus rules: https://www.w3.org/TR/WCAG22/
- GOV.UK components: https://design-system.service.gov.uk/components/

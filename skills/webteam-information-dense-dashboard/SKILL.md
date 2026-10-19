---
name: webteam-information-dense-dashboard
description: "Design task-oriented dashboards and analytical workspaces with appropriate density, hierarchy, metric integrity and actionable data visualization."
---

# webteam-information-dense-dashboard

## Purpose and activation
Design task-oriented dashboards and analytical workspaces with appropriate density, hierarchy, metric integrity and actionable data visualization.

**Activate when:** Dashboards, analytics, reporting, operations consoles, KPI monitoring, educational/admin workflows, charts and filter-heavy screens.

**Required inputs:** User decision goals, metric definitions/formulas, data freshness, error ranges, permissions, sample real/synthetic-labelled datasets and business workflows.

## Professional workflow
1. For each audience, write the decisions users must make and their frequency; prioritize exceptions, work queues and trends over decorative KPI tiles.
2. Define every metric: name, calculation, denominator, unit, time grain, comparison period, freshness, caveats and authorized audience. Never invent values.
3. Select chart type based on task (trend→line, comparisons→bar, distribution→histogram/box, relationship→scatter, exact rows→table); avoid pies when accurate comparison is needed.
4. Design cross-filtering, drill-down, actionable states, precise tooltips, comparison periods and data-source explanations; avoid filters that cannot be implemented.
5. Specify density modes (comfortable/compact only if user tasks justify), fixed important headers, accessible chart alternatives, color-blind-safe differentiation and export/print semantics.
6. Handle missing/stale/late data, empty filters, restricted access, giant values, negative values, zero and outliers explicitly.
7. Validate task completion with representative users/QA scenarios and verify responsive tables/charts in real browsers.

## Extended related page patterns (load only when needed)
Distinguish an **operational dashboard** (next action, outstanding work, exception triage) from an **analytical report** (questions, measures, denominators, time range, export). For report/drill-down use **P10** and for incident observability use **P22** in `skill://webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md`. For chart/KPI contracts use **C24** in `skill://webteam-component-interaction-contracts/references/COMPONENT_CATALOG.md`. Avoid forcing all domain work onto metric cards; factual correctness and role-based actionable context have precedence over aesthetics.

## Known anti-patterns
Fake KPIs and trend badges; four identical colorful metrics without user decisions; unlabeled units; decorative gradients on every chart; collapsing complex analysis into random cards.

## Deliverables
Dashboard decision map, metric dictionary, chart/table specification, annotated layout and tests.

## Quality gate / Definition of Done
Every number has defined semantics; primary decisions are quicker; the screen remains functional with zero, many or unavailable results.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving information dense dashboard, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

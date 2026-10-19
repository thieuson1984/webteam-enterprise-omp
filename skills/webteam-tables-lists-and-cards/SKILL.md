---
name: webteam-tables-lists-and-cards
description: "Design sophisticated DataTables, lists, cards, filters and bulk workflows with correct data density and business-task ergonomics."
---

# webteam-tables-lists-and-cards

## Purpose and activation
Design sophisticated DataTables, lists, cards, filters and bulk workflows with correct data density and business-task ergonomics.

**Activate when:** DataTable, CRUD admin, user/course/product lists, searchable directories, dashboards with record grids or comparisons.

**Required inputs:** Actual entities/permissions, data volumes, fields, sorting/filtering needs, row actions, navigation rules, display constraints.

## Professional workflow
1. Select table/list/card based on information structure, not visual habit: table for many aligned attributes/compare, list for scan+action, card for rich visual entity or heterogeneous information.
2. Create explicit column taxonomy: primary identifier, key decision fields, supporting metadata, sortable values, status, actions. Specify widths, alignment, truncation, wrapping and hidden/stacked narrow modes.
3. Model browse/search/filter/save-view/sort/paginate-or-virtualize/bulk-select/export flows with server/client ownership and error boundaries.
4. Design stable density and semantic row states: hover, focus, selected, expanded, disabled, loading, skeleton, stale, validation failure, empty, no-results, permission-limited.
5. Ensure keyboard/screen-reader semantics, table headers, accessible sorting cues, selected-row announcement and focus persistence after edit/delete.
6. Differentiate destructive/bulk actions, confirmation and undo; show units, time zones, pagination totals and consistent row action placement.
7. Validate with 0, 1, 10, 1000 records, text extremes, long localized headers, 320px viewport and huge values; use actual Playwright visual and behavioral tests when available.

## Extended related page patterns (load only when needed)
Search and faceted discovery use **P01**, record-detail and master/detail use **P02**, approvals/admin action queues use **P06**, board/kanban uses **P17**. Refer to `skill://webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md` by matching section. For component-level contracts use **C19** semantic table vs interactive grid, **C20** filters, **C21** cards/list, **C22** treegrid, **C33** pagination/virtualization from `skill://webteam-component-interaction-contracts/references/COMPONENT_CATALOG.md`. Selection across server pages/filtered records and keyboard grid behavior must be explicit; “all rows” is ambiguous until specified.

## Known anti-patterns
All CRUD data as cards; every row having three equal buttons; fake clickable cells; hard-coded table widths; phantom selection; missing zero/filter-empty state; meaningless badge colors.

## Deliverables
Component choice rationale, row/column/action contract, sample responsive states, integration tests and visual baseline scope.

## Quality gate / Definition of Done
Users can scan, compare, filter and act predictably on realistic data without losing context or accessibility.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving tables lists and cards, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

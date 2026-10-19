---
name: webteam-layout-composition-and-rhythm
description: "Create purposeful, proportionally balanced layouts with editorial rhythm, optical alignment and responsive behavior beyond repeated card grids."
---

# webteam-layout-composition-and-rhythm

## Purpose and activation
Create purposeful, proportionally balanced layouts with editorial rhythm, optical alignment and responsive behavior beyond repeated card grids.

**Activate when:** Layout design or redesign, repeated generic cards, poor proportions, responsive issues, visually weak dashboard/landing/setting surfaces.

**Required inputs:** Real content inventory, task priority, viewport matrix, product identity, existing grid/tokens and representative data extremes.

## Professional workflow
1. Prioritize user task and critical content: identify the first five seconds of visual scanning and primary actionable decision.
2. Choose composition family appropriate to the surface: asymmetric editorial split, dense workbench, side-by-side inspector, navigation-first admin, focused single-column form, comparison matrix, or modular story grid.
3. Select max content widths and density tiers based on reading or task type. Use whitespace to group and separate meaning, not as filler.
4. Establish baseline grid, proportion rules, heading alignment, rhythm between regions and treatment of sticky UI. Allow controlled asymmetry when it reinforces focus.
5. Design 320px–wide narrow behavior and large desktops with actual content priority, not simple 3→2→1 card wrapping. Explicitly place search, filters, primary action and critical status.
6. Test longest labels, missing data, 1/1000 records, modal/menus, zoom, orientation and keyboard focus; inspect actual browser rendering.
7. Remove redundant containers, borders, shadows and cards. Prefer transparent grouping or typographic hierarchy when controls are already understandable.

## Known anti-patterns
Every page rendered as heading + four KPI cards + uniform chart tiles; centered everything; redundant boxed sections; cramped overfull 12-column grids; floating elements without meaning.

## Deliverables
Composition rationale and wireframes for primary/narrow/expanded screens, layout tokens, responsive and overflow checklist.

## Quality gate / Definition of Done
The first task is visibly prioritized; composition survives content extremes; dense and expressive screens are distinct while remaining part of one system.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving layout composition and rhythm, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

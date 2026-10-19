---
name: webteam-visual-identity-systems
description: "Engineer distinctive but usable color, surface, icon, texture and visual identity systems backed by semantic design tokens."
---

# webteam-visual-identity-systems

## Purpose and activation
Engineer distinctive but usable color, surface, icon, texture and visual identity systems backed by semantic design tokens.

**Activate when:** Creating or modernizing a palette, introducing themes, tuning visual polish, comparing branded interfaces, or auditing inconsistent color.

**Required inputs:** Design direction, current tokens/CSS, brand constraints, screen captures, target light/dark contexts, content/data state requirements.

## Professional workflow
1. Start with surface and text neutral ramp; pick one principal accent and restrained supporting accents only where useful. Define hue/chroma/lightness relationships rather than independent random hex codes.
2. Declare semantic roles: canvas, surface, raised, inset, border, text primary/secondary, link, interactive, focus, selection, destructive, success, warning, error, information and chart categorical/sequential/diverging.
3. Map roles to real components and states (rest, hover, focus-visible, pressed, selected, disabled, loading). Ensure dark mode is intentionally rebalanced, not simple inversion.
4. Use automatic contrast measurements plus manual review; WCAG 2.2 AA text targets 4.5:1 normally, 3:1 large text; relevant interactive boundaries/non-text 3:1. Confirm exceptions precisely.
5. Test palette on forms, status chips, dense tables, charts and real long-copy screens, not only a hero. Do not communicate meaning by color alone.
6. Create one or two coherent signature elements (editorial rule, sharp grid, illustration language, chart style, materiality) only if they reinforce the product and render well across devices.
7. Export CSS variables or design tokens with stable semantic names; test computed styles and component variants. Record token provenance and migration exceptions.

## Known anti-patterns
Brand-color flooding, neon-on-neon UI, purple-blue gradient as universal default, random glass, 12 unrelated accent colors, opacity-only text that fails contrast.

## Deliverables
Design token map, palette rationale, light/dark samples, iconography/imagery policy, component-state contrast evidence.

## Quality gate / Definition of Done
Semantic state meaning is stable; contrast validated; actual UI screens show recognizable and restrained brand language without overwhelming content.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving visual identity systems, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

---
name: webteam-design-direction-and-taste
description: "Establish a product-specific art direction and critique visual taste before building new or significantly redesigned UI."
---

# webteam-design-direction-and-taste

## Purpose and activation
Establish a product-specific art direction and critique visual taste before building new or significantly redesigned UI.

**Activate when:** New products, major visual redesigns, visually generic proposals, ambiguous branding, or a high-impact page whose design direction is not yet established.

**Required inputs:** PRODUCT.md, approved brand assets, audience, content samples, constraints, existing DESIGN.md/Design DNA, 2–4 licensed/linked references if available.

## Professional workflow
1. Write a one-sentence product character, a three-word design personality, and an anti-personality (what it should NOT feel like). Make them relevant to actual tasks/users, not style buzzwords.
2. Inventory true information hierarchy and user decision points; choose a content-first composition before choosing colors, shadows, effects, or fonts.
3. Explore TWO or THREE materially different directions when the scope is new/major (e.g. editorial, precise utility, distinctive institutional). Vary structural composition, density, tone, hierarchy and interaction model, not only hue.
4. For each direction document audience fit, reference provenance, signature element, typography logic, whitespace density, constraints, risks and implementation cost. Do not copy distinctive competitor identity.
5. Run a substitution test: remove the logo and brand name; explain which elements still make the product distinguishable and useful. If indistinguishable from generic SaaS, revise the information architecture or art direction.
6. Select one recommended direction with explicit rationale and ask for approval when it materially changes established brand identity; record accepted/rejected directions in DESIGN.md.
7. Ask Designer + Product + Frontend to check actual content, usability and implementability. Use reviewer disagreement to identify falsifiable issues rather than cosmetic voting.

## Known anti-patterns
Uniform hero/cards/grid regardless of product; abstract “premium futuristic modern” labels with no visual decisions; copying a screenshot pixel-for-pixel; decorative metrics invented to fill space.

## Deliverables
docs/design/ART_DIRECTION.md or section in DESIGN.md: selected direction, alternatives, signature motifs, density, sources, approvals, exceptions.

## Quality gate / Definition of Done
A collaborator could build a recognizably different product surface from the documented decisions; no contradictory direction, copied brand, fake content or inaccessible contrast.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving design direction and taste, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

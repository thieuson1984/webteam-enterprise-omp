---
name: webteam-design-system-evolution
description: "Preserve existing project Design DNA while evolving shared components and tokens safely through explicit migrations."
---

# webteam-design-system-evolution

## Purpose and activation
Preserve existing project Design DNA while evolving shared components and tokens safely through explicit migrations.

**Activate when:** Existing project work, new component variants, rebranding, shared CSS/token changes, redesigns or UI tech migrations.

**Required inputs:** DESIGN.md and Design DNA, source/token consumers via repo/CBM, screenshot baselines, approved UX decisions and Git diff.

## Professional workflow
1. Classify design change as preserve, normalize, evolve or redesign; determine approval level before touching globals.
2. Inventory token/variant consumers, CSS specificity and per-page exceptions from current source; use CBM only as navigation and confirm real code.
3. Write expected behavioral/visual delta, affected routes and selected rollback mechanism. For significant changes record ADR/design decision.
4. Prototype changed variants in isolation; prefer stable component contracts and tokens over global CSS find/replace.
5. Preserve old behavior until all relevant pages are migrated; compare real screenshots and E2E interaction before/after.
6. Never auto-accept new snapshot baselines just to pass CI; require explicit reviewer confirmation of intentional changes.
7. Update DESIGN.md, component inventory and tests only after actual implementation matches approved evolution.

## Known anti-patterns
Redesigning old app from scratch because it looks dated; global token change without usage audit; blanket shadow/radius rewrites; approving own baseline.

## Deliverables
Change-impact map, migration plan, new/retired tokens, per-route visual deltas and rollback notes.

## Quality gate / Definition of Done
No unexplained regressions and original identity preserved unless explicit redesign approval granted.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving design system evolution, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

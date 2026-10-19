---
name: webteam-uiux-design-critique
description: "Conduct evidence-led design critique with measurable UX defects and qualitative craft assessment; reject aesthetic scoring by model taste alone."
---

# webteam-uiux-design-critique

## Purpose and activation
Conduct evidence-led design critique with measurable UX defects and qualitative craft assessment; reject aesthetic scoring by model taste alone.

**Activate when:** Before approving a major design, after UI implementation, visual inconsistency audit, generic interface complaint or design review.

**Required inputs:** Actual screenshots/DOM, DESIGN.md, target workflows, real content, device matrix, approved brand, evidence and acceptance criteria.

## Professional workflow
1. Separate objective defects (broken layout, contrast, clipping, dead controls) from subjective craft concerns (visual rhythm, generic identity, awkward typography).
2. Run rubric dimensions: product distinction, hierarchy, composition, typography, color/material restraint, content authenticity, component cohesion, interaction quality, accessibility and responsive robustness.
3. For each finding give ID, route, viewport, observed evidence/path/screenshot, expected user outcome, severity, confidence and smallest useful change.
4. Use the brand-blind/substitution test and a purposeful-variation test: do important page types have distinct information structures without fragmenting the design system?
5. Identify monotonous repeated card/grid patterns and unnecessary decorative effects. Do not call something “AI slop” without a specific reproducible reason.
6. Rank by user impact + likelihood + repair cost + regression risk; keep subjective style recommendations optional and require approval for brand-redesign work.
7. Coordinate review with Product, Frontend, Accessibility, QA, and a second independent visual evaluator when justified; screenshot absence is UNVERIFIED, never PASS.

## Extended professional coverage audit
For every explicitly requested page or component, classify it using `webteam-page-experience-patterns` (P01–P22) and/or `webteam-component-interaction-contracts` (C01–C38). Audit **only applicable** contracts and report `NOT_APPLICABLE` for irrelevant domains; do not inflate severity for absent commerce, calendar or complex-grid features unless the product actually requires them. Verify five layers: task completeness, content/data truth, interaction/focus states, responsive/perceptual craft and permission boundaries. Include supported screen evidence and explicit `NOT_RUN` labels for untested behavior. Report objective functionality/a11y failures separately from subjective visual craft suggestions.

## Known anti-patterns
Subjective “looks cheap” without evidence; numeric “professionalism 97/100”; passing accessibility based on appearance; applying generic style unrelated to product.

## Deliverables
Auditable UIUX report, defect ledger, conceptual design critique, prioritized fix list and validation evidence.

## Quality gate / Definition of Done
All high-priority findings are actionable and reproducible; distinguish taste from compliance and intentional variation.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving uiux design critique, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

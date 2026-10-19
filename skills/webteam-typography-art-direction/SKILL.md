---
name: webteam-typography-art-direction
description: "Design editorial-grade typography and font pairing that creates hierarchy, supports the product languages and avoids template-like UI."
---

# webteam-typography-art-direction

## Purpose and activation
Design editorial-grade typography and font pairing that creates hierarchy, supports the product languages and avoids template-like UI.

**Activate when:** Font/pairing selection, inconsistent hierarchy, dashboards with poor scanability, localization, responsive design or visually bland interfaces.

**Required inputs:** Content hierarchy, density needs, target languages including Vietnamese where relevant, font licensing/loading limits, current design tokens.

## Professional workflow
1. Classify content roles before font selection: brand/display, titles, page/section labels, body, annotations, table values, financial numerals and code.
2. Choose ONE purposeful primary family and add a contrast family only when it improves hierarchy. Compare x-height, numeral behavior, weight range, character width, diacritics and fallback metrics.
3. Define a modular but non-mechanical responsive scale with explicit hierarchy (display, H1–H4, body, small, caption); specify weight, leading, tracking, paragraph measure and wrapping behavior.
4. Check long Vietnamese labels, accented names, dates, currency, tabular numerals, empty states and validation copy. Prevent text clipping and layout shift from font loading.
5. Use type as composition: editorial headings can lead marketing; information-dense tools prioritize legible compact body and aligned numerals. Do not apply a giant display type to every admin screen.
6. Test at mobile widths, 200% browser zoom, and with system font fallback. Verify license, caching and payload effects.
7. Document chosen pair, rejected alternatives and implementation mapping to CSS variables/classes.

## Known anti-patterns
Blindly choosing fashionable fonts; excessive mixed families; uniformly bold headings; microscopic table labels; letter spacing that harms Vietnamese glyphs; unverified font licensing.

## Deliverables
Typography direction, role-based CSS tokens, font-loading/fallback plan, locale and zoom snapshots.

## Quality gate / Definition of Done
Clear editorial rhythm and accessible reading speed across dense/marketing screens; numbers and Vietnamese accents align correctly.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving typography art direction, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

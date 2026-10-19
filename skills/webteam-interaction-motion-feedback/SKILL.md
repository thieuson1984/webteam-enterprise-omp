---
name: webteam-interaction-motion-feedback
description: "Define precise interaction behavior, progressive disclosure and meaningful motion with reduced-motion accessibility and functional states."
---

# webteam-interaction-motion-feedback

## Purpose and activation
Define precise interaction behavior, progressive disclosure and meaningful motion with reduced-motion accessibility and functional states.

**Activate when:** Dialogs, menus, filters, onboarding, forms, transitions, complex UI workflows, motion-heavy marketing or usability complaints.

**Required inputs:** User journey, component/state specs, latency/loading behavior, reduced-motion policy, device and accessibility needs.

## Professional workflow
1. List explicit input-trigger → system state → feedback → recovery actions for each component; verify actions exist.
2. Keep interactive affordances consistent and visible across mouse, keyboard and touch; focus state and error announcements cannot be decorative afterthoughts.
3. Choose duration/easing only to clarify continuity, feedback and orientation; allow direct transitions for efficiency-critical data applications.
4. Handle pending, success, failed, no-access, disabled and retry states. Never show optimistic success when server operation fails.
5. Provide reduced-motion alternatives and avoid scroll-jacking, nonessential parallax or focus-moving entrance animations.
6. Test dialog focus trap/restoration, escape/back, portal clipping, mobile overlays and high-latency request behavior.
7. Document component contract for Frontend/QA with event/state tables.

## Known anti-patterns
Buttons with hover effect but no click behavior; motion used to mask latency; distracting constant animation; live states conveyed only by color.

## Deliverables
Interaction state map, motion tokens/constraints, acceptance scenarios and Playwright checks.

## Quality gate / Definition of Done
Every visible control is functional, discoverable and accessible; motion helps rather than dominates.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving interaction motion feedback, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

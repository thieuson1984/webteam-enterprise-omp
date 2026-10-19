---
name: webteam-page-experience-patterns
description: "Design and audit complete page-specific experiences beyond generic dashboards: search, entity detail, workflow/approvals, forms, billing, scheduling, collaboration, files, developer portals, AI-assisted flows, system states and more; use the matching blueprint only."
---

# WebTeam — Page Experience Patterns

## When to use
Use when creating, extending, or auditing a *page or end-to-end journey*, especially page types not covered by the existing dashboard, landing, data-table, and auth/settings skills. Select the relevant page blueprint from [Page Blueprints](references/PAGE_BLUEPRINTS.md) (`skill://webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md`). **Do not read every blueprint for a small task.**

## Responsibility
`webteam-designer` owns the page experience contract. `webteam-product` validates the actual task and language; `webteam-frontend` owns code; `webteam-backend` and `webteam-security` validate data, authorization and operations; `webteam-accessibility` checks semantics/interaction; `webteam-qa` records observed tests and screenshots. Do not invent an additional design agent.

## Page design sequence
1. **Identify the page job.** Who visits? What decision/action must they complete? What data can they actually see? What irreversible actions or privacy boundaries exist? Identify novice/expert and mobile/desktop needs.
2. **Locate its blueprint.** Prefer existing Design DNA, app workflows, reusable components and approved brand; use reference pages for *patterns*, never copy a competitor's visual identity.
3. **Write the content model first.** Record true field names, units, timestamp meaning, status sources, search metadata, realistic min/max values, error cases and permissions. Synthetic fixtures must be labelled.
4. **Select one meaningful layout.** Establish above-the-fold decision hierarchy, action location, page density, nav depth and conditional details; don't force every route into a hero + three cards + uniform grid.
5. **Specify state and action matrix.** Initial/loading/empty/no-results/filtered-empty/partial/error/permission-denied/offline/success/conflict/saving/draft/disabled, as applicable. For each action specify feedback, recoverability, confirmation and focus return.
6. **Specify adaptive behavior.** At narrow width re-prioritize content and interactions; don't simply squeeze desktop columns. Cover keyboard, pointer, touch, zoom, longer Vietnamese strings and assistive technology expectations.
7. **Create testable contracts.** For every important route: purpose, primary/secondary actions, content sources, responsive rules, permissions, component choices, interaction transitions, microcopy, acceptance checks, screenshots and owners.
8. **Validate with the browser when available.** Inspect actual content, not decorative mock data. Compare with approved Design DNA. Document unverified claims and design approvals.

## Pattern selection (read just the matching section)
- **Find/inspect:** search/filter/results, record detail, directory, comparison.
- **Create/operate:** wizard and form, onboarding, admin/access, approval and review, scheduling, file management, CMS/editor.
- **Monitor/collaborate:** analytics/reports, inbox/notifications, activity/history, kanban/workspace, maps/geospatial.
- **Transact/integrate:** pricing/billing/checkout, catalogue/orders, developer/API console, AI assistant.
- **Recover/support:** knowledge/help, error/not-found/maintenance/offline, feedback and incident surfaces.

## Required deliverable — Page Contract
For the scoped route produce:
`PAGE-ID | persona/job | real data and provenance | navigation | primary action | secondary actions | reading order | key states/transitions | responsive priorities | accessibility/keyboard | permission/privacy boundary | copy | tests | open decisions`.
Use concrete sample values *only if supplied or labelled fixture*. Annotate preserved Design DNA versus proposed changes.

## Anti-patterns and stop conditions
Reject identical dashboard/card layouts for fundamentally different tasks; invented metrics; hidden critical actions; no recovery on failure; mobile functionality removed without an alternative; fake permission buttons; notification-only confirmation of irreversible changes. Brand-wide redesign, new paid flows, retention/consent changes, critical authorization changes and production side effects require explicit scope approval. Static inspection cannot be reported as visual/browser verification.

## Acceptance
Every required action is findable, meaningful, authorized and recoverable; dense and empty datasets remain useful; content is real or transparently synthetic; keyboard/touch and mobile pathways are documented; visual differentiation is grounded in the domain instead of novelty for its own sake.

## References
- W3C WAI-ARIA APG patterns: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- MOJ Design System components: https://design-patterns.service.justice.gov.uk/components/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

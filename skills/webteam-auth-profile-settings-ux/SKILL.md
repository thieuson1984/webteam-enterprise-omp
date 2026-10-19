---
name: webteam-auth-profile-settings-ux
description: "Design trustworthy and polished login/logout, onboarding, profile, account and settings experiences with complete edge states and privacy affordances."
---

# webteam-auth-profile-settings-ux

## Purpose and activation
Design trustworthy and polished login/logout, onboarding, profile, account and settings experiences with complete edge states and privacy affordances.

**Activate when:** Login/signup/logout, password reset, account onboarding, user profile, settings, security preference, organization membership.

**Required inputs:** Auth and session requirements, security/privacy policy, access roles, user journeys, real form errors, locales, current design system.

## Professional workflow
1. Choose a focused auth layout without overdecorating security-sensitive forms; show product identity through typography, craft, tone and restrained assets.
2. Map flows: signup, sign-in, SSO if allowed, MFA, recovery, invalid/expired token, lockout, permission denied, redirect, logout and session-expired feedback.
3. Design usable labels, autocomplete, password manager support, recovery paths, validation, status and progressive disclosure; do not reveal sensitive existence/account enumeration.
4. Design profile fields and settings IA around user goals; group by meaning (identity, workspace, preferences, security, notifications, privacy), with clear save/cancel/pending/unsaved states.
5. Ensure destructive settings have deliberate confirmations and account state change feedback; never use deceptive dark patterns.
6. Validate mobile keyboard, autofill, screen-reader announcements, contrast, touch targets, locale/date/time format and navigability.
7. Coordinate with Backend/Security: forms cannot claim authentication/authorization was enforced unless actual server behavior exists.

## Extended related page patterns (load only when needed)
For invitation, organization/workspace switching and first-run activation, load **P04** from `skill://webteam-page-experience-patterns/references/PAGE_BLUEPRINTS.md`. For administrator roles and security-sensitive member settings, load **P05** and the permissions matrix; Backend/Security must confirm actual authorization, not just hidden controls. For session, passkey and OTP control contracts, select **C35/C12** from `skill://webteam-component-interaction-contracts/references/COMPONENT_CATALOG.md`. Include account deletion, reauthentication, recovery, expired invite and conflict in actual page state contract when applicable; do not assume these flows exist.

## Known anti-patterns
Login page with giant irrelevant illustrations; fake social login buttons; unlabeled toggles; hidden security consequences; logout that only routes client-side; destructive settings with silent side effects.

## Deliverables
Auth/account state map, form/content spec, privacy/security UX decisions, tests covering failed and success paths.

## Quality gate / Definition of Done
Every auth and settings action behaves predictably and is operable with keyboard/touch/assistive technology.

## Coordination, boundaries and recovery
Owner: `webteam-designer`. Coordinate with Product for user intent and truthfulness, Frontend for faithful implementation, QA for reproducible functional/visual evidence, Accessibility for WCAG checks, and Reviewer for critical change approval. Read relevant `docs/PRODUCT.md`, `docs/DESIGN.md` and `docs/design/DESIGN_DNA.md` selectively; do not load every design skill at once. For a pre-existing project, preserve confirmed style and behavior by default. For a missing browser, mark actual rendering unverified; do not fabricate visual test results. Escalate changes to brand, permissions, production UX or consequential data displays.

## Task example
Given a scoped request involving auth profile settings ux, state source evidence and user goal, make one bounded design decision, produce implementable design contracts and request actual browser review when available.

## Review checklist
- [ ] Decisions are anchored to the target audience and real workflows.
- [ ] No invented facts or unlicensed reference copying.
- [ ] Components have keyboard, mobile, error/empty and content-extreme states.
- [ ] New identity is distinctive without gratuitous effects.
- [ ] Existing Design DNA remains intact unless approved.
- [ ] Tests, screenshots and approvals are described truthfully.

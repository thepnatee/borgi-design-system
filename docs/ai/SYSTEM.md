# Borgi AI System Rules

## Purpose

This document is the source of truth for AI agents generating Borgi visuals, product specifications, interface copy, and implementation guidance.

## Priority order

When instructions conflict, use this order:

1. Approved product and legal requirements
2. Approved brand and mascot specifications
3. Design tokens and component specifications
4. Screen and flow specifications
5. Shared visual prompt
6. Individual generation prompt

## Product identity rules

- Borgi is a general-purpose booking and reminder SaaS platform.
- Do not interpret the mascot as evidence that Borgi is a pet-care product.
- Generated interfaces must show realistic booking operations, not decorative concept art only.
- Every primary action must be understandable without relying on the mascot.

## Mascot rules

- Use `references/borgi-master.png` as the primary visual reference.
- Preserve the orange-and-cream coat, asymmetric eyes, teal scarf, gold bell, and crooked teal-and-orange propeller beanie.
- Do not redesign Borgi between screens.
- Do not add human hands, long limbs, realistic fur, or pet-care props.
- Use Borgi only when it supports hierarchy, emotion, onboarding, an empty state, or feedback.

## UI generation rules

- Produce implementable product layouts, not mood boards or collages.
- Use clear page hierarchy, navigation, content regions, and primary actions.
- Include realistic labels and data without generating sensitive personal information.
- Keep typography legible and avoid text embedded into complex illustration areas.
- Use consistent spacing, radius, shadow, and icon language.
- Reserve enough whitespace for responsive implementation.

## Required screen states

Each product screen specification must consider:

- Loading
- Empty
- Populated
- Validation
- Success
- Error
- Offline or timeout where relevant
- Permission restricted
- Responsive behavior
- Accessibility

## Prompt construction

A generation prompt should contain:

1. Product and audience context
2. Asset or screen goal
3. Required composition
4. Required content hierarchy
5. Mascot role and scale
6. Brand colors and visual language
7. Negative constraints
8. Aspect ratio and output purpose
9. Quality criteria

## Reference image policy

- Use one mascot master image by default.
- Add one UI-style reference only when necessary.
- Add a third brand reference only if it contributes unique information.
- Never submit the entire reference folder automatically.
- When references conflict, the mascot master and written specification take priority.

## Copy generation rules

- Follow `docs/brand/VOICE-AND-TONE.md`.
- Keep copy concise and action-oriented.
- Do not use jokes for payment, privacy, security, data loss, or destructive actions.
- Generate Thai and English copy as separate localized strings, not mixed-language sentences.

## Quality rejection criteria

Reject output containing:

- A changed mascot identity
- Pet-care positioning
- Garbled or unreadable text
- Floating controls without layout structure
- Duplicate limbs or malformed anatomy
- Inconsistent navigation across related screens
- Missing primary action
- Insufficient contrast
- A decorative layout that cannot reasonably be implemented

## Review checklist

- [ ] Product purpose is clear.
- [ ] Borgi identity matches the canonical specification.
- [ ] UI hierarchy is implementable.
- [ ] Content and labels are legible.
- [ ] No pet-care imagery appears.
- [ ] Brand colors and tokens are respected.
- [ ] Required states and edge cases are documented.
- [ ] Accessibility and localization are considered.

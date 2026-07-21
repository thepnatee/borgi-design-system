# Component Specification Template

## Metadata

- Component:
- Category:
- Status: draft | review | approved | deprecated
- Design owner:
- Engineering owner:

## Purpose

Explain the problem this component solves and when it should be used.

## Anatomy

| Part | Required | Description |
|---|---:|---|
| Container | Yes | |

## Variants

List visual and behavioral variants. Avoid variants that only rename the same behavior.

## Sizes

Document minimum size, padding, icon size, typography, and touch target.

## States

- Default
- Hover
- Focus visible
- Pressed
- Selected
- Disabled
- Loading
- Error
- Success
- Read-only

## Behavior

Describe interaction, keyboard behavior, dismissal, validation, overflow, and asynchronous behavior.

## Content rules

- Label length
- Capitalization
- Icon use
- Truncation
- Localization
- Empty values

## Accessibility

- Semantic role
- Accessible name
- Keyboard interaction
- Focus management
- Contrast
- Screen-reader announcement
- Minimum target size

## Responsive behavior

Describe mobile, tablet, and desktop behavior.

## Tokens

| Property | Token |
|---|---|
| Background | |
| Text | |
| Radius | |
| Spacing | |
| Shadow | |
| Motion | |

## Do

- Add approved examples.

## Do not

- Add prohibited or confusing examples.

## Engineering contract

Document props, events, slots, validation, default values, and breaking-change rules.

## Quality checklist

- [ ] All states exist.
- [ ] Keyboard operation works.
- [ ] Screen-reader behavior is defined.
- [ ] Long Thai and English labels are tested.
- [ ] Loading and error behavior are defined.
- [ ] Tokens are used instead of hard-coded values.

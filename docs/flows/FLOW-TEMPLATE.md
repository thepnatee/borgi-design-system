# Flow Template

Use this template for every Borgi user flow.

## Metadata

- Flow ID:
- Name:
- Owner:
- Status: draft | review | approved | deprecated
- Last updated:
- Related screens:
- Related APIs:

## Goal

Describe the user outcome in one or two sentences.

## Actors

| Actor | Role in this flow |
|---|---|
| Primary actor | |
| Supporting actor | |
| System | |

## Preconditions

- Required account state
- Required permissions
- Required configuration
- Required data

## Entry points

- Screen, deep link, notification, email, QR code, or external integration

## Main flow

| Step | Actor | Screen or service | Action | System response |
|---:|---|---|---|---|
| 1 | | | | |

## Alternative flows

### Alternative A

Describe when the branch occurs and how the user returns to the main flow.

## Error and edge cases

| Case | Expected behavior | Recovery action |
|---|---|---|
| Network unavailable | | |
| Session expired | | |
| Permission denied | | |
| Data changed by another user | | |
| Duplicate submission | | |

## States

- Loading
- Empty
- Validation
- Success
- Partial success
- Error
- Offline
- Permission restricted

## Notifications

List email, LINE, SMS, push, or in-app notifications and their trigger conditions.

## Analytics

| Event | Trigger | Properties |
|---|---|---|
| | | |

## Audit requirements

State which actions must record actor, timestamp, previous value, new value, source, and reason.

## Accessibility

Document focus order, screen-reader labels, keyboard behavior, error announcement, and reduced-motion behavior.

## Acceptance criteria

- [ ] Main path is complete.
- [ ] Alternative paths are documented.
- [ ] Loading, empty, validation, success, and error states are covered.
- [ ] Permissions are defined.
- [ ] Responsive behavior is defined.
- [ ] Analytics and audit events are defined.

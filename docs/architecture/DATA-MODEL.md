# Canonical Data Model

## Core entities

### Workspace
Identity, locale, timezone, booking policy, subscription and status.

### Member
User-to-workspace membership, role, branch scope and status.

### Branch
Location, contact details, timezone override, opening hours and closures.

### Service
Name, description, duration, buffers, price, capacity, booking rules and active status.

### Staff
Member/profile reference, skills, branch assignment, service eligibility and availability rules.

### Resource
Room, equipment or capacity unit required by a service.

### AvailabilityRule
Recurring schedule, date override, closure and effective range.

### Customer
Identity, contact channels, locale, consent, notes and deletion status.

### Appointment
Workspace, service, staff, branch, resources, customer, start/end, status, price snapshot, source and policy snapshot.

### Payment
Appointment, provider, amount, currency, state, external IDs and reconciliation details.

### Notification
Appointment/event reference, template version, channel, recipient, state and attempts.

### AuditEvent
Actor, action, entity, before/after references, source, timestamp and request ID.

## Invariants
- Every business entity is scoped by `workspace_id`.
- Appointment times are stored as UTC and evaluated with a recorded timezone.
- Historical appointments retain service, price and policy snapshots.
- Soft deletion cannot break audit or financial history.
- Email and phone normalization are separate from display values.
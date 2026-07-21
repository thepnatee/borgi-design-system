# Payments

## Supported MVP cases
- Pay later / no payment.
- Full payment during booking.
- Optional deposit.
- Manual payment confirmation for supported workspaces.

## Payment states
`not_required`, `pending`, `authorized`, `paid`, `failed`, `cancelled`, `partially_refunded`, `refunded`.

## Rules
- Amount, currency, tax, discount and deposit are snapshotted on the appointment.
- Payment provider callbacks are verified and processed idempotently.
- A successful provider payment must reconcile to one internal payment record.
- Booking confirmation policy determines whether pending payment reserves a slot.
- Refunds preserve the original payment and create auditable refund records.

## UI requirements
Show price breakdown, payment timing, cancellation/refund policy, processing state and a recoverable failure path. Never display raw provider errors to customers.

## Reporting
Track gross value, successful collections, refunds, outstanding balance, provider fees and reconciliation status. Financial exports require explicit permission.
# Cancel Booking Flow

## Actors
Customer, staff, manager and system.

## Preconditions
Appointment exists, actor is authorized and cancellation policy is available.

## Flow
1. Open appointment details.
2. Select cancel and show policy, fee and refund impact.
3. Require reason when configured.
4. Confirm destructive action.
5. Atomically update appointment status, release capacity and create audit event.
6. Trigger refund when eligible and enqueue notifications.
7. Show cancellation reference and refund expectation.

## Edge cases
Already cancelled, appointment started, refund provider unavailable, concurrent reschedule, notification failure and policy changed since booking. Preserve the appointment record; never hard-delete it.

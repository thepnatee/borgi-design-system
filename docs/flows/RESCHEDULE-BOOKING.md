# Reschedule Booking Flow

## Preconditions
Appointment is reschedulable and the actor can view current availability.

## Flow
1. Open appointment and select reschedule.
2. Keep current slot reserved while the user explores alternatives for a short timeout.
3. Validate service, staff, branch, resource, duration and timezone.
4. Present fee or policy differences before confirmation.
5. Atomically reserve the new slot and release the old slot.
6. Record previous and new values in the audit log.
7. Send updated confirmation and reminders.

## Edge cases
Slot taken during confirmation, price changed, staff unavailable, payment adjustment required, recurring appointment and external calendar sync failure. Failure must leave the original appointment unchanged.

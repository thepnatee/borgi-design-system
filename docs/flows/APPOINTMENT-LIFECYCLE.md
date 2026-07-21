# Appointment Lifecycle

States: `draft`, `pending_payment`, `confirmed`, `checked_in`, `in_progress`, `completed`, `cancelled`, `no_show`, `expired`.

Allowed transitions:
- draft → pending_payment | confirmed | expired
- pending_payment → confirmed | expired | cancelled
- confirmed → checked_in | in_progress | completed | cancelled | no_show
- checked_in → in_progress | completed | cancelled
- in_progress → completed

Every transition records actor, timestamp, reason, source and previous/new state. Terminal states are completed, cancelled, no_show and expired. Corrections require an audited admin action rather than silent mutation.

Rescheduling preserves history and links the old slot to the new slot. Cancellation applies policy, fee and notification rules using the workspace timezone.
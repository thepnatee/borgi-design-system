# Borgi Product Scope

## Product goal

Borgi is a multi-business booking and reminder platform. It helps businesses publish services, manage availability, accept bookings, communicate with customers, reduce no-shows, and review operations.

## Product principles

- Booking must be fast for customers.
- Daily operations must be visible at a glance.
- Every state needs loading, empty, success, validation, error, and permission behavior.
- The system must support different service industries without becoming industry-specific.
- Mobile layouts are task-focused; desktop layouts favor operational density.

## Roles

| Role | Primary responsibility |
|---|---|
| Owner | Workspace, billing, policy, full access |
| Admin | Operations, configuration, reporting |
| Manager | Team and branch operations |
| Staff | Assigned schedule and appointment handling |
| Customer | Create and manage personal bookings |
| Guest | Browse and start booking without an account |

## MVP modules

### Marketing

- Landing page
- Features
- Pricing
- Contact and help entry points

### Authentication

- Sign in
- Sign up
- Password recovery
- Email or OTP verification
- Invitation acceptance

### Onboarding

- Workspace creation
- Business profile
- Timezone and locale
- Branch setup
- Service setup
- Staff setup
- Availability setup
- Booking page preview

### Customer booking

- Business or booking landing
- Service selection
- Branch selection
- Staff preference
- Date and time selection
- Customer information
- Booking summary
- Optional payment
- Confirmation
- Cancel and reschedule

### Admin operations

- Dashboard
- Today view
- Calendar
- Appointments
- Customers
- Services
- Staff
- Branches
- Rooms and resources
- Notifications and reminders
- Reports
- Settings

### Commercial

- Plans and subscription
- Billing profile
- Invoices and receipts
- Payment configuration

## Post-MVP modules

- Waitlist
- Packages and memberships
- Coupons and campaigns
- Feedback and review collection
- Advanced automation
- External calendar synchronization
- Webhooks and API access
- Multi-brand workspace
- Enterprise SSO
- Advanced audit and compliance controls

## Explicitly out of scope for initial MVP

- Medical diagnosis or clinical records
- Marketplace discovery across unrelated businesses
- Delivery and inventory management
- Payroll
- Full accounting
- Pet-care-specific workflows
- Social network features

## Cross-cutting requirements

### Accessibility

Target WCAG 2.2 AA for color contrast, keyboard access, focus visibility, labels, and error messaging.

### Localization

Support Thai and English from the beginning. Dates, timezones, phone numbers, and currency must be locale-aware.

### Privacy

Collect only necessary customer data. Sensitive fields require explicit purpose, access control, retention policy, and auditability.

### Responsive behavior

- Mobile: single-column task flows and bottom actions
- Tablet: adaptive split views where useful
- Desktop: side navigation, dense tables, multi-column dashboards

### Product quality gate

A feature is not complete until its happy path, loading, empty, validation, failure, permission, responsive, accessibility, analytics, and audit requirements are documented.

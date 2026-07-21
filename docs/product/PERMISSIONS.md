# Permissions

## Roles

### Owner
Full workspace access, billing, security, integrations, role assignment and deletion/export controls.

### Admin
Manage operations, services, staff, customers, reports and notifications. Cannot transfer ownership or access owner-only security settings unless explicitly granted.

### Staff
View and manage assigned appointments, availability and permitted customer details. Cannot view billing or organization-wide reports by default.

### Viewer
Read-only access to selected dashboards, calendars and reports.

## Permission domains
`workspace`, `members`, `branches`, `services`, `resources`, `appointments`, `customers`, `communications`, `reports`, `billing`, `integrations`, `audit`.

Actions use `view`, `create`, `update`, `delete`, `export`, `manage`.

## Rules
- Deny by default.
- Workspace and branch scope are always enforced server-side.
- UI visibility never replaces API authorization.
- Sensitive exports require an explicit permission and audit event.
- Role or permission changes invalidate relevant sessions or cached authorization.
- Owners cannot remove the last active owner.
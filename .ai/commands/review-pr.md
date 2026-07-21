# Pull Request Review Workflow

Review the change against the repository source of truth, not only the diff description.

## Review order

1. Product scope and SME value
2. Tenant isolation and permissions
3. Domain and data integrity
4. API compatibility and idempotency
5. UX states and accessibility
6. Payment or LINE specialist checks when relevant
7. Tests, observability, migration and rollback
8. Documentation and analytics updates

## Output

Separate findings into:

- `blocker` — unsafe, incorrect, data-loss, security or tenant-isolation risk
- `required` — incomplete production behavior or violated standard
- `suggestion` — useful improvement that does not block this MVP slice
- `backlog` — valid idea explicitly excluded from this PR

For every finding, cite the affected file or requirement and propose the smallest correction. Do not request speculative abstractions.
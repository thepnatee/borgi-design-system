# New Feature Workflow

Use this workflow before writing implementation code.

## Input

Feature name, target user and observed problem.

## Steps

1. Read `AGENTS.md` and `.ai/context/product.md`.
2. Ask the Product Owner Agent to classify the feature.
3. Ask the SME Advisor to review setup and daily operation.
4. Define the smallest production-ready vertical slice.
5. Ask the Solution Architect for data, API, security and failure behavior.
6. Use specialist reviewers when payment or LINE is involved.
7. Produce implementation tasks and a QA/release plan.

## Required artifact

```markdown
# Feature
## Customer problem
## Evidence
## Scope classification
## User story
## Acceptance criteria
## Out of scope
## UX states
## Data/API impact
## Security and tenant impact
## Analytics
## Test plan
## Rollout and rollback
```

Stop and move the feature to backlog when the customer problem or evidence is insufficient.
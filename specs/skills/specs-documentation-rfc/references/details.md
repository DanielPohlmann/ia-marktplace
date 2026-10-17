<!-- Part of the specs-documentation-rfc skill. Loaded on demand from SKILL.md. -->

# RFC (Request for Comments) / Design Documents — details

## RFC Workflow

```
Draft  -->  Review  -->  Accepted  -->  Implementation
                 |                            |
                 |                            v
                 +------>  Rejected       ADR(s) Created
                 |
                 +------>  Withdrawn
```

### Workflow Stages

| Stage | Description | Duration |
|-------|-------------|----------|
| **Draft** | Author writes the RFC and shares it for early informal feedback | 1-5 days |
| **Review** | RFC is formally submitted for team review. Comments, questions, and suggestions are collected | 3-10 business days |
| **Accepted** | The proposal is approved. Implementation can begin. Final decisions are recorded as ADRs | Decision point |
| **Rejected** | The proposal is declined with documented reasoning. May be revised and resubmitted | Decision point |
| **Withdrawn** | The author withdraws the RFC (context changed, better approach found, no longer needed) | Any time |

### Review Process

1. **Author submits the RFC** as a pull request or shared document.
2. **Reviewers are assigned** -- typically tech leads, architects, and affected team members.
3. **Review period opens** -- minimum duration (e.g., 5 business days) to ensure everyone has time to read and respond.
4. **Discussion happens** -- inline comments, meeting discussions, or async threads.
5. **Author addresses feedback** -- revises the RFC or explains why feedback was not incorporated.
6. **Decision is made** -- the designated decision-maker (tech lead, architecture council) accepts or rejects.
7. **Outcome is recorded** -- if accepted, create ADRs for the key decisions. If rejected, document the reasoning.

## Managing RFCs

### Where to Store RFCs

| Location | Convention |
|----------|-----------|
| `docs/rfcs/` | Dedicated RFC directory |
| `docs/design/` | Combined with other design documents |
| Pull requests | RFC as a PR -- discussion happens in PR comments |
| Wiki | Confluence, Notion, or GitHub Wiki |

### RFC as a Pull Request

A popular pattern is to submit the RFC as a PR to the `docs/rfcs/` directory:

1. Create a branch: `rfc/graphql-migration`
2. Add the RFC file: `docs/rfcs/2025-01-graphql-migration.md`
3. Open a PR with the RFC content
4. Team reviews and comments on the PR
5. Author revises based on feedback
6. PR is merged when the RFC is accepted (or closed if rejected)

This approach leverages existing code review tools for RFC review.

### Numbering and Naming

```
docs/rfcs/
  001-adopt-graphql-for-bff.md
  002-migrate-to-kubernetes.md
  003-implement-event-sourcing.md
```

or date-based:

```
docs/rfcs/
  2025-01-graphql-migration.md
  2025-02-kubernetes-migration.md
  2025-03-event-sourcing.md
```

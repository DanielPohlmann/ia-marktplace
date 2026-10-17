<!-- Part of the specs-documentation-adr skill. Loaded on demand from SKILL.md. -->

# Architecture Decision Records (ADR) — details

## ADR Lifecycle

```
Proposed  -->  Accepted  -->  Deprecated
                  |                |
                  |                v
                  +--------->  Superseded by ADR-NNNN
```

| Status | Meaning |
|--------|---------|
| **Proposed** | Decision is under discussion, not yet finalized |
| **Accepted** | Decision has been agreed upon and is in effect |
| **Deprecated** | Decision is no longer relevant (system decommissioned, context changed) |
| **Superseded** | A newer ADR replaces this one. Link to the superseding ADR |

### Superseding an ADR

When a decision is replaced, update both the old and new ADRs:

**Old ADR (updated):**
```markdown
## Status
Superseded by [ADR-0015](0015-switch-to-kafka-for-messaging.md)
```

**New ADR:**
```markdown
## Status
Accepted. Supersedes [ADR-0004](0004-use-rabbitmq-for-async-messaging.md)

## Context
Since ADR-0004 was accepted, our message volume has grown from 1,000/min
to 50,000/min. RabbitMQ's single-node architecture cannot sustain this
throughput without significant operational complexity...
```

## adr-tools CLI

[adr-tools](https://github.com/npryce/adr-tools) is a command-line tool for managing ADRs.

### Installation

```bash
# macOS
brew install adr-tools

# npm (cross-platform)
npm install -g adr-tools

# Manual
git clone https://github.com/npryce/adr-tools.git
cd adr-tools && sudo make install
```

### Usage

```bash
# Initialize ADR directory
adr init docs/decisions

# Create a new ADR
adr new "Use PostgreSQL as Primary Database"
# Creates: docs/decisions/0003-use-postgresql-as-primary-database.md

# Create a new ADR that supersedes an existing one
adr new -s 4 "Switch to Kafka for Async Messaging"
# Creates new ADR and updates ADR-0004 status to "Superseded"

# List all ADRs
adr list

# Generate a table of contents
adr generate toc

# Generate a dependency graph
adr generate graph | dot -Tpng -o adr-graph.png

# Link two ADRs
adr link 5 "Complements" 3 "Is complemented by"
```

### adr-tools Template

When you run `adr new`, it generates a file with this template:

```markdown
# [NUMBER]. [TITLE]

Date: YYYY-MM-DD

## Status

Proposed

## Context

[Describe the context here]

## Decision

[Describe the decision here]

## Consequences

[Describe the consequences here]
```

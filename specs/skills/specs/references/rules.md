# Specifications & Architecture Documentation Rules

Best practices and rules for Specifications & Architecture Documentation.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start with a C4 Context diagram before diving into... | MEDIUM | [`specs-start-with-a-c4-context-diagram-before-diving-into.md`](specs-start-with-a-c4-context-diagram-before-diving-into.md) |
| 2 | Use ADRs to record every significant architecture decision... | MEDIUM | [`specs-use-adrs-to-record-every-significant-architecture-decision.md`](specs-use-adrs-to-record-every-significant-architecture-decision.md) |
| 3 | Write Gherkin scenarios alongside PRDs so acceptance... | MEDIUM | [`specs-write-gherkin-scenarios-alongside-prds-so-acceptance.md`](specs-write-gherkin-scenarios-alongside-prds-so-acceptance.md) |
| 4 | Use Mermaid for diagrams embedded in Markdown docs (PRs,... | MEDIUM | [`specs-use-mermaid-for-diagrams-embedded-in-markdown-docs-prs.md`](specs-use-mermaid-for-diagrams-embedded-in-markdown-docs-prs.md) |
| 5 | Use spec-driven tools like GitHub Spec Kit to automate the... | MEDIUM | [`specs-use-spec-driven-tools-like-github-spec-kit-to-automate-the.md`](specs-use-spec-driven-tools-like-github-spec-kit-to-automate-the.md) |
| 6 | Keep diagrams as code (Mermaid, D2, PlantUML, Structurizr... | MEDIUM | [`specs-keep-diagrams-as-code-mermaid-d2-plantuml-structurizr.md`](specs-keep-diagrams-as-code-mermaid-d2-plantuml-structurizr.md) |

---

---
title: "Keep diagrams as code (Mermaid, D2, PlantUML, Structurizr..."
impact: MEDIUM
impactDescription: "general best practice"
tags: specs, specification-driven-development, architecture-documentation-strategy, choosing-diagram-types
---

## Keep diagrams as code (Mermaid, D2, PlantUML, Structurizr...

Keep diagrams as code (Mermaid, D2, PlantUML, Structurizr DSL) and version them in Git alongside the source code they describe.

---

---
title: "Start with a C4 Context diagram before diving into..."
impact: MEDIUM
impactDescription: "general best practice"
tags: specs, specification-driven-development, architecture-documentation-strategy, choosing-diagram-types
---

## Start with a C4 Context diagram before diving into...

Start with a C4 Context diagram before diving into implementation — it forces you to define system boundaries and external dependencies.

---

---
title: "Use ADRs to record every significant architecture decision..."
impact: MEDIUM
impactDescription: "general best practice"
tags: specs, specification-driven-development, architecture-documentation-strategy, choosing-diagram-types
---

## Use ADRs to record every significant architecture decision...

Use ADRs to record every significant architecture decision so future developers understand the "why" behind the "what."

---

---
title: "Use Mermaid for diagrams embedded in Markdown docs (PRs,..."
impact: MEDIUM
impactDescription: "general best practice"
tags: specs, specification-driven-development, architecture-documentation-strategy, choosing-diagram-types
---

## Use Mermaid for diagrams embedded in Markdown docs (PRs,...

Use Mermaid for diagrams embedded in Markdown docs (PRs, ADRs, RFCs) — it renders natively on GitHub.

---

---
title: "Use spec-driven tools like GitHub Spec Kit to automate the..."
impact: MEDIUM
impactDescription: "general best practice"
tags: specs, specification-driven-development, architecture-documentation-strategy, choosing-diagram-types
---

## Use spec-driven tools like GitHub Spec Kit to automate the...

Use spec-driven tools like GitHub Spec Kit to automate the spec → plan → tasks → implementation pipeline.

---

---
title: "Write Gherkin scenarios alongside PRDs so acceptance..."
impact: MEDIUM
impactDescription: "general best practice"
tags: specs, specification-driven-development, architecture-documentation-strategy, choosing-diagram-types
---

## Write Gherkin scenarios alongside PRDs so acceptance...

Write Gherkin scenarios alongside PRDs so acceptance criteria are executable from day one.

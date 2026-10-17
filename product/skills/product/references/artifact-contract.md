# Artifact contract

## Folder layout

```
docs/product/<slug>/
  01-ideation.md
  02-design.md
  prototype/<screen>.html
  03-architecture.md
```

Stage 3's Event Storming lives where the project keeps them (default `.planning/event-storming/<slug>.md`), linked from `03-architecture.md`.

## Frontmatter

```yaml
---
idea: <slug>
stage: ideation | design | architecture
status: draft | in-review | approved
approved_on:
inputs: []
---
```

`inputs` lists the artifacts the stage consumed (e.g. `[01-ideation.md]`). `approved_on` is empty unless approved.

## Transitions

| From | To | Trigger |
|---|---|---|
| — | `draft` | stage creates the file |
| `draft` | `in-review` | self-review done, approval requested |
| `in-review` | `draft` | user requested changes |
| `in-review` | `approved` | explicit user approval in chat |
| `approved` | `draft` | user reopens; later artifacts also go to `draft` |

## Change log

Every artifact ends with:

```markdown
## Change log

| Date | Change |
|---|---|
| YYYY-MM-DD | Created |
```

One row per status change or substantive edit.

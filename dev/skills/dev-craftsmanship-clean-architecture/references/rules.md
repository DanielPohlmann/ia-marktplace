# Clean Architecture Rules

Best practices and rules for Clean Architecture.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Enforce the Dependency Rule with linter rules or... | HIGH | [`clean-architecture-enforce-the-dependency-rule-with-linter-rules-or.md`](clean-architecture-enforce-the-dependency-rule-with-linter-rules-or.md) |
| 2 | Defer framework decisions as long as possible | MEDIUM | [`clean-architecture-defer-framework-decisions-as-long-as-possible.md`](clean-architecture-defer-framework-decisions-as-long-as-possible.md) |
| 3 | Keep Use Cases as pure orchestrators | MEDIUM | [`clean-architecture-keep-use-cases-as-pure-orchestrators.md`](clean-architecture-keep-use-cases-as-pure-orchestrators.md) |
| 4 | Use the Humble Object pattern at every boundary to maximize... | MEDIUM | [`clean-architecture-use-the-humble-object-pattern-at-every-boundary-to-maximize.md`](clean-architecture-use-the-humble-object-pattern-at-every-boundary-to-maximize.md) |
| 5 | Name modules after business capabilities, not technical... | MEDIUM | [`clean-architecture-name-modules-after-business-capabilities-not-technical.md`](clean-architecture-name-modules-after-business-capabilities-not-technical.md) |
| 6 | Test inner layers with unit tests (fast, no I/O) | MEDIUM | [`clean-architecture-test-inner-layers-with-unit-tests-fast-no-i-o.md`](clean-architecture-test-inner-layers-with-unit-tests-fast-no-i-o.md) |
| 7 | When in doubt about which layer something belongs to, ask | MEDIUM | [`clean-architecture-when-in-doubt-about-which-layer-something-belongs-to-ask.md`](clean-architecture-when-in-doubt-about-which-layer-something-belongs-to-ask.md) |

---

---
title: "Defer framework decisions as long as possible"
impact: MEDIUM
impactDescription: "general best practice"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## Defer framework decisions as long as possible

Defer framework decisions as long as possible. The architecture should work without Express, React, or PostgreSQL.

---

---
title: "Enforce the Dependency Rule with linter rules or..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## Enforce the Dependency Rule with linter rules or...

Enforce the Dependency Rule with linter rules or architectural tests (e.g., ArchUnit, dependency-cruiser).

---

---
title: "Keep Use Cases as pure orchestrators"
impact: MEDIUM
impactDescription: "general best practice"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## Keep Use Cases as pure orchestrators

Keep Use Cases as pure orchestrators — they call Entities and Ports but contain minimal logic themselves.

---

---
title: "Name modules after business capabilities, not technical..."
impact: MEDIUM
impactDescription: "general best practice"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## Name modules after business capabilities, not technical...

Name modules after business capabilities, not technical layers — let the architecture scream.

---

---
title: "Test inner layers with unit tests (fast, no I/O)"
impact: MEDIUM
impactDescription: "general best practice"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## Test inner layers with unit tests (fast, no I/O)

Test inner layers with unit tests (fast, no I/O). Test boundaries with integration tests. Test the outermost layer with end-to-end tests sparingly.

---

---
title: "Use the Humble Object pattern at every boundary to maximize..."
impact: MEDIUM
impactDescription: "general best practice"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## Use the Humble Object pattern at every boundary to maximize...

Use the Humble Object pattern at every boundary to maximize testable code.

---

---
title: "When in doubt about which layer something belongs to, ask"
impact: MEDIUM
impactDescription: "general best practice"
tags: clean-architecture, dev, craftsmanship, dependency-rule-enforcement, layer-separation, boundary-design
---

## When in doubt about which layer something belongs to, ask

When in doubt about which layer something belongs to, ask: "If I change the database / framework / UI, does this need to change?" If yes, it belongs in an outer layer.

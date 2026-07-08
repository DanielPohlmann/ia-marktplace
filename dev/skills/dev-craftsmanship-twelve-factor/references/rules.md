# Twelve-Factor App Rules

Best practices and rules for Twelve-Factor App.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Treat the twelve factors as a checklist during architecture... | MEDIUM | [`twelve-factor-treat-the-twelve-factors-as-a-checklist-during-architecture.md`](twelve-factor-treat-the-twelve-factors-as-a-checklist-during-architecture.md) |
| 2 | Adopt factors incrementally | CRITICAL | [`twelve-factor-adopt-factors-incrementally.md`](twelve-factor-adopt-factors-incrementally.md) |
| 3 | Use containers (Docker) as the natural packaging for... | HIGH | [`twelve-factor-use-containers-docker-as-the-natural-packaging-for.md`](twelve-factor-use-containers-docker-as-the-natural-packaging-for.md) |
| 4 | Combine twelve-factor with cloud-native patterns | MEDIUM | [`twelve-factor-combine-twelve-factor-with-cloud-native-patterns.md`](twelve-factor-combine-twelve-factor-with-cloud-native-patterns.md) |
| 5 | Automate compliance | CRITICAL | [`twelve-factor-automate-compliance.md`](twelve-factor-automate-compliance.md) |
| 6 | When twelve-factor conflicts with pragmatism (e | MEDIUM | [`twelve-factor-when-twelve-factor-conflicts-with-pragmatism-e.md`](twelve-factor-when-twelve-factor-conflicts-with-pragmatism-e.md) |

---

---
title: "Adopt factors incrementally"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: twelve-factor, dev, craftsmanship, cloud-native-app-design, environment-configuration, stateless-process-design
---

## Adopt factors incrementally

Adopt factors incrementally — you do not need to satisfy all twelve on day one.

---

---
title: "Automate compliance"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: twelve-factor, dev, craftsmanship, cloud-native-app-design, environment-configuration, stateless-process-design
---

## Automate compliance

Automate compliance: use CI checks to verify no secrets in code (Factor III), lock files present (Factor II), and health endpoints exist (Factor IX).

---

---
title: "Combine twelve-factor with cloud-native patterns"
impact: MEDIUM
impactDescription: "general best practice"
tags: twelve-factor, dev, craftsmanship, cloud-native-app-design, environment-configuration, stateless-process-design
---

## Combine twelve-factor with cloud-native patterns

Combine twelve-factor with cloud-native patterns: circuit breakers, retries with backoff, health checks, and graceful degradation.

---

---
title: "Treat the twelve factors as a checklist during architecture..."
impact: MEDIUM
impactDescription: "general best practice"
tags: twelve-factor, dev, craftsmanship, cloud-native-app-design, environment-configuration, stateless-process-design
---

## Treat the twelve factors as a checklist during architecture...

Treat the twelve factors as a checklist during architecture reviews and pull requests.

---

---
title: "Use containers (Docker) as the natural packaging for..."
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: twelve-factor, dev, craftsmanship, cloud-native-app-design, environment-configuration, stateless-process-design
---

## Use containers (Docker) as the natural packaging for...

Use containers (Docker) as the natural packaging for twelve-factor apps: they enforce dependency isolation, port binding, and process disposability.

---

---
title: "When twelve-factor conflicts with pragmatism (e"
impact: MEDIUM
impactDescription: "general best practice"
tags: twelve-factor, dev, craftsmanship, cloud-native-app-design, environment-configuration, stateless-process-design
---

## When twelve-factor conflicts with pragmatism (e

When twelve-factor conflicts with pragmatism (e.g., local file caching for performance), document the deviation and contain the blast radius.

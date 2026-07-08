# Threat Modeling Rules

Best practices and rules for Threat Modeling.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Start simple and iterate | CRITICAL | [`threat-modeling-start-simple-and-iterate.md`](threat-modeling-start-simple-and-iterate.md) |
| 2 | Involve the whole team | CRITICAL | [`threat-modeling-involve-the-whole-team.md`](threat-modeling-involve-the-whole-team.md) |
| 3 | Use DFDs as the common language | CRITICAL | [`threat-modeling-use-dfds-as-the-common-language.md`](threat-modeling-use-dfds-as-the-common-language.md) |
| 4 | Prioritize ruthlessly with DREAD | MEDIUM | [`threat-modeling-prioritize-ruthlessly-with-dread.md`](threat-modeling-prioritize-ruthlessly-with-dread.md) |
| 5 | Track threats as first-class backlog items | MEDIUM | [`threat-modeling-track-threats-as-first-class-backlog-items.md`](threat-modeling-track-threats-as-first-class-backlog-items.md) |
| 6 | Keep the threat model alive | MEDIUM | [`threat-modeling-keep-the-threat-model-alive.md`](threat-modeling-keep-the-threat-model-alive.md) |

---

---
title: "Involve the whole team"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: threat-modeling, security, stride, dread
---

## Involve the whole team

Involve the whole team: threat modeling is not solely a security engineer's responsibility. Developers, architects, and product owners all bring essential context about how the system works and what matters most to protect.

---

---
title: "Keep the threat model alive"
impact: MEDIUM
impactDescription: "general best practice"
tags: threat-modeling, security, stride, dread
---

## Keep the threat model alive

Keep the threat model alive: a threat model is a living document. Store it alongside the code (e.g., in the repository), version it, and update it as the system evolves.

---

---
title: "Prioritize ruthlessly with DREAD"
impact: MEDIUM
impactDescription: "general best practice"
tags: threat-modeling, security, stride, dread
---

## Prioritize ruthlessly with DREAD

Prioritize ruthlessly with DREAD: not all threats are equal. Use quantitative scoring to focus mitigation effort on the threats with the highest combined impact and likelihood.

---

---
title: "Start simple and iterate"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: threat-modeling, security, stride, dread
---

## Start simple and iterate

Start simple and iterate: a basic threat model that covers the most critical data flows is far more valuable than a perfect model that never gets completed. Use the four-question framework as a starting point.

---

---
title: "Track threats as first-class backlog items"
impact: MEDIUM
impactDescription: "general best practice"
tags: threat-modeling, security, stride, dread
---

## Track threats as first-class backlog items

Track threats as first-class backlog items: identified threats and their mitigations should be tracked alongside feature work in the project management system, with clear ownership and deadlines.

---

---
title: "Use DFDs as the common language"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: threat-modeling, security, stride, dread
---

## Use DFDs as the common language

Use DFDs as the common language: data flow diagrams provide a shared visual representation that bridges the gap between technical implementation details and security analysis.

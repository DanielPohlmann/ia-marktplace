# Security Rules

Best practices and rules for Security.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Defense in depth | CRITICAL | [`security-defense-in-depth.md`](security-defense-in-depth.md) |
| 2 | Least privilege | MEDIUM | [`security-least-privilege.md`](security-least-privilege.md) |
| 3 | Secure defaults | CRITICAL | [`security-secure-defaults.md`](security-secure-defaults.md) |
| 4 | Shift left | CRITICAL | [`security-shift-left.md`](security-shift-left.md) |
| 5 | Zero trust mindset | MEDIUM | [`security-zero-trust-mindset.md`](security-zero-trust-mindset.md) |
| 6 | Automate security gates | CRITICAL | [`security-automate-security-gates.md`](security-automate-security-gates.md) |
| 7 | Keep dependencies current | MEDIUM | [`security-keep-dependencies-current.md`](security-keep-dependencies-current.md) |
| 8 | Treat security as a team responsibility | CRITICAL | [`security-treat-security-as-a-team-responsibility.md`](security-treat-security-as-a-team-responsibility.md) |

---

---
title: "Automate security gates"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Automate security gates

Automate security gates: use CI/CD pipelines to enforce security scanning, secret detection, and compliance checks before code reaches production.

---

---
title: "Defense in depth"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Defense in depth

Defense in depth: never rely on a single security control; layer multiple defenses so that a failure in one does not compromise the system.

---

---
title: "Keep dependencies current"
impact: MEDIUM
impactDescription: "general best practice"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Keep dependencies current

Keep dependencies current: regularly update libraries and frameworks, monitor for CVEs, and generate Software Bills of Materials (SBOMs) for auditability.

---

---
title: "Least privilege"
impact: MEDIUM
impactDescription: "general best practice"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Least privilege

Least privilege: grant the minimum permissions necessary for any user, service, or process to perform its function.

---

---
title: "Secure defaults"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Secure defaults

Secure defaults: ship systems in a secure configuration; require explicit action to weaken security posture rather than to strengthen it.

---

---
title: "Shift left"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Shift left

Shift left: integrate security analysis (threat modeling, SAST, dependency scanning) as early as possible in the development lifecycle.

---

---
title: "Treat security as a team responsibility"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Treat security as a team responsibility

Treat security as a team responsibility: security is not solely the security team's job; every developer, operator, and architect shares accountability for building and maintaining secure systems.

---

---
title: "Zero trust mindset"
impact: MEDIUM
impactDescription: "general best practice"
tags: security, application-security-strategy, security-architecture, choosing-security-controls
---

## Zero trust mindset

Zero trust mindset: authenticate and authorize every request regardless of network location; assume the perimeter has already been breached.

# Secure SDLC Rules

Best practices and rules for Secure SDLC.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Automate security checks in CI/CD | CRITICAL | [`secure-sdlc-automate-security-checks-in-ci-cd.md`](secure-sdlc-automate-security-checks-in-ci-cd.md) |
| 2 | Define clear severity thresholds for gate blocking | CRITICAL | [`secure-sdlc-define-clear-severity-thresholds-for-gate-blocking.md`](secure-sdlc-define-clear-severity-thresholds-for-gate-blocking.md) |
| 3 | Maintain a living threat model | MEDIUM | [`secure-sdlc-maintain-a-living-threat-model.md`](secure-sdlc-maintain-a-living-threat-model.md) |
| 4 | Invest in developer security training | CRITICAL | [`secure-sdlc-invest-in-developer-security-training.md`](secure-sdlc-invest-in-developer-security-training.md) |
| 5 | Track security debt explicitly | CRITICAL | [`secure-sdlc-track-security-debt-explicitly.md`](secure-sdlc-track-security-debt-explicitly.md) |
| 6 | Use security as code | CRITICAL | [`secure-sdlc-use-security-as-code.md`](secure-sdlc-use-security-as-code.md) |
| 7 | Conduct regular retrospectives on security incidents | CRITICAL | [`secure-sdlc-conduct-regular-retrospectives-on-security-incidents.md`](secure-sdlc-conduct-regular-retrospectives-on-security-incidents.md) |
| 8 | Establish metrics and report on them | CRITICAL | [`secure-sdlc-establish-metrics-and-report-on-them.md`](secure-sdlc-establish-metrics-and-report-on-them.md) |

---

---
title: "Automate security checks in CI/CD"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Automate security checks in CI/CD

Automate security checks in CI/CD: manual-only security processes do not scale and create bottlenecks; automate SAST, SCA, secrets scanning, and container scanning as pipeline stages.

---

---
title: "Conduct regular retrospectives on security incidents"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Conduct regular retrospectives on security incidents

Conduct regular retrospectives on security incidents: blameless postmortems improve process; feed findings back into security requirements and automated checks.

---

---
title: "Define clear severity thresholds for gate blocking"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Define clear severity thresholds for gate blocking

Define clear severity thresholds for gate blocking: not every finding should block a deployment; establish policies for which severity levels (e.g., critical and high) are gate-blockers versus tracked issues.

---

---
title: "Establish metrics and report on them"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Establish metrics and report on them

Establish metrics and report on them: track mean time to remediate, gate pass/fail rates, security debt trends, and champion program participation to demonstrate program effectiveness and justify investment.

---

---
title: "Invest in developer security training"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Invest in developer security training

Invest in developer security training: annual secure coding training is a minimum; supplement with hands-on exercises, CTF events, and lessons learned from real incidents.

---

---
title: "Maintain a living threat model"
impact: MEDIUM
impactDescription: "general best practice"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Maintain a living threat model

Maintain a living threat model: update threat models when architecture changes, new features are added, or new attack vectors emerge; stale threat models provide false confidence.

---

---
title: "Track security debt explicitly"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Track security debt explicitly

Track security debt explicitly: log security findings that are accepted or deferred as security debt with clear ownership, timelines, and risk acceptance sign-off.

---

---
title: "Use security as code"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: secure-sdlc, security, devsecops, shift-left-security
---

## Use security as code

Use security as code: express security policies, configurations, and checks as version-controlled code (e.g., OPA policies, security-as-code frameworks) for auditability and repeatability.

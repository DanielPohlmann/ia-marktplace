# Security Testing Tools Rules

Best practices and rules for Security Testing Tools.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Layer multiple testing approaches | CRITICAL | [`security-testing-layer-multiple-testing-approaches.md`](security-testing-layer-multiple-testing-approaches.md) |
| 2 | Integrate security testing into CI/CD as quality gates | CRITICAL | [`security-testing-integrate-security-testing-into-ci-cd-as-quality-gates.md`](security-testing-integrate-security-testing-into-ci-cd-as-quality-gates.md) |
| 3 | Tune tools aggressively to reduce false positives | MEDIUM | [`security-testing-tune-tools-aggressively-to-reduce-false-positives.md`](security-testing-tune-tools-aggressively-to-reduce-false-positives.md) |
| 4 | Enable incremental scanning | MEDIUM | [`security-testing-enable-incremental-scanning.md`](security-testing-enable-incremental-scanning.md) |
| 5 | Generate and store SBOMs | MEDIUM | [`security-testing-generate-and-store-sboms.md`](security-testing-generate-and-store-sboms.md) |
| 6 | Run secrets detection as a pre-commit hook | CRITICAL | [`security-testing-run-secrets-detection-as-a-pre-commit-hook.md`](security-testing-run-secrets-detection-as-a-pre-commit-hook.md) |
| 7 | Keep security tool rulesets and vulnerability databases up to date | CRITICAL | [`security-testing-keep-security-tool-rulesets-and-vulnerability-databases-up.md`](security-testing-keep-security-tool-rulesets-and-vulnerability-databases-up.md) |
| 8 | Track security testing metrics | CRITICAL | [`security-testing-track-security-testing-metrics.md`](security-testing-track-security-testing-metrics.md) |

---

---
title: "Enable incremental scanning"
impact: MEDIUM
impactDescription: "general best practice"
tags: security-testing, security, sast, dast, sca
---

## Enable incremental scanning

Enable incremental scanning: for SAST tools in pull requests so that developers receive fast feedback on only the code they changed, reserving full scans for nightly or weekly runs.

---

---
title: "Generate and store SBOMs"
impact: MEDIUM
impactDescription: "general best practice"
tags: security-testing, security, sast, dast, sca
---

## Generate and store SBOMs

Generate and store SBOMs: for every release using CycloneDX or SPDX format; SBOMs enable rapid impact assessment when new vulnerabilities are disclosed in dependencies.

---

---
title: "Integrate security testing into CI/CD as quality gates"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security-testing, security, sast, dast, sca
---

## Integrate security testing into CI/CD as quality gates

Integrate security testing into CI/CD as quality gates: fail builds on critical and high-severity findings to prevent vulnerable code from reaching production.

---

---
title: "Keep security tool rulesets and vulnerability databases up to date"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security-testing, security, sast, dast, sca
---

## Keep security tool rulesets and vulnerability databases up to date

Keep security tool rulesets and vulnerability databases up to date: outdated rules miss new vulnerability patterns; automate rule updates as part of your tool maintenance.

---

---
title: "Layer multiple testing approaches"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security-testing, security, sast, dast, sca
---

## Layer multiple testing approaches

Layer multiple testing approaches: no single tool catches everything; combine SAST, DAST, SCA, container scanning, secrets detection, and IaC scanning for comprehensive coverage.

---

---
title: "Run secrets detection as a pre-commit hook"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security-testing, security, sast, dast, sca
---

## Run secrets detection as a pre-commit hook

Run secrets detection as a pre-commit hook: and scan the full Git history periodically; secrets committed even briefly remain in Git history and must be rotated immediately upon detection.

---

---
title: "Track security testing metrics"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: security-testing, security, sast, dast, sca
---

## Track security testing metrics

(findings by severity, mean time to remediate, false positive rate, scan coverage) and report them to engineering leadership to drive continuous improvement.

---

---
title: "Tune tools aggressively to reduce false positives"
impact: MEDIUM
impactDescription: "general best practice"
tags: security-testing, security, sast, dast, sca
---

## Tune tools aggressively to reduce false positives

Tune tools aggressively to reduce false positives: a noisy tool is an ignored tool; invest time in suppressing false positives and writing custom rules tuned to your codebase.

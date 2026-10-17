---
name: security-security-testing
description: Use when selecting or configuring security scanners in CI/CD. USE FOR: SAST, DAST, SCA, Semgrep, CodeQL, SonarQube, Snyk, ZAP, Burp, Trivy, GitLeaks, TruffleHog, Checkov, container, secrets, and IaC scanning. DO NOT USE FOR: SBOM and signing (use security-supply-chain), threat modeling (use security-threat-modeling), remediation by category (use security-owasp).
---

# Security Testing Tools

## Overview

Security testing spans the entire software delivery pipeline — from the moment code is written through build, deployment, and runtime in production. No single tool or technique is sufficient; effective security testing requires layering multiple approaches at different stages of the pipeline. Static analysis catches coding flaws before execution, dynamic analysis discovers runtime vulnerabilities in deployed applications, composition analysis identifies known vulnerabilities in dependencies, and runtime monitoring detects threats in production. The goal is to create a security testing strategy that is automated, continuous, and integrated into the CI/CD pipeline so that vulnerabilities are caught as early and as cheaply as possible.

## Best Practices

- **Layer multiple testing approaches** — no single tool catches everything; combine SAST, DAST, SCA, container scanning, secrets detection, and IaC scanning for comprehensive coverage.
- **Integrate security testing into CI/CD as quality gates** — fail builds on critical and high-severity findings to prevent vulnerable code from reaching production.
- **Tune tools aggressively to reduce false positives** — a noisy tool is an ignored tool; invest time in suppressing false positives and writing custom rules tuned to your codebase.
- **Enable incremental scanning** for SAST tools in pull requests so that developers receive fast feedback on only the code they changed, reserving full scans for nightly or weekly runs.
- **Generate and store SBOMs** for every release using CycloneDX or SPDX format; SBOMs enable rapid impact assessment when new vulnerabilities are disclosed in dependencies.
- **Run secrets detection as a pre-commit hook** and scan the full Git history periodically; secrets committed even briefly remain in Git history and must be rotated immediately upon detection.
- **Keep security tool rulesets and vulnerability databases up to date** — outdated rules miss new vulnerability patterns; automate rule updates as part of your tool maintenance.
- **Track security testing metrics** (findings by severity, mean time to remediate, false positive rate, scan coverage) and report them to engineering leadership to drive continuous improvement.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | Security Testing Categories; SAST (Static Application Security Testing); DAST (Dynamic Application Security Testing); SCA (Software Composition Analysis); Container Security; Secrets Detection; IaC Security; CI/CD Integration |

## References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [NIST SP 800-115 Technical Guide to Information Security Testing](https://csrc.nist.gov/publications/detail/sp/800-115/final)
- [Semgrep Documentation](https://semgrep.dev/docs/)

See references/rules.md for the full rule catalog.

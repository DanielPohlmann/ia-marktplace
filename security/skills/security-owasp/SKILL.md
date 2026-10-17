---
name: security-owasp
description: Use when classifying, assessing, or baselining vulnerabilities against OWASP standards. USE FOR: OWASP Top 10 (2021), API Security Top 10 (2023), CWE Top 25, risk scoring, access control, injection, XSS, SSRF, misconfiguration. DO NOT USE FOR: LLM vulns (use security-ai-security), scanner setup (use security-security-testing), crypto (use security-cryptography), validation rules (use security-input-validation).
---

# OWASP Standards

## Overview

The Open Worldwide Application Security Project (OWASP) is a nonprofit foundation dedicated to improving software security. OWASP produces freely available standards, tools, and documentation that serve as industry benchmarks for identifying and mitigating application security risks. The OWASP Top 10 for web applications and the OWASP API Security Top 10 are widely adopted as minimum security baselines by organizations worldwide. Combined with the CWE/SANS Top 25, these lists provide a comprehensive taxonomy of the most dangerous and prevalent software weaknesses, enabling development teams to prioritize their security efforts against the threats that matter most.

## Best Practices

- **Start with the OWASP Top 10 as a baseline**: treat these categories as the minimum set of risks every application must address, not as an exhaustive security program.
- **Map vulnerabilities to CWEs**: use CWE identifiers to communicate precisely about vulnerability types across teams, tools, and reports.
- **Automate checks in CI/CD**: integrate SAST, DAST, and SCA tools that map findings to OWASP and CWE categories for consistent tracking.
- **Revisit lists on each release cycle**: OWASP updates its Top 10 periodically; ensure your security baselines reflect the latest version.
- **Combine lists for full coverage**: no single list covers everything; use the OWASP Top 10, API Security Top 10, and CWE Top 25 together for comprehensive risk coverage.
- **Train developers on the Top 10**: security awareness training centered on OWASP categories is one of the highest-ROI investments for reducing vulnerabilities at the source.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/owasp-top-10-2021.md](references/owasp-top-10-2021.md) | OWASP Top 10 (2021) |
| [references/owasp-api-security-top-10-2023.md](references/owasp-api-security-top-10-2023.md) | OWASP API Security Top 10 (2023) |
| [references/cwe-sans-top-25-selected-critical-entries.md](references/cwe-sans-top-25-selected-critical-entries.md) | CWE/SANS Top 25 (Selected Critical Entries) |
| [references/details.md](references/details.md) | Mapping Between Lists |

## References

- [OWASP Top Ten Project](https://owasp.org/www-project-top-ten/)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [CWE/SANS Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/)

See references/rules.md for the full rule catalog.

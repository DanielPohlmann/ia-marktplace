---
name: security-penetration-testing
description: Use when planning or running an authorized penetration test of web apps, APIs, networks, or mobile apps. USE FOR: OWASP Testing Guide, PTES, OSSTMM, scoping, rules of engagement, tools, severity, reporting, retest, bug bounty, disclosure. DO NOT USE FOR: CI scanning (use security-security-testing), design-time threats (use security-threat-modeling), kill-chain simulation (use security-red-teaming).
---

# Penetration Testing

## Overview

Penetration testing is the authorized practice of simulating attacks against a system to discover exploitable vulnerabilities before malicious actors do. Unlike automated security scanning (SAST/DAST), pen testing involves human expertise to chain vulnerabilities, test business logic flaws, and assess real-world exploitability. Pen tests are conducted under a clear scope and rules of engagement, and results are reported with severity ratings and remediation guidance.

> **Important**: Penetration testing must always be performed with explicit written authorization. Unauthorized testing is illegal in virtually every jurisdiction. Ensure you have a signed rules of engagement document before beginning any testing.

### Key References

| Title | Author(s) | Focus |
|-------|-----------|-------|
| *The Web Application Hacker's Handbook* | Stuttard & Pinto | Web app vulnerability discovery and exploitation |
| *Penetration Testing* | Georgia Weidman | Hands-on pen testing methodology |
| *The Hacker Playbook 3* | Peter Kim | Red team tactics and techniques |
| *OWASP Testing Guide v4.2* | OWASP Foundation | Comprehensive web application testing methodology |
| *PTES (Penetration Testing Execution Standard)* | PTES.org | Industry-standard pen testing framework |

## Testing Approaches

| Approach | Knowledge Given | Simulates | Best For |
|----------|----------------|-----------|----------|
| **Black Box** | No internal knowledge | External attacker | Realistic external threat assessment |
| **Gray Box** | Partial knowledge (credentials, architecture docs) | Authenticated attacker or insider threat | Most common; best efficiency-to-realism ratio |
| **White Box** | Full source code, architecture, credentials | Comprehensive audit | Maximum coverage; code-assisted testing |

## Scoping and Rules of Engagement

Every pen test must begin with a formal scoping and rules of engagement agreement:

| Element | Description |
|---------|-------------|
| **Scope** | Specific IP ranges, domains, applications, or environments to be tested |
| **Out of scope** | Systems, networks, or actions explicitly excluded |
| **Testing window** | Dates and hours when testing is permitted |
| **Authorization** | Written permission from system owner (get-out-of-jail letter) |
| **Communication plan** | Emergency contacts, escalation procedures, status reporting |
| **Data handling** | How sensitive data discovered during testing will be handled and destroyed |
| **Rules** | No denial of service, no data destruction, no social engineering (unless scoped), notification on critical findings |
| **Deliverables** | Report format, debrief meeting, retest timeline |

## Reporting

A pen test report should include:

1. **Executive Summary** — non-technical overview of findings, risk level, and key recommendations for leadership
2. **Scope and Methodology** — what was tested, how, and testing approach (black/gray/white box)
3. **Findings** — each vulnerability with: title, severity (CVSS), description, affected asset, evidence (screenshots, request/response), business impact, remediation steps
4. **Risk Summary** — findings grouped by severity with counts
5. **Remediation Roadmap** — prioritized list of fixes with effort estimates
6. **Appendices** — tool output, raw scan results, methodology details

## Best Practices

- **Always obtain written authorization** before testing — unauthorized pen testing is a criminal offense regardless of intent.
- **Scope tightly** — clearly define what is in and out of scope to protect both the tester and the organization.
- **Use gray-box testing** as the default for most engagements — it provides the best balance of realism and coverage.
- **Report findings with business impact**, not just technical severity — help stakeholders understand the real-world risk.
- **Verify remediations** with a retest engagement after fixes are deployed — do not assume fixes are complete.
- **Maintain a vulnerability disclosure policy (VDP)** even if you do not run a bug bounty — it gives researchers a safe way to report issues.
- **Separate pen testing from automated scanning** — automated tools find known patterns; human testers find business logic flaws and chained exploits.
- **Conduct pen tests at least annually** and after major releases or architecture changes.
- **Treat pen test reports as confidential** — they contain detailed exploitation instructions for your systems.
- **Rotate pen testing firms** periodically to get fresh perspectives and avoid blind spots from familiarity.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/pen-testing-tools.md](references/pen-testing-tools.md) | Pen Testing Tools — Reconnaissance and Enumeration, Web Application Testing, Network and Infrastructure, Post-Exploitation, Mobile, Cloud |
| [references/details.md](references/details.md) | Methodologies; Pen Test Types; Severity Rating; Bug Bounty and Responsible Disclosure |

## References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Penetration Testing Execution Standard (PTES)](http://www.pentest-standard.org)
- [NIST SP 800-115 Technical Guide to Information Security Testing](https://csrc.nist.gov/publications/detail/sp/800-115/final)

See references/rules.md for the full rule catalog.

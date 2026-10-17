---
name: legal-content-moderation
description: Use when a platform hosts user-generated content and needs its legal obligations. USE FOR: Section 230, EU DSA tiers, DMCA takedown and counter-notice, CSAM reporting, terrorist content, transparency reports, safe harbor. DO NOT USE FOR: IP strategy (use legal-intellectual-property), consumer terms (use legal-consumer-protection), routing (use legal).
---

# Content Moderation

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Any platform that hosts, transmits, or displays user-generated content faces legal obligations around content moderation, illegal content removal, and transparency. The legal landscape varies dramatically by jurisdiction -- from broad immunity (US Section 230) to proactive monitoring obligations (EU DSA for very large platforms). Understanding these frameworks is essential for any company operating a platform where users can post, share, or communicate content.

## Best Practices

- **Always consult qualified legal counsel for content moderation policy decisions.** CSAM reporting failures carry criminal liability, and the legal landscape for platform obligations is evolving rapidly across jurisdictions. An experienced attorney can help you navigate these obligations.
- **Implement a robust notice-and-action system.** Design clear workflows for receiving, evaluating, and acting on content reports. Document every step to demonstrate compliance with legal obligations and to support any disputes.
- **Register a DMCA designated agent and keep the registration current.** This is a prerequisite for safe harbor protection under US copyright law. Ensure the agent's contact information is also prominently displayed on your platform.
- **Build CSAM detection and reporting into your platform from day one.** Use established tools (such as PhotoDNA or similar hash-matching technologies) and report all apparent CSAM to the appropriate authorities (NCMEC in the US). Never delay reporting.
- **Maintain detailed records of all content moderation actions.** Record what was removed, why, when, by whom (or by what automated system), and what notice was given to the user. These records are essential for DSA compliance, legal defense, and internal auditing.
- **Provide meaningful appeal mechanisms for users.** Both the DSA and general principles of due process require that users have the ability to challenge content moderation decisions. Ensure appeals are reviewed by a human who was not involved in the original decision.
- **Train content moderation teams and invest in their well-being.** Moderators reviewing harmful content face significant psychological risks. Provide regular training on legal obligations, platform policies, and emerging content types, along with mental health support.
- **Monitor regulatory developments across all jurisdictions where you operate.** Content moderation law is one of the fastest-evolving areas of technology regulation. Assign responsibility for tracking legislative and regulatory changes and updating your policies accordingly.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/dmca-takedown-process.md](references/dmca-takedown-process.md) | DMCA Takedown Process — Step-by-Step Process, Requirements for a Valid DMCA Notice, Designated Agent Registration |
| [references/details.md](references/details.md) | Intermediary Liability Frameworks; EU DSA Obligations by Platform Size; Mandatory Reporting Obligations; Content Moderation Approaches; Transparency Requirements |

## References

- [EU Digital Services Act (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)
- [U.S. Code Section 230 — Communications Decency Act](https://www.law.cornell.edu/uscode/text/47/230)
- [U.S. Copyright Office — DMCA](https://www.copyright.gov/dmca/)

See references/rules.md for the full rule catalog.

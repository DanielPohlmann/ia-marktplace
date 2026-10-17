---
name: legal-consumer-protection
description: Use when identifying consumer-protection duties for a digital product. USE FOR: ToS/EULA, refunds, dark patterns, auto-renewal and subscription laws, DMA/DSA, FTC Act, CAN-SPAM, COPPA. DO NOT USE FOR: privacy rights (use legal-privacy-data-protection), platform content liability (use legal-content-moderation), B2B contracts (use legal-contracts).
---

# Consumer Protection

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Consumer protection laws govern the relationship between software companies and their users or customers. These laws increasingly target digital-specific practices like dark patterns, auto-renewal subscriptions, and manipulative design. As regulators worldwide focus more attention on digital markets, software companies must ensure their user interfaces, pricing practices, marketing, and terms of service comply with a growing body of consumer protection legislation. Failure to comply can result in enforcement actions, significant fines, class action lawsuits, and reputational damage.

## Best Practices

- **Have legal counsel review all consumer-facing terms, pricing practices, and user interface flows.** Consumer protection law varies significantly by jurisdiction, and enforcement is increasing. What is permissible in one market may be illegal in another.
- **Design cancellation flows to be as simple as sign-up flows.** The FTC's "click to cancel" rule and similar state and EU requirements make this a legal obligation, not just a best practice.
- **Disclose all material terms before the consumer commits.** Ensure pricing, auto-renewal terms, cancellation policies, and any limitations are presented clearly and conspicuously before the consumer clicks "subscribe" or "buy."
- **Avoid dark patterns in all user interfaces.** Audit your product regularly for confirmshaming, hidden costs, roach motel patterns, forced continuity, and misdirection. What product teams see as "growth optimization" may constitute an unfair or deceptive practice under consumer protection law.
- **Implement age-appropriate design for products accessible to children.** If your service is likely to be used by minors, comply with COPPA, GDPR Article 8, and the UK Age Appropriate Design Code. When in doubt, apply the most protective standard.
- **Use clickwrap consent for all terms of service.** Require affirmative user action (clicking "I agree") rather than relying on browsewrap terms that may be unenforceable.
- **Send clear confirmation and renewal notices.** After a consumer subscribes, send a confirmation that includes the terms, price, renewal date, and cancellation instructions. Send renewal reminders before each billing cycle.
- **Monitor enforcement trends and regulatory guidance.** The FTC, EU Commission, and state attorneys general regularly publish guidance, enforcement actions, and rulemaking proposals that signal where consumer protection law is heading. Stay informed and adapt your practices proactively.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/dark-patterns.md](references/dark-patterns.md) | Dark Patterns — Common Dark Patterns, Regulatory Landscape for Dark Patterns |
| [references/terms-of-service-eula.md](references/terms-of-service-eula.md) | Terms of Service / EULA — Essential Terms, Enforceability Considerations |
| [references/details.md](references/details.md) | Key Consumer Protection Laws; Subscription and Auto-Renewal; Children's Privacy (COPPA / EU Age Requirements) |

## References

- [Federal Trade Commission (FTC) — Consumer Protection](https://www.ftc.gov/about-ftc/bureaus-offices/bureau-consumer-protection)
- [EU Digital Markets Act (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/1925/oj)
- [EU Digital Services Act (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)

See references/rules.md for the full rule catalog.

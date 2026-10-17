---
name: legal-employment-labor
description: Use when identifying employment-law issues for software teams, especially distributed or global ones. USE FOR: contractor vs employee, IP assignment, non-competes, cross-border remote work, employer of record, equity, whistleblowers, employee monitoring. DO NOT USE FOR: patent/IP strategy (use legal-intellectual-property), employee data privacy (use legal-privacy-data-protection).
---

# Employment & Labor

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Software companies with distributed teams face complex employment law across multiple jurisdictions. Misclassifying workers, failing to secure IP assignment, or violating local labor laws can result in significant liability — including back taxes, penalties, loss of intellectual property rights, and lawsuits. As remote work becomes the norm and companies hire across borders, understanding the employment law landscape is essential to building a legally compliant and sustainable workforce.

## Contractor vs Employee Classification

### Why It Matters

The distinction between an independent contractor and an employee has profound consequences:

- **Tax obligations** — Employers must withhold income taxes, pay Social Security/Medicare (US) or equivalent contributions, and file employment tax returns for employees. Contractors handle their own taxes.
- **Benefits** — Employees may be entitled to health insurance, retirement plans, paid leave, unemployment insurance, and workers' compensation. Contractors receive none of these.
- **IP ownership** — In many jurisdictions, work created by employees belongs to the employer by default. Work created by contractors generally belongs to the contractor unless assigned by written agreement.
- **Liability** — Companies are generally liable for the acts of employees (respondeat superior) but have more limited liability for independent contractors.

### Classification Tests

| Test | Jurisdiction | Key Factors |
|---|---|---|
| **ABC Test** | California (AB5), many US states | Worker is presumed an employee unless: (A) free from control and direction, (B) performs work outside the hiring entity's usual course of business, (C) is engaged in an independently established trade or occupation |
| **Common Law Test** | US (IRS) | Evaluates behavioral control (how work is performed), financial control (business aspects of the work), and the type of relationship (contracts, benefits, permanency) |
| **IR35** | UK | Examines personal service (must the individual do the work personally), mutuality of obligation (is there an ongoing obligation to offer/accept work), and control (does the client control how the work is done) |
| **EU Directive on Platform Work** | EU | Establishes a rebuttable presumption of employment if two or more of five criteria are met: pay level set by platform, electronic monitoring, restricted freedom in scheduling, restricted ability to work for others, restricted ability to build client base |

### Consequences of Misclassification

- **Back taxes and penalties** — The IRS can assess back employment taxes plus penalties and interest. Similar consequences apply in other jurisdictions.
- **Back benefits** — Misclassified workers may be entitled to retroactive benefits including health insurance, retirement contributions, overtime pay, and paid leave.
- **IP ownership disputes** — If a contractor was actually an employee, the work-for-hire doctrine may not apply as expected, creating uncertainty about who owns the IP.
- **Class action risk** — Misclassification cases are frequently brought as class actions, multiplying the potential liability across all similarly situated workers.

## Best Practices

- **Consult employment counsel in each jurisdiction where you have workers.** Employment law varies dramatically across borders, and even within countries (e.g., California vs Texas in the US). Local counsel is essential for compliance.
- **Classify workers correctly from the start.** Perform a classification analysis using the applicable test before engaging any worker. Document the analysis. When in doubt, err toward employee classification — the consequences of misclassifying an employee as a contractor are far more severe than the reverse.
- **Execute written IP assignment agreements before work begins.** Never assume that contractor work product belongs to the company. Get a signed, jurisdiction-appropriate IP assignment agreement in place before the contractor writes a single line of code.
- **Audit your non-compete agreements.** Given the rapid changes in non-compete law, review all existing non-compete agreements with counsel. Consider whether non-solicitation or confidentiality agreements would better serve your interests with lower legal risk.
- **Use an Employer of Record for international hires until you establish local entities.** EORs provide a compliant way to hire in foreign jurisdictions without the cost and complexity of setting up a local subsidiary.
- **Get local tax and securities advice before granting equity to international employees.** Equity compensation triggers different tax and regulatory consequences in every jurisdiction. A plan that is tax-efficient in the US may create severe tax liabilities for a recipient in another country.
- **Implement transparent and proportionate employee monitoring policies.** If you monitor employees, disclose the monitoring clearly, limit it to what is necessary for legitimate business purposes, and comply with local laws regarding consent and employee representation.
- **Establish whistleblower reporting channels.** Even if not legally required in every jurisdiction where you operate, internal reporting channels demonstrate good governance and can help surface problems before they become enforcement actions.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/ip-assignment.md](references/ip-assignment.md) | IP Assignment — Work-for-Hire Doctrine (US), Invention Assignment Agreements, IP Ownership by Jurisdiction |
| [references/non-compete-agreements.md](references/non-compete-agreements.md) | Non-Compete Agreements — Recent Developments (2024-2025), Enforceability by Jurisdiction, Alternatives to Non-Competes |
| [references/details.md](references/details.md) | Remote Work Across Borders; Equity Compensation; Whistleblower Protections; Employee Monitoring |

## References

- [U.S. Department of Labor](https://www.dol.gov)
- [IRS Independent Contractor vs Employee Classification](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee)
- [EU Employment Law (European Commission)](https://ec.europa.eu/social/main.jsp?catId=157&langId=en)

See references/rules.md for the full rule catalog.

---
name: legal-open-source-licensing
description: Use when choosing, consuming, or distributing open-source software, or auditing a dependency tree's licenses. USE FOR: MIT, Apache, BSD, GPL, LGPL, MPL, AGPL SaaS impact, compatibility, distribution obligations, SBOM license audits, CLAs, dual licensing. DO NOT USE FOR: IP strategy (use legal-intellectual-property), crypto export (use legal-export-controls), NOTICE files (use legal-attribution).
---

# Open-Source Licensing

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Open-source software is the foundation of modern development, but every OSS component carries license obligations that can affect how you distribute your software. A single incompatible dependency can force you to relicense your product, release proprietary source code, or remove the component entirely. Understanding the spectrum of open-source licenses -- from permissive to strong copyleft -- is essential for any team that builds on open-source foundations.

## Common Licenses Quick Reference

| License | Permissions | Conditions | Limitations | Key Risk |
|---|---|---|---|---|
| **MIT** | Commercial use, modification, distribution, private use | Include copyright notice and license text | No liability, no warranty | Very low -- one of the most permissive licenses |
| **Apache 2.0** | Commercial use, modification, distribution, patent use, private use | Include copyright notice, license text, state changes, include NOTICE file | No liability, no warranty, no trademark use | Low -- includes explicit patent grant, which is an advantage |
| **BSD 2-Clause** | Commercial use, modification, distribution, private use | Include copyright notice and license text | No liability, no warranty | Very low -- similar to MIT |
| **GPL 2.0** | Commercial use, modification, distribution, private use | Disclose source, include license, same license for derivative works | No liability, no warranty | High -- derivative works must be GPL 2.0, no patent grant |
| **GPL 3.0** | Commercial use, modification, distribution, patent use, private use | Disclose source, include license, same license for derivative works, no tivoization | No liability, no warranty | High -- derivative works must be GPL 3.0, includes anti-tivoization and patent provisions |
| **LGPL 2.1** | Commercial use, modification, distribution, private use | Disclose source of library modifications, include license, allow relinking | No liability, no warranty | Medium -- modifications to the library must be LGPL, but linking from proprietary code is permitted |
| **LGPL 3.0** | Commercial use, modification, distribution, patent use, private use | Disclose source of library modifications, include license, allow relinking | No liability, no warranty | Medium -- similar to LGPL 2.1 with GPL 3.0 base terms |
| **MPL 2.0** | Commercial use, modification, distribution, patent use, private use | Disclose source of modified files, include license | No liability, no warranty, no trademark use | Medium -- file-level copyleft; only modified files must remain MPL |
| **AGPL 3.0** | Commercial use, modification, distribution, patent use, private use | Disclose source (including over network), include license, same license | No liability, no warranty | Very high -- network use triggers source disclosure; affects SaaS products |
| **BSL (Business Source License)** | Non-production use; converts to open-source after change date | Cannot use in production without commercial license until change date | Production use restricted | High -- not a true open-source license; restricts commercial use until a specified date |

## Best Practices

- **Always consult qualified legal counsel for GPL compliance.** The boundary between a "derivative work" and an independent work is legally nuanced. A licensed attorney can evaluate your specific linking, modification, and distribution patterns.
- **Maintain a software bill of materials (SBOM).** Track every open-source component, its version, and its license. An up-to-date SBOM is the foundation of license compliance.
- **Integrate license scanning into your CI/CD pipeline.** Automated tools catch license issues before they reach production. Configure allow/deny lists to block incompatible licenses at build time.
- **Establish an open-source policy for your organization.** Define which licenses are approved, which require legal review, and which are prohibited. Communicate this policy to all developers.
- **Review license obligations before adopting any new dependency.** A quick check before adding a library is far less costly than discovering an incompatibility after shipping.
- **Pay special attention to AGPL in SaaS environments.** AGPL's network copyleft provision can require you to disclose the source code of your entire application if you use an AGPL component in a networked service.
- **Track license changes across dependency updates.** Libraries can change their license between versions. Ensure your tooling alerts you when a dependency's license changes.
- **Contribute back to the open-source projects you depend on.** Beyond legal compliance, contributing upstream strengthens the ecosystem and builds goodwill with the communities that power your product.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/details.md](references/details.md) | License Categories; License Compatibility Matrix; Compliance Obligations by Distribution Type; License Auditing Tools; Contributor License Agreements (CLA); Dual Licensing |

## References

- [Open Source Initiative (OSI) — License List](https://opensource.org/licenses)
- [Choose an Open Source License](https://choosealicense.com)
- [SPDX License List](https://spdx.org/licenses/)

See references/rules.md for the full rule catalog.

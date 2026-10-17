---
name: legal-attribution
description: Use when determining what must be credited, where, and how in a software product. USE FOR: OSS license notices, NOTICE files, Creative Commons, fonts, images, API and data-source attribution, credits in UI and docs. DO NOT USE FOR: choosing a license (use legal-open-source-licensing), IP ownership (use legal-intellectual-property), routing (use legal).
---

# Attribution

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Attribution is a legal obligation that arises from many sources — open-source licenses, Creative Commons media, font licenses, API terms of service, data provider agreements, and more. Failing to provide required attribution can constitute license violation (risking license termination and copyright infringement claims), breach of contract, or regulatory non-compliance. Many companies underestimate attribution requirements because the obligation is spread across dozens of different asset types, each with its own rules.

## Compliance Checklist

| # | Check | Frequency |
|---|-------|-----------|
| 1 | **Audit all dependencies** for license types and attribution requirements | Every release |
| 2 | **Generate NOTICE/THIRD-PARTY-NOTICES file** from dependency metadata | Every build (automate) |
| 3 | **Review media assets** (images, icons, fonts, audio) for license terms | When assets are added |
| 4 | **Check API ToS** for attribution requirements | When integrating new APIs and on ToS change notifications |
| 5 | **Verify data source licenses** for attribution and share-alike terms | When incorporating new data sources |
| 6 | **Display attribution** in the correct location for your distribution type | Every release |
| 7 | **Verify modified fonts** are renamed per OFL requirements | When customizing fonts |
| 8 | **Document attribution decisions** in a central register | Ongoing |

## Best Practices

- **Always consult legal counsel** when unsure about attribution requirements — getting it wrong can terminate your license to use the software.
- **Automate NOTICE file generation** as part of your CI/CD pipeline — tools like `license-checker`, `FOSSA`, and `go-licenses` catch new dependencies automatically.
- **Maintain a central attribution register** that tracks every third-party component, its license, and where attribution is displayed.
- **Include attribution in your release checklist** — it is easy to add a dependency and forget to update the NOTICE file.
- **Check API Terms of Service** on a scheduled basis — attribution requirements change with ToS updates without notice.
- **Do not strip copyright notices or license headers** from source files — many licenses explicitly require preserving them.
- **Display attribution accessibly** — a legal/licenses page that users can actually find, not buried in an invisible footer.
- **Treat font licenses as seriously as code licenses** — font piracy lawsuits are common and penalties can be per-seat or per-pageview.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/open-source-attribution.md](references/open-source-attribution.md) | Open-Source Attribution — What Most OSS Licenses Require, NOTICE File Structure, Automation Tools, Where to Display OSS Attribution |
| [references/details.md](references/details.md) | Attribution by Asset Type; Creative Commons Attribution; Font Licensing; API and Service Attribution; Data Source Attribution |

## References

- [Creative Commons Licenses](https://creativecommons.org/licenses/)
- [Open Source Initiative (OSI) — License List](https://opensource.org/licenses)
- [SPDX License List](https://spdx.org/licenses/)

See references/rules.md for the full rule catalog.

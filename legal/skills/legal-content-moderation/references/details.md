<!-- Part of the legal-content-moderation skill. Loaded on demand from SKILL.md. -->

# Content Moderation — details

## Intermediary Liability Frameworks

| Framework | Jurisdiction | Approach | Key Provision |
|---|---|---|---|
| **Section 230 CDA** | US | Broad immunity | Platforms are not liable for third-party content, with exceptions for federal criminal law, intellectual property, and CSAM |
| **EU Digital Services Act** | EU | Conditional immunity with obligations | Notice-and-action procedures, transparency requirements, risk assessments for VLOPs, and systemic risk management |
| **E-Commerce Directive Art 14** | EU (legacy) | Hosting immunity if no actual knowledge | Being superseded by the DSA; provided immunity for hosting services that did not have actual knowledge of illegal content |
| **Online Safety Act** | UK | Duty of care | Proactive measures required for priority illegal content, plus child safety duties for platforms likely to be accessed by children |
| **IT Act Section 79** | India | Safe harbor with conditions | Due diligence requirements for intermediaries, including 36-hour takedown on government order |
| **NetzDG** | Germany | Platform accountability for illegal content | 24-hour removal for clearly illegal content, 7 days for other illegal content, with reporting obligations |

## EU DSA Obligations by Platform Size

The EU Digital Services Act imposes a tiered system of obligations based on platform size and type, with increasing requirements for larger platforms.

| Platform Type | Size | Key Obligations |
|---|---|---|
| **All intermediaries** | Any | Transparency reports, Terms of Service clarity, cooperation with national authorities, single point of contact for authorities and users |
| **Hosting services** | Any | Notice-and-action mechanisms, statement of reasons for content removals, notification to users of moderation decisions |
| **Online platforms** | Any with public content | Additional transparency requirements, internal complaint-handling systems, out-of-court dispute resolution, trusted flagger mechanisms, measures against misuse |
| **Very Large Online Platforms (VLOPs)** | 45M+ EU users | Systemic risk assessment, independent audits, data access for vetted researchers, crisis response protocols, advertising repositories, recommender system transparency |
| **Very Large Online Search Engines** | 45M+ EU users | Similar obligations to VLOPs, including systemic risk assessments, independent audits, and researcher data access |

## Mandatory Reporting Obligations

### CSAM (Child Sexual Abuse Material)

Child sexual abuse material carries the most stringent legal obligations of any content category. Failure to comply can result in criminal liability.

- **United States** — Federal law (18 USC 2258A) requires electronic service providers to report apparent CSAM to the National Center for Missing & Exploited Children (NCMEC). Failure to report is a federal offense carrying fines of up to $300,000 for a first offense and $600,000 for subsequent offenses.
- **European Union** — The proposed EU CSAM Regulation would introduce detection orders requiring platforms to scan for known and new CSAM using approved technologies. Member states already have national reporting obligations.
- **Criminal penalties** — Beyond reporting obligations, knowingly distributing, possessing, or producing CSAM carries severe criminal penalties in virtually every jurisdiction worldwide.

### Terrorist Content

- **EU Terrorism Content Online (TCO) Regulation** — Requires hosting service providers to remove terrorist content within one hour of receiving a removal order from a competent authority in an EU member state. Platforms must also take specific measures to address the dissemination of terrorist content, including the use of automated tools where appropriate.
- **Christchurch Call** — A voluntary commitment by governments and technology companies to eliminate terrorist and violent extremist content online.

## Content Moderation Approaches

Different content moderation strategies carry different legal implications depending on the jurisdiction and the type of content involved.

| Approach | Description | Legal Considerations |
|---|---|---|
| **Proactive filtering** | Automated detection and removal before publication | May increase liability awareness in some jurisdictions; required for CSAM in some proposals; must avoid over-removal under DSA |
| **Reactive / notice-and-action** | Respond to reports and notices from users, rightsholders, or authorities | Standard approach under US and EU frameworks; essential for maintaining safe harbor protections |
| **Human review** | Manual review of flagged content by trained moderators | Required for complex decisions under DSA; necessary for context-dependent content; raises worker welfare concerns |
| **Hybrid** | Automated flagging combined with human review for final decisions | Recommended approach that balances scale with accuracy; aligns with DSA requirements for meaningful human oversight |

## Transparency Requirements

Modern content moderation laws increasingly mandate transparency as a core obligation for platforms.

- **DSA transparency reports** — Platforms must publish regular reports detailing the volume of content moderation actions, the types of content removed, the grounds for removal, and the use of automated tools.
- **Content moderation algorithmic transparency** — VLOPs must explain how their recommender systems work and offer users at least one option not based on profiling.
- **Advertising transparency** — VLOPs must maintain publicly accessible repositories of all advertisements displayed on their platform, including information about the advertiser, the content, the targeting parameters, and the period of display.
- **Terms of Service clarity** — All platforms must ensure their Terms of Service clearly describe content moderation policies, including the types of content restricted, the tools and methods used, and the rights of users to appeal decisions.

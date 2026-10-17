<!-- Part of the legal-attribution skill. Loaded on demand from SKILL.md. -->

# Attribution — details

## Attribution by Asset Type

| Asset Type | Common Licenses/Terms | Attribution Required | Where to Attribute |
|-----------|----------------------|---------------------|-------------------|
| **Open-source libraries** | MIT, Apache 2.0, BSD, GPL, LGPL, MPL | Yes (nearly all OSS licenses) | NOTICE file, about/legal screen, documentation |
| **Fonts** | OFL (SIL Open Font License), proprietary EULA | OFL: yes; Proprietary: per EULA | Font credits page, CSS comments, documentation |
| **Images / Icons** | Creative Commons, stock photo licenses, proprietary | CC BY: yes; Stock: per license; Proprietary: per contract | Image credits, about page, metadata |
| **Audio / Video** | Creative Commons, royalty-free licenses, sync licenses | CC BY: yes; Royalty-free: per license | Credits section, end cards, metadata |
| **Datasets** | CC BY, ODC-BY, government open data licenses | CC BY/ODC-BY: yes; Some government: yes | Data source citations, documentation |
| **APIs** | Terms of service, developer agreements | Many require "powered by" branding | UI badge/logo, documentation, per ToS |
| **Maps** | Google Maps Platform, Mapbox, OpenStreetMap | Yes (all major providers) | Map overlay attribution, per ToS |
| **AI/ML models** | Model cards, Hugging Face licenses, proprietary | Varies — many require model credit | Documentation, about page, per license |

## Creative Commons Attribution

Creative Commons licenses are common for media, data, and documentation.

| License | Attribution Required | Share Alike | Commercial Use |
|---------|---------------------|-------------|----------------|
| **CC0** | No | No | Yes |
| **CC BY 4.0** | Yes | No | Yes |
| **CC BY-SA 4.0** | Yes | Yes (derivatives same license) | Yes |
| **CC BY-NC 4.0** | Yes | No | No |
| **CC BY-NC-SA 4.0** | Yes | Yes | No |
| **CC BY-ND 4.0** | Yes | No (no derivatives) | Yes |

### Proper CC BY Attribution (TASL)

Creative Commons specifies the **TASL** format:

- **T**itle — name of the work
- **A**uthor — creator name (linked to profile if available)
- **S**ource — URL where the work was found
- **L**icense — license name linked to the license deed

Example:
```
"Sunset Over Mountains" by Jane Smith (https://example.com/photo/123)
is licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
```

## Font Licensing

Fonts carry their own licensing terms that are frequently overlooked.

| License | Attribution | Embedding | Modification |
|---------|-------------|-----------|-------------|
| **SIL Open Font License (OFL)** | Required (original name + copyright) | Web/app/document embedding allowed | Allowed (must rename modified version) |
| **Apache 2.0** (some Google Fonts) | Required (copyright + license) | Allowed | Allowed |
| **Proprietary (Adobe, Monotype, etc.)** | Per EULA | Per EULA (often limited seats/pageviews) | Typically prohibited |
| **Desktop-only licenses** | Per EULA | Web embedding NOT allowed | Per EULA |

### Font Attribution Pitfalls

- **Web fonts** loaded via Google Fonts CDN do not require separate attribution (Google's ToS handles it), but self-hosted Google Fonts do require including the license file.
- **Icon fonts** (Font Awesome, Material Icons) have separate licenses for the font file vs the CSS/SVG — check both.
- **Custom font subsets** may trigger modification clauses — OFL requires renaming modified fonts.

## API and Service Attribution

Many APIs and services require visible attribution as a condition of use.

| Service | Attribution Requirement |
|---------|----------------------|
| **Google Maps** | "Google" logo on map + "Map data ©20XX Google" + Terms link |
| **Mapbox** | "© Mapbox" + "© OpenStreetMap" on map display |
| **OpenStreetMap** | "© OpenStreetMap contributors" with link to copyright page |
| **Twilio** | No visible attribution required (per current ToS) |
| **Stripe** | "Powered by Stripe" badge on checkout (optional but encouraged) |
| **OpenAI API** | No required attribution (per current ToS), but must not claim AI output is human-generated |
| **GitHub API** | Must comply with ToS; no mandatory badge |
| **Unsplash** | Attribution appreciated but not required (Unsplash License) |

> **Always check the current Terms of Service.** API attribution requirements change with ToS updates. What was optional last year may be mandatory now.

## Data Source Attribution

| Data License | Attribution Required | Derivative Works |
|-------------|---------------------|-----------------|
| **Open Data Commons Attribution (ODC-BY)** | Yes — credit source | Yes |
| **Open Data Commons ODbL** | Yes — credit source + share alike | Yes (same license) |
| **CC BY 4.0 (for datasets)** | Yes — TASL format | Yes |
| **Government open data (US)** | Generally no (public domain) | Yes |
| **Government open data (UK)** | OGL — yes, crown copyright | Yes |
| **Government open data (EU)** | Varies by member state | Varies |

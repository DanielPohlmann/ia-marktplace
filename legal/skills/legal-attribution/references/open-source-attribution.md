<!-- Part of the legal-attribution skill. Loaded on demand from SKILL.md. -->

# Open-Source Attribution

Open-source attribution is the most common and most frequently violated attribution requirement in software.

## What Most OSS Licenses Require

| License | Requirements | NOTICE File | License Text | Copyright Notice |
|---------|-------------|-------------|-------------|-----------------|
| **MIT** | Include copyright notice + license text in copies | Recommended | Required | Required |
| **Apache 2.0** | Include NOTICE file + license text; state changes | Required | Required | Required |
| **BSD 2-Clause** | Include copyright notice + license text | Recommended | Required | Required |
| **BSD 3-Clause** | Same as 2-Clause + no endorsement clause | Recommended | Required | Required |
| **ISC** | Include copyright notice + license text | Recommended | Required | Required |
| **MPL 2.0** | License text in source files; larger work can be proprietary | Per-file | Required (per file) | Required |
| **LGPL 2.1/3.0** | License text + copyright + link to source for modifications | Required | Required | Required |
| **GPL 2.0/3.0** | Full license + copyright + source offer for binaries | Required | Required | Required |
| **AGPL 3.0** | Same as GPL + network interaction triggers | Required | Required | Required |

## NOTICE File Structure

The standard approach for bundling attribution in a distributable product:

```
NOTICE

This product includes software developed by third parties.

================================================================================
Library: react
Version: 18.2.0
License: MIT
Copyright (c) Meta Platforms, Inc. and affiliates.
================================================================================

================================================================================
Library: lodash
Version: 4.17.21
License: MIT
Copyright JS Foundation and other contributors
================================================================================

================================================================================
Library: express
Version: 4.18.2
License: MIT
Copyright (c) 2009-2014 TJ Holowaychuk
Copyright (c) 2013-2014 Roman Shtylman
Copyright (c) 2014-2015 Douglas Christopher Wilson
================================================================================
```

## Automation Tools

| Tool | Ecosystem | Output |
|------|-----------|--------|
| **license-checker** | npm | JSON/CSV/Markdown of all dependency licenses |
| **license-report** | npm | Detailed license report with texts |
| **pip-licenses** | Python | Tabular license output for pip packages |
| **go-licenses** | Go | License detection and NOTICE file generation |
| **dotnet-project-licenses** | .NET | NuGet package license report |
| **FOSSA** | Multi-language | Full compliance management platform |
| **Snyk** | Multi-language | License auditing as part of SCA |
| **licenseFinder** | Multi-language (Ruby-based) | Approve/deny license policies |

## Where to Display OSS Attribution

| Distribution Method | Where to Show Attribution |
|--------------------|--------------------------|
| **Web application (SaaS)** | "Legal" or "Open Source Licenses" page linked from footer |
| **Desktop application** | About dialog → "Third-Party Licenses" section |
| **Mobile app (iOS)** | Settings → Licenses (use `Settings.bundle` or acknowledgements plist) |
| **Mobile app (Android)** | About → Open Source Licenses (use `oss-licenses-plugin` for Gradle) |
| **CLI tool** | `--licenses` flag or `THIRD-PARTY-NOTICES.txt` bundled in distribution |
| **Library / SDK** | `NOTICE` or `THIRD-PARTY-NOTICES` file in package root |
| **Container image** | `/licenses/` directory or `NOTICE` file in image root |
| **Documentation** | Acknowledgements section in README or docs site |

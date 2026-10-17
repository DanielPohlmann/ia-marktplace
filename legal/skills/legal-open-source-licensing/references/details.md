<!-- Part of the legal-open-source-licensing skill. Loaded on demand from SKILL.md. -->

# Open-Source Licensing — details

## License Categories

| Category | Obligations | Examples |
|---|---|---|
| **Permissive** | Minimal: attribution, include license text, no warranty disclaimer | MIT, Apache 2.0, BSD 2-Clause, BSD 3-Clause, ISC |
| **Weak Copyleft** | Modifications to the library must be shared under the same license, but you can link from proprietary code | LGPL 2.1, LGPL 3.0, MPL 2.0, EPL 2.0 |
| **Strong Copyleft** | Derivative works must use the same license -- this is the "viral" effect | GPL 2.0, GPL 3.0, AGPL 3.0 |
| **Network Copyleft** | Copyleft is triggered even by network use (providing the software as a service) without traditional distribution | AGPL 3.0 |

## License Compatibility Matrix

The following table shows whether code under the **Inbound** (column) license can be included in a project distributed under the **Outbound** (row) license:

| Outbound \ Inbound | MIT | Apache 2.0 | LGPL 2.1 | MPL 2.0 | GPL 2.0 | GPL 3.0 | AGPL 3.0 |
|---|---|---|---|---|---|---|---|
| **MIT** | Yes | No | No | No | No | No | No |
| **Apache 2.0** | Yes | Yes | No | No | No | No | No |
| **LGPL 2.1** | Yes | No | Yes | No | No | No | No |
| **MPL 2.0** | Yes | Yes | No | Yes | No | No | No |
| **GPL 2.0** | Yes | No | Yes | Yes | Yes | No | No |
| **GPL 3.0** | Yes | Yes | Yes | Yes | No | Yes | No |
| **AGPL 3.0** | Yes | Yes | Yes | Yes | No | Yes | Yes |

**Key insight**: GPL is one-directional. Permissive code can be included in GPL projects, but GPL code cannot be included in permissive projects. Code flows "upward" toward more restrictive licenses but never "downward."

## Compliance Obligations by Distribution Type

| Distribution Method | Obligation | Examples |
|---|---|---|
| **SaaS (no distribution)** | Fewer obligations -- most licenses are not triggered because no binary or source is distributed. **Exception**: AGPL requires source disclosure even for network use. | Web applications, API services, hosted platforms |
| **Binary distribution** | Must fulfill all license terms including attribution, license inclusion, and source disclosure (for copyleft). | Desktop applications, mobile apps, embedded firmware |
| **Source distribution** | Include license notices and copyright headers in all distributed source files. Maintain LICENSE and NOTICE files. | Libraries, SDKs, open-source projects, npm/PyPI packages |
| **Container images** | Binary distribution rules apply. Container images are considered binaries containing all bundled dependencies. | Docker images, OCI images published to registries |

## License Auditing Tools

| Tool | What It Does |
|---|---|
| **FOSSA** | Automated license compliance and vulnerability scanning across multiple languages and package managers. Generates SBOM and license reports. |
| **Snyk** | Identifies open-source license risks alongside security vulnerabilities. Supports policy-based license filtering. |
| **Black Duck (Synopsys)** | Enterprise-grade SCA tool for license compliance, vulnerability management, and code audit for M&A due diligence. |
| **Licensee** | Ruby-based tool that identifies the license of a project by examining LICENSE files. Used by GitHub for license detection. |
| **license-checker (npm)** | Scans npm dependencies and reports the license for each package. Supports allow/deny lists for CI enforcement. |
| **pip-licenses (Python)** | Lists licenses of installed Python packages. Supports output in CSV, JSON, and Markdown for integration into compliance workflows. |
| **go-licenses** | Scans Go module dependencies and reports licenses. Can check for disallowed licenses and export license notices. |

## Contributor License Agreements (CLA)

A **Contributor License Agreement** is a legal document that contributors sign before their code is accepted into a project. CLAs grant the project maintainer (or owning organization) certain rights over the contributed code, typically including:

- The right to relicense the contribution.
- A patent license for any patents the contributor holds that are embodied in the contribution.
- A representation that the contributor has the right to make the contribution.

**Why projects use CLAs**: CLAs protect the project from future IP disputes and give the maintainer flexibility to change the project's license or offer commercial licensing without needing to contact every past contributor.

**CLA vs DCO (Developer Certificate of Origin)**: A DCO is a lighter-weight alternative where contributors sign off (via `Signed-off-by` in commit messages) that they have the right to submit the code and agree to the project's license. The Linux kernel uses DCO. CLAs provide broader rights to the project maintainer, while DCOs simply certify the contributor's right to contribute under the existing license.

## Dual Licensing

**Dual licensing** is a business model in which software is released under two licenses simultaneously:

1. **An open-source license** (often a strong copyleft license like GPL or AGPL) that is free for open-source use.
2. **A commercial license** that allows proprietary use without the copyleft obligations, typically for a fee.

This model enables companies to sustain open-source development through commercial revenue. Users who are comfortable with the copyleft terms use the software for free; users who need proprietary use purchase a commercial license.

**Examples**:
- **MySQL** — Available under GPL and a commercial license from Oracle.
- **Qt** — Available under LGPL/GPL and a commercial license from The Qt Company.
- **MongoDB** — Moved from AGPL to SSPL (Server Side Public License), which imposes strong copyleft-like conditions on service providers, effectively encouraging commercial licensing.

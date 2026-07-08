# Supply Chain Security Rules

Best practices and rules for Supply Chain Security.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Generate and maintain SBOMs | MEDIUM | [`supply-chain-generate-and-maintain-sboms.md`](supply-chain-generate-and-maintain-sboms.md) |
| 2 | Run dependency scanning in CI | CRITICAL | [`supply-chain-run-dependency-scanning-in-ci.md`](supply-chain-run-dependency-scanning-in-ci.md) |
| 3 | Commit lock files to version control | MEDIUM | [`supply-chain-commit-lock-files-to-version-control.md`](supply-chain-commit-lock-files-to-version-control.md) |
| 4 | Sign all release artifacts | MEDIUM | [`supply-chain-sign-all-release-artifacts.md`](supply-chain-sign-all-release-artifacts.md) |
| 5 | Target SLSA Level 2 or higher | CRITICAL | [`supply-chain-target-slsa-level-2-or-higher.md`](supply-chain-target-slsa-level-2-or-higher.md) |
| 6 | Enable automatic dependency update PRs | MEDIUM | [`supply-chain-enable-automatic-dependency-update-prs.md`](supply-chain-enable-automatic-dependency-update-prs.md) |
| 7 | Use reproducible, hermetic builds | HIGH | [`supply-chain-use-reproducible-hermetic-builds.md`](supply-chain-use-reproducible-hermetic-builds.md) |
| 8 | Audit your transitive dependency tree | MEDIUM | [`supply-chain-audit-your-transitive-dependency-tree.md`](supply-chain-audit-your-transitive-dependency-tree.md) |

---

---
title: "Audit your transitive dependency tree"
impact: MEDIUM
impactDescription: "general best practice"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Audit your transitive dependency tree

Audit your transitive dependency tree: regularly — most supply chain attacks target deep transitive dependencies that are less visible to maintainers.

---

---
title: "Commit lock files to version control"
impact: MEDIUM
impactDescription: "general best practice"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Commit lock files to version control

Commit lock files to version control: and review lock file diffs in pull requests to detect unexpected dependency changes.

---

---
title: "Enable automatic dependency update PRs"
impact: MEDIUM
impactDescription: "general best practice"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Enable automatic dependency update PRs

Enable automatic dependency update PRs: via Dependabot, Renovate, or Snyk to keep dependencies current and reduce the window of exposure.

---

---
title: "Generate and maintain SBOMs"
impact: MEDIUM
impactDescription: "general best practice"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Generate and maintain SBOMs

Generate and maintain SBOMs: for every release artifact using SPDX or CycloneDX format, and store them alongside the artifacts they describe.

---

---
title: "Run dependency scanning in CI"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Run dependency scanning in CI

Run dependency scanning in CI: on every pull request and on a nightly schedule; block merges with critical or high unpatched vulnerabilities.

---

---
title: "Sign all release artifacts"
impact: MEDIUM
impactDescription: "general best practice"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Sign all release artifacts

Sign all release artifacts: use Sigstore/cosign for container images, GPG for packages, and enable npm provenance or PyPI Trusted Publishers as applicable.

---

---
title: "Target SLSA Level 2 or higher"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Target SLSA Level 2 or higher

Target SLSA Level 2 or higher: for production build pipelines, with signed provenance generated automatically by the build platform.

---

---
title: "Use reproducible, hermetic builds"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: supply-chain, security, sbom, software-bill-of-materials, dependency-scanning
---

## Use reproducible, hermetic builds

Use reproducible, hermetic builds: to ensure that build output can be independently verified and is not dependent on external state.

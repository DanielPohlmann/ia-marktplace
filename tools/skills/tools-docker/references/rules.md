# Docker & Containers Rules

Best practices and rules for Docker & Containers.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use multi-stage builds | CRITICAL | [`docker-use-multi-stage-builds.md`](docker-use-multi-stage-builds.md) |
| 2 | Pin base image versions with SHA | MEDIUM | [`docker-pin-base-image-versions-with-sha.md`](docker-pin-base-image-versions-with-sha.md) |
| 3 | Run as non-root | CRITICAL | [`docker-run-as-non-root.md`](docker-run-as-non-root.md) |
| 4 | Use .dockerignore | CRITICAL | [`docker-use-dockerignore.md`](docker-use-dockerignore.md) |
| 5 | Scan images in CI | MEDIUM | [`docker-scan-images-in-ci.md`](docker-scan-images-in-ci.md) |
| 6 | Use health checks | MEDIUM | [`docker-use-health-checks.md`](docker-use-health-checks.md) |
| 7 | Prefer COPY over ADD | LOW | [`docker-prefer-copy-over-add.md`](docker-prefer-copy-over-add.md) |
| 8 | Keep images small | HIGH | [`docker-keep-images-small.md`](docker-keep-images-small.md) |

---

---
title: "Keep images small"
impact: HIGH
impactDescription: "significant quality or reliability improvement"
tags: docker, tools, podman, dockerfile
---

## Keep images small

Use alpine/slim bases, clean up package manager caches in the same `RUN` layer, and avoid installing unnecessary packages.

---

---
title: "Pin base image versions with SHA"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, tools, podman, dockerfile
---

## Pin base image versions with SHA

Use `FROM node:22-alpine@sha256:abc123...` for immutable, reproducible builds that cannot be affected by upstream tag changes.

---

---
title: "Prefer COPY over ADD"
impact: LOW
impactDescription: "recommended but situational"
tags: docker, tools, podman, dockerfile
---

## Prefer COPY over ADD

`COPY` is explicit and predictable; `ADD` has implicit behaviors (URL fetching, tar extraction) that can surprise you.

---

---
title: "Run as non-root"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: docker, tools, podman, dockerfile
---

## Run as non-root

Always add a `USER` instruction to run the container process as a non-root user for defense in depth.

---

---
title: "Scan images in CI"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, tools, podman, dockerfile
---

## Scan images in CI

Integrate Trivy or Docker Scout into your CI pipeline to catch vulnerabilities before deployment.

---

---
title: "Use .dockerignore"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: docker, tools, podman, dockerfile
---

## Use .dockerignore

Exclude unnecessary files from the build context to speed up builds and avoid leaking secrets into images.

---

---
title: "Use health checks"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, tools, podman, dockerfile
---

## Use health checks

Add `HEALTHCHECK` instructions so orchestrators can detect and replace unhealthy containers automatically.

---

---
title: "Use multi-stage builds"
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: docker, tools, podman, dockerfile
---

## Use multi-stage builds

Separate build and runtime stages to keep production images small and free of build tools and source code.

# Docker Rules

Best practices and rules for Docker.

## Rules

| # | Rule | Impact | File |
|---|------|--------|------|
| 1 | Use multi-stage builds to keep production images small... | CRITICAL | [`docker-use-multi-stage-builds-to-keep-production-images-small.md`](docker-use-multi-stage-builds-to-keep-production-images-small.md) |
| 2 | Use specific version tags (`node | MEDIUM | [`docker-use-specific-version-tags-node.md`](docker-use-specific-version-tags-node.md) |
| 3 | Run as a non-root user (`USER node`, `USER nobody`, `USER... | MEDIUM | [`docker-run-as-a-non-root-user-user-node-user-nobody-user.md`](docker-run-as-a-non-root-user-user-node-user-nobody-user.md) |
| 4 | Use `.dockerignore` to exclude `node_modules/`, ` | MEDIUM | [`docker-use-dockerignore-to-exclude-node-modules.md`](docker-use-dockerignore-to-exclude-node-modules.md) |
| 5 | Copy dependency manifests before source code to leverage... | MEDIUM | [`docker-copy-dependency-manifests-before-source-code-to-leverage.md`](docker-copy-dependency-manifests-before-source-code-to-leverage.md) |
| 6 | Use `--no-cache-dir` for pip installs to reduce image size | MEDIUM | [`docker-use-no-cache-dir-for-pip-installs-to-reduce-image-size.md`](docker-use-no-cache-dir-for-pip-installs-to-reduce-image-size.md) |
| 7 | Use `depends_on` with `condition | MEDIUM | [`docker-use-depends-on-with-condition.md`](docker-use-depends-on-with-condition.md) |
| 8 | Use named volumes for persistent data (databases) and bind... | MEDIUM | [`docker-use-named-volumes-for-persistent-data-databases-and-bind.md`](docker-use-named-volumes-for-persistent-data-databases-and-bind.md) |

---

---
title: "Copy dependency manifests before source code to leverage..."
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Copy dependency manifests before source code to leverage...

Copy dependency manifests before source code to leverage layer caching.

---

---
title: "Run as a non-root user (`USER node`, `USER nobody`, `USER..."
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Run as a non-root user (`USER node`, `USER nobody`, `USER...

Run as a non-root user (`USER node`, `USER nobody`, `USER $APP_UID`).

---

---
title: "Use `depends_on` with `condition"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Use `depends_on` with `condition

Use `depends_on` with `condition: service_healthy` in Compose for startup ordering.

---

---
title: "Use `.dockerignore` to exclude `node_modules/`, `"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Use `.dockerignore` to exclude `node_modules/`, `

Use `.dockerignore` to exclude `node_modules/`, `.git/`, and other unnecessary files.

---

---
title: "Use multi-stage builds to keep production images small..."
impact: CRITICAL
impactDescription: "essential for correctness or security"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Use multi-stage builds to keep production images small...

Use multi-stage builds to keep production images small (build deps stay in build stage).

---

---
title: "Use named volumes for persistent data (databases) and bind..."
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Use named volumes for persistent data (databases) and bind...

Use named volumes for persistent data (databases) and bind mounts for development source code.

---

---
title: "Use `--no-cache-dir` for pip installs to reduce image size"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Use `--no-cache-dir` for pip installs to reduce image size

Use `--no-cache-dir` for pip installs to reduce image size.

---

---
title: "Use specific version tags (`node"
impact: MEDIUM
impactDescription: "general best practice"
tags: docker, iac, dockerfiles, docker-compose, multi-stage-builds
---

## Use specific version tags (`node

Use specific version tags (`node:22-alpine`) not `latest` for reproducibility.

---
name: tools-docker
description: Use when working with Docker or Podman in general — CLI, Dockerfiles, Compose, local infrastructure. USE FOR: Dockerfile instructions, multi-stage builds, Compose, networking, volumes, image optimization, BuildKit, rootless, registries, hardening. DO NOT USE FOR: .NET-specific Dockerfiles (use stack-docker), image scanning (use security-security-testing), Git (use tools-git), Kubernetes.
---

# Docker & Containers

## Overview

Containers package an application with all its dependencies into a portable, reproducible unit. Docker is the dominant container runtime; Podman is a daemonless, rootless alternative with Docker CLI compatibility. Containers are the foundation of modern deployment workflows, enabling consistent environments from development through production.

> **Detailed Dockerfile, multi-stage, image-optimization, Compose and operational how-tos with full examples live in [references/guide.md](references/guide.md); project-specific rules are in [references/rules.md](references/rules.md).** The material below is enough to orient and choose an approach.

## Docker vs Podman

| Feature              | Docker                     | Podman                              |
|----------------------|----------------------------|--------------------------------------|
| Daemon               | dockerd required           | Daemonless                           |
| Rootless             | Supported                  | Default                              |
| CLI Compatibility    | `docker`                   | `podman` / `alias docker=podman`     |
| Compose              | docker compose v2          | podman-compose                       |
| OCI Compliant        | Yes                        | Yes                                  |
| Systemd Integration  | Limited                    | Native with quadlets                 |
| Build Tool           | BuildKit                   | Buildah (integrated)                 |

---

## Common Commands

### Images

```bash
# Build an image
docker build -t myapp:1.0 .
docker build -t myapp:1.0 -f Dockerfile.prod .

# Build with BuildKit (recommended)
DOCKER_BUILDKIT=1 docker build -t myapp:1.0 .

# Pull an image
docker pull nginx:alpine

# Push to a registry
docker tag myapp:1.0 registry.example.com/myapp:1.0
docker push registry.example.com/myapp:1.0

# List images
docker images

# Remove an image
docker rmi myapp:1.0

# Inspect image details
docker inspect myapp:1.0

# View image history (layers)
docker history myapp:1.0
```

### Containers

```bash
# Run a container
docker run -d --name web -p 3000:3000 myapp:1.0

# Run interactively
docker run -it --rm ubuntu:22.04 bash

# Run with environment variables
docker run -d --name web -e NODE_ENV=production -p 3000:3000 myapp:1.0

# Execute a command in a running container
docker exec -it web sh
docker exec web cat /etc/os-release

# Stop / start / restart
docker stop web
docker start web
docker restart web

# Remove a container
docker rm web
docker rm -f web    # Force remove running container

# List containers
docker ps           # Running only
docker ps -a        # All (including stopped)

# View logs
docker logs web
docker logs -f web          # Follow
docker logs --tail 100 web  # Last 100 lines

# Copy files to/from container
docker cp web:/app/data.json ./data.json
docker cp ./config.yml web:/app/config.yml
```

### Volumes

```bash
# Create a named volume
docker volume create mydata

# List volumes
docker volume ls

# Remove a volume
docker volume rm mydata

# Run with a named volume
docker run -d -v mydata:/app/data myapp:1.0

# Run with a bind mount
docker run -d -v $(pwd)/src:/app/src myapp:1.0

# Run with a read-only bind mount
docker run -d -v $(pwd)/config:/app/config:ro myapp:1.0
```

**Named Volumes vs Bind Mounts:**
- **Named volumes** — managed by Docker, persist across container restarts, portable, use for databases and persistent data
- **Bind mounts** — map a host directory into the container, use for development (hot reloading source code)

### Networks

```bash
# Create a network
docker network create mynet

# List networks
docker network ls

# Run container on a specific network
docker run -d --name web --network mynet myapp:1.0

# Connect a running container to a network
docker network connect mynet web

# Inspect a network
docker network inspect mynet
```

**Network Drivers:**
- **bridge** — default, isolated network for containers on a single host
- **host** — share host network stack (no isolation, best performance)
- **none** — no networking

### System Maintenance

```bash
# Remove unused data (stopped containers, dangling images, unused networks)
docker system prune

# Also remove unused volumes
docker system prune --volumes

# Show disk usage
docker system df

# Remove build cache
docker builder prune

# Remove all unused images (not just dangling)
docker image prune -a
```

---

## .dockerignore

A `.dockerignore` file excludes files from the build context, reducing build time and image size.

```
# Version control
.git
.gitignore

# Dependencies (rebuilt in container)
node_modules
vendor
__pycache__
*.pyc
bin/
obj/

# Environment and secrets
.env
.env.*
*.pem
*.key

# IDE and OS files
.vscode
.idea
*.swp
.DS_Store
Thumbs.db

# Documentation
*.md
LICENSE
docs/

# Docker files (not needed inside the image)
docker-compose*.yml
Dockerfile*
.dockerignore

# Build artifacts
dist/
build/
coverage/
.nyc_output/

# Tests (if not running tests in container)
test/
tests/
*.test.js
*.spec.js
```

---

## Best Practices

1. **Use multi-stage builds** — Separate build and runtime stages to keep production images small and free of build tools and source code.
2. **Pin base image versions with SHA** — Use `FROM node:22-alpine@sha256:abc123...` for immutable, reproducible builds that cannot be affected by upstream tag changes.
3. **Run as non-root** — Always add a `USER` instruction to run the container process as a non-root user for defense in depth.
4. **Use .dockerignore** — Exclude unnecessary files from the build context to speed up builds and avoid leaking secrets into images.
5. **Scan images in CI** — Integrate Trivy or Docker Scout into your CI pipeline to catch vulnerabilities before deployment.
6. **Use health checks** — Add `HEALTHCHECK` instructions so orchestrators can detect and replace unhealthy containers automatically.
7. **Prefer COPY over ADD** — `COPY` is explicit and predictable; `ADD` has implicit behaviors (URL fetching, tar extraction) that can surprise you.
8. **Keep images small** — Use alpine/slim bases, clean up package manager caches in the same `RUN` layer, and avoid installing unnecessary packages.

## Detailed reference

Load only the file that matches the task — each is self-contained.

| File | Contents |
|---|---|
| [references/dockerfile.md](references/dockerfile.md) | Dockerfile — Common Instructions, Example: Node.js Application, Example: Python Application |
| [references/details.md](references/details.md) | Multi-Stage Builds; Image Optimization; Docker Compose; Container Security; Registries |

## References

- [Docker Documentation](https://docs.docker.com)
- [Podman Documentation](https://podman.io/docs)
- [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)

See references/rules.md for the full rule catalog.

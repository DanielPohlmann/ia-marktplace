<!-- Part of the tools-docker skill. Loaded on demand from SKILL.md. -->

# Docker & Containers — details

## Multi-Stage Builds

Multi-stage builds produce smaller production images by separating the build environment from the runtime environment. Build tools, source code, and intermediate artifacts are left behind in the build stage.

```dockerfile
# Stage 1: Build
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:22-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./

USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Go Application (Scratch Base)

```dockerfile
FROM golang:1.22-alpine AS build
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

FROM scratch
COPY --from=build /app/server /server
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
EXPOSE 8080
ENTRYPOINT ["/server"]
```

---

## Image Optimization

| Technique                           | Impact                                                |
|-------------------------------------|-------------------------------------------------------|
| Use alpine/slim base images         | 5-10x smaller than full images                        |
| Multi-stage builds                  | Remove build dependencies from production image       |
| Order layers for cache              | COPY package.json before source code                  |
| Combine RUN commands                | Fewer layers, smaller image                           |
| Use .dockerignore                   | Exclude unnecessary files from build context          |
| Use specific tags, not `:latest`    | Reproducible builds, predictable behavior             |
| Clean up in the same RUN layer      | `RUN apt install -y pkg && rm -rf /var/lib/apt/lists/*` |
| Pin base image by SHA digest        | Immutable, tamper-proof base images                   |

### Layer Caching Example

```dockerfile
# GOOD: Dependencies change less often than source code
COPY package.json package-lock.json ./
RUN npm ci
COPY . .

# BAD: Any source change invalidates the npm ci cache
COPY . .
RUN npm ci
```

---

## Docker Compose

Docker Compose defines multi-container applications in a single YAML file.

### Example: Web App + Database + Redis

```yaml
# docker-compose.yml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - ./src:/app/src    # Dev: mount source for hot reload
    networks:
      - app-network
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: myapp
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d myapp"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - app-network

volumes:
  postgres-data:
  redis-data:

networks:
  app-network:
    driver: bridge
```

### Common Compose Commands

```bash
# Start all services in detached mode
docker compose up -d

# Stop and remove containers
docker compose down

# Stop, remove containers, and delete volumes
docker compose down -v

# View logs
docker compose logs
docker compose logs -f web    # Follow logs for specific service

# Rebuild images
docker compose build
docker compose up -d --build

# Scale a service
docker compose up -d --scale web=3

# Run a one-off command
docker compose exec web sh
docker compose run --rm web npm test

# List running services
docker compose ps
```

---

## Container Security

### Run as Non-Root User

```dockerfile
# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
```

### Read-Only File System

```bash
docker run --read-only --tmpfs /tmp myapp:1.0
```

### Drop Capabilities

```bash
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myapp:1.0
```

### No Privileged Mode

```bash
# NEVER use --privileged in production
# Instead, add only the specific capabilities needed
docker run --cap-add SYS_PTRACE myapp:1.0
```

### Scan Images

```bash
# Trivy — open-source vulnerability scanner
trivy image myapp:1.0

# Docker Scout (built into Docker Desktop)
docker scout cves myapp:1.0

# Scan during CI
trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:1.0
```

### Use Distroless or Scratch Base Images

```dockerfile
# Distroless — minimal base with no shell, no package manager
FROM gcr.io/distroless/static-debian12
COPY --from=build /app/server /server
CMD ["/server"]

# Scratch — empty base image (for statically compiled binaries)
FROM scratch
COPY --from=build /app/server /server
CMD ["/server"]
```

### Secrets Handling

```bash
# Docker secrets (Swarm mode)
echo "my-secret-value" | docker secret create db_password -

# BuildKit secrets (build-time only, not stored in image layers)
docker build --secret id=mysecret,src=./secret.txt .
```

```dockerfile
# Use secret during build (not persisted in image)
RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret
```

**Never use ENV for secrets** — environment variables are visible in `docker inspect` and image history.

---

## Registries

| Registry                          | Provider        | Key Feature                         |
|-----------------------------------|-----------------|-------------------------------------|
| Docker Hub                        | Docker          | Default public registry             |
| GitHub Container Registry (ghcr.io) | GitHub        | Integrated with GitHub Actions      |
| AWS ECR                           | Amazon          | Integrated with AWS IAM             |
| Azure ACR                         | Microsoft       | Integrated with Azure AD            |
| GCP Artifact Registry             | Google          | Multi-format (Docker, npm, Maven)   |
| Harbor                            | CNCF / self-hosted | Enterprise self-hosted registry  |

### Pushing to a Registry

```bash
# Docker Hub
docker login
docker tag myapp:1.0 username/myapp:1.0
docker push username/myapp:1.0

# GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag myapp:1.0 ghcr.io/username/myapp:1.0
docker push ghcr.io/username/myapp:1.0

# AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
docker tag myapp:1.0 123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
```

---

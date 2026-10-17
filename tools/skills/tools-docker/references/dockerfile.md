<!-- Part of the tools-docker skill. Loaded on demand from SKILL.md. -->

# Dockerfile

## Common Instructions

| Instruction    | Purpose                                    | Example                                          |
|----------------|--------------------------------------------|--------------------------------------------------|
| `FROM`         | Set base image                             | `FROM node:22-alpine`                            |
| `RUN`          | Execute command during build               | `RUN npm ci`                                     |
| `COPY`         | Copy files from host to image              | `COPY package.json ./`                           |
| `ADD`          | Copy files (supports URLs, tar extraction) | `ADD app.tar.gz /app`                            |
| `WORKDIR`      | Set working directory                      | `WORKDIR /app`                                   |
| `ENV`          | Set environment variable                   | `ENV NODE_ENV=production`                        |
| `ARG`          | Build-time variable                        | `ARG VERSION=latest`                             |
| `EXPOSE`       | Document container port                    | `EXPOSE 3000`                                    |
| `CMD`          | Default command (overridable)              | `CMD ["node", "server.js"]`                      |
| `ENTRYPOINT`   | Main executable (not easily overridden)    | `ENTRYPOINT ["python", "app.py"]`                |
| `USER`         | Set runtime user                           | `USER node`                                      |
| `HEALTHCHECK`  | Container health check                     | `HEALTHCHECK CMD curl -f http://localhost:3000/` |
| `LABEL`        | Add metadata                               | `LABEL maintainer="team@example.com"`            |

## Example: Node.js Application

```dockerfile
FROM node:22-alpine

WORKDIR /app

# Copy dependency files first (better layer caching)
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copy application code
COPY src/ ./src/

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["node", "src/server.js"]
```

## Example: Python Application

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

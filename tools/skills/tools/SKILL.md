---
name: tools
description: Router skill for core cross-cutting developer tools — Docker/containers and Git version control. Use only when unsure which sub-skill applies; prefer tools-docker or tools-git directly for any concrete task. USE FOR: deciding between tools-docker and tools-git, general container or version-control orientation questions. DO NOT USE FOR: any concrete Docker task (use tools-docker), any concrete Git task (use tools-git), Kubernetes orchestration, cloud container services, GitHub/GitLab platform features, CI/CD pipeline configuration, .NET-specific Dockerfile patterns (use stack-docker).
---

# Development Tools

## Overview

This skill tree covers the cross-cutting developer tools used throughout the LinkDaily project: **Docker** for containerization and local environment orchestration, and **Git** for version control and collaborative workflows.

## Sub-Skills

| Sub-Skill | Covers |
|-----------|--------|
| `docker` | Dockerfiles, multi-stage builds, docker-compose, image optimization, container networking, volumes, registries, and security |
| `git` | Branching strategies, merging, rebasing, conflict resolution, hooks, worktrees, and common Git workflows |

## Choosing the Right Sub-Skill

| Need | Sub-Skill |
|------|-----------|
| Write or optimize a Dockerfile | `docker` |
| Set up docker-compose for local dev | `docker` |
| Container image size reduction | `docker` |
| Rootless containers or security hardening | `docker` |
| Branch naming, merge vs rebase strategy | `git` |
| Resolve merge conflicts | `git` |
| Set up or debug a Git hook | `git` |
| Cherry-pick, bisect, or rewrite history | `git` |
| Trunk-based development vs Gitflow | `git` |

## Best Practices

- Keep Docker and Git skills separate — container concerns (build, run, network) should not bleed into version control decisions and vice versa.
- Use the `docker` sub-skill before writing any new `Dockerfile` to ensure consistency with existing multi-stage build patterns in the project.
- Use the `git` sub-skill when proposing branching or merge strategies so the approach aligns with how the team already works.

## References

- [Docker Documentation](https://docs.docker.com)
- [Git Documentation](https://git-scm.com/doc)

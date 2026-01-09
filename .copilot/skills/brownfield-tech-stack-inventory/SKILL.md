---
name: tech-stack-inventory
description: Determine the repository’s tech stack (languages, frameworks, build/test/deploy tooling) and generate/refresh a technical-requirements.md baseline for brownfield development.
---

## Goal
Produce `technical-requirements.md` that documents the detected tech stack and “how this repo runs” with evidence links.

## Inputs
- Repository working tree
- Existing `technical-requirements.md` (if present)

## Output
- Create or update `technical-requirements.md` at repo root.

## Procedure

### 1) Establish repo type and boundaries
- Identify whether this is monorepo vs single service.
- Detect top-level apps/services (folders like apps/, services/, src/, packages/).
- Note any “example/”, “legacy/”, “archive/” areas and exclude them unless they are active.

### 2) Detect languages and primary frameworks (evidence-first)
Scan for canonical files and record findings with file evidence:
- Node/TS: package.json, tsconfig.json, pnpm-lock.yaml/yarn.lock/package-lock.json
- Java: pom.xml, build.gradle(.kts), settings.gradle
- .NET: *.sln, *.csproj, global.json
- Python: pyproject.toml, requirements*.txt, poetry.lock, pipfile
- Go: go.mod
- Ruby: Gemfile
- PHP: composer.json

For each detected stack element, record:
- What it is
- Where it is proven (file path)
- Confidence: confirmed / likely / guess

### 3) Build and run commands
Extract canonical commands from:
- README.md / docs/
- package.json scripts
- Makefile / Taskfile.yml / justfile
- CI config (GitHub Actions, Azure DevOps, Jenkinsfile, etc.)

Prefer “copyable” commands and include prerequisites (e.g., JDK version, Node version).

### 4) Test strategy snapshot
Detect test frameworks and how to run them:
- Unit/integration/e2e hints from configs and folder conventions
- Coverage tools if present
- Known test entrypoints (scripts, gradle tasks, dotnet test, pytest, etc.)

### 5) Runtime topology & integration points (lightweight)
Without overreaching into architecture:
- Identify executables / entrypoints (main files, startup classes, server.js, Program.cs, etc.)
- Detect external dependencies: DBs, queues, caches, third-party APIs via config files and docker-compose/k8s manifests.
- List config sources (env vars, config files, secrets management references)

### 6) Deploy/build pipelines & environments
Detect:
- Containerization: Dockerfile, docker-compose.yml
- Orchestration: k8s manifests, Helm charts, Terraform, Pulumi
- CI/CD: workflows and what they build/deploy
- Environments: dev/stage/prod naming in config

### 7) Generate `technical-requirements.md`
- If file exists: update in-place, preserving any repo-specific notes.
- If not: create from the template in `assets/technical-requirements.template.md`.
- Ensure every major claim has evidence (file paths).
- Add a “Verification checklist” section: exact commands to confirm assumptions.

### 8) Quality bar
Before finishing:
- No invented versions. If version is unknown, say “not found” and list where you looked.
- Separate “Detected” vs “Assumed/Conventional” clearly.
- Keep to one page where possible; move long lists to appendix.

## References
- If stack-specific variants are needed (Angular/AWS, Next.js/AWS), add them under `references/` and link from this file.
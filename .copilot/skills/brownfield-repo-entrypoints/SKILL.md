---
name: brownfield-repo-entrypoints
description: Identify what runs in a brownfield repository (services/apps/jobs), where the entrypoints are, and the canonical commands to start/execute them, producing an entrypoints.md artifact with evidence.
---

## Goal
Produce `entrypoints.md` that answers:
- What runnable things exist?
- Where are their entrypoints?
- How do you run them locally (as discovered, not invented)?
- What config they require (lightweight)?

## Inputs
- Repository working tree
- Existing `entrypoints.md` (if present)

## Output
- Create or update `entrypoints.md` at repo root.

## Procedure

### 1) Enumerate runnable units (don’t infer architecture)
- Scan repo structure for likely apps/services/jobs:
  - apps/, services/, src/, packages/, cmd/, server/, api/, web/, worker/, jobs/
- Mark each as: service / web app / CLI / background worker / scheduled job / library-only.
- Note monorepo boundaries: which folders are independent run targets.

### 2) Detect entrypoint files/classes (evidence-first)
For each runnable unit, identify the concrete entrypoint(s) using file evidence:
- Node: main/module in package.json, scripts, src/index.*, server.*, app.*
- Java: SpringBootApplication main class, application.yml, bootRun tasks
- .NET: Program.cs, Startup.cs, launchSettings.json
- Python: __main__.py, console_scripts, manage.py, app.py, wsgi/asgi entrypoints
- Go: cmd/*/main.go
- Containers: Dockerfile ENTRYPOINT/CMD
- K8s: deployment args/command, container image refs

Record:
- Entrypoint (path + symbol/class if applicable)
- How it’s invoked (script/task/command)
- Confidence: confirmed / likely / guess

### 3) Extract canonical run/exec commands
Prefer authoritative sources, in this order:
1) README/docs
2) package.json scripts / Makefile / Taskfile / justfile
3) Docker Compose profiles/services
4) CI workflows (build + run steps)
5) IDE launch configs (launch.json / launchSettings.json)

Capture copy/paste commands per runnable unit.

### 4) Identify runtime dependencies & required config (lightweight)
Without going deep into architecture:
- Required env vars/config files (list names only; don’t guess values)
- Local deps: DB, cache, queue, object storage, mock servers
- Ports and URLs (from config, compose, k8s)

### 5) Validate “what runs” claims
- If a runnable unit has no runnable command found, explicitly mark it “unknown” and list where you looked.
- Never invent versions or commands.

### 6) Generate/refresh `entrypoints.md`
- If file exists: update in place; preserve hand-written notes.
- Ensure each runnable unit includes: purpose, entrypoint, run command, required config, deps, evidence.

## References
- Add stack-specific heuristics under `references/` only when needed.

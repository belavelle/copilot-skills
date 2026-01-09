---
name: brownfield-codebase-recon
description: First-pass reconnaissance of an unfamiliar/brownfield codebase to produce a minimal, evidence-backed orientation packet (how to build/run/test, entrypoints, module map, risks, and next questions) without making architectural assumptions.
---

## Goal
Produce a small orientation packet that lets a developer safely begin feature/enhancement work.

## Outputs
- recon.md (primary)
- entrypoints.md (via brownfield-repo-entrypoints, if multiple runnable units exist)

## Procedure

### 1) Establish scope
Identify monorepo vs single service, active vs legacy areas, and likely runnable units.

### 2) Read repo docs fast
Scan README, docs, ADRs, CI configs. Prefer CI truth over prose.

### 3) Determine build/run/test
Extract copyable commands with file-path evidence. Never invent commands.

### 4) Identify entrypoints
If multiple runnable units exist:
- Run brownfield-repo-entrypoints
- Link entrypoints.md in Section 2 of recon.md
Otherwise, document the single entrypoint with evidence.

### 5) Thin module map
List top-level modules (max ~10) with 1-line purpose notes.

### 6) Representative execution path
Trace one end-to-end flow relevant to the repo’s purpose.

### 7) Constraints, risks, unknowns
List explicitly, with evidence and follow-up locations.

### 8) Write recon.md
Keep to ~1 page where possible. Evidence-first.

## Time & Quality Bar
- Target time: ≤ 30 minutes
- Recon Confidence Score ≥ 7/10 required to begin coding
- No invented behavior or versions

## References
- See references/recon-heuristics.multi-stack.md

# Brownfield Skills & Playbooks

This repository provides a structured system for working safely and effectively in
brownfield (existing, unfamiliar, or legacy) codebases.

It separates **execution**, **decision-making**, and **guardrails** into distinct concepts
so agents and humans can collaborate without mixing responsibilities.

---

## Core Concepts

### Skills
**Skills are executable procedures.**

They:
- perform discovery or analysis
- produce concrete artifacts (markdown files)
- are time-boxed and evidence-driven
- avoid opinions or architectural prescriptions

Examples:
- `brownfield-codebase-recon`
- `brownfield-repo-entrypoints`
- `tech-stack-inventory`

Skills answer questions like:
- *What is here?*
- *What runs?*
- *How do I build/test/start this?*

---

### Assets
**Assets are templates and checklists used by skills.**

They:
- standardize outputs
- reduce reasoning overhead
- are not loaded into agent context by default

Examples:
- `recon.template.md`
- `recon-completion-checklist.md`

Assets ensure consistency without inflating prompts.

---

### References
**References are deep heuristics and domain knowledge.**

They:
- support trained coding/test agents
- are consulted selectively
- never define required behavior

Examples:
- `recon-heuristics.multi-stack.md`

If something becomes too detailed for a skill, it belongs in references.

---

### Playbooks
**Playbooks guide decisions, not execution.**

They:
- define *when* and *how* to act
- set safety boundaries
- prevent premature or dangerous changes
- apply after or between skills

Examples:
- `brownfield-first-feature.md`
- `brownfield-stop-rules.md`

Playbooks answer questions like:
- *What is a safe next step?*
- *When should I stop and escalate?*

---

## How They Work Together (Typical Flow)

1. **Run a skill**
   - e.g. `brownfield-codebase-recon`
   - Produces `recon.md`

2. **Validate readiness**
   - Use `recon-completion-checklist.md`
   - Check Recon Confidence Score

3. **Consult playbooks**
   - Choose a safe first change (`brownfield-first-feature.md`)
   - Verify no stop conditions apply (`brownfield-stop-rules.md`)

4. **Run additional skills as needed**
   - `brownfield-repo-entrypoints`
   - `tech-stack-inventory`

5. **Begin coding**
   - With explicit constraints, risks, and rollback paths

---

## Design Principles

- **Evidence over inference**
- **Small, reversible steps**
- **Explicit stop conditions**
- **No architectural speculation during recon**
- **Decision discipline beats heroics**

If something feels unclear or requires guessing, stop and escalate.
That is success, not failure.

---

## Intended Audience

- Engineers onboarding to unfamiliar systems
- Senior developers working in legacy codebases
- Coding- and test-trained agents assisting with brownfield work

---

## Final Note

Skills discover reality.  
Playbooks protect judgment.  

Do not substitute one for the other.

# Copilot Skills System – Architecture & Conventions

## Purpose

This repository defines a lightweight, intentional system for extending
GitHub Copilot (VS Code, agent mode) with reusable skills, governance prompts,
and progressive context loading.

The goal is to:
- Encode domain knowledge and workflows once
- Avoid prompt sprawl and repeated explanations
- Keep the context window small and intentional
- Enable skill composition (stacking constraints + execution)
- Allow new contributors or chat sessions to pick up immediately

This is a prompt- and structure-based system, not a plugin or extension.

---

## Core Design Principles

### 1. Concise Is Key
The context window is a shared, finite resource.

- Assume the model is already capable
- Include only non-obvious, procedural, or reusable knowledge
- Prefer examples over explanations
- Delete before adding

---

### 2. Progressive Disclosure
Context is loaded in layers:

1. Instructions – always-on rules (very small)
2. Prompts – behavior and process (invoked explicitly)
3. Skills (SKILL.md) – domain workflows (loaded intentionally)
4. References / Scripts / Assets – loaded only when needed

Nothing loads implicitly.

---

### 3. Separation of Concerns

Concept | Location | Purpose
------- | -------- | -------
Policy | .github/copilot-instructions.md | Always-on rules
Process | .prompts/ | Selection, execution, critique
Domain Knowledge | .copilot/skills/* | How to do real work
Deep Detail | references/ | Large or specific info
Determinism | scripts/ | Reusable helpers
Output Resources | assets/ | Templates, boilerplate

---

## Repository Structure

```
.
├── .github/
│   └── copilot-instructions.md
├── .copilot/
│   └── skills/
│       ├── skill-creator/
│       │   └── SKILL.md
│       ├── frontend-design/
│       │   └── SKILL.md
│       └── internal-technical-standards/
│           ├── SKILL.md
│           └── references/
│               ├── technical-preferences.angular-aws.md
│               └── technical-preferences.nextjs-aws.md
└── .prompts/
    ├── skills-index.prompt.md
    ├── skill-selection-checklist.prompt.md
    ├── skill-execution.prompt.md
    └── skill-critique-refactor.prompt.md
```

---

## Instructions

.github/copilot-instructions.md is always-on and small.
It establishes conventions, progressive disclosure, and guardrails.

---

## Prompts

Prompts live in .prompts/ and govern behavior, not domain knowledge.

- Skills index – discovery and routing
- Selection checklist – decide whether to use/create a skill
- Execution – disciplined skill use
- Critique & refactor – improve skills over time

Prompts are not skills.

---

## Skills

Skills live in .copilot/skills/*.

A skill is a domain-specific onboarding guide for a Copilot agent.

### SKILL.md Rules

- YAML frontmatter with name and description only
- Description defines when the skill applies
- Body is procedural and lean (< ~500 lines)
- Move detail to references early

---

## Bundled Resources

### references/
- Loaded only when needed
- Schemas, policies, APIs, variants

### scripts/
- Deterministic helpers
- Run manually by developers

### assets/
- Templates, boilerplate, output resources
- Not loaded into context

---

## Skill Composition

Skills are composable.

Example:
- internal-technical-standards constrains choices
- frontend-design applies aesthetics within constraints

Do not mix responsibilities.

---

## Skill Lifecycle

1. Decide if a skill is needed
2. Design with skill-creator
3. Implement minimally
4. Use on real work
5. Critique and refactor
6. Iterate

---

## Starting a New Chat Session

To continue in a new chat:

1. Paste this file first
2. Then describe the task
3. Invoke prompts or skills explicitly

This file is the canonical context.

---

## Design Intent

This system favors:
- Intentionality over automation
- Explicit over implicit
- Structure over cleverness
- Evolution over completeness

It is designed to scale from:

- a single developer
- to a team
- to an internal platform

without becoming fragile or opaque.

---

## How to Use This Practically

### For **you**
- Paste this file at the start of a new chat
- Then continue as if nothing was lost

### For **others**
- Share the repo
- Tell them: *“Start by reading COPILOT-SKILLS-SYSTEM.md”*
- They can immediately contribute or test

### For **future automation**
- This document becomes the spec
- Tooling can be added later without rethinking the model

---

## Final Recommendation

This is the **right moment** to freeze context into a document.

You’ve done the hard part — the system thinking.
Now you’ve made it durable.

If you want, next time we pick this up we can:
- pressure test skill composition
- add versioning conventions
- or design a “skill maturity” rubric

But for now: this document will carry you forward cleanly.
---
name: skill-creator
description: Create or update Copilot skills that encode reusable workflows, domain knowledge, or helper resources. Use when designing a new skill or refining an existing one.
---

# Skill Creator

This skill guides the creation of effective Copilot skills.

## What a Skill Is

A skill is a small, self-contained package that teaches a Copilot agent how to
perform a specialized task by providing:

1. Procedural workflows
2. Domain-specific knowledge
3. Reusable helpers (scripts, references, assets)

Think of skills as *onboarding guides* for specific problem domains.

## Core Principles

### Concise Is Key

The context window is shared and finite.

**Default assumption: the model is already capable.**
Only include information that is:
- Non-obvious
- Procedural
- Reused across tasks

Prefer short examples over explanations.

### Set the Right Degree of Freedom

Match specificity to task fragility:

- **High freedom**: Text guidance and heuristics
- **Medium freedom**: Pseudocode or parameterized patterns
- **Low freedom**: Fixed scripts or strict sequences

Fragile tasks need guardrails. Flexible tasks need space.

## Skill Anatomy

Each skill consists of a required `SKILL.md` and optional bundled resources:

```
skill-name/
├── SKILL.md        (required)
├── references/     (optional)
├── scripts/        (optional)
└── assets/         (optional)
```

### SKILL.md

- **Frontmatter**: `name` and `description` only
  - Description defines *when the skill applies*
- **Body**: Essential instructions only
  - Loaded intentionally by the user or agent

### References (`references/`)

Documentation loaded **only when needed**.

Use for:
- Schemas
- API docs
- Policies
- Detailed workflows

Guidelines:
- Link references from SKILL.md
- Avoid duplication
- For large files, include search cues

### Scripts (`scripts/`)

Executable helpers for deterministic or repetitive work.

Use when:
- The same code is rewritten repeatedly
- Reliability matters

Notes:
- Scripts are run by developers, not agents
- Scripts may still be read or modified

### Assets (`assets/`)

Files used in outputs, not loaded into context.

Examples:
- Templates
- Boilerplate projects
- Fonts, images, icons

## What Not to Include

Do **not** add:
- README files
- Installation guides
- Changelogs
- Process documentation

A skill should contain only what another agent needs to do the job.

## Progressive Disclosure

Use three levels:

1. **Metadata** – name + description
2. **SKILL.md body** – core workflow
3. **Bundled resources** – loaded selectively

Keep SKILL.md small. Split early.

## Skill Creation Process

1. **Understand usage**
   - Collect concrete examples
   - Identify trigger phrases

2. **Plan reusable contents**
   - Decide what belongs in scripts, references, or assets

3. **Create the skill folder**
   - Add SKILL.md with clear frontmatter
   - Add only necessary resources

4. **Implement and refine**
   - Write imperative instructions
   - Test scripts manually if present
   - Remove unused placeholders

5. **Iterate**
   - Observe real usage
   - Tighten instructions
   - Move excess detail into references

# Copilot Skills System (Conventions)

This repository uses a lightweight “skills” system to encode reusable workflows,
domain knowledge, and patterns for Copilot agents.

## Core Principles
- **Concise is key**: Only include information the model does not already know.
- **Progressive disclosure**: Keep core instructions small; move details to references.
- **No doc sprawl**: Do not add README, setup guides, or auxiliary documentation.

## Skill Structure
Each skill lives in its own folder:

.copilot/skills/<skill-name>/
├── SKILL.md          (required)
├── references/       (optional, load only when needed)
├── scripts/          (optional, developer-executed helpers)
└── assets/           (optional, templates/resources for output)

## SKILL.md Rules
- Must include YAML frontmatter with **name** and **description** only
- Description defines *when the skill should be used*
- Body contains only essential procedural guidance
- Keep under ~500 lines; split into references when needed

## Scripts
Scripts are helpers for developers, not autonomous agent tools.
They may be referenced, inspected, or modified, but are run manually.

When creating or updating skills, follow these conventions strictly.

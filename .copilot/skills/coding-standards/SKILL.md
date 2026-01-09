---
name: coding-standards
description: Cross-language standards for generating or modifying code in this repo. Emphasizes security, consistency, and reuse (prefer lib/ helpers over ad-hoc code).
---

# Coding Standards

## Security
- Do not hard-code secrets or credentials.
- Treat all external input as untrusted.
- Avoid injection-prone patterns.
- Do not weaken existing security controls.

## Consistency
- Follow existing repo conventions.
- Prefer small, reviewable changes.

## Reuse First
- Prefer helpers in lib/.
- If logic is reusable, move it to lib/.

## Output Expectations
- List files changed.
- Provide minimal run/test steps.
- Ask one targeted question if inputs are missing.

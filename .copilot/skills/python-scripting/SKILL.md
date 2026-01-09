---
name: python-scripting
description: Python scripting standards for safe, consistent, reusable code. Use when creating or editing Python scripts, CLIs, or automation. Emphasizes security, error handling, typing discipline, and reuse (prefer lib/ helpers).
---

# Python Scripting

## Baseline
- Prefer explicit, readable code over cleverness.
- Use small functions with clear contracts.

## Contracts
- Validate external inputs early.
- Define inputs, outputs, and error behavior.

## Error Handling
- Never use bare `except:`.
- Do not silently swallow exceptions.
- Raise with context or return a structured error.

## Security
- No secrets in code.
- Avoid eval/exec.
- Avoid subprocess shell=True unless explicitly required and inputs validated.

## Reuse First
- Prefer helpers in lib/.
- If logic is reused or fragile, centralize it in lib/.

## Typing
- Add type hints for public and non-trivial functions.
- Keep return types consistent.

## Linting
- Prefer lint-clean code (see references).
- Document intentional rule suppressions.

## References
- Security: references/python-security.md
- Errors: references/python-errors.md
- Typing: references/python-typing.md
- Linting: references/python-linting-workflow.md
- lib/: references/python-lib-conventions.md

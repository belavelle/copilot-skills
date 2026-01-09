---
name: bash-scripting
description: Bash scripting standards with safe quoting, parameter expansion, error handling, and command execution patterns. Use for any .sh file edits.
---

# Bash Scripting

## Baseline
- Use bash with strict mode unless documented.
- Use local variables in functions.

## Quoting & Expansion
- Quote variables by default.
- Use "$@" not $*.
- Use ${10}+ for positional parameters above 9.

## Command Execution
- Treat bash -lc wrappers as string-command APIs.
- Never join arguments with "$*".

## Security
- Validate inputs.
- Avoid eval.
- Minimize remote shell injection risk.

## Reuse
- Prefer lib/ helpers for logging, exec, fs, asserts.

## ShellCheck
- Prefer ShellCheck-clean code.
- Document SC suppressions when required.

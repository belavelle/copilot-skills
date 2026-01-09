# Copilot Skills Prototype

A lightweight, repo-native framework for building **reusable Copilot agent skills** in VS Code.

This repository uses **files and conventions** (not an extension) to encode internal standards,
repeatable workflows, and language-specific guardrails so Copilot produces more **consistent,
secure, high-quality results**.

---

## Repository Layout

- `.github/copilot-instructions.md`  
  Always-on conventions for how skills are authored and used.

- `.prompts/`  
  Governance prompts (selection/execution/critique) used intentionally in Copilot Chat.

- `.copilot/skills/`  
  Skills that encode domain workflows and constraints. Each skill is self-contained.

- `lib/`  
  Small reusable helpers (Bash + Python) to reduce fragile copy/paste patterns.

- `COPILOT-SKILLS-SYSTEM.md`  
  Canonical “context rehydration” doc for starting new chat windows.

---

## How to Use (VS Code Copilot Agent Mode)

### Recommended flow
1. **Select a skill**  
   Run `.prompts/skills-index.prompt.md` and choose the best fit.

2. **Decide if a skill is warranted** (optional)  
   Run `.prompts/skill-selection-checklist.prompt.md`.

3. **Execute the skill**  
   Tell Copilot which skill to use, then run `.prompts/skill-execution.prompt.md`.

4. **Improve skills over time**  
   After real usage, run `.prompts/skill-critique-refactor.prompt.md`.

### Example prompts
- “Help me decide which skill applies to this task.”
- “Use the `bash-scripting` skill to refactor this script for safe input handling and ShellCheck cleanliness.”
- “Use `internal-technical-standards` to create `technical-preferences.md` for this repo (Next.js stack).”
- “Critique and refactor the `python-scripting` skill based on the last run.”

---

## Starting New Chat Windows With Context

Context windows fill up. To continue work reliably:

1. Open `COPILOT-SKILLS-SYSTEM.md`
2. Paste it into the first message of a new Copilot chat
3. Then describe the new task and invoke prompts/skills as needed

Tip: Keep `COPILOT-SKILLS-SYSTEM.md` up to date as the system evolves.

---

## Creating a New Skill

Use the `skill-creator` skill.

### Process
1. Collect 2–3 real examples of the task
2. Identify the non-obvious rules, constraints, and common failure modes
3. Write a lean `SKILL.md` (procedural; < ~500 lines)
4. Move depth into `references/`
5. If logic is fragile/reused, centralize it in `lib/`

### Template
```
.copilot/skills/<new-skill>/
├── SKILL.md
├── references/   (optional)
├── scripts/      (optional; developer-run)
└── assets/       (optional)
```

After adding a new skill, update `.prompts/skills-index.prompt.md`.

---

## Notes on Security & Input Validation

This prototype is intentionally security-first:
- Treat external inputs as untrusted
- Validate early using allowlists/patterns
- Avoid injection-prone constructs (shell string composition, eval/exec)
- Prefer reusable helpers in `lib/`

---

## Contributing

This system improves through real usage:
- Start lean
- Pressure test with real tasks
- Prefer deletion over addition
- Split into references early
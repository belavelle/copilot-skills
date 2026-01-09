
## Make `tech-stack-inventory` depend on it (minimal change)

In `tech-stack-inventory`’s procedure, add an early step like:

- **Step 1: Invoke/consume `brownfield-repo-entrypoints` output**
  - If `entrypoints.md` exists, use it as the authoritative list of runnable units + run commands.
  - If it doesn’t exist, run `brownfield-repo-entrypoints` first, then proceed.

Then, in `tech-stack-inventory`, you can explicitly say:
- “Use the runnable-units list from `entrypoints.md` to scope stack detection per unit (avoid scanning irrelevant folders).”
- “Use the discovered run/build/test commands as primary evidence for tooling.”

That’s exactly the “stacking constraints + execution” composition pattern you described, without mixing responsibilities. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

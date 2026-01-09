A brownfield skill set that composes well
1) brownfield-codebase-recon

When: First contact with an unfamiliar repo.
Goal: Produce a small “orientation packet” without making assumptions.
Outputs (small, repeatable):

- Repo “fact sheet” (language(s), frameworks, build, run, test, package manager)
- Entry points (executables, services, web apps, cron jobs)
- High-level module map (top 10 folders/modules + purpose guesses with confidence)
- “How to run locally” steps (as discovered, not invented)
- Open questions + where to look next

Why it’s a skill: This is the highest ROI repeatable workflow for brownfield.

2) brownfield-architecture-map

When: You need to explain “what this system is” to a human.
Goal: A stable architecture diagram in text: components, boundaries, dependencies, data flows.
Outputs:

- C4-ish Level 1/2 narrative (no drawings required): System → containers → major components
- Runtime topology (processes/services, ports, queues, databases)
- Key domain nouns and where they live in code
 -“Trust boundaries” and external integrations

Composes with: recon (uses its outputs; doesn’t repeat scanning).

3) brownfield-request-tracing

When: “Where does this API/UI action end up?”
Goal: Trace a single request/event end-to-end.
Outputs:

- Call chain (controller → service → repo → DB, etc.)
- Data shape evolution (DTOs/entities/messages)
- Side effects (writes, publishes, caches, external calls)
- Trace notes with file paths + symbols to jump to

This is the core brownfield superpower for feature work.

4) brownfield-change-impact-analysis

When: Before you implement a new feature/enhancement.
Goal: Identify blast radius + risk.
Outputs:

- “Impact set”: code areas likely touched + why
- Coupling hotspots (shared modules, static singletons, config, cross-cutting concerns)
- Backwards-compat constraints (schema, API contracts, messaging)
- Risk register + mitigation ideas

5) brownfield-safe-change-plan

When: You’re about to start coding.
Goal: Turn the impact analysis into a stepwise plan that’s safe to merge.
Outputs:

- Minimal sequence of commits/PRs (e.g., scaffolding → behavior → cleanup)
- Feature flags / toggles plan (if relevant)
- Rollback strategy
- Validation plan (what tests, what manual checks)

Composes with: request tracing + impact analysis.

6) brownfield-test-harness-setup

When: Tests are weak, slow, flaky, or missing.
Goal: Create a “testing foothold” to make change safe.
Outputs:

- Identify test pyramid state (unit/integration/e2e)
- Add a thin seam for dependency injection / fakes if needed
- Propose 3–5 high-value tests for the change area
- Guidance for local + CI run commands

7) brownfield-refactor-with-guardrails

When: Enhancements require cleanup but you can’t risk a big rewrite.
Goal: Refactor incrementally with measurable safety.
Outputs:

- Refactor target + rationale tied to upcoming feature
- Small refactor steps (each leaves code working)
- Characterization tests first (if behavior unclear)
- “Stop conditions” (don’t refactor beyond X)

8) brownfield-tech-debt-ledger

When: You keep discovering landmines.
Goal: Capture debt in a consistent format without derailing delivery.
Outputs:

- Debt items with: location, symptom, risk, suggested fix, effort, priority
- Link each item to a concrete observed friction (not vibes)
- “Debt paydown candidates” aligned to next likely enhancements

A recommended brownfield workflow (skill composition)

This flow keeps context tight and prevents re-reading the repo repeatedly:

1. brownfield-codebase-recon → build a thin shared mental model

2. brownfield-architecture-map (only if needed) → stable explanation artifact

3. brownfield-request-tracing for the specific feature path

4. brownfield-change-impact-analysis → blast radius + risks

5. brownfield-safe-change-plan → sequencing + validation

6. Optional safety boosters:
- brownfield-test-harness-setup
- brownfield-refactor-with-guardrails

7. Ongoing: brownfield-tech-debt-ledger

This matches your “progressive disclosure” principle and composability model. 

Two “meta” conventions to bake into every brownfield skill

These make the skills consistently useful across languages/frameworks:

- Evidence-first rule: any claim about behavior must be backed by where in code it was observed (file path + symbol + short quote/snippet if needed).
- Confidence tagging: label uncertain interpretations (confirmed / likely / guess) to prevent hallucinated certainty.
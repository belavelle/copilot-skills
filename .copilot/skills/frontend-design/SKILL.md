---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use when building or styling web components, pages, dashboards, landing pages, or apps (React, HTML/CSS, etc.). Avoid generic AI aesthetics; commit to a clear visual direction with strong typography, color, layout, and motion.
---

# Frontend Design

Build frontend UI that looks *intentionally designed* (not template-like).

## Design Commitment (Do First)

Before coding, decide internally:

- **Purpose**: what it does + who it’s for
- **Tone**: choose a strong aesthetic (minimal, editorial, brutalist, retro, luxury, playful, industrial, etc.)
- **Differentiation**: one memorable visual idea
- **Constraints**: framework, perf, accessibility

Then execute consistently.

## Implementation Requirements

- Deliver **working, production-grade code**
- Match complexity to the vision (minimal = precision; maximal = orchestration)
- Prefer a small number of high-impact moments over scattered effects

## Aesthetic Rules

### Typography
- Make typography a design feature
- Avoid default/generic fonts (Inter/Roboto/Arial/system)
- Pair a distinctive display font with a refined body font

### Color & Theme
- Use a cohesive, opinionated palette
- Use CSS variables/tokens
- Favor dominant colors + sharp accents (avoid timid, evenly-spread palettes)

### Layout & Composition
- Use intentional composition: asymmetry, overlap, grid breaks, negative space, or controlled density
- Avoid predictable “component library default” layouts

### Motion
- Use animation for hierarchy + delight (page-load reveals, hover states, scroll effects)
- Prefer CSS-first solutions; use a motion library when appropriate
- One well-orchestrated sequence beats many weak micro-interactions

### Depth & Atmosphere
Avoid flat defaults. Use backgrounds/details that fit the tone:
- gradient meshes, grain/noise, patterns
- layered transparency, borders, dramatic shadows

## Hard “Don’ts”
- No generic AI aesthetics (safe fonts, cliché palettes, cookie-cutter layouts)
- No purple-gradient-on-white-by-default look
- Don’t reuse the same “safe” design choices across unrelated UIs

## Output Expectations
- Provide complete runnable code (and setup notes if needed)
- Briefly explain key design decisions and the chosen aesthetic direction
- If requirements are missing, ask for the minimum inputs before coding

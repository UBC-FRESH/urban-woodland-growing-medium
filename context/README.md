# Context Tree

This directory is the persistent working memory for humans and coding agents
refining the specifications in this repository. Read it before editing any
specification source, and update it whenever a decision, assumption, or open
question changes.

The specification documents themselves live in `specification/` as Markdown.
Everything here is supporting knowledge: why the numbers are what they are,
where they came from, what is still unresolved, and what has been decided.

## Files

- `design-basis.md` — the agreed design basis and authored project defaults
  for the CWH urban woodland specification (layer profile, physical and
  chemical limits, soil allocations), including which figures are authored
  defaults rather than verified limits.
- `sources.md` — the technical sources behind the specification, with links,
  what each source was actually used for, and sources explicitly excluded.
- `open-items.md` — everything unresolved before tender issue: the project
  schedule fields, unverified supplied nutrient figures, and confirmations
  owed by the project team.
- `decisions.md` — the dated decision log. Append new entries; do not rewrite
  decided entries except to mark them superseded with a pointer to the newer
  decision.
- `bec-mapping.md` — research notes and the LMH77 page map behind the
  deployment-context (BEC analogue) framework.
- `plant-palette.md` — the draft target palette of CWH-native species, its
  per-species deployment-context fit, and what the palette implies for the
  growing medium.
- `palette-bec-crosswalk.md` — cross-reference of the palette against LMH77
  site-unit descriptions for the dry-end BEC13 units; reverse-engineers the
  analogue (CWHdm3 zonal core plus CDFmm xeric cohort) behind the deployment
  contexts.
- `default-validation.md` — first-pass validation of the adjusted per-context
  defaults against LMH77 soil descriptions, published texture/available-water
  ranges, and the CCISS tree-layer suitability dataset; records which targets
  are inside published ranges and which are stretch values needing laboratory
  confirmation.

## Conventions

- Keep these files factual and sourced. Distinguish authored project defaults
  from published limits, and supplied reference figures from enforceable
  criteria.
- When a specification edit changes a default, resolves an open item, or
  adopts a new source, update the matching file here in the same change.
- `reference/` at the repository root holds the untracked original ChatGPT
  export bundle (provenance only); never copy its contents into tracked files
  wholesale.

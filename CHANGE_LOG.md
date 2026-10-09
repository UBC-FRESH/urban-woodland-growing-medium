# Change Log

Newest entries last. Keep this file synchronized with roadmap phase/task
completion and GitHub issue comments.

## 2026-10-09

- Created the public repository `UBC-FRESH/urban-woodland-growing-medium` and
  seeded `main` with `LICENSE`, `.gitignore`, and a stub `README.md`.
- Imported the ChatGPT export bundle
  (`reference/CWH_Woodland_Complete_Export.zip`) as local-only provenance
  material; per public-repo hygiene policy the raw transcripts, QA renders,
  and nested archives stay untracked under `reference/`.
- Opened Phase 0 on `feature/p0-bootstrap-scaffold` with parent issue #1 and
  child issues #2 through #5 to establish governance, planning, package, docs,
  and CI scaffold.
- Completed P0.1 (#2): added `AGENTS.md`, `ROADMAP.md`, `CHANGE_LOG.md`,
  `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `planning/` notes recording
  the bootstrap rationale and the sanitized design basis with unresolved
  pre-tender items.
- Completed P0.2 (#3): ported the ChatGPT-export builder scripts into the
  `src/`-layout package `woodland_spec` with a thin `woodland-spec` CLI,
  tracked both specification DOCX deliverables under `specification/`, and
  added metadata, CLI, and build/content tests. Regenerated DOCX files are
  text-identical to the tracked deliverables.
- Completed P0.3 (#4): added the Sphinx documentation skeleton, the CI
  workflow (Ruff, pytest, warning-clean docs build, package build, and
  `twine check` on Python 3.11 and 3.12), and docs configuration tests.
- Completed P0.4 (#5): full local verification passed — `ruff check`,
  12 pytest tests, warning-clean `sphinx-build -W`, `python -m build`, and
  `twine check dist/*` — roadmap and changelog synchronized.
- Completed Phase 0 by merging PR #6 to `main` (merge commit `196c080`),
  verifying post-merge CI green on Python 3.11 and 3.12, and closing parent
  issue #1.
- Completed Phase 0.5 (maintainer-directed, recorded as roadmap phase 0.5):
  replaced the `woodland_spec` package and its hardcoded DOCX builders with a
  Markdown source of truth
  (`specification/cwh-urban-woodland-growing-medium.md`, one sentence per
  line), archived the original DOCX deliverables under
  `specification/archive/`, added the `context/` tree (design basis, sources,
  open items, decision log), added `scripts/export.py` (pandoc via
  pypandoc-binary) as the on-demand DOCX/HTML export path, and replaced the
  package tests with Markdown content guards and export pipeline checks.
  Local verification: `ruff check scripts tests`, `pytest` (10 tests), and
  `scripts/export.py` all pass; exported DOCX text matches the archived
  ten-page deliverable except that pandoc collapses the double spacing
  around the pipe in the section banner line.
- Completed Phase 0.6 (maintainer-directed): differentiated the specification
  into three BEC-anchored deployment contexts (UW-M sheltered mesic, UW-D
  slightly dry, UW-X very dry) in one parameterized document, with a
  deployment-context adjustment table covering depth, per-tree volume,
  organic matter, plant-available water, mulch, texture selection,
  irrigation and species checks. Contexts are anchored to BEC13
  subzone/variant climate analogues and CWHdm3 edatopic site series.
- Adopted Land Management Handbook 77 (2026, BEC13) as the master BEC
  reference; downloaded a local untracked copy to `reference/LMH77.pdf`
  (canonical source http://library.nrs.gov.bc.ca/digipub/LMH77.pdf), verified
  the CWHdm unit descriptions and the CWHdm3 edatopic grid, corrected the
  Vancouver-area variant name to CWHdm3 Eastern Variant, and anchored the
  deployment contexts to CWHdm3 site series 101/102/103.
- Added `context/bec-mapping.md` (research notes and LMH77 page map) and
  updated `context/` sources, design basis, open items and decision log.
- Recorded the user-supplied draft target palette of 19 CWH-native forest
  species in `context/plant-palette.md`, with per-species deployment-context
  fit, growing-medium implications (acid organic surface layer, mulch and
  nurse-wood analogues, no routine fertilization), and verification tasks
  (CCISS suitability, Berberis repens versus nervosa, coastal stock supply,
  professional review).
- Cross-referenced the palette against LMH77 site-unit descriptions for the
  five dry-end BEC13 units (`context/palette-bec-crosswalk.md`),
  reverse-engineering the assemblage to a CWHdm3 zonal-forest core
  (101/103/110) plus a CDFmm-flavoured xeric open-rock cohort; refined the
  UW-M site analogue in the specification to include site series 110 on
  richer mesic sites, and flagged kinnikinnick (CWHdm2/xs indicator) and
  Berberis repens as analogue mismatches for follow-up.

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

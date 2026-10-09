# Urban Woodland Growing Medium

Tender-ready growing medium specification for constructed urban woodland in
the Coastal Western Hemlock (CWH) biogeoclimatic zone of British Columbia.

The specification covers new trees plus woodland shrubs, ferns, and
herbaceous plants in an open soil bed constructed over compacted urban fill
or disturbed construction soil. It includes materials, laboratory acceptance
criteria, subgrade preparation, drainage, installation, quality assurance
hold points, and two-year establishment maintenance.

**Status: pre-tender draft.** The specification is not issued for
construction and is not professionally certified. Numerical limits are
authored project defaults for a fresh-to-moist, freely drained CWH woodland,
not official CWH-wide limits. See `context/design-basis.md` for the design
basis and `context/open-items.md` for unresolved pre-tender items.

Repository: https://github.com/UBC-FRESH/urban-woodland-growing-medium

## Deliverables

- `specification/cwh-urban-woodland-growing-medium.md` — the maintained
  source of truth: the ten-page specification with Table 1A covering the
  thirteen requested properties, formatted one sentence per line so every
  content change is a reviewable diff.
- `specification/archive/` — the two original ChatGPT-produced DOCX
  deliverables (original nine-page and updated ten-page versions), kept
  immutable for provenance.

Word and other distributable formats are generated on demand and are not
tracked in git.

## Export The Specification

Requires Python 3.11 or newer. pandoc is provided by the `pypandoc-binary`
package in the development environment:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python scripts/export.py                    # -> outputs/*.docx
python scripts/export.py --format html      # -> outputs/*.html
```

Visual layout review of the exported DOCX in Word or LibreOffice is a manual
pre-tender step. PDF export is deferred until a PDF engine is chosen; see
`context/decisions.md`.

## Repository Map

- `specification/` — Markdown specification sources and the DOCX archive.
- `context/` — persistent working memory: design basis, sources, open items,
  and the decision log. Read it before editing the specification.
- `planning/` — dated historical planning notes.
- `scripts/export.py` — the only supported export path.
- `tests/` — content guards and export pipeline checks.

## Roadmap

Near-term phases are tracked in `ROADMAP.md`:

- Phase 0: bootstrap governance, docs, and automation scaffold (complete).
- Phase 1: pre-tender completion (project schedule, numerical-default
  confirmation, environmental criteria).
- Phase 2: site-specific design review and tender issue.

Development follows the UBC-FRESH phase/task/subtask workflow:

- `ROADMAP.md` maps phases and tasks to GitHub issues.
- `CHANGE_LOG.md` records the dated project narrative.
- One active phase generally maps to one parent issue and feature branch.
- Roadmap tasks map to child issues linked from the parent issue body.

## Public-Repo Hygiene

Do not commit private project data, raw chat transcripts, unpublished source
documents, generated local outputs, or machine-specific paths. Keep scratch
material under ignored local paths such as `tmp/`, `local/`, `data/private/`,
`outputs/`, or `reference/`.

Use GitHub issues for public bug reports, documentation issues, and feature
requests. Do not attach private project material to public issues.

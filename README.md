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
not official CWH-wide limits. See `planning/design_basis.md` for the design
basis, authored defaults, and unresolved pre-tender items.

Repository: https://github.com/UBC-FRESH/urban-woodland-growing-medium

## Deliverables

Tracked under `specification/`:

- `CWH_Woodland_Growing_Medium_Specification_Updated.docx` — current working
  version, ten pages, with Table 1A covering the thirteen requested
  properties.
- `CWH_Woodland_Growing_Medium_Specification_Original.docx` — original
  nine-page version, retained for provenance.

The DOCX files are generated artifacts. The durable source of truth is the
Python package under `src/woodland_spec/`; regenerate the documents from
source after any content change instead of editing them in Word.

## Rebuild The Specification

Requires Python 3.11 or newer:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
woodland-spec build --output-dir outputs
```

`woodland-spec build` regenerates both DOCX versions. Page rendering and
visual layout review require Word or LibreOffice and are manual pre-tender
steps.

## Roadmap

Near-term phases are tracked in `ROADMAP.md`:

- Phase 0: bootstrap package, governance, docs, and automation scaffold.
- Phase 1: pre-tender completion (project schedule, numerical-default
  confirmation, environmental criteria).
- Phase 2: site-specific design review and tender issue.

Development follows the UBC-FRESH phase/task/subtask workflow:

- `ROADMAP.md` maps phases and tasks to GitHub issues.
- `CHANGE_LOG.md` records the dated project narrative.
- `planning/` stores design basis and focused notes.
- One active phase generally maps to one parent issue and feature branch.
- Roadmap tasks map to child issues linked from the parent issue body.

## Public-Repo Hygiene

Do not commit private project data, raw chat transcripts, unpublished source
documents, generated local outputs, or machine-specific paths. Keep scratch
material under ignored local paths such as `tmp/`, `local/`, `data/private/`,
`outputs/`, or `reference/`.

Use GitHub issues for public bug reports, documentation issues, and feature
requests. Do not attach private project material to public issues.

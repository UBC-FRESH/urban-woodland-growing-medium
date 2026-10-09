# Urban Woodland Growing Medium Roadmap

This roadmap is the current project plan and issue tracker map. Keep it
synchronized with GitHub issues, planning notes, pull requests, and
`CHANGE_LOG.md`.

## Issue Tracker Map

| Phase | Parent issue | Branch | Status |
| --- | --- | --- | --- |
| P0 Bootstrap scaffold | #1 | `feature/p0-bootstrap-scaffold` | Complete |
| P1 Pre-tender completion | TBD | `feature/p1-pre-tender-completion` | Planned |
| P2 Site-specific design review and tender issue | TBD | `feature/p2-design-review-tender-issue` | Planned |

## Phase 0: Bootstrap Scaffold

Parent issue: #1

Branch: `feature/p0-bootstrap-scaffold`

Status: complete

Goal: establish this repository as a public UBC-FRESH project with strict
governance, planning, docs, CI, and an importable Python package that
reproducibly builds the CWH woodland growing medium specification DOCX from
tracked source.

- [x] P0.1 Governance and planning scaffold (#2)
  - [x] Add `AGENTS.md` coding-agent contract.
  - [x] Add `ROADMAP.md` with issue tracker map.
  - [x] Add `CHANGE_LOG.md` seed entry.
  - [x] Add `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.
  - [x] Add `planning/phase0_bootstrap_rationale.md`.
  - [x] Add `planning/design_basis.md`.
- [x] P0.2 Specification builder package and CLI skeleton (#3)
  - [x] Add `pyproject.toml` with metadata, extras, and tool configuration.
  - [x] Port `build_spec.py` into `src/woodland_spec/build_spec.py`.
  - [x] Port `add_properties.py` into `src/woodland_spec/add_properties.py`.
  - [x] Add `src/woodland_spec/__init__.py` and `src/woodland_spec/cli.py`.
  - [x] Track both specification DOCX files under `specification/`.
  - [x] Add tests for metadata, CLI, and specification build/content.
  - [x] Regenerate the updated DOCX and confirm content equivalence.
- [x] P0.3 Docs and CI scaffold (#4)
  - [x] Add `docs/conf.py` and starter pages.
  - [x] Add `.github/workflows/ci.yml`.
  - [x] Add docs configuration import sanity test.
  - [x] Confirm warning-clean Sphinx build.
- [x] P0.4 Phase closeout and verification (#5)
  - [x] Run local acceptance commands.
  - [x] Update roadmap and changelog closeout notes.
  - [x] Comment on child issues and parent issue with verification results.
  - [x] Push branch and open PR to `main`.

Phase 0 local verification passed with:

- `python -m ruff check .`
- `python -m pytest` (12 tests)
- `sphinx-build -b html docs _build/html -W`
- `python -m build`
- `twine check dist/*`
- regenerated original and updated DOCX text-identical to the tracked
  deliverables under `specification/`

## Phase 1: Pre-Tender Completion (Planned)

Goal: complete the unresolved items identified in the design basis before the
specification can be issued for tender. Candidate tasks distilled from
`planning/design_basis.md`:

- Fill the project schedule: site and authority, plant palette and subzone,
  bed footprint and soil quantities, per-tree soil allocations.
- Record geotechnical, utility, and excavation constraints, groundwater
  conditions, designed drainage, and authorized outlet.
- Set environmental QP contaminant criteria and the sampling plan.
- Confirm numerical defaults with the project team and available
  laboratory/supplier capability.
- Resolve the source, extraction method, and total-versus-extractable basis of
  the supplied phosphorus (324 ppm) and potassium (1,956 ppm) reference
  figures, or keep them explicitly non-enforceable.
- Coordinate applicable municipal requirements.

## Phase 2: Site-Specific Design Review And Tender Issue (Planned)

Goal: complete the site-specific design review, obtain professional sign-off
as required by the authority having jurisdiction, and issue the specification
for tender.

- Full-depth trial bed and hold-point schedule confirmed for the site.
- Visual layout review of the regenerated DOCX in Word or LibreOffice.
- Independent review and professional certification as required.
- Tender issue record in `CHANGE_LOG.md`.

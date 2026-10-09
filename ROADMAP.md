# Urban Woodland Growing Medium Roadmap

This roadmap is the current project plan and issue tracker map. Keep it
synchronized with GitHub issues, planning notes, pull requests, and
`CHANGE_LOG.md`.

## Issue Tracker Map

| Phase | Parent issue | Branch | Status |
| --- | --- | --- | --- |
| P0 Bootstrap scaffold | #1 | `feature/p0-bootstrap-scaffold` | Active |
| P1 Pre-tender completion | TBD | `feature/p1-pre-tender-completion` | Planned |
| P2 Site-specific design review and tender issue | TBD | `feature/p2-design-review-tender-issue` | Planned |

## Phase 0: Bootstrap Scaffold

Parent issue: #1

Branch: `feature/p0-bootstrap-scaffold`

Goal: establish this repository as a public UBC-FRESH project with strict
governance, planning, docs, CI, and an importable Python package that
reproducibly builds the CWH woodland growing medium specification DOCX from
tracked source.

- [ ] P0.1 Governance and planning scaffold (#2)
  - [ ] Add `AGENTS.md` coding-agent contract.
  - [ ] Add `ROADMAP.md` with issue tracker map.
  - [ ] Add `CHANGE_LOG.md` seed entry.
  - [ ] Add `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.
  - [ ] Add `planning/phase0_bootstrap_rationale.md`.
  - [ ] Add `planning/design_basis.md`.
- [ ] P0.2 Specification builder package and CLI skeleton (#3)
  - [ ] Add `pyproject.toml` with metadata, extras, and tool configuration.
  - [ ] Port `build_spec.py` into `src/woodland_spec/build_spec.py`.
  - [ ] Port `add_properties.py` into `src/woodland_spec/add_properties.py`.
  - [ ] Add `src/woodland_spec/__init__.py` and `src/woodland_spec/cli.py`.
  - [ ] Track both specification DOCX files under `specification/`.
  - [ ] Add tests for metadata, CLI, and specification build/content.
  - [ ] Regenerate the updated DOCX and confirm content equivalence.
- [ ] P0.3 Docs and CI scaffold (#4)
  - [ ] Add `docs/conf.py` and starter pages.
  - [ ] Add `.github/workflows/ci.yml`.
  - [ ] Add docs configuration import sanity test.
  - [ ] Confirm warning-clean Sphinx build.
- [ ] P0.4 Phase closeout and verification (#5)
  - [ ] Run local acceptance commands.
  - [ ] Update roadmap and changelog closeout notes.
  - [ ] Comment on child issues and parent issue with verification results.
  - [ ] Push branch and open PR to `main`.

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

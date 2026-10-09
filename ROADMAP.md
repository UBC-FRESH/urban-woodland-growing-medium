# Urban Woodland Growing Medium Roadmap

This roadmap is the current project plan and issue tracker map. Keep it
synchronized with GitHub issues, planning notes, pull requests, and
`CHANGE_LOG.md`.

## Issue Tracker Map

| Phase | Parent issue | Branch | Status |
| --- | --- | --- | --- |
| P0 Bootstrap scaffold | #1 | `feature/p0-bootstrap-scaffold` | Complete |
| P0.5 Markdown source-of-truth restructure | none (maintainer-directed) | `main` | Complete |
| P0.6 Deployment-context differentiation | none (maintainer-directed) | `main` | Complete |
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

## Phase 0.5: Markdown Source-Of-Truth Restructure

Status: complete (2026-10-09, maintainer-directed, outside the issue workflow)

Goal: make the specification itself the tracked source of truth and shrink
the tooling to what the deliverable actually needs.

- Replaced the `woodland_spec` Python package (specification prose hardcoded
  in DOCX builder modules, one of them self-modifying source) with a single
  Markdown source: `specification/cwh-urban-woodland-growing-medium.md`, one
  sentence per line so sentences are the diffable unit.
- Moved the two original ChatGPT-produced DOCX deliverables to
  `specification/archive/` as immutable provenance; generated documents now
  land in the ignored `outputs/` directory via `scripts/export.py` (pandoc via
  pypandoc).
- Added the `context/` tree (design basis, sources, open items, decision log)
  as persistent agent and collaborator memory.
- Replaced package tooling with `requirements-dev.txt`, `pytest.ini`, and
  `ruff.toml`; replaced builder tests with Markdown content guards and export
  pipeline checks; simplified CI to lint, test, and an export smoke test.
- Removed `src/`, `docs/`, `pyproject.toml`, and `dist/`.
- Rationale and consequences recorded in `context/decisions.md`.

## Phase 0.6: Deployment-Context Differentiation

Status: complete (2026-10-09, maintainer-directed, outside the issue workflow)

Goal: differentiate the specification for the slightly to very dry urban
planting environments typical of Vancouver projects, anchored to defensible
BEC analogues.

- Added a Deployment contexts section defining UW-M sheltered mesic, UW-D
  slightly dry and UW-X very dry, each anchored to a BEC13 climate analogue
  (CWHdm3, CWHdm1, CWHxs; CDFmm as the CCISS future-climate analogue) and a
  CWHdm3 edatopic site-series analogue (101, 103, 102).
- Added the deployment-context adjustment table (authored defaults) covering
  depth, per-tree volume, organic matter, plant-available water, mulch,
  texture-selection guidance, irrigation and species checks, with Table 1
  override rules.
- Added a project-schedule row for context assignment and pre-issue review
  confirmations; extended Appendix A with biogeoclimatic analogue sources.
- Adopted LMH77 (BEC13) as the master BEC reference (local untracked copy at
  `reference/LMH77.pdf`) and recorded research in `context/bec-mapping.md`.
- Confirmation of the adjusted defaults with the project team is tracked in
  `context/open-items.md` and remains Phase 1 scope.

## Phase 1: Pre-Tender Completion (Planned)

Goal: complete the unresolved items identified in the design basis before the
specification can be issued for tender. Candidate tasks distilled from
`context/design-basis.md` and `context/open-items.md`:

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
- Produce a pandoc reference-doc (Word style template) so exported DOCX files
  carry the required headers, footers, and page numbering ahead of the manual
  layout review.

## Phase 2: Site-Specific Design Review And Tender Issue (Planned)

Goal: complete the site-specific design review, obtain professional sign-off
as required by the authority having jurisdiction, and issue the specification
for tender.

- Full-depth trial bed and hold-point schedule confirmed for the site.
- Visual layout review of the regenerated DOCX in Word or LibreOffice.
- Independent review and professional certification as required.
- Tender issue record in `CHANGE_LOG.md`.

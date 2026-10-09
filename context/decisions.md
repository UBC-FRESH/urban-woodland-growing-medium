# Decision Log

Dated, append-only record of project decisions. Mark superseded entries rather
than deleting them.

## 2026-10-08 — Exclude the Vancouver GRI planting guidelines

The City of Vancouver GRI planting guidelines PDF was excluded as a source by
explicit user preference from an earlier plant project. The specification
states this exclusion in Appendix A; do not reintroduce the document as a
source. Recorded here from the original ChatGPT conversation.

## 2026-10-09 — Markdown is the source of truth; DOCX is an on-demand export

The specification source of truth is
`specification/cwh-urban-woodland-growing-medium.md`, formatted one sentence
per line so sentences are the diffable unit in git. Word (and later other
formats) are generated on demand by `scripts/export.py` (pandoc via
pypandoc) and are not tracked; generated outputs land in the ignored
`outputs/` directory.

This replaces the Phase 0 structure, in which two Python builder modules
(`src/woodland_spec/`, with all specification prose hardcoded as string
literals, one of them self-modifying source carried over from the original
ChatGPT session) generated the DOCX. That structure made prose diffs hard to
review, fought the linter, and added packaging ceremony with no
parameterization benefit.

Consequences:

- The two original ChatGPT-produced DOCX deliverables are no longer
  reproducible from source; they are kept immutable under
  `specification/archive/` for provenance.
- Heading mapping for export: the source's single level-1 heading becomes the
  Word Title style (`pandoc --shift-heading-level-by=-1`); level-2 and level-3
  headings become Word Heading 1 and Heading 2, matching the archived layout.
- Word headers/footers/page numbering from the archived DOCX are not yet
  reproduced; layout polish (via a pandoc reference-doc) is a pre-tender
  layout task, reviewed manually in Word or LibreOffice.
- Exported text is identical to the archived deliverable except that pandoc
  collapses the double spacing around the pipe in the "Section 32 91 13"
  banner line; accepted as cosmetic.

## 2026-10-09 — Tooling: pypandoc-binary in the venv; PDF deferred

pandoc is provided by the `pypandoc-binary` pip package in the repository
virtual environment (see `requirements-dev.txt`), keeping tooling inside the
working directory. PDF export is deferred: pandoc requires a separate PDF
engine (LaTeX or HTML-to-PDF), none is installed, and DOCX is the tender
deliverable. Revisit when a PDF is actually requested.

## 2026-10-09 — Deployment-context differentiation, BEC-anchored

The specification differentiates into three deployment contexts in one
parameterized document (not per-context files): UW-M sheltered mesic, UW-D
slightly dry, UW-X very dry. Each context is anchored to a BEC13 climate
analogue (subzone/variant) and an edatopic site analogue (SMR position and
CWHdm3 site series), with CCISS future-analogue commentary kept informative
only. Adjusted per context: rootable depth, per-tree volume, Layer A organic
matter, plant-available water, mulch depth, texture-selection guidance,
irrigation, and species-compatibility checks. All adjusted values remain
authored project defaults pending project-team confirmation; the Table 1
acceptance skeleton, laboratory protocols, hold points, and environmental
controls stay shared.

Alternatives rejected: per-context specification files (shared clauses would
drift) and two dry-only classes (leaves no specified option for sheltered or
irrigated beds).

## 2026-10-09 — Adjusted defaults retained after first-pass validation, with two stretch flags

The adjusted per-context defaults were validated against LMH77 soil
descriptions, published texture/available-water ranges, and the CCISS
tree-layer dataset (`context/default-validation.md`). Outcome: framework and
anchors validated; plant-available-water targets retained, with UW-X Layer A
≥16% and Layer B ≥12% explicitly flagged as stretch values to be confirmed by
laboratory test or relaxed to demonstrated blend values before tender. Shore
pine's CCISS E3 rating on CWHdm3 102/103 is accepted as "expected low vigor
on harsh analogue sites", mitigated by the constructed profile being far
deeper than the natural 102 soil (<20 cm). The CCISS check covers the tree
layer only; understorey verification remains the LMH77 cross-reference.

## 2026-10-09 — UW-M site analogue refined after palette cross-reference

Cross-referencing the 19-species palette against LMH77 site-unit descriptions
(`context/palette-bec-crosswalk.md`) reverse-engineered the assemblage to a
CWHdm3 zonal-forest core (site series 101/103/110) plus a CDFmm-flavoured
xeric open-rock cohort, retaining the three-context structure. The UW-M site
analogue in the specification was refined from "101" to "101, and 110 on
richer mesic sites" so the moist-herb cohort (vanilla leaf, sword fern
habitat) has an on-analogue home. Palette-level corrections (kinnikinnick
versus hairy manzanita, Berberis repens versus nervosa) are recorded in
`context/plant-palette.md` and tracked in `open-items.md`.

## 2026-10-09 — Draft target plant palette recorded

A user-supplied palette of 19 CWH-native forest species is adopted as the
working target palette and recorded with per-species context fit in
`context/plant-palette.md`. The palette stays in the context tree, not in the
specification: the specification remains a tender template whose project
schedule and Species compatibility rows reference palettes, while the
concrete palette is project input. Verification tasks (CCISS suitability,
Berberis repens versus nervosa, coastal stock supply, professional review)
are tracked in `open-items.md`.

## 2026-10-09 — LMH77 adopted as master BEC reference

Land Management Handbook 77 (2026, BEC13) is the master biogeoclimatic
reference for this project. A local untracked copy is kept at
`reference/LMH77.pdf` (722 pages, Part 1 of 2); the canonical source is
http://library.nrs.gov.bc.ca/digipub/LMH77.pdf. Two corrections it settled,
recorded in `context/bec-mapping.md`: the Vancouver-area unit is CWHdm3
**Eastern** Variant (not "lower mainland variant"), and the dry-end unit
names follow the BEC13 reclassification (CWHdm1/dm2/dm3 replacing CWHxm1/xm2
and the old lower-mainland CWHdm). The deployment-context site analogues use
the CWHdm3 site series from its edatopic grid (printed page 246).

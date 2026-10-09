# Phase 0 Bootstrap Rationale

## Why this repository exists

The CWH woodland growing medium specification was drafted in a ChatGPT
environment in October 2026. That environment produced two Word deliverables
(original and updated), the Python scripts that generate them, and a complete
export bundle with conversation transcript, QA renders, and handoff notes.

A chat workspace is not durable infrastructure: it has no version control, no
issue tracking, no review workflow, and no portability between environments
or collaborators. This repository moves the project onto the standard
UBC-FRESH footing so the specification can be revised, reviewed, verified,
and eventually issued for tender with a auditable history.

## What was imported

Tracked in git:

- The portable builder scripts `build_spec.py` and `add_properties.py`,
  refactored into the `woodland_spec` package with unchanged content.
- The two generated deliverables under `specification/`:
  `CWH_Woodland_Growing_Medium_Specification_Original.docx` (nine pages) and
  `CWH_Woodland_Growing_Medium_Specification_Updated.docx` (ten pages, adds
  Table 1A with the 13 requested properties).

Retained locally but untracked (per public-repo hygiene policy):

- The full export bundle `reference/CWH_Woodland_Complete_Export.zip`,
  including the conversation transcript, message JSON, QA page renders,
  nested document bundle, and original scripts with sandbox-specific paths.

## Why the builders are the source of truth

The specification DOCX files are generated artifacts. Keeping the Python
builders as the tracked source means every content change is a reviewable
diff, the document can be regenerated in any environment with only Python and
`python-docx`, and content tests can guard against accidental drift. The
tracked DOCX files exist so reviewers can read the document without running
anything; they must be regenerated from source after content changes, never
edited directly in Word.

## Design decisions

- `src/` layout package `woodland_spec` with a thin `woodland-spec` CLI,
  matching the UBC-FRESH workflow contract (thin CLI over importable APIs).
- Ruff line-length concessions (per-file `E501` ignores) are limited to the
  two builder modules, whose long string literals are specification prose.
- No release, Pages site, or PyPI publication in Phase 0; the repository is a
  working project specification, not a published package.
- The Vancouver GRI planting guidelines PDF was excluded as a source by
  explicit user preference recorded in the original conversation; see
  `planning/design_basis.md`.

## Provenance

- Original conversation: ChatGPT project chat, 8–10 October 2026, exported as
  `CWH_Woodland_Complete_Export.zip` (retained untracked under `reference/`).
- The original DOCX was recreated in the chat environment from its retained
  generation source after direct retrieval failed; the updated DOCX is the
  retained latest deliverable. Both are tracked here unchanged.
- Repository bootstrap: 9 October 2026, Phase 0 issues #1–#5.

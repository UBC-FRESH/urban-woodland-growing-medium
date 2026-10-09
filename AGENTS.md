# AGENTS.md

This file is the working contract for AI coding agents in this repository.

## Project Purpose

`urban-woodland-growing-medium` develops and maintains a tender-ready growing
medium specification for constructed urban woodland — new trees plus woodland
understory in an open soil bed over compacted fill or disturbed construction
soil — within the Coastal Western Hemlock (CWH) biogeoclimatic zone of British
Columbia. The repository is structured to grow into a family of similarly
authored, defensible specifications for other special cases and deployment
contexts.

The specification is a project draft. It is not issued for construction and is
not professionally certified. Numerical limits are authored project defaults
for a fresh-to-moist, freely drained CWH woodland, not official CWH-wide
limits, until the project team confirms them for a specific site.

## Source Of Truth Model

- The durable source of truth is Markdown: one file per specification under
  `specification/`, formatted **one sentence per line** so sentences are the
  diffable unit in git. Tables are pandoc pipe tables, one row per line.
- Word (and later other formats) are **generated artifacts**, produced on
  demand by `scripts/export.py` (pandoc via pypandoc) into the ignored
  `outputs/` directory. Never edit a generated document; edit the Markdown
  and re-export.
- `specification/archive/` holds the two original ChatGPT-produced DOCX
  deliverables. They are immutable provenance, not current deliverables, and
  are no longer reproducible from source — do not modify, regenerate, or
  delete them.
- Export heading mapping: the single level-1 heading becomes the Word Title
  style; level-2/3 headings become Word Heading 1/2, matching the archived
  layout. Keep exactly one `#` heading per specification file.

## Current Repo State

- `README.md`: concise public overview and current status.
- `ROADMAP.md`: phase/task roadmap and issue tracker map.
- `CHANGE_LOG.md`: append-only project narrative.
- `AGENTS.md`: this working contract.
- `specification/`: Markdown specification sources plus the DOCX `archive/`.
- `context/`: persistent agent memory — design basis, sources, open items,
  and the decision log. Read it before editing a specification; update it in
  the same change when defaults, sources, or open items move.
- `planning/`: dated historical planning notes (Phase 0 bootstrap rationale).
- `scripts/export.py`: thin pandoc wrapper; the only supported export path.
- `tests/`: content guards for the Markdown source and export pipeline checks.
- `requirements-dev.txt`, `pytest.ini`, `ruff.toml`: tooling configuration.
  There is no installable Python package.
- `.github/workflows/`: CI checks.
- `reference/`: ignored local area holding the original ChatGPT export bundle
  (transcripts, QA renders, nested archives). Not tracked.
- `tmp/`: ignored local working area.

## Public-Repo Hygiene

- Keep `tmp/`, `local/`, `data/private/`, `outputs/`, and `reference/`
  ignored.
- Do not commit private project data, raw chat transcripts, QA image dumps,
  credentials, machine-specific paths, or unpublished source documents.
- Keep provenance explicit: record where specification content, numerical
  defaults, and external references came from in `context/design-basis.md`,
  `context/sources.md`, and the specification appendices.
- Do not state or imply that the specification is issued for tender,
  issued for construction, or professionally certified until the roadmap
  records that milestone.

## Working Principles

- Read `AGENTS.md`, `ROADMAP.md`, `CHANGE_LOG.md`, and `context/` before
  making project-shaping changes.
- Edit specification content in the Markdown source. Keep one sentence per
  line; do not hard-wrap sentences, and do not reflow table rows.
- Preserve uncertainty. Distinguish authored project defaults from verified
  acceptance limits, and supplied reference figures from enforceable criteria.
- Keep `context/` synchronized with specification edits: design-basis changes
  update `design-basis.md`, new or dropped citations update `sources.md`,
  resolved items move out of `open-items.md`, and significant choices get a
  dated `decisions.md` entry.
- Keep changes scoped to the active roadmap phase and issue.

## Planning Workflow

This repo follows the UBC-FRESH phase/task/subtask workflow:

- `ROADMAP.md` is the current plan and issue tracker map.
- One roadmap phase maps to one GitHub parent issue and one feature branch.
- One roadmap task maps to one child issue linked from the parent issue body.
- Subtasks usually stay as checklist items inside the child issue body.
- Use at most three issue levels: phase, task, implementation subtask.
- Record issue numbers beside roadmap phases and tasks once created.
- Keep `ROADMAP.md`, `CHANGE_LOG.md`, planning notes, issue bodies, and PR
  descriptions synchronized.
- Open a PR from the phase branch to `main` only after phase tasks, tests,
  docs, and closeout notes are complete or explicitly deferred.

## Strict Development Workflow

Use this workflow for active development from the first phase boundary onward:

- One active roadmap phase should generally correspond to one GitHub parent
  issue and one feature branch.
- Create or activate the GitHub parent issue before starting a roadmap phase.
- Create the feature branch from current `main` for that parent issue.
- Create child issues for roadmap tasks under the parent issue.
- Document task subtasks as checklist steps inside the child issue body unless
  they are large enough to deserve third-level implementation issues.
- Work child issues one at a time where practical, usually in roadmap order.
- Before closing a child issue, update every issue-body checklist item to
  checked, or rewrite the issue body to make explicitly clear which items were
  superseded or are not applicable.
- Close each child issue only after its repo changes, documentation,
  issue-body checklist, and verification for that task are complete.
- Keep `ROADMAP.md`, `CHANGE_LOG.md`, and issue comments synchronized as task
  state changes.
- Open a PR from the phase branch back to `main` when the parent issue's
  child issues are complete or explicitly deferred.
- Close the parent issue only after the PR has merged back to `main`.
- Do not start a new active parent issue and branch until the current parent
  issue is closed, unless the maintainer explicitly approves a parallel lane.

## GitHub Issue And Comment Formatting

Formatting matters. GitHub issue bodies and comments must be readable as
rendered Markdown, not flattened prose.

Rules:

- Use short section labels on their own lines, such as `Roadmap task: P1.1`,
  `Parent phase issue: #6`, `Status: active`, and `Checklist:`.
- Use real GitHub task-list syntax, with one checklist item per line.
- Never write inline pseudo-checklists such as
  `Checklist: [ ] first. [ ] second.`
- Wrap branch names, file paths, commands, and commit hashes in backticks.
- For parent phase issues, list child issues as task-list bullets with issue
  numbers and task IDs.
- Before creating or editing several issues, prepare bodies as multi-line
  Markdown strings or temporary body files.

## GitHub Issue Body Quality Standard

Issue bodies are part of the project specification and onboarding material.
Write them so a new lab student, external collaborator, or coding agent can
understand the task, implement it, verify it, and close it without reading the
original chat transcript.

Parent phase issues must include phase identifier, status, branch name,
roadmap links, goal, scope, out-of-scope boundaries, architecture notes, child
task checklist, acceptance criteria, verification, and closeout requirements.

Child task issues must include task identifier, parent phase issue, status,
related planning links, goal, scope, out-of-scope boundaries, subtasks,
acceptance criteria, verification commands, artifacts, risks, and completion
metadata once closed.

Do not create placeholder issue bodies with only a title and a short checklist
unless the maintainer explicitly asks for a placeholder.

## Verification

Default local checks:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m ruff check scripts tests
python -m pytest
python scripts/export.py --output-dir outputs
```

Default CI must not require private project data, commercial office software,
credentials, or network downloads beyond package installation. Word or
LibreOffice layout rendering checks are manual pre-tender steps and are not
part of CI.

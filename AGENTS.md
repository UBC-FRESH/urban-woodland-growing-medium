# AGENTS.md

This file is the working contract for AI coding agents in this repository.

## Project Purpose

`urban-woodland-growing-medium` develops and maintains a tender-ready growing
medium specification for constructed urban woodland — new trees plus woodland
understory in an open soil bed over compacted fill or disturbed construction
soil — within the Coastal Western Hemlock (CWH) biogeoclimatic zone of British
Columbia.

The durable source of truth is the tracked Python source that builds the
specification DOCX, plus the governance and planning records in this
repository. The tracked DOCX deliverables under `specification/` are generated
artifacts kept under version control so reviewers can read them without
running the builders; regenerate them from source rather than editing them in
an office application.

The specification is a project draft. It is not issued for construction and is
not professionally certified. Numerical limits are authored project defaults
for a fresh-to-moist, freely drained CWH woodland, not official CWH-wide
limits, until the project team confirms them for a specific site.

## Current Repo State

- `README.md`: concise public overview and current status.
- `ROADMAP.md`: phase/task roadmap and issue tracker map.
- `CHANGE_LOG.md`: append-only project narrative.
- `AGENTS.md`: this working contract.
- `planning/`: design basis, bootstrap rationale, and focused notes.
- `pyproject.toml`: package metadata and optional dependency groups.
- `src/woodland_spec/`: importable package that builds the specification DOCX
  files, plus a thin `woodland-spec` CLI.
- `specification/`: tracked generated DOCX deliverables (original and updated
  versions).
- `tests/`: package metadata, CLI, docs, and specification build/content
  tests.
- `docs/`: Sphinx documentation skeleton.
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
  defaults, and external references came from in `planning/design_basis.md`
  and the specification appendices.
- Do not state or imply that the specification is issued for tender,
  issued for construction, or professionally certified until the roadmap
  records that milestone.

## Working Principles

- Read `AGENTS.md`, `ROADMAP.md`, and `CHANGE_LOG.md` before making
  project-shaping changes.
- Keep CLI commands thin wrappers over Python APIs.
- Edit specification content in the Python builders, not in the DOCX files;
  regenerate and re-run content tests.
- Preserve uncertainty. Distinguish authored project defaults from verified
  acceptance limits, and supplied reference figures from enforceable criteria.
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
python -m ruff check .
python -m pytest
sphinx-build -b html docs _build/html -W
python -m build
twine check dist/*
```

Default CI must not require private project data, commercial office software,
credentials, or network downloads beyond package installation. Word or
LibreOffice layout rendering checks are manual pre-tender steps and are not
part of CI.

Development Workflow
====================

This repository follows the UBC-FRESH phase/task/subtask workflow. See
``AGENTS.md`` for the full working contract and ``ROADMAP.md`` for the
current plan and issue tracker map.

- One active roadmap phase maps to one GitHub parent issue and one feature
  branch.
- Roadmap tasks map to child issues linked from the parent issue body.
- Subtasks usually stay as checklist items inside the child issue body.
- Keep ``ROADMAP.md``, ``CHANGE_LOG.md``, planning notes, issue bodies, and
  PR descriptions synchronized.

Local checks:

.. code-block:: bash

   python -m ruff check .
   python -m pytest
   sphinx-build -b html docs _build/html -W
   python -m build
   twine check dist/*

CI runs the same checks on Python 3.11 and 3.12 and must not require private
project data, commercial office software, credentials, or network downloads
beyond package installation.

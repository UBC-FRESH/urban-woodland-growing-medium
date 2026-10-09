Specification Deliverables
==========================

Tracked generated DOCX files live under ``specification/``:

- ``CWH_Woodland_Growing_Medium_Specification_Updated.docx`` — current working
  version, ten pages, with Table 1A covering the thirteen requested
  properties (C:N, %OM, %sand, %silt, %clay, total silt and clay, pH, maximum
  particle size, N, P, K, saturated-extract EC, and SAR).
- ``CWH_Woodland_Growing_Medium_Specification_Original.docx`` — original
  nine-page version, retained for provenance.

The DOCX files are generated artifacts. The durable source of truth is the
``woodland_spec`` Python package; edit the builders, then regenerate:

.. code-block:: bash

   woodland-spec build --output-dir outputs

Regenerated files are compared block-for-block against the tracked
deliverables in ``tests/test_spec_build.py``, so content drift fails CI.

Visual layout review in Word or LibreOffice is a manual pre-tender step and
is not part of CI.

# Design Basis

Distilled from the ChatGPT export handoff (`handoff/CONTINUE_HERE.md` in the
untracked export bundle under `reference/`). This note is the sanitized public
record of the agreed design basis and authored project defaults for the CWH
urban woodland growing medium specification.

## Project intent

A detailed tender specification for new trees and woodland understory in a
constructed urban bed over compacted fill or disturbed construction soil,
within the Coastal Western Hemlock (CWH) biogeoclimatic zone.

## Agreed design basis and draft defaults

- Fresh-to-moist, freely drained woodland (not a wetland).
- 300 mm upper organic Layer A over 600 mm mineral Layer B.
- Generally 75 mm settled wood-chip mulch.
- Upper layer organic matter 5–8% dry mass; lower layer 1–3%.
- pH 5.0–6.5; saturated-paste EC ≤ 2 dS/m; SAR ≤ 4.
- Mineral texture: sand 50–70%, silt 15–35%, clay 10–20%, summing to 100% of
  the fine mineral fraction; total silt plus clay 30–50% on that same basis.
- Table 1A distinguishes total-medium dry-mass percentages using the measured
  fine mineral fraction F.
- 30 m³ net usable soil allocation per large tree.
- Soil and mulch depths, the 30 m³ allocation, and physical limits and
  frequencies are authored project defaults, not official CWH-wide limits.

The specification also includes laboratory protocols, independent lot
sampling, subgrade preparation, drainage, a full-depth trial bed, five hold
points, field verification, corrections, two-year maintenance, and
measurement/payment rules. Subgrade and drainage must be accepted before
imported soil covers them.

## Deployment contexts (added 2026-10-09)

The specification is differentiated into three deployment contexts, anchored
to BEC13 climate analogues (subzone/variant) and edatopic site analogues
(CWHdm3 site series from LMH77); see `context/bec-mapping.md` and
`decisions.md`:

- **UW-M sheltered mesic** — zonal CWHdm3 climate, site series 101
  (FdcHw–Red huckleberry–Salal); corresponds to the original base profile
  above.
- **UW-D slightly dry** — drier end of CWHdm3, subxeric–submesic; site series
  103 (FdcHw–Salal–Step moss).
- **UW-X very dry** — CWHdm1 or CWHxs climate analogue, subxeric–xeric; site
  series 102/103; CCISS future analogue for the Vancouver area trends toward
  CDFmm.

Adjusted defaults per context (rootable depth, per-tree volume, Layer A
organic matter, plant-available water, mulch depth, texture-selection
guidance, irrigation, species checks) live in the specification's
deployment-context adjustment table. They are authored project defaults, not
verified limits, pending the confirmations listed in `open-items.md`.

The draft target palette of 19 CWH-native species is recorded in
`context/plant-palette.md` with per-species context fit and growing-medium
implications; it spans all three deployment contexts.

## Status

The draft is not issued-for-construction and not professionally certified.
Numerical limits are authored project defaults for a fresh-to-moist, freely
drained CWH woodland, not official CWH-wide limits, until the project team
confirms them for a specific site. Open pre-tender items are tracked in
`context/open-items.md`; the sources behind the defaults are listed in
`context/sources.md`.

## Current deliverable

`specification/cwh-urban-woodland-growing-medium.md` — the maintained source
of truth, covering the ten-page specification with Table 1A on the requested
thirteen properties. Export it to DOCX with `scripts/export.py`. The two
original ChatGPT-produced DOCX files are kept immutable under
`specification/archive/` for provenance.

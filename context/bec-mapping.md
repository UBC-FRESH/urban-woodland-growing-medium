# BEC Mapping Research — Urban Deployment Contexts

Research notes on differentiating the growing medium specification using
Biogeoclimatic Ecosystem Classification (BEC) subzone/variant analogues for
Vancouver urban planting environments, with emphasis on slightly to very dry
deployment contexts. Captured 2026-10-09; the adopted framework is recorded
in `decisions.md` and implemented in the specification's Deployment contexts
section.

## Master reference

Land Management Handbook 77 — *A Field Guide to Ecosystem Classification and
Identification for Coastal British Columbia (excluding Haida Gwaii)*, 2026
(BEC13). Local untracked copy: `reference/LMH77.pdf` (722 pages, Part 1 of
2). Canonical source: http://library.nrs.gov.bc.ca/digipub/LMH77.pdf

Useful locations (printed page ≈ PDF page − 16):

- CWH zone overview and dry maritime subzone: printed 97 (PDF 113).
- CWHdm1 Central Variant unit section: printed 98–100 (PDF 114–116).
- CWHdm2 Western Variant unit section: printed 101–103 (PDF 117–119).
- CWHdm3 Eastern Variant unit section: printed 104–106 (PDF 120–122).
- CWHxs Very Dry Submaritime subzone: printed 171 (PDF ~187).
- CWHdm3 site units with edatopic grid: printed 246 (PDF 262).
- CDFmm site units: printed 200; CWHdm1: printed 216; CWHdm2: printed 230.

## Why BEC applies to urban fill sites at all

An urban bed on compacted fill has no natural BEC classification; BEC
describes zonal climate and the ecosystems it supports. The defensible use is
as an **analogue framework** on two axes:

1. **Climate analogue** — a BGC subzone/variant whose moisture and
   temperature regime resembles the urban exposure (hot, open, shallow,
   wind-exposed beds behave like drier climatic units than the surrounding
   zonal forest) and/or resembles the site's projected future climate.
2. **Edaphic analogue** — a position on the BEC **edatopic grid**: relative
   soil moisture regime (SMR; very xeric through subhydric) crossed with soil
   nutrient regime (SNR; very poor through very rich). Site series are defined
   per subzone/variant as groups of edatopes, so "which site series would
   this bed behave like" is the precise form of the question.

Source: CCISS Definitions (bcgov-ffec.ca/cciss-docs/Definitions.html),
sections 7.1 (edatopic grid, site series) and 7.3 (BEC codes); LMH77.

## BEC13 reclassification that matters here

LMH77 (BEC13) reclassified the dry end of the CWH zone — the names in older
sources are out of date:

| BEC13 (current) | BEC12 (old) | Notes |
| --- | --- | --- |
| CWHdm1 Central | CWHxm1 Eastern Very Dry Maritime | Driest of the three dry-maritime units; rainshadow of the Vancouver Island Ranges (LMH77 p. 99) |
| CWHdm2 Western | CWHxm2 Western Very Dry Maritime | Dry maritime, western Vancouver Island |
| CWHdm3 Eastern | CWHdm (lower mainland portion) | **Includes Vancouver**; the local zonal unit |
| CWHxs Very Dry Submaritime | (new; portions of old IDFww) | South coast interior transition; hotter, more continental |
| CDFmm | CDFmm | Coastal Douglas-fir; driest coastal forest climate of the region (SE Vancouver Island / Gulf Islands) |

Source: CCISS Definitions section 7.5 (LMH77 updates and crosswalk tables);
LMH77 Chapter 5.

## LMH77 on CWHdm3 (the Vancouver-area unit)

From the unit description (LMH77 printed 105, PDF 121):

- Climate: rainshadow of the Vancouver Island Ranges; warm, dry summers and
  mild, relatively wet winters with little snow; long growing seasons; and —
  the hook for the dry deployment contexts — **"water deficits occur on
  submesic and drier sites, as the Pacific High dominates the summer climate
  pattern."**
- Vegetation: forests generally co-dominated by Douglas-fir and western
  hemlock with a western redcedar component; shore pine common on dry sites;
  salal, dull Oregon-grape, vine maple and red huckleberry dominant in the
  shrub layer.
- Soils: upland Humo-Ferric Podzols with Dystric Brunisols on dry sites;
  predominant humus forms Mors, with Moders on richer sites.

From the CWHdm3 edatopic grid (LMH77 printed 246, PDF 262), with SMR common
terms from the same page:

| Site series | Name | Edatope position | Common moisture term |
| --- | --- | --- | --- |
| 101 | FdcHw–Red huckleberry–Salal | mesic, medium (zonal) | fresh |
| 102 | PlcFdc–Rock mosses–Clad lichens | very xeric–xeric, very poor | very dry |
| 103 | FdcHw–Salal–Step moss | subxeric–submesic, poor | slightly to moderately dry |
| 104 | FdcCw–Vine maple–Sword fern | submesic–mesic, richer | fresh |
| 110–113 | various FdcHwCw / CwFdc / HwCw / SsCw | subhygric–hygric | moist to very moist |

(Floodplain and wetland units — Fm53, Fl51, Fl52, Ws56, Ws58 — are out of
scope for the freely drained woodland concept.)

Mapping adopted in the specification: UW-M ≈ site series 101; UW-D ≈ 103;
UW-X ≈ 102/103 under a drier CWHdm1 or CWHxs climate analogue. The spec's
older "fresh-to-moist" phrasing corresponds to the mesic–subhygric SMR range.

## Tools and data sources

- LMH77 local copy: `reference/LMH77.pdf` (see Master reference above).
- CCISS documentation (definitions, methods): https://bcgov-ffec.ca/cciss-docs/
- Interactive BGC unit map (user-supplied): https://thebeczone.ca/shiny/bybecmap/
  — useful for confirming which unit a project site falls in; JavaScript app,
  not script-scrapable; treat as a manual lookup tool.
- CCISS tool itself: climate-analogue projections of subzone/variant
  suitability — the hook for "design for the site's future climate analogue",
  which for Vancouver points at drier units (toward CDFmm conditions).
- BC Data Catalogue hosts the CCISS environmental suitability dataset.

## Design implications adopted

- Three deployment contexts (UW-M sheltered mesic, UW-D slightly dry, UW-X
  very dry) in one parameterized specification, anchored to subzone/variant
  plus edatope position, with a CCISS future-analogue note. See
  `decisions.md` (2026-10-09 entries) and the specification's Deployment
  contexts section.
- Adjusted parameters per context: rootable depth, per-tree soil volume,
  Layer A organic matter, plant-available water, mulch depth, texture
  selection guidance, irrigation, species compatibility checks.
- Shared skeleton unchanged: pH, EC, SAR, texture acceptance window,
  laboratory protocols, hold points, environmental controls.

## Remaining verification tasks (tracked in open-items.md)

- Pull per-unit climate statistics (mean annual precipitation/temperature
  ranges, growing-season deficit) from LMH77 Chapter 5 tables for CWHdm3,
  CWHdm1, CWHdm2 and CWHxs if numeric climate anchors are ever needed beyond
  the qualitative unit descriptions.
- Confirm the CWHdm1 and CWHxs site-series lists (LMH77 printed 216 and 497)
  if the UW-X analogue needs site-series precision under those climates.

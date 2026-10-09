# Validation of the Deployment-Context Adjusted Defaults

First-pass validation of the adjusted per-context defaults against checkable
sources, 2026-10-09. Verdict per target: **inside published range**,
**plausible via design lever** (organic matter gradient), or **stretch —
needs laboratory confirmation**. All adjusted values remain authored project
defaults; this note bounds them, it does not certify them.

## 1. Soil and humus anchors from LMH77

What the analogue site series actually grow in (CWHdm3 site-unit
descriptions, LMH77 printed 246–251, PDF 262–267):

| Site series | Natural soil profile | Humus form |
| --- | --- | --- |
| 102 PlcFdc–Rock mosses–Clad lichens | very shallow, generally <20 cm, over bedrock; medium to coarse textured; moderate to high coarse fragments | thin to moderately thick Mor |
| 103 FdcHw–Salal–Step moss | coarse-textured glaciofluvial, shallow colluvium or shallow morainal materials | mostly moderately thick Mors |
| 101 FdcHw–Red huckleberry–Salal | deep, well-drained, mostly morainal; Orthic Humo-Ferric Podzol | moderately thick Mors or Mormoders |
| 110 FdcHwCw–Sword fern | circum-mesic nutrient-rich; Humo-Ferric to Ferro-Humic Podzols | moderately thick Moders |

Two design implications:

- The constructed UW-X profile (600–900 mm) is far deeper than the natural
  102 soil (<20 cm). The natural analogue proves the species tolerate
  extreme drought; the constructed profile provides buffering the analogue
  never had. This is the core viability argument for UW-X, not a mismatch.
- The spec's "moderately organic surface layer over a lower-organic mineral
  layer plus wood-chip mulch" maps cleanly onto Mor/Moder-over-Podzol; a
  humus-form design treatment remains a possible refinement (open item).

## 2. Plant-available water targets vs published texture ranges

Published available-water-capacity ranges by texture class (1 in/ft ≈ 8.3
vol %):

- Loamy sand: 0.75–1.25 in/ft → 6–10 vol %
- Sandy loam: 1.2–1.7 in/ft → 10–14 vol %
- Loam: ~1.9–2.0 in/ft → ~16 vol %

Sources: USDA NRCS, Estimating Soil Moisture by Feel and Appearance
(wcc.nrcs.usda.gov/ftpref/wntsc/waterMgt/irrigation/EstimatingSoilMoisture.pdf);
UC ANR Center for Landscape and Urban Horticulture, Soil Water Holding
Characteristics (ucanr.edu/site/center-landscape-urban-horticulture/soil-water-holding-characteristics).

Our blends are sandy loam (sand 50–70% of the fine mineral fraction), so the
mineral-skeleton range is ~10–14 vol %. Verdicts on the spec targets:

| Target | Verdict |
| --- | --- |
| Layer A ≥12% (UW-M) | **Inside published range** for sandy loam |
| Layer A ≥14% (UW-D) | **Plausible via design lever**: top of the sandy-loam range, supported by the 6.0–9.0% organic matter and finer-half texture selection |
| Layer A ≥16% (UW-X) | **Stretch — needs laboratory confirmation**: above the published sandy-loam mineral range; reachable only via the 8.0–12.0% organic matter plus finer-half texture selection; organic matter raises available water capacity (Saxton & Rawls 2006, SSSAJ 70:1569–1578) |
| Layer B ≥10% (UW-M) | **Inside published range** (sandy-loam/loamy-sand boundary) |
| Layer B ≥11–12% (UW-D/UW-X) | **Stretch** at 1.0–3.0% organic matter; UW-X Layer B ≥12% in particular needs laboratory demonstration or an organic-matter rethink |

Action this implies (already open): confirm the UW-X water-retention targets
with the testing laboratory before tender, and be prepared to relax ≥16%/≥12%
to demonstrated blend values.

## 3. CCISS tree-layer suitability check

Dataset: CCISS Environmental Suitability Ratings (BC Data Catalogue record
1810fdca-8762-4d6a-8886-4e8cefbdb640; CSV from bcgov/ccissr `feas_tables`
branch; local untracked copy `reference/cciss_suitability.csv`, 15,620 rows,
96 tree species). Ratings: E1 high, E2 moderate, E3 low; ENA = no rating.

**Scope limitation**: CCISS rates tree species only. Of the 19 palette
species, exactly one is covered — shore pine (Pl). The shrub and herb layer
cannot be CCISS-checked; their verification remains the LMH77 vegetation
cross-reference (`palette-bec-crosswalk.md`).

Shore pine (Pl) historic ratings in the relevant units:

| Unit | Ratings |
| --- | --- |
| CWHdm3 | 102 = E3; 103 = E3; Wb55 (bog) = E2; no zonal 101 rating |
| CWHdm1 | 103 = E2; 102 = E3; Wb55 = E1 |
| CWHdm2 | 104 = E2; 102/103 = E3; Wb55 = E1 |
| CWHxs | all ENA (new BEC13 unit; no ratings yet) |
| CDFmm | 101–106, 111 = E3; Wb55 = E2 |

Interpretation:

- E3 on 102/103 is consistent with the ecology, not a red flag: E3 denotes
  occurrence near the tolerance limit on harsh sites (the CCISS E3 definition
  explicitly covers "very xeric sites with shallow, discontinuous soils").
  LMH77 independently calls shore pine common on dry sites and bogs in
  CWHdm3, and the 102 site series is literally named PlcFdc.
- The E1/E2 bog ratings confirm the species' edaphic (not climatic) control:
  it occupies the dry and wet extremes and is excluded from zonal sites by
  competition. An urban UW-X bed is climatically benign by comparison; the
  E3 caveat reads as "expect low vigor", with the deeper constructed profile
  as the mitigation.
- CWHxs has no CCISS ratings (all ENA), so the UW-X climate-analogue check
  rests on CWHdm1/dm2 and CDFmm only.
- Observation for professional review (not a soil-spec issue): the palette
  contains no zonal canopy conifer — no Douglas-fir, western hemlock or
  western redcedar — while every analogue site series is canopied by them
  (Fd is E1 on CWHdm3 101/103/104/110). If the woodland concept intends a
  conifer overstorey, this is a palette decision to take deliberately.

## 4. Summary verdict

- Framework and anchors: validated (LMH77 unit descriptions, edatopic grid,
  CCISS tree-layer data all consistent with the deployment-context design).
- PAW targets: UW-M inside range; UW-D plausible via the organic-matter and
  texture levers; UW-X Layer A ≥16% and Layer B ≥12% are stretch values
  flagged for laboratory confirmation before tender.
- Remaining authored guesses not yet bounded: mulch depths (100–150 mm
  UW-X), 40 m³ per-tree volume, Layer A organic matter 8.0–12.0% for UW-X
  (settlement and hydrophobicity risks at the top end).

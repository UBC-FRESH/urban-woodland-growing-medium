# Palette ↔ BEC Cross-Reference (Reverse-Engineering the Analogue)

Cross-referencing the 19-species target palette against LMH77 Chapter 6
site-unit descriptions for the five dry-end BEC13 units, to reverse-engineer
which biogeoclimatic unit and edatope positions the assemblage most resembles.
Method and caveats first, then the matrix, then the conclusion.

## Method and caveats

- Source: LMH77 site-unit chapters for CDFmm (printed 200+), CWHdm1 (216+),
  CWHdm2 (230+), CWHdm3 (246+), CWHxs (497+); local copy
  `reference/LMH77.pdf`.
- Matching by common and Latin names against the prose descriptions and
  vegetation flowcharts. LMH77 prose lists indicator and characteristic
  species; absence from the prose does **not** mean a species is absent from
  the unit — widespread minor species are simply not diagnostic.
- Hits below therefore mean "named in that unit's site-unit literature", a
  positive signal; misses are weak negative evidence only.

## Presence matrix (19 palette species + 3 reference species)

| Species | CDFmm | CWHdm1 | CWHdm2 | CWHdm3 | CWHxs |
| --- | --- | --- | --- | --- | --- |
| Vine Maple | – | – | – | Y | Y |
| Vanilla Leaf | Y | Y | Y | Y | – |
| Nodding Onion | – | – | – | – | – |
| Red Columbine | – | – | – | – | – |
| Kinnikinnick | – | – | Y | – | Y |
| Hairy Manzanita (ref) | – | Y | – | Y | – |
| Wild Ginger | – | – | – | – | Y |
| Creeping Oregon-grape | – | – | – | – | – |
| Dull Oregon-grape (ref) | Y | Y | Y | Y | Y |
| Tall Oregon-grape (ref) | Y | – | – | Y | Y |
| Bunchberry | – | – | Y | Y | – |
| Black Hawthorn | – | – | – | – | – |
| Bleeding Heart | – | – | – | – | – |
| White Fawn Lily | Y | – | – | – | – |
| Salal | Y | Y | Y | Y | – |
| False Solomon's Seal | – | – | – | Y | Y |
| Wild Plum | Y | – | – | – | – |
| Shore Pine | Y | Y | Y | Y | Y |
| Sword Fern | Y | Y | Y | Y | – |
| Stonecrop | Y | – | – | – | – |
| Evergreen Huckleberry | Y | – | – | – | – |
| Red Huckleberry | Y | Y | Y | Y | Y |
| **Palette hits (of 19)** | **9** | **5** | **7** | **8** | **6** |

## Reading the matrix

The hits cluster by ecology, not by unit:

- **CWHdm3 forest core (8 hits)**: vine maple, vanilla leaf, bunchberry,
  salal, false Solomon's seal, shore pine, sword fern, red huckleberry — plus
  reference indicators dull Oregon-grape and hairy manzanita. This is the
  101/103/110 zonal-forest flora.
- **CDFmm dry-open cohort (9 hits)**: white fawn lily, stonecrop, evergreen
  huckleberry, wild plum, plus the widespread salal/shore pine/sword fern/red
  huckleberry. The distinctive hits are the Garry-oak / dry Douglas-fir
  open-rock species — the palette's xeric herb and shrub cohort.
- CWHdm2 (7) catches kinnikinnick plus the forest cohort; CWHdm1 (5) and
  CWHxs (6) are weaker matches.
- Not diagnostic anywhere in the dry-end prose: nodding onion, red columbine,
  black hawthorn, bleeding heart, creeping Oregon-grape. They are widespread
  minor species; they neither support nor contradict an assignment.

## Edatope placement within CWHdm3

From the CWHdm3 flowchart and site-series descriptions (LMH77 printed
248–251, PDF 264–267):

| Site series | SMR (common term) | Diagnostic flora relevant to the palette |
| --- | --- | --- |
| 102 PlcFdc–Rock mosses–Clad lichens | 0–1 (very dry) | open Douglas-fir + shore pine on bedrock; oceanspray or hairy manzanita; salal moderate; polypody ferns; rock mosses and reindeer lichens |
| 103 FdcHw–Salal–Step moss | (1)2 (very to moderately dry) | Douglas-fir dominated; salal high cover; red huckleberry generally present; dull Oregon-grape often; bracken fern |
| 101 FdcHw–Red huckleberry–Salal | 3–4 (slightly dry to fresh) — **zonal** | Fd+Hw+Cw; red huckleberry + salal usually with vine maple and/or dull Oregon-grape; sword fern <5%; bracken |
| 104 FdcCw–Vine maple–Sword fern | 1–2, nutrient-rich colluvial | sword fern moderate to high |
| 110 FdcHwCw–Sword fern | ~4, rich (fresh) | vine maple and red huckleberry typical; sword fern diagnostic; vanilla-leaf and foamflower often present |

## Conclusion

The palette reverse-engineers to a **CWHdm3 zonal-forest core with a
CDFmm-flavoured xeric open-rock cohort** — exactly the hybrid the
deployment-context structure assumes:

- **UW-M** ← CWHdm3 101 (zonal) and 110 (richer mesic: vanilla-leaf, sword
  fern). The moist-herb cluster (bunchberry, wild ginger, false Solomon's
  seal) fits here; wild ginger is not a CWHdm3 indicator at all and needs the
  moist end of UW-M.
- **UW-D** ← CWHdm3 103 (and 104 on rich dry colluvium).
- **UW-X** ← CWHdm3 102 for the woody frame (Douglas-fir, shore pine, salal)
  with the herb/bulb cohort drawn from CDFmm-analogue open-rock flora (white
  fawn lily, stonecrop, nodding onion, red columbine, evergreen huckleberry).

Two palette corrections this evidence supports:

- **Kinnikinnick** is a CWHdm2/CWHxs indicator; the actual CWHdm3 102
  manzanita is *Arctostaphylos columbiana* (hairy manzanita). Keep
  kinnikinnick as a horticultural choice if desired, but note the analogue
  mismatch; hairy manzanita is the on-analogue 102 shrub.
- **Creeping Oregon-grape (B. repens)** appears nowhere in the dry-end prose;
  the CWHdm3 Oregon-grape is dull Oregon-grape (B. nervosa), named across
  101/103/104/110. Confirms the earlier flag in `plant-palette.md`.

The three-context structure and its site-series anchors are therefore
retained, with the UW-M analogue refined to "101, and 110 on richer mesic
sites" in the specification.

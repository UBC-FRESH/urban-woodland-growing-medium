"""Build the updated ten-page CWH woodland growing medium specification.

The updated version adds the Table 1A requested-properties summary and a
nutrient test interpretation note to the original specification. It is
composed by injecting the additional section into the ``build_spec`` source
and executing the result, which is how the retained deliverable was produced.
"""

from pathlib import Path

_PART3_ANCHOR = 'page("Part 3 Verification protocols and site preparation")'
_MUNICIPAL_ANCHOR = 'h("Municipal contract coordination")'

# Injected immediately before the Part 3 section inside build_document().
# Statement lines are indented to match the function body they are injected
# into; bracket-continuation lines may start at column zero.
_TABLE_1A_SECTION = """page('Table 1A Requested properties summary')
    p('This table supplements Table 1 and arranges the properties in the requested order. The existing physical performance criteria remain mandatory. Limits below are project requirements for the defined woodland profile.')
    table(['Property','Layer A upper 300 mm','Layer B lower 600 mm'],[
('C:N Carbon to nitrogen','10:1–25:1','Report; no fixed acceptance ratio at low organic C'),
('Organic matter % of total dry weight','5.0–8.0%','1.0–3.0%'),
('Sand % of total dry weight','0.50F–0.70F%; equivalent to 50–70% of fine mineral fraction','0.50F–0.70F%; equivalent to 50–70% of fine mineral fraction'),
('Silt % of total dry weight','0.15F–0.35F%; equivalent to 15–35% of fine mineral fraction','0.15F–0.35F%; equivalent to 15–35% of fine mineral fraction'),
('Clay % of total dry weight','0.10F–0.20F%; equivalent to 10–20% of fine mineral fraction','0.10F–0.20F%; equivalent to 10–20% of fine mineral fraction'),
('Total silt and clay','0.30F–0.50F% of total dry weight; 30–50% of fine mineral fraction','Same as A'),
('Acidity pH','5.0–6.5; 1:2 soil mass to water volume','Same as A'),
('Maximum particle size','100% passing 25 mm; gravel 2–25 mm ≤5% total dry weight','Same as A'),
('Nitrogen N','Report total N as % dry weight; nitrate-N and ammonium-N separately in mg/kg','Same as A'),
('Phosphorus P ppm','Report extractable elemental P in mg/kg dry soil, with method; no fixed limit','Same as A'),
('Potassium K ppm','Report extractable elemental K in mg/kg dry soil, with method; no fixed limit','Same as A'),
('EC saturated extract at 25°C','≤2.0 dS/m, equivalent to ≤2.0 mS/cm','Same as A'),
('SAR saturated extract','≤4; conventionally reported without units, not as a percentage','Same as A')],[2.2,2.4,2.4])
    p('Dry-weight basis: F is the laboratory-measured fine mineral fraction (<2 mm, organic matter removed), expressed as a percentage of the original total dry medium. For example, F = 90 means sand limits of 45–63% of total dry medium. Require the lab to report both total-medium dry-mass percentages and normalized mineral texture, including its mass-balance procedure. Do not substitute normalized texture percentages for total dry-weight percentages. Sand + silt + clay = F on the total-medium basis and 100% on the normalized mineral basis. Total silt and clay is derived from sand, not an additional independent mix allowance.')
    p('Supplied reference figures: phosphorus 324 ppm and potassium 1,956 ppm. These are retained for review only and are not acceptance targets, minimums, maximums or fertilizer instructions. Confirm source, extraction method, total versus extractable measurement and applicable planting category before adopting them. No universal N, P or K target is assigned to all CWH woodland species; review the laboratory results against the actual plant palette before any amendment.')
    """

# Injected immediately before the municipal coordination heading.
_NUTRIENT_NOTE = (
    'h("Nutrient test interpretation")\n'
    "    p('University of Minnesota Soil Testing Laboratory. Our Methods. "
    "Documents separate extraction procedures for available phosphorus and "
    "potassium; used here only to explain analytical distinctions, not to set "
    "BC woodland nutrient targets. "
    "https://soiltest.cfans.umn.edu/about-us/our-methods')\n"
    "    "
)


def build_updated_document():
    """Build and return the updated specification as a python-docx Document."""
    source_path = Path(__file__).with_name("build_spec.py")
    source = source_path.read_text()
    if _PART3_ANCHOR not in source:
        msg = f"Part 3 anchor not found in {source_path.name}"
        raise RuntimeError(msg)
    if _MUNICIPAL_ANCHOR not in source:
        msg = f"Municipal coordination anchor not found in {source_path.name}"
        raise RuntimeError(msg)
    source = source.replace(_PART3_ANCHOR, _TABLE_1A_SECTION + _PART3_ANCHOR)
    source = source.replace(_MUNICIPAL_ANCHOR, _NUTRIENT_NOTE + _MUNICIPAL_ANCHOR)
    namespace = {}
    exec(compile(source, str(source_path), "exec"), namespace)  # noqa: S102
    return namespace["build_document"]()

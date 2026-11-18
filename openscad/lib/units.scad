import re

mm = 1
cm = 10 * mm
dm = 100 * mm
m = 1000 * mm

inch = 25.4 * mm

MAP = {
    "mm": mm,
    "cm": cm,
    "dm": dm,
    "m": m,
    "inch": inch,
    "in": inch,
}


def parse_size(size_desc:str) -> float:
    """
    Parses a size description into millimeters

    Example: "10.5cm" -> 105 (millimeters)
    """
    matches = re.findall(r"(\d+(\.\d+)?)(\w+)", size_desc)[0]

    return float(matches[0]) * MAP[matches[2]]

from collections import namedtuple

# NOTE: All measurements in millimeters (mm)

def __constant(name, **kwargs):
    const_class = namedtuple(f"{name}Const", kwargs.keys())
    return const_class(**kwargs)



# Standard Measurements
Standard = __constant(
    "Standard",
    mm=1,
    cm=10,
    dm=100,
    m=1000,
    inch=25.4
)


# Base Dims
Base = __constant(
    "Base",
    dia=32.0,
    thk=3.90
)

# Court pieces
Court = __constant(
    "Court",
    base_dia=Base.dia - 2,
    base_thk=Base.thk,
)

# Pawn pieces
Pawn = __constant(
    "Pawn",
    base_dia=Base.dia - 4,
    base_thk=Base.thk,
    height=24.35
)

# Magnet dimensions
# Used to generate "cutouts" for a magnet to fit into
# 15mm x 2mm
Magnet15 = __constant(
    "Magnet",
    dia=15.5,
    thk=2.50
)

# 20mm x 1mm
Magnet20 = __constant(
    "Magnet",
    dia=20.60,
    thk=1.75
)

Magnet = Magnet20

# Board tiles
Tile = __constant(
    "Tile",
    size=38.0,
    thk=Magnet.thk + 1
)

Crown = __constant(
    "Crown",
    base_dia=9.5, base_thk=2,
    dia1=(Base.dia / 2) + 1.5,
    dia2=(Base.dia / 2) + 6.0,
    height=10,
    dome_dia=11
)

# Invididual Pieces
King = __constant(
    "King",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    # height of just profile, exclude base and crown
    height=43.4
)

Queen = __constant(
    "Queen",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    # height of just profile, exclude base and crown
    dia=23.3,
    height=46.9,
    pom_dia=4
)

Knight = __constant(
    "Knight",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    head_w=33.0,
    head_h=33.8,
    head_thk=4,
    mid_height = 22.3,
    mid_dia1 = 25,
    mid_dia2 = 15
)

Bishop = __constant(
    "Bishop",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    height=40.0
)

Brick = __constant(
    "Brick",
    length=7.625,
    width=3.625,
    height=2.25
)

Rook = __constant(
    "Rook",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    height=47.0 - 5.0
    # height=20
)

#

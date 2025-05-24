from collections import namedtuple

# NOTE: All measurements in millimeters (mm)

def __constant(name, **kwargs):
    const_class = namedtuple(f"{name}Const", kwargs.keys())
    return const_class(**kwargs)


# Base Dims
Base = __constant(
    "Base",
    dia=32.0,
    thk=3.90
)

#  Piece Middle
Middle = __constant(
    "Middle",
    height=48.7
)

# Court pieces
Court = __constant(
    "Court",
    base_dia=Base.dia - 2,
    base_thk=Base.thk,
    height=Middle.height * 0.75
)

# Pawn pieces
Pawn = __constant(
    "Pawn",
    base_dia=Base.dia - 4,
    base_thk=Base.thk,
    height=Middle.height * 0.5
)

# Magnet dimensions
# Used to generate "cutouts" for a magnet to fit into
Magnet = __constant(
    "Magnet",
    dia=15.5,
    thk=2.50
)

# Board tiles
Tile = __constant(
    "Tile",
    size=38.0,
    thk=Magnet.thk + 1
)


Crown = __constant(
    "Crown",
    base_dia=11, base_thk=2,
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
    height=Court.height
)

Queen = __constant(
    "Queen",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    height=Court.height,
    pom_dia=4
)

Knight = __constant(
    "Knight",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    height = Court.height
)

Bishop = __constant(
    "Bishop",
    base_dia=Court.base_dia,
    base_thk=Court.base_thk,
    height = Court.height
)



#

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


# Base
Base = __constant(
    "Base",
    width=8.0,
    height=8.0
)

# Board tiles
Tile = __constant(
    "Tile",
    width=Base.width + 4.0,
    thk=2.0
)

# Court pieces
Court = __constant(
    "Court",
    width=Base.width + 2.0,
    height=Base.height + (Base.height * 0.75)
)

# Pawn pieces
Pawn = __constant(
    "Pawn",
    width=Base.width,
    height=Base.height
)

# Court Pieces
King = __constant(
    "King",
    width=Court.width,
    height=Court.height
)

Queen = __constant(
    "Queen",
    width=Court.width,
    height=Court.height
)

Knight = __constant(
    "Knight",
    width=Court.width,
    height=Court.height
)

Bishop = __constant(
    "Bishop",
    width=Court.width,
    height=Court.height
)

Rook = __constant(
    "Rook",
    width=Court.width,
    height=Court.height
)

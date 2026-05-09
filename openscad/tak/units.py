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
    inch=25.4,
)


# Base Dims
Base = __constant(
    "Base",
    dia=32.0,
    thk=3.90,
)

# CapStone pieces
CapStone1 = __constant(
    "CapStone1",
    base_dia=Base.dia - 4,
    base_thk=Base.thk,
    height=24.35,
)

BoardTile = __constant(
    "BoardTile",
    size=40.0,
    count=5,
    # size=20,
)

BoardBorder = __constant(
    "BoardBorder",
    width=3,
)

BoardInset = __constant(
    "BoardInset",
    width=1,
    thk=1,
)

Board = __constant(
    "Board",
    thk=3,
    tile=BoardTile,
    inset=BoardInset,
    border=BoardBorder,
    tile_count=BoardTile.count,
    inset_count=BoardTile.count+1,
)

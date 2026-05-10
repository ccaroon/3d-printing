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


# # Base Dims
# Base = __constant(
#     "Base",
#     dia=32.0,
#     thk=3.90,
# )


Tile = __constant(
    "Tile",
    size=20.0,
    count=2,
    # size=20,
)

TileInset = __constant(
    "TileInset",
    height=Tile.size * 0.07,
    length=Tile.size * 0.25,
)

BoardBorder = __constant(
    "BoardBorder",
    width=TileInset.length,
)

GridInset = __constant(
    "GridInset",
    width=1,
    thk=1,
)

Board = __constant(
    "Board",
    thk=3,
    tile=Tile,
    inset=GridInset,
    border=BoardBorder,
    tile_inset=TileInset,
    tile_count=Tile.count,
    inset_count=Tile.count+1,
)

# Player One - Stones
Stone = __constant(
    "Stone",
    width=Tile.size * 0.90,
    height=Tile.size * 0.90,
    thk=5,
)

CapStone = __constant(
    "CapStone",
    width=Tile.size * 0.50,
    height=Tile.size * 0.90,
    thk=5
)








#

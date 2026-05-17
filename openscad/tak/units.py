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

# Board
Tile = __constant(
    "Tile",
    # Real Size
    size=37.5,
    count=5,
    #
    # Test Size
    # size=37.5,
    # count=1,
)

TileInset = __constant(
    "TileInset",
    height=Tile.size * 0.07,
    length=Tile.size * 0.25,
    count=Tile.count + 1,
    depth_offset=0.75,
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

Magnet = __constant(
    "Magnet",
    dia=10.30,
    thk=1.30,
)

Board = __constant(
    "Board",
    thk=Tile.size * 0.15,
    tile=Tile,
    inset=GridInset,
    border=BoardBorder,
    magnet=Magnet,
    tile_inset=TileInset,
    tile_count=Tile.count,
    # Total Board size (width & height)
    size=(
        (Tile.size * Tile.count)
        + (GridInset.width * TileInset.count)
        + (BoardBorder.width * 2)
    ),
)

# Stones
STONE_SCALE = 0.80
Stone = __constant(
    "Stone",
    width=Tile.size * STONE_SCALE,
    height=Tile.size * STONE_SCALE,
    thk=(Tile.size * STONE_SCALE) * 0.25,
)

# CAPSTONE_SCALE = 0.70
CapStone = __constant(
    "CapStone",
    base_dia=Tile.size * 0.80,
    base_h=3.0,
    mid_height=Tile.size * 0.65,
    top_dia=(Tile.size * 0.75) * 0.55,
)


#

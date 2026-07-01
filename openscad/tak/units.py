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

MiniSet = __constant(
    "MiniSet",
    tile_size=13,
    tile_count=5,
    stone_cnt1=12,
    stone_cnt2=18,
)

LargeSet = __constant(
    "LargeSet",
    tile_size=37.5,
    tile_count=5,
    stone_cnt1=25,
    stone_cnt2=5,
)

TestSet = __constant(
    "TestSet",
    tile_size=37.5,
    tile_count=1,
    stone_cnt1=1,
    stone_cnt2=1,
)

# -----------------------------------------------------------------------------
# NOTE NOTE NOTE NOTE
# Change this to switch between Full, Mini & Test Sets
ActiveSet = LargeSet
# -----------------------------------------------------------------------------

# Board
Tile = __constant(
    "Tile",
    size=ActiveSet.tile_size,
    count=ActiveSet.tile_count,
)

TileInset = __constant(
    "TileInset",
    height=Tile.size * 0.07,
    length=Tile.size * 0.25,
    depth_offset=0.75,
)

TileInsetS2 = __constant(
    "TileInsetS2",
    height=Tile.size * 0.055,
    radius=Tile.size * 0.20,
    padding=0.30,
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
    # dia=round(Tile.size * 0.275, 1),
    thk=1.30,
)

Board = __constant(
    "Board",
    thk=Tile.size * 0.15,
    tile=Tile,
    inset=GridInset,
    border=BoardBorder,
    magnet=Magnet,
    magnet_offset=5,
    ti_s1=TileInset,
    ti_s2=TileInsetS2,
    ti_count=Tile.count + 1,
    tile_count=Tile.count,
    # Total Board size (width & height)
    size=(
        (Tile.size * Tile.count)
        + (GridInset.width * Tile.count + 1)
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

CapStone = __constant(
    "CapStone",
    base_dia=Stone.width,
    base_h=3.0,
    mid_height=Tile.size * 0.65,
    top_dia=(Tile.size * 0.75) * 0.55,
)

CasePost = __constant(
    "CasePost",
    width=Magnet.dia + (Board.magnet_offset * 2),
    length=Magnet.dia + (Board.magnet_offset * 2),
)

CaseS1 = __constant(
    "CaseS1",
    width=Board.size,
    length=Board.size,
    # + Board.thk to account for bottom height
    height=Stone.width + 3 + Board.thk,
    wall_thk=Board.thk,
    stone_cnt1=ActiveSet.stone_cnt1,
    stone_cnt2=ActiveSet.stone_cnt2,
)

case_s2_wall_thk = 2
CaseS2 = __constant(
    "CaseS2",
    width=Board.size,
    length=Board.size,
    height=Stone.height + case_s2_wall_thk + 2,
    wall_thk=case_s2_wall_thk,
)

PointToken = __constant(
    "PointToken",
    dia=20.0,
    thk=1.0,
    emboss_scale=0.90,
)

Scroll = __constant(
    "Scroll",
    dia=21.0,
    height=5.0,
    thk=1.0,
    core_length=80.0,
)


#

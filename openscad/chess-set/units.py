from collections import namedtuple

# NOTE: All measurements in millimeters (mm)

# Piece Base
Base = namedtuple("Base", ["dia", "thk"])
base = Base(30.0, 3.75)

#  Piece Middle
Middle = namedtuple("Middle", "height")
middle = Middle(48.7)

# Piece Top
# Top = namedtuple("Top", [])
# top = Top()

# Court pieces
Court = namedtuple("Court",
    ["base_dia", "base_thk", "height"]
)
court = Court(base.dia - 2, base.thk, middle.height * 0.75)

# Pawn pieces
Pawn = namedtuple("Pawn", ["base_dia", "base_thk", "height"])
pawn = Pawn(base.dia - 4, base.thk, middle.height * 0.5)

# Board tiles
Tile = namedtuple("Tile", ["size", "thk"])
tile = Tile(38.0, 3.25)

# Magnet dimensions
# Used to generate "cutouts" for a magnet to fit into
Magnet = namedtuple("Magnet", ["dia", "thk"])
magnet = Magnet(15.5, 2.30)

# Invididual Pieces
King = namedtuple("King", [
    "base_dia", "base_thk", "height",
    "crown_base_dia", "crown_base_thk",
    "crown_dia1", "crown_dia2", "crown_height",
    "crown_dome_dia"
])
king = King(
    court.base_dia, court.base_thk, court.height,
    11, 2,
    (base.dia / 2) + 1.5, (base.dia / 2) + 6.0, 10,
    11
)

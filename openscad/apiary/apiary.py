import math
from solid2 import *

import units

set_global_fn(150)

class Apiary:
    # Length of each flat side
    HEX_SIDE = 26.50 * units.mm

    # point-to-point
    # Also, the diameter if it were a circle
    HEX_LENGTH = HEX_SIDE * 2

    # top-to-bottom
    HEX_WIDTH = math.sqrt(3) * HEX_SIDE

    HEX_HEIGHT = 2.00 * units.mm

    HEX_CUTOUT = 39 * units.mm

    WALL_THK = 2.00 * units.mm
    BOTT_THK = 1.00 * units.mm
    PADDING  = 1.00 * units.mm

    # HIVES = (
    #     "langstroth",
    #     "log",
    #     "poppleton",
    #     "skep",
    #     "warre"
    # )

    def build(self, name, **kwargs):
        """
        Build an Apiary Component
        """
        model = None
        try:
            builder = getattr(self, f"_{name}")
            model = builder(**kwargs)
        except AttributeError as err:
            print(err)
            model = None

        return model


    def __grid_pos(self, row, col):
        """
        Given an row & col, translate that to an x,y,z position in a hex grid

        NOTE: For now z will always be 0
        """
        # Side + Wall - Wall/2 (bc I want the walls to overlap)
        adjusted_side = Apiary.HEX_SIDE + Apiary.WALL_THK - (Apiary.WALL_THK / 2)

        x = 1.5 * adjusted_side * col
        y = math.sqrt(3) * adjusted_side * ( row + 0.5 * (col % 2) )

        return (x,y,0)


    def __hive_grid(self, positions, **kwargs):
        """
        Build a Grid of Hexes based on given positions.

        Args:
            positions (list|tuple): Iterable of iterables describing the position of each Hex in the grid in (row, col) format.
        """
        hex = self._hex(**kwargs)

        origin = positions[0]
        hive = hex.translate(self.__grid_pos(origin[0], origin[1]))

        for pos in positions[1:]:
            hive += hex.translate(self.__grid_pos(pos[0], pos[1]))

        return hive


    def _hex(self, **kwargs):
        hex = None

        outside = cylinder(
            d=Apiary.HEX_LENGTH + Apiary.WALL_THK  + Apiary.PADDING,
            h=Apiary.HEX_HEIGHT + Apiary.BOTT_THK,
            _fn=6
        )

        inside  = cylinder(
            d=Apiary.HEX_LENGTH + Apiary.PADDING,
            h=Apiary.HEX_HEIGHT + Apiary.PADDING,
            _fn=6
        )

        hex = outside - inside.up(Apiary.BOTT_THK)
        if kwargs.get("cutout", False):
            cutout = cylinder(
                d=Apiary.HEX_CUTOUT,
                h=Apiary.HEX_HEIGHT + Apiary.PADDING,
                _fn=6
            )
            hex -= cutout.down(1)

        return hex


    def _starting_tile(self, **kwargs):
        """ The Faction & 2 Resources Tile """
        # kwargs["cutout"] = False

        positions = (
            (0, 0), (0, 1), (1,0),
        )
        grid = self.__hive_grid(positions, **kwargs)

        # To remove the inner walls
        eraser = cylinder(
            d=Apiary.HEX_LENGTH + Apiary.PADDING + 1.00,
            h=Apiary.HEX_HEIGHT + Apiary.PADDING + 0.50,
        )

        tile = (
            grid
            - eraser.translate([
                (Apiary.HEX_SIDE + Apiary.PADDING) / 2,
                (Apiary.HEX_WIDTH + Apiary.PADDING + 0.75) / 2,
                Apiary.BOTT_THK
            ])
        )

        return tile


    def _frame(self, **kwargs):
        """ Hive Expansion Frame """
        hex = self._hex(**kwargs)

        frame = (
            hex.translate(self.__grid_pos(0,0))
            + hex.translate(self.__grid_pos(0,1))
            + hex.translate(self.__grid_pos(0,2))
            + hex.translate(self.__grid_pos(-1,1))
        )

        return frame


    def _log(self, **kwargs):
        """ The Log Hive Mat"""

        stile = self._starting_tile(**kwargs)

        positions = (
            (0,-1),
            (1,-1), (1,1), (1,2),
            (2,0),  (2,1), (2,2)

        )

        hive_grid = self.__hive_grid(positions, **kwargs)

        return stile + hive_grid


    def _langstroth(self, **kwargs):
        """ The Langstroth Hive Mat """

        stile = self._starting_tile(**kwargs)
        positions = (
            (1,1), (1,2),
            (2,-2), (2,-1), (2,0), (2,2),
            (3, -2)
        )

        hive_grid = self.__hive_grid(positions, **kwargs)

        return stile + hive_grid


    def _poppleton(self, **kwargs):
        """ The Poppleton Hive Mat """
        stile = self._starting_tile(**kwargs)

        pos1 = (
            (1,1), (1,2),
            (2,0), (2,2), (2,3),
            # (3,4), (3,5)
        )

        pos2 = (
            # (1,1), (1,2),
            # (2,0), (2,2), (2,3),
            (3,4), (3,5)
        )

        pplton = None
        section = kwargs.get("section")
        if section == "part1":
            hive_grid = self.__hive_grid(pos1, **kwargs)
            pplton = stile + hive_grid
        elif section == "part2":
            hive_grid = self.__hive_grid(pos2, **kwargs)
            pplton = hive_grid
        else:
            raise ValueError("Error: Poppleton -> Must specify `section` (part1 | part2)")

        return pplton


    def _skep(self, **kwargs):
        """ The Skep Hive Mat """
        stile = self._starting_tile(**kwargs)

        positions = (
            (1,1), (1,2),
            (2,0), (2,1), (2,2),
            (3,0), (3,2)
        )

        hive_grid = self.__hive_grid(positions, **kwargs)

        return stile + hive_grid


    def _warre(self, **kwargs):
        """ The Warre Hive Mat """
        stile = self._starting_tile(**kwargs)

        positions = (
            (1,-1), (1,1), (1,2),
            (2,0),
            (3,-1), (3,0), (3,1)
        )

        hive_grid = self.__hive_grid(positions, **kwargs)

        return stile + hive_grid

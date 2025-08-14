import math
from solid2 import *


import units

class Apiary:
    # Length of each flat side
    HEX_SIDE = 26.00 * units.mm

    # point-to-point
    # Also, the diameter if it were a circle
    HEX_LENGTH = HEX_SIDE * 2

    # top-to-bottom
    HEX_WIDTH = math.sqrt(3) * HEX_SIDE

    HEX_HEIGHT = 1.75  * units.mm

    WALL_THK = 2.00  * units.mm
    PADDING  = 1.00  * units.mm

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


    def _hex(self, **kwargs):
        outside = cylinder(
            d=Apiary.HEX_LENGTH + Apiary.WALL_THK  + Apiary.PADDING,
            h=Apiary.HEX_HEIGHT + Apiary.WALL_THK,
            _fn=6
        )

        inside  = cylinder(
            d=Apiary.HEX_LENGTH + Apiary.PADDING,
            h=Apiary.HEX_HEIGHT + Apiary.PADDING,
            _fn=6
        )

        return outside - inside.up(Apiary.WALL_THK)

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


    def _frame(self, **kwargs):
        hex = self._hex(**kwargs)

        frame = (
            hex.translate(self.__grid_pos(0,0))
            + hex.translate(self.__grid_pos(0,1))
            + hex.translate(self.__grid_pos(0,2))
            + hex.translate(self.__grid_pos(-1,1))
        )

        return frame


    def __hive_mat(self, positions, **kwargs):
        """
        Build a Hive Mat based on given positions.

        Args:
            positions (tuple): Tuple of tuples describing the position of each
                               Hex in the grid.
        """
        hex = self._hex(**kwargs)

        origin = positions[0]
        hive = hex.translate(self.__grid_pos(origin[0], origin[1]))

        for pos in positions[1:]:
            hive += hex.translate(self.__grid_pos(pos[0], pos[1]))

        return hive


    def _log(self, **kwargs):
        """ The Log Hive Mat"""

        positions = (
            (0, 0), (0, 1), (0, 2),
            (-1, 1),
            (1, 0), (1, 1), (1, 2),
            (2, 2), (1, 3), (0,3),
        )

        return self.__hive_mat(positions, **kwargs)


    def _langstroth(self, **kwargs):
        """ The Langstroth Hive Mat """
        positions = (
            (0,0), (0,1),
            (1,0), (1,1) ,(1,2),
            (2,0), (2,2),
            (2,-1), (2,-2),
            (3,-2)
        )

        return self.__hive_mat(positions, **kwargs)


    def _poppleton(self, **kwargs):
        """ The Poppleton Hive Mat """
        positions = (
            (0,0), (0,1),
            (1,0), (1,1), (1,2),
            (2,0), (2,2),
            (2,3), (3,4), (3,5)
        )

        return self.__hive_mat(positions, **kwargs)


    def _skep(self, **kwargs):
        """ The Skep Hive Mat """
        positions = (
            (0,0), (0,1),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2),
            (3,0), (3,2)
        )

        return self.__hive_mat(positions, **kwargs)


    def _warre(self, **kwargs):
        """ The Warre Hive Mat """
        positions = (
            (0,0), (0,1),
            (1,0), (1,1), (1,2),
            (1,-1),
            (2,0),
            (3,-1), (3,0), (3,1)

        )

        return self.__hive_mat(positions, **kwargs)









#

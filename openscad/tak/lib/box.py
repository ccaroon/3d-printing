from solid2 import *


class Box:
    """
    An Open-topped box
    """

    DIMS_INNER = "inner"
    DIMS_OUTER = "outer"

    def __init__(self, width, length, height, wall_thk, dim_type=DIMS_OUTER):
        self.__width = width
        self.__length = length
        self.__height = height
        self.wall_thk = wall_thk
        self.__dim_type = dim_type

    @property
    def width(self):
        w = self.__width
        if self.__dim_type == self.DIMS_INNER:
            w = self.__width + (self.wall_thk * 2)

        return w

    @property
    def length(self):
        l = self.__length
        if self.__dim_type == self.DIMS_INNER:
            l = self.__length + (self.wall_thk * 2)

        return l

    @property
    def height(self):
        h = self.__height
        if self.__dim_type == self.DIMS_INNER:
            h = self.__height + self.wall_thk

        return h

    def build(self):
        inner_dims = []
        outer_dims = []

        match self.__dim_type:
            case self.DIMS_INNER:
                inner_dims = [
                    self.__width,
                    self.__length,
                    self.__height,
                ]
                outer_dims = [
                    inner_dims[0] + (self.wall_thk * 2),
                    inner_dims[1] + (self.wall_thk * 2),
                    inner_dims[2],
                ]
            case self.DIMS_OUTER:
                outer_dims = [
                    self.__width,
                    self.__length,
                    self.__height,
                ]
                inner_dims = [
                    outer_dims[0] - (self.wall_thk * 2),
                    outer_dims[1] - (self.wall_thk * 2),
                    outer_dims[2],
                    # - self.wall_thk + 1
                ]
            case _:
                raise ValueError(f"Invalid Dimension Type: [{self.__dim_type}]")

        outer = cube(outer_dims)
        inner = cube(inner_dims)

        return outer - inner.translate(self.wall_thk, self.wall_thk, self.wall_thk)

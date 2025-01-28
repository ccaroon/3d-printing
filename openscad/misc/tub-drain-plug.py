#!/usr/bin/env python
import math

from solid2 import *

from lib import units

PLUG_HEIGHT = 30 * units.mm
PLUG_WIDTH = 37 * units.mm
WALL_THICKNESS = 2 * units.mm
DRAIN_HOLE_DIA = 4 * units.mm

def tub_drain_plug():
    plug = cylinder(d=PLUG_WIDTH, h=PLUG_HEIGHT)
    cutout = cylinder(d=PLUG_WIDTH - WALL_THICKNESS, h=PLUG_HEIGHT)

    # Drain Holes
    # AngleToXY: tan(θ) = (y-coordinate)/(x-coordinate)
    # Spiral: r = aθ
    # ---------------
    # Polar to Cartesian
    # x = r * cos(θ)
    # y = r * sin(θ)
    hole = cylinder(d=DRAIN_HOLE_DIA, h=WALL_THICKNESS*2)
    # center hole
    plug -= hole.down(WALL_THICKNESS//2)

    # other angles do weird things
    angle_delta = 45
    start_angle = 0
    for angle in range(start_angle+angle_delta, 360-angle_delta, angle_delta):
        for r in (5,10,15):
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            plug -= hole.translate([x, y, -WALL_THICKNESS//2])

    start_angle = 12
    for angle in range(start_angle+angle_delta, 360-angle_delta, angle_delta):
        for r in (10,15):
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            plug -= hole.translate([x, y, -WALL_THICKNESS//2])

    return plug - cutout.up(WALL_THICKNESS)


if __name__ == "__main__":
    set_global_fn(150)
    drain_plug = tub_drain_plug()
    drain_plug.save_as_scad("./models/tub-drain-plug.scad")

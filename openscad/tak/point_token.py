from solid2 import *

from units import PointToken


def build(opts):
    base = cylinder(d=PointToken.dia, h=PointToken.thk)

    value = opts.get("value", None)
    if not value:
        raise ValueError(f"Please provide a point value: -o value=N")

    mid = None
    points = int(value)
    match points:
        case 1:
            width = 3
            mid = (
                cube(
                    width,
                    PointToken.dia * PointToken.emboss_scale,
                    PointToken.thk,
                )
                .translate(
                    (width / 2) * -1,
                    -(PointToken.dia * PointToken.emboss_scale) / 2,
                    PointToken.thk,
                )
                .color("grey")
            )
        case 2:
            pass
        case _:
            mid = (
                cylinder(
                    d=PointToken.dia * PointToken.emboss_scale,
                    h=PointToken.thk,
                    _fn=points,
                )
                .up(PointToken.thk)
                .color("grey")
            )

    piece = base + mid

    return piece


# -----------------------------------------------------------------------------
# stashed code
# -----------------------------------------------------------------------------
# fnt_size = PointToken.dia * 0.75
# pnt_text = (
#     text(
#         text=str(points),
#         font="FreeSerif",
#         size=fnt_size,
#         halign="center",
#         valign="center",
#     )
#     .linear_extrude(height=1)
#     .color("blue")
# )

# piece += pnt_text.up(PointToken.thk)

# --------------------------------------------------
# angle = (points - 2) * 180 / points
# fnt_size = PointToken.dia * 0.50
# pnt_text = (
#     text(
#         text=str(points),
#         font="FreeSerif",
#         size=fnt_size,
#         halign="center",
#         valign="center",
#     )
#     .linear_extrude(height=2)
#     .color("blue")
# )
# ----
# piece += mid.up(PointToken.thk) - pnt_text.up(PointToken.thk).forward(
#     1
# ).rotateZ(angle / 2)

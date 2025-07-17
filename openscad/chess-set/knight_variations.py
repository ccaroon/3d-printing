from solid2 import *
from units import Knight

# Head (left+right) in an upright position
def __build_head_stack():
    head =  import_(
        file="../images/knight/piper-profile-fill.svg"
        ).linear_extrude(
            height=Knight.head_thk
        )
    head = head.resize([Knight.head_w, Knight.head_h, 0])

    for data in ((0.8, "grey"), (0.7, "black")):
        scale = data[0]
        tx = (Knight.head_w - (Knight.head_w * scale)) / 2
        ty = (Knight.head_h - (Knight.head_h * scale)) / 2

        left = head.scale([scale,scale,scale]
            ).translate([tx,ty,Knight.head_thk]
            ).color(data[1])

        right = head.scale([scale,scale,scale]
            ).translate([tx,ty,-Knight.head_thk * scale]
            ).color(data[1])

        head = head + left + right

    part = head.rotateX(90).translate(
        [-Knight.head_w / 1.5, Knight.head_thk / 2, 0]
    )

    return part


def __build_head_bevel():
    head =  surface(
        file="../images/knight/piper-profile-grad.png",
        invert=False
        ).scale([1,1,.05])
        # .linear_extrude(
        #     height=Knight.head_thk
        # )
    head = head.resize([Knight.head_w, Knight.head_h, 0])

    return head



def __build_half_head(mirror=False):
    head =  import_(
        file="../images/knight/piper-profile-fill.svg"
        ).linear_extrude(
            height=Knight.head_thk
        )
    head = head.resize([Knight.head_w, Knight.head_h, 0])

    for data in ((0.8, "grey"), (0.7, "black")):
        scale = data[0]
        tx = (Knight.head_w - (Knight.head_w * scale)) / 2
        ty = (Knight.head_h - (Knight.head_h * scale)) / 2

        head += head.scale([scale,scale,scale]
            ).translate([tx,ty,Knight.head_thk]
            ).color(data[1])

    if mirror:
        part = head.mirrorX()
    else:
        part = head

    return part

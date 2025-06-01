from invoke import task

import calib


@task
def build(ctx, model, opt=None):
    """ Build a Model """
    match model:
        case "calib":
            calib.build(opt)
        case _:
            print(f"==> Unknown model: '{model}'")

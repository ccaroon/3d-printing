import re
from invoke import task

from apiary import Apiary

@task(iterable=["options"])
def build(ctx, name, options=[]):
    """
    Build the named Apiary Component.

    :param name: The name of the component.
    :param options: Comp. specific options in KEY=VALUE format.
    """

    kwargs = {}
    for opt in options:
        (key,value) = opt.split("=", 2)
        kwargs[key] = value

    apiary = Apiary()
    model = apiary.build(name, **kwargs)

    if model:
        base_name = f"apiary-{name}"
        if options:
            opts_sfx = "-".join(options)
            opts_sfx = re.sub(r"\W", "-", opts_sfx)
            base_name += f"-{opts_sfx}"

        file_name = f"./models/{base_name}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")
    else:
        print(f"=> Unknown component: {name}")


@task
def clean(ctx):
    """ Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")

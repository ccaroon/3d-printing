from invoke import task

import parts

@task(iterable=['opts'])
def build(ctx, name, opts=None):
    """
    Build the named Ballista part.

    :param name: The name of the part.
    :param opt: Part specific options.
    """
    part_name = name.upper()
    parts.build(part_name, opts)


@task
def clean(ctx):
    """ Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")

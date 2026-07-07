import os
import sys

from invoke import Collection, task

dot_dot = os.path.dirname(__file__) + "/.."
sys.path.insert(0, dot_dot)


from . import enigma
from . import factory
from . import tools


@task
def clean(ctx):
    """Clean up generated files"""
    with ctx.cd("models"):
        ctx.run("rm -f *.stl")


ns = Collection(
    clean,
    enigma,
    factory,
    tools,
)

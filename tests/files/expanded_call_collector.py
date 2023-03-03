from os import listdir

from ...somewhere import something2  # type: ignore
from . import something  # type: ignore
from .somewhere import something1  # type: ignore

listdir(".")


def new_context():
    from os.path import dirname as listdir

    listdir(".")


listdir(".")


async def new_new_context():
    from os.path import dirname as listdir

    listdir(".")


print("Hello World")
listdir(".")
something()
something1()
something2()

from os import listdir

from . import something  # type: ignore

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

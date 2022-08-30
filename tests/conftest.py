import ast

import pytest


@pytest.fixture()
def ast_getter():
    def getter(name: str):
        name = name if name.endswith(".py") else f"{name}.py"
        with open(f"tests/files/{name}", "rb") as f:
            return ast.parse(f.read())

    return getter

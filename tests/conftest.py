from __future__ import annotations

import ast

import ast_comments as astcom
import pytest

from pyaphid.analyzer import ImportsTracker


@pytest.fixture()
def ast_getter():
    def getter(name: str):
        name = name if name.endswith(".py") else f"{name}.py"
        with open(f"tests/files/{name}", "rb") as f:
            return astcom.parse(f.read())

    return getter


@pytest.fixture()
def collect_calls():
    class CallCollector(ast.NodeVisitor):
        def __init__(self) -> None:
            self.calls: list[ast.Call] = []

        def visit_Call(self, node: ast.Call):
            self.calls.append(node)

    def collect(tree: ast.AST):
        collector = CallCollector()
        collector.visit(tree)
        return collector.calls

    return collect


@pytest.fixture()
def collect_imports():
    def _collect_imports(file_name: str, tree: ast.AST):
        file_name = file_name if file_name.endswith(".py") else f"{file_name}.py"

        class ImportCollector(ast.NodeVisitor, ImportsTracker):
            pass

        collector = ImportCollector(file_path=f"tests/files/{file_name}")
        collector.visit(tree)

        return collector.imports, collector.import_froms

    return _collect_imports

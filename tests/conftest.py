from __future__ import annotations

import ast

import pytest

from pyaphid.analyzer import ImportsTracker


@pytest.fixture()
def ast_getter():
    def getter(name: str):
        name = name if name.endswith(".py") else f"{name}.py"
        with open(f"tests/files/{name}", "rb") as f:
            return ast.parse(f.read())

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
    class ImportCollector(ast.NodeVisitor, ImportsTracker):
        pass

    def collect(tree: ast.AST):
        collector = ImportCollector()
        collector.visit(tree)

        return collector.imports, collector.import_froms

    return collect

from __future__ import annotations

import ast

from pyaphid.analyzer import get_call_signature


def test_call_signatures(ast_getter):
    tree = ast_getter("call_signatures")

    class CallCollector(ast.NodeVisitor):
        def __init__(self) -> None:
            self.calls: list[ast.Call] = []

        def visit_Call(self, node: ast.Call):
            self.calls.append(node)

    collector = CallCollector()
    collector.visit(tree)

    call_signatures = [get_call_signature(call) for call in collector.calls]
    assert len(call_signatures)
    assert call_signatures == [
        ("", "print"),
        ("os", "listdir"),
        ("os.path", "dirname"),
        ("os.listdir().pop()", "encode"),
    ]

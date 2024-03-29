from __future__ import annotations

import pytest

from pyaphid.analyzer import (
    ExpandedCallCollector,
    Visitor,
    expand_call,
    get_call_signature,
)


def test_call_signatures(ast_getter, collect_calls):
    tree = ast_getter("call_signatures")
    calls = collect_calls(tree)

    call_signatures = [get_call_signature(call) for call in calls]
    assert len(call_signatures)
    assert call_signatures == [
        ("", "print"),
        ("os", "listdir"),
        ("os.path", "dirname"),
        ("path", "dirname"),
        ("os.listdir().pop()", "encode"),
    ]


def test_import_tracker(ast_getter, collect_imports):
    tree = ast_getter("expand_calls")
    imports, import_froms = collect_imports("expand_calls", tree)
    assert len(imports) == 5
    assert len(import_froms) == 6


def test_expand_calls(ast_getter, collect_calls, collect_imports):
    tree = ast_getter("expand_calls")

    calls = collect_calls(tree)
    imports, import_froms = collect_imports("expand_calls", tree)

    expanded_calls = [expand_call(call, imports, import_froms) for call in calls]

    assert expanded_calls == [
        "os.listdir",
        "os.path.dirname",
        "open",
        "tomli.load",
        "os.path.dirname",
        "tests.files.something",
        "os.chdir",
        "base64.b64encode",
        "base64.b16decode",
        "base64.b32decode",
        "json.encoder.JSONEncoder",
        "black.nullcontext",
    ]


def test_expanded_call_collector(ast_getter):
    tree = ast_getter("expanded_call_collector")

    collector = ExpandedCallCollector(
        file_path="tests/files/expanded_call_collector.py"
    )
    collector.visit(tree)
    assert [call.match for call in collector.calls] == [
        "os.listdir",
        "os.path.dirname",
        "os.listdir",
        "os.path.dirname",
        "print",
        "os.listdir",
        "tests.files.something",
        "tests.files.somewhere.something1",
        "tests.somewhere.something3",
    ], [call.match for call in collector.calls]


def test_visitor(ast_getter):
    tree = ast_getter("expanded_call_collector")
    filepath = "tests/files/expanded_call_collector.py"
    visitor = Visitor(filepath, ["os.listdir"])
    visitor.visit(tree)

    assert len(visitor.matches) == 3

    visitor = Visitor(filepath, ["os.path.dirname"])
    visitor.visit(tree)

    assert len(visitor.matches) == 2
    visitor2 = Visitor(filepath, ["os.path.*"])
    visitor2.visit(tree)

    assert len(visitor.matches) == 2
    assert visitor2.matches == visitor.matches


def test_func_name_collision(capsys: pytest.CaptureFixture, ast_getter):
    tree = ast_getter("func_name_collision")
    filepath = "tests/files/func_name_collision.py"
    visitor = Visitor(filepath, ["print"])
    visitor.visit(tree)

    assert len(visitor.matches) == 4
    assert [match.match for match in visitor.matches] == [
        "print",
        "print",
        "print",
        "print",
    ]

    assert (
        capsys.readouterr().out
        == "./tests/files/func_name_collision.py:15:9: Local definition of print collides with forbidden built-in. print calls will be ignored in this scope\n./tests/files/func_name_collision.py:24:1: Local definition of print collides with forbidden built-in. print calls will be ignored in this scope\n"  # noqa: E501
    )


def test_assignment_collision(capsys: pytest.CaptureFixture, ast_getter):
    tree = ast_getter("assignment_collision")
    filepath = "tests/files/assignment_collision.py"
    visitor = Visitor(filepath, ["print"])
    visitor.visit(tree)

    assert len(visitor.matches) == 4
    assert [match.match for match in visitor.matches] == [
        "print",
        "print",
        "print",
        "print",
    ]

    assert (
        capsys.readouterr().out
        == "./tests/files/assignment_collision.py:14:9: Assignment of print collides with forbidden built-in. print calls will be ignored in this scope\n./tests/files/assignment_collision.py:29:9: Assignment of print collides with forbidden built-in. print calls will be ignored in this scope\n./tests/files/assignment_collision.py:33:1: Assignment of print collides with forbidden built-in. print calls will be ignored in this scope\n"  # noqa: E501
    )

from __future__ import annotations

from pyaphid.analyzer import expand_call, get_call_signature


def test_call_signatures(ast_getter, collect_calls):
    tree = ast_getter("call_signatures")
    calls = collect_calls(tree)

    call_signatures = [get_call_signature(call) for call in calls]
    assert len(call_signatures)
    assert call_signatures == [
        ("", "print"),
        ("os", "listdir"),
        ("os.path", "dirname"),
        ("os.listdir().pop()", "encode"),
    ]


def test_import_tracker(ast_getter, collect_imports):
    tree = ast_getter("expand_calls")
    imports, import_froms = collect_imports(tree)
    assert len(imports) == 5
    assert len(import_froms) == 4


def test_expand_calls(ast_getter, collect_calls, collect_imports):
    tree = ast_getter("expand_calls")

    calls = collect_calls(tree)
    imports, import_froms = collect_imports(tree)

    expanded_calls = [expand_call(call, imports, import_froms) for call in calls]

    assert expanded_calls == [
        "os.listdir",
        "os.path.dirname",
        "open",
        "tomli.load",
        None,
        "os.chdir",
        "base64.b64encode",
        "base64.b16decode",
        "base64.b32decode",
        "json.encoder.JSONEncoder",
        "black.nullcontext",
    ]

from typer.testing import CliRunner

from pyaphid.cli import app

runner = CliRunner()


def test_cli():
    path = "tests/files"

    res = runner.invoke(app)
    assert res.exit_code == 1

    res = runner.invoke(app, path)
    assert res.exit_code == 23  # 23 print matches in our test files

    res = runner.invoke(app, "tests/files/call_signatures.py")
    assert res.exit_code == 1  # one print match

    res = runner.invoke(app, "tests/files/expand_calls.py")
    assert res.exit_code == 0  # no print match

    res = runner.invoke(app, [path, "--names"])
    assert res.exit_code == 0

    res = runner.invoke(app, [path, "-n"])
    assert res.exit_code == 0


def test_pypahid_ignore():
    res = runner.invoke(app, "tests/files/pyaphid_ignore.py")
    assert res.exit_code == 1

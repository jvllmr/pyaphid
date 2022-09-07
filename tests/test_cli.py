from click.exceptions import Exit

from pyaphid.cli import main


def test_cli():
    path = "tests/files"

    try:
        main([])
    except Exit as exc:
        assert exc.exit_code == 1

    try:
        main([path], print_names_only=False)
    except Exit as exc:
        assert exc.exit_code == 9  # 2 time print in our test files

    try:
        main(["tests/files/call_signatures.py"], print_names_only=False)
    except Exit as exc:
        assert exc.exit_code == 1

    try:
        main(["tests/files/expand_calls.py"], print_names_only=False)
    except Exit as exc:
        assert exc.exit_code == 0

    try:
        main([path], print_names_only=True)
    except Exit as exc:
        assert exc.exit_code == 0

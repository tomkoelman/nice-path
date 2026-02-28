from pathlib import Path

import pytest

from nice_path import nice_path


HOME = Path.home()


def test_home_itself():
    assert nice_path(HOME) == "~"


def test_path_under_home():
    p = HOME / "Documents" / "foo.txt"
    assert nice_path(p) == "~/Documents/foo.txt"


def test_string_input():
    p = str(HOME / "projects")
    assert nice_path(p) == "~/projects"


def test_tilde_input():
    assert nice_path("~/projects") == "~/projects"


def test_path_outside_home():
    p = Path("/tmp").resolve()
    assert nice_path(p) == str(p)


def test_resolves_dotdot():
    p = HOME / "a" / ".." / "b"
    assert nice_path(p) == "~/b"

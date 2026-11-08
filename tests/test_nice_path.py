from pathlib import Path

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


def test_symlinked_home(tmp_path, monkeypatch):
    real_home = tmp_path / "real_home"
    (real_home / "docs").mkdir(parents=True)
    link_home = tmp_path / "link_home"
    link_home.symlink_to(real_home)
    monkeypatch.setenv("HOME", str(link_home))

    assert nice_path("~") == "~"
    assert nice_path("~/docs") == "~/docs"
    assert nice_path(link_home / "docs") == "~/docs"
    assert nice_path(real_home / "docs") == "~/docs"

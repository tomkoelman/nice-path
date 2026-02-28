from pathlib import Path


def nice_path(path: Path | str) -> str:
    """Return a nice path string, relative to ~ if possible."""
    p = Path(path).expanduser().resolve()
    home = Path.home()
    try:
        rel = p.relative_to(home)
        rel_str = str(rel)
        return "~/" + (rel_str if rel_str != "." else "")
    except ValueError:
        return str(p)

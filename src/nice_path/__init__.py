from pathlib import Path


def nice_path(path: Path | str) -> str:
    """Return a nice path string, relative to ~ if possible."""
    p = Path(path).expanduser().resolve()
    home = Path.home()
    try:
        rel = p.relative_to(home)
        if str(rel) == ".":
            return "~"
        else:
            return str(Path("~") / rel)
    except ValueError:
        return str(p)

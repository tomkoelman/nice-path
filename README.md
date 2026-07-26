# nice_path

A Python library for formatting a path in a nice way. If a path is
relative to the users home directory it will rewrite it to use `~`.

## Examples

```python
from nice_path import nice_path
from pathlib import Path

nice_path("/Users/<user>/.config/something")  # "~/.config/something"

nice_path("/Users/<user>/")  # "~"

nice_path("/tmp")  # "/tmp"

nice_path(Path("/Users/<user>/Documents"))  # "~/Documents"
```

## License

This project is licensed under the MIT License.

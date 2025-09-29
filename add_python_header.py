#!/usr/bin/env python3
import sys
from pathlib import Path
import tempfile
import shutil

HEADER = "# -*- coding: utf-8 -*-\n\n"

def ensure_python_header(filepath: Path) -> bool:
    """Ensure the file starts with UTF-8 header.
    Returns True if modified, False otherwise."""

    # Skip Odoo special files
    if filepath.name in {"__manifest__.py", "__init__.py"}:
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines and lines[0].strip() == HEADER.strip():
        return False  # Already has header

    # Write new file with header
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
        tmp.write(HEADER)
        tmp.writelines(lines)
        tempname = tmp.name

    shutil.move(tempname, filepath)
    print(f"Fixed {filepath} (added UTF-8 header)")
    return True


def main(argv):
    modified = False
    for filename in argv[1:]:
        filepath = Path(filename)
        if filepath.suffix == ".py":
            if ensure_python_header(filepath):
                modified = True
    # Exit code 1 tells pre-commit "I fixed something"
    return 1 if modified else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

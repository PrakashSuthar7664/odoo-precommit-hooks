#!/usr/bin/env python3
import sys
from pathlib import Path
import tempfile
import shutil

HEADER = "/** @odoo-module */\n\n"

def ensure_js_header(filepath: Path) -> bool:
    """Ensure the file starts with Odoo JS header.
    Returns True if modified, False otherwise."""
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
    print(f"Fixed {filepath} (added @odoo-module header)")
    return True


def main(argv):
    modified = False
    for filename in argv[1:]:
        filepath = Path(filename)
        if filepath.suffix == ".js":
            if ensure_js_header(filepath):
                modified = True
    return 1 if modified else 0  # pre-commit convention


if __name__ == "__main__":
    sys.exit(main(sys.argv))

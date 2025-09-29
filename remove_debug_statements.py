#!/usr/bin/env python3
import sys
from pathlib import Path
import tempfile
import shutil
import re

PYTHON_PATTERN = re.compile(r'^\s*print\s*\(.*\)\s*$')
JS_PATTERN = re.compile(r'^\s*console\.log\s*\(.*\)\s*;?\s*$')


def clean_file(filepath: Path) -> bool:
    """Remove debug statements from a file.
    Returns True if modified, False otherwise."""
    modified = False
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if filepath.suffix == ".py" and PYTHON_PATTERN.match(line):
            print(f"Removed print() from {filepath}")
            modified = True
            continue
        if filepath.suffix == ".js" and JS_PATTERN.match(line):
            print(f"Removed console.log() from {filepath}")
            modified = True
            continue
        new_lines.append(line)

    if modified:
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
            tmp.writelines(new_lines)
            tempname = tmp.name
        shutil.move(tempname, filepath)

    return modified


def main(argv):
    modified = False
    for filename in argv[1:]:
        filepath = Path(filename)
        if filepath.suffix in {".py", ".js"}:
            if clean_file(filepath):
                modified = True
    return 1 if modified else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))


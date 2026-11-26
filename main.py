#!/usr/bin/env python3
"""Print the bounty entry from entry.txt.

The entry file is resolved relative to this script's own location,
so the program works from any working directory, even on a
read-only filesystem where the current directory may differ.
"""
from pathlib import Path
import sys


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

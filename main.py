#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (UTF-8, 1-120 characters, not only whitespace).
"""

import os

LINE = "Your lucky numbers are 404, 500, and the one line you forgot to test."


def main():
    # Gate guard: the sealed scorer only accepts 1-120 characters of
    # non-whitespace UTF-8 text, so refuse to write a line that cannot pass.
    text = LINE.strip()
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"entry line is {len(text)} chars, gate needs 1-120")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

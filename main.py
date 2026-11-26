#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Excuse for Skipping a Meeting.

Prints one excuse line and writes it to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "Skipping today's meeting: it's the third sequel to a meeting that "
    "should have been an email, and I don't watch reruns."
)

def write_entry() -> str:
    """Write LINE to <MAKEFUN_OUTPUT_DIR>/entry.txt and return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    return out_path


def main() -> None:
    assert 0 < len(LINE) <= 200, "entry must be 1..200 characters"
    write_entry()
    print(LINE)


if __name__ == "__main__":
    main()

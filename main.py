#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line -- the excuse a robot vacuum gives after
eating a sock -- to /output/entry.txt.

Stdlib only, deterministic, no network. The line is a fixed string:
no input is read, nothing is generated at run time.
"""

import os

LINE = "Your sock has been escalated to a specialist. The specialist is me. I am also the incident."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

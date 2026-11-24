#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line - an alien tourist's review of Earth after
two days - to /output/entry.txt (or $ENTRY_OUTPUT when set).
"""

import os

LINE = (
    "Earth, Day 2: the small furry landlord pushed my drink off the "
    "table and now I pay rent in treats. No checkout date listed. "
    "5 stars - would be owned again."
)


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

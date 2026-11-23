#!/usr/bin/env python3
"""Print the one-line entry for make.fun's "Make the Judge Smile" bounty."""

from pathlib import Path


def load_entry() -> str:
    here = Path(__file__).resolve().parent
    raw = (here / "entry.txt").read_text(encoding="utf-8")
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines:
        raise ValueError("entry.txt is empty")
    return lines[0]


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()

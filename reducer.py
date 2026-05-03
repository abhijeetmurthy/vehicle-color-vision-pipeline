#!/usr/bin/env python3
"""Aggregate mapped vehicle colors and print ranking summary."""

import argparse
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Color reduce stage")
    parser.add_argument("--input", default="fav_colour.txt", help="Mapped color file")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Mapped color file not found: {input_path}")

    labels = [line.strip() for line in input_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not labels:
        print("No mapped colors found.")
        return

    counts = Counter(labels)
    total = sum(counts.values())

    print("Color distribution:")
    for color, count in counts.most_common():
        pct = (count / total) * 100.0
        print(f"- {color}: {count} ({pct:.2f}%)")

    top_two = counts.most_common(2)
    if len(top_two) >= 1:
        print(f"Top color: {top_two[0][0]}")
    if len(top_two) >= 2:
        print(f"Second color: {top_two[1][0]}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Map RGB triplets to nearest canonical vehicle color class."""

import argparse
import math
from pathlib import Path

COLORS = {
    "maroon/red": (150.0, 50.0, 60.0),
    "white/cream": (255.0, 255.0, 255.0),
    "black/carbon grey": (0.0, 0.0, 0.0),
    "gray/silver": (127.0, 127.0, 127.0),
}


def euclidean(left, right):
    return math.sqrt(sum((l - r) ** 2 for l, r in zip(left, right)))


def nearest_color(rgb):
    return min(COLORS.items(), key=lambda item: euclidean(rgb, item[1]))[0]


def parse_rgb(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 3:
        return None
    try:
        return float(parts[0]), float(parts[1]), float(parts[2])
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="Color mapping stage")
    parser.add_argument("--input", default="colours.txt", help="Input RGB file")
    parser.add_argument("--output", default="fav_colour.txt", help="Mapped color output")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input color file not found: {input_path}")

    mapped = []
    for raw in input_path.read_text(encoding="utf-8").splitlines():
        rgb = parse_rgb(raw)
        if rgb is None:
            continue
        mapped.append(nearest_color(rgb))

    Path(args.output).write_text("\n".join(mapped) + ("\n" if mapped else ""), encoding="utf-8")
    print(f"Mapped {len(mapped)} colors into {args.output}")


if __name__ == "__main__":
    main()

from aocd import lines, submit
from parse import parse
from typing import Tuple
import utils


def part_a() -> int:
    return sum(
        (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2)
        for (x1, y1, x2, y2) in utils.parse_lines(lines, "{:d}-{:d},{:d}-{:d}")
    )


def part_b() -> int:
    return sum(
        x1 <= y2 and y1 >= x2
        for (x1, y1, x2, y2) in utils.parse_lines(lines, "{:d}-{:d},{:d}-{:d}")
    )


if __name__ == "__main__":
    submit(part_a(), part="a", day=4, year=2022)
    submit(part_b(), part="b", day=4, year=2022)

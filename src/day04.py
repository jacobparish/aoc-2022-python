from aocd import lines, submit
from parse import parse
from typing import Tuple
import utils


def ranges_contain(range_tuple: Tuple[int, int, int, int]):
    (x1, y1, x2, y2) = range_tuple
    return (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2)


def part_a() -> int:
    ranges = utils.parse_lines(lines, "{:d}-{:d},{:d}-{:d}")
    return sum(map(ranges_contain, ranges))


def ranges_overlap(range_tuple: Tuple[int, int, int, int]):
    (x1, y1, x2, y2) = range_tuple
    return x1 <= y2 and y1 >= x2


def part_b() -> int:
    ranges = utils.parse_lines(lines, "{:d}-{:d},{:d}-{:d}")
    return sum(map(ranges_overlap, ranges))


if __name__ == "__main__":
    submit(part_a(), part="a", day=4, year=2022)
    submit(part_b(), part="b", day=4, year=2022)

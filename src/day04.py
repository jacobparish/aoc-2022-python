from aocd import lines, submit
from parse import parse
from typing import Tuple


def parse_ranges(line: str):
    return parse("{:d}-{:d},{:d}-{:d}", line)


def ranges_contain(range_tuple: Tuple[int, int, int, int]):
    (x1, y1, x2, y2) = range_tuple
    return (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2)


def ranges_overlap(range_tuple: Tuple[int, int, int, int]):
    (x1, y1, x2, y2) = range_tuple
    return x1 <= y2 and y1 >= x2


def part_a() -> int:
    return sum(map(ranges_contain, map(parse_ranges, lines)))


def part_b() -> int:
    return sum(map(ranges_overlap, map(parse_ranges, lines)))


if __name__ == "__main__":
    submit(part_a(), part="a", day=4, year=2022)
    submit(part_b(), part="b", day=4, year=2022)

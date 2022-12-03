from aocd import lines, submit
import more_itertools as mit
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase


def score_line(line: str):
    c1 = line[: len(line) // 2]
    c2 = line[len(line) // 2 :]
    item = set(c1).intersection(c2).pop()
    return alphabet.index(item) + 1


def part_a() -> int:
    return sum(map(score_line, lines))


def score_line_group(line_group):
    item = set.intersection(*map(set, line_group)).pop()
    return alphabet.index(item) + 1


def part_b() -> int:
    return sum(map(score_line_group, mit.chunked(lines, 3)))


if __name__ == "__main__":
    submit(part_a(), part="a", day=3, year=2022)
    submit(part_b(), part="b", day=3, year=2022)

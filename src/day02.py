from aocd import lines, submit


def calc_score_a(line):
    [p1, p2] = line.split(" ")
    p1num = "ABC".index(p1)
    p2num = "XYZ".index(p2)
    return 3 * ((p2num - p1num + 1) % 3) + p2num + 1


def part_a() -> int:
    return sum(map(calc_score_a, lines))


def calc_score_b(line):
    [p1, p2] = line.split(" ")
    p1num = "ABC".index(p1)
    result = "XYZ".index(p2)
    return 3 * result + (p1num + result - 1) % 3 + 1


def part_b() -> int:
    return sum(map(calc_score_b, lines))


if __name__ == "__main__":
    submit(part_a(), part="a", day=2, year=2022)
    submit(part_b(), part="b", day=2, year=2022)

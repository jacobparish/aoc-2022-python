from aocd import lines, submit
import itertools as it
import heapq


def parse_calorie_data(lines):
    return [
        [ int(line) for line in line_group ]
        for is_empty, line_group in it.groupby(lines, lambda l: l == '')
        if not is_empty
    ]


def calorie_totals(lines):
    return [ sum(calorie_group) for calorie_group in parse_calorie_data(lines) ]


def part_a() -> int:
    return max(calorie_totals(lines))


def part_b() -> int:
    return sum(heapq.nlargest(3, calorie_totals(lines)))


if __name__ == "__main__":
    submit(part_a(), part="a", day=1, year=2022)
    submit(part_b(), part="b", day=1, year=2022)

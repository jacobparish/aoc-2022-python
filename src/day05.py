from typing import List
from aocd import lines, submit
import utils


def parse_input(lines: List[str]):
    crate_rows, instrs = utils.parse_line_groups(
        lines, (None, "move {:d} from {:d} to {:d}")
    )

    ncrates = (len(crate_rows.pop()) + 1) // 4

    crates = [[] for _ in range(ncrates)]

    for row in crate_rows:
        for i, val in enumerate(row[1::4]):
            if val != " ":
                crates[i].append(val)

    return crates, instrs


def part_a() -> str:
    crates, instrs = parse_input(lines)

    for count, src, dst in instrs:
        for _ in range(count):
            crates[dst - 1].insert(0, crates[src - 1].pop(0))

    return "".join(crate[0] for crate in crates)


def part_b() -> str:
    crates, instrs = parse_input(lines)

    for count, src, dst in instrs:
        for i in range(count):
            crates[dst - 1].insert(i, crates[src - 1].pop(0))

    return "".join(crate[0] for crate in crates)


if __name__ == "__main__":
    submit(part_a(), part="a", day=5, year=2022)
    submit(part_b(), part="b", day=5, year=2022)

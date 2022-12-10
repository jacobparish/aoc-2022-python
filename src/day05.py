from aocd import lines
import utils
from typing import List


crate_rows, instrs = utils.parse_line_groups(
    lines, (None, "move {:d} from {:d} to {:d}")
)

ncrates = (len(crate_rows.pop()) + 1) // 4

crates1 = [[] for _ in range(ncrates)]
crates2 = [[] for _ in range(ncrates)]

for row in crate_rows:
    for i, val in enumerate(row[1::4]):
        if val != " ":
            crates1[i].append(val)
            crates2[i].append(val)

for count, src, dst in instrs:
    for i in range(count):
        crates1[dst - 1].insert(0, crates1[src - 1].pop(0))
        crates2[dst - 1].insert(i, crates2[src - 1].pop(0))

p1 = "".join(crate[0] for crate in crates1)
p2 = "".join(crate[0] for crate in crates2)

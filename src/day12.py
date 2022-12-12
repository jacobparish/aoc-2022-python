from aocd import lines
import string
import utils


def get_elevation(c: str) -> int:
    return string.ascii_lowercase.index("z" if c == "E" else "a" if c == "S" else c)


def get_neighbors(grid: list[str], i: int, j: int):
    curr = get_elevation(grid[i][j])
    if i > 0 and get_elevation(grid[i - 1][j]) - curr <= 1:
        yield (i - 1, j)
    if i < len(grid) - 1 and get_elevation(grid[i + 1][j]) - curr <= 1:
        yield (i + 1, j)
    if j > 0 and get_elevation(grid[i][j - 1]) - curr <= 1:
        yield (i, j - 1)
    if j < len(grid[0]) - 1 and get_elevation(grid[i][j + 1]) - curr <= 1:
        yield (i, j + 1)


grid = lines
start = None
end = None

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "S":
            start = (i, j)
        if val == "E":
            end = (i, j)

p1 = utils.shortest_path(start, end, lambda v: get_neighbors(grid, *v))
p2 = p1

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "a":
            try:
                p2 = min(
                    p2,
                    utils.shortest_path((i, j), end, lambda v: get_neighbors(grid, *v)),
                )
            except utils.NodeUnreachableError:
                pass

from aocd import lines
import string
from utils import CharGrid, NodeUnreachableError, shortest_path


def get_elevation(c: str) -> int:
    return string.ascii_lowercase.index("z" if c == "E" else "a" if c == "S" else c)


def get_neighbors(grid: CharGrid, v: tuple[int, int]):
    curr = get_elevation(grid[v])
    for w in grid.neighbors4(*v):
        if get_elevation(grid[w]) - curr <= 1:
            yield w


grid = CharGrid(lines)
start = grid.find("S")
end = grid.find("E")

p1 = shortest_path(start, end, lambda v: get_neighbors(grid, v))
p2 = p1

for s in grid.find_all("a"):
    try:
        p2 = min(p2, shortest_path(s, end, lambda v: get_neighbors(grid, v)))
    except NodeUnreachableError:
        pass

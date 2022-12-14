from aocd import lines
from parse import findall
import more_itertools as mit

paths = [list(findall("{:d},{:d}", line)) for line in lines]

ymax = max(y for path in paths for _, y in path)

grid: set[tuple[int, int]] = set()

# fill in paths
for path in paths:
    for (x1, y1), (x2, y2) in mit.sliding_window(path, 2):
        if x1 == x2:
            grid.update((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            grid.update((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
        else:
            raise ValueError(f"invalid path: {x1},{y1} -> {x2},{y2}")


p1 = 0
p2 = 0

reached_abyss = False

while (500, 0) not in grid:
    x, y = 500, 0

    while y < ymax + 1:
        stuck = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if (x + dx, y + dy) not in grid:
                x += dx
                y += dy
                stuck = False
                break
        if stuck:
            break

    grid.add((x, y))

    if y == ymax + 1:
        reached_abyss = True

    p1 += not reached_abyss
    p2 += 1

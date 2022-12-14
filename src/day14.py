from aocd import lines
from parse import findall
import more_itertools as mit
import numpy as np

paths = [list(findall("{:d},{:d}", line)) for line in lines]

width = 1000  # figure out how to not have to hardcode this
height = max(y for path in paths for _, y in path) + 3
grid = np.zeros((width, height), dtype=bool)

# fill in paths
for path in paths:
    for (x1, y1), (x2, y2) in mit.sliding_window(path, 2):
        grid[min(x1, x2) : max(x1, x2) + 1, min(y1, y2) : max(y1, y2) + 1] = True

# fill bottom row
grid[:, -1] = True

p1 = 0
p2 = 0

reached_abyss = False

while not grid[500, 0]:
    x, y = 500, 0

    while True:
        stuck = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if not grid[x + dx, y + dy]:
                x += dx
                y += dy
                stuck = False
                break
        if stuck:
            break

    grid[x, y] = True

    if y == height - 2:
        reached_abyss = True

    p1 += not reached_abyss
    p2 += 1

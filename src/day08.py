from aocd import lines
import utils


grid = utils.parse_digit_grid(lines)

visible = set()

for i, row in enumerate(grid.rows):
    tallest = -1
    for j, el in enumerate(row):
        if el > tallest:
            visible.add((i, j))
            tallest = el

    tallest = -1
    for j, el in reversed(list(enumerate(row))):
        if el > tallest:
            visible.add((i, j))
            tallest = el

for j, col in enumerate(grid.cols):
    tallest = -1
    for i, el in enumerate(col):
        if el > tallest:
            visible.add((i, j))
            tallest = el

    tallest = -1
    for i, el in reversed(list(enumerate(col))):
        if el > tallest:
            visible.add((i, j))
            tallest = el

p1 = len(visible)


p2 = 0

for i0, row in enumerate(grid.rows[1:-1], start=1):
    for j0, col in enumerate(grid.cols[1:-1], start=1):
        val = col[i0]
        score = 1
        # up
        i = i0 - 1
        while i >= 1 and col[i] < val:
            i -= 1
        score *= i0 - i
        # down
        i = i0 + 1
        while i < grid.nrows - 1 and col[i] < val:
            i += 1
        score *= i - i0
        # left
        j = j0 - 1
        while j >= 1 and row[j] < val:
            j -= 1
        score *= j0 - j
        # right
        j = j0 + 1
        while j < grid.ncols - 1 and row[j] < val:
            j += 1
        score *= j - j0

        if score > p2:
            p2 = score

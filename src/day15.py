from aocd import lines
from utils import parse_lines, size_of_interval_union, Vec2


sensors = parse_lines(
    lines, "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}"
)

row = 2e6
intervals = []

for xs, ys, xb, yb in sensors:
    d = abs(xs - xb) + abs(ys - yb) - abs(row - ys)
    if d >= 0:
        x1 = xs - d + ((xs - d, row) == (xb, yb))
        x2 = xs + d - ((xs + d, row) == (xb, yb))
        intervals.append((x1, x2))

p1 = size_of_interval_union(intervals)
size = 4e6

for xs1, ys1, xb1, yb1 in sensors:
    d1 = abs(xs1 - xb1) + abs(ys1 - yb1)
    border = {
        (x, y)
        for x, y in Vec2(xs1, ys1).circle1(d1 + 1)
        if 0 <= x <= size and 0 <= y <= size
    }
    for xs2, ys2, xb2, yb2 in sensors:
        d2 = abs(xs2 - xb2) + abs(ys2 - yb2)
        border = {
            (x, y)
            for x, y in border
            if abs(x - xs2) + abs(y - ys2) >= d2 and (x, y) != (xb2, yb2)
        }
    if len(border) > 0:
        assert len(border) == 1
        x, y = border.pop()
        p2 = size * x + y
        break

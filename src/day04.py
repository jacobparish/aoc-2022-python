from aocd import lines
import utils


ranges = utils.parse_lines(lines, "{:d}-{:d},{:d}-{:d}")
p1 = sum(
    (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2) for (x1, y1, x2, y2) in ranges
)
p2 = sum(x1 <= y2 and y1 >= x2 for (x1, y1, x2, y2) in ranges)

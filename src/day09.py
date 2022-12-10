from aocd import lines
import utils
from typing import List


def simulate_rope(lines: List[str], rope_len: int) -> int:
    rope = [[0, 0] for _ in range(rope_len)]
    head = rope[0]
    tail = rope[-1]
    tail_positions = {tuple(tail)}

    for dir, amt in utils.parse_lines(lines, "{} {:d}"):
        for _ in range(amt):
            if dir == "R":
                head[0] += 1
            elif dir == "L":
                head[0] -= 1
            elif dir == "D":
                head[1] += 1
            elif dir == "U":
                head[1] -= 1

            for k1, k2 in zip(rope, rope[1:]):
                if abs(k1[0] - k2[0]) > 1 or abs(k1[1] - k2[1]) > 1:
                    if k1[0] > k2[0]:
                        k2[0] += 1
                    elif k1[0] < k2[0]:
                        k2[0] -= 1
                    if k1[1] > k2[1]:
                        k2[1] += 1
                    elif k1[1] < k2[1]:
                        k2[1] -= 1

            tail_positions.add(tuple(tail))

    return len(tail_positions)


p1 = simulate_rope(lines, 2)
p2 = simulate_rope(lines, 10)

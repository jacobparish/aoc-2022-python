from aocd import lines
from collections import defaultdict
from utils import Vec2, bounding_box2

elves = {
    Vec2(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == "#"
}
dir_groups = [
    [Vec2(-1, 0), Vec2(-1, 1), Vec2(-1, -1)],
    [Vec2(1, 0), Vec2(1, 1), Vec2(1, -1)],
    [Vec2(0, -1), Vec2(1, -1), Vec2(-1, -1)],
    [Vec2(0, 1), Vec2(1, 1), Vec2(-1, 1)],
]
p1 = 0
p2 = 0
did_move = True

while did_move:
    proposals = defaultdict(list)

    for e in elves:
        if elves.isdisjoint(e.neighbors8()):
            continue

        for dir_group in dir_groups[p2 % 4 :] + dir_groups:
            if all(e + d not in elves for d in dir_group):
                proposals[e + dir_group[0]].append(e)
                break

    did_move = False

    for dst in proposals:
        if len(proposals[dst]) == 1:
            elves.remove(proposals[dst].pop())
            elves.add(dst)
            did_move = True

    p2 += 1
    if p2 == 10:
        p1 = bounding_box2(elves).area - len(elves)

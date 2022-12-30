from aocd import lines
from queue import SimpleQueue
from utils import Vec3, parse_lines

pts = {Vec3(*xyz) for xyz in parse_lines(lines, "{:d},{:d},{:d}")}

xmin = min(p.x for p in pts) - 1
ymin = min(p.y for p in pts) - 1
zmin = min(p.z for p in pts) - 1
xmax = max(p.x for p in pts) + 1
ymax = max(p.y for p in pts) + 1
zmax = max(p.z for p in pts) + 1

q: SimpleQueue[Vec3] = SimpleQueue()
s = Vec3(xmin, ymin, zmin)
outer_nbhd = {s}
q.put(s)

while not q.empty():
    p = q.get()
    for n in p.neighbors6():
        if (
            xmin <= n.x <= xmax
            and ymin <= n.y <= ymax
            and zmin <= n.z <= zmax
            and n not in outer_nbhd
            and n not in pts
        ):
            outer_nbhd.add(n)
            q.put(n)

p1 = sum(n not in pts for p in pts for n in p.neighbors6())
p2 = sum(n in outer_nbhd for p in pts for n in p.neighbors6())

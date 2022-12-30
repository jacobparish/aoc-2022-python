from aocd import lines
import itertools as it
from utils import parse_lines, shortest_paths, dijkstra
from typing import NamedTuple


class Valve(NamedTuple):
    rate: int
    neighbors: list[str]


valves: dict[str, Valve] = {
    v: Valve(r, t.split(" ", 4)[-1].split(", "))
    for v, r, t in parse_lines(lines, "Valve {} has flow rate={:d}; {}")
}

nonzero_valves = frozenset(v for v in valves if valves[v].rate != 0)

all_dists = {}

for v in nonzero_valves.union(["AA"]):
    dists = shortest_paths(v, lambda w: valves[w].neighbors)
    all_dists.update({(v, w): dists[w] for w in nonzero_valves})


def get_neighbors(state):
    v, vc, t = state
    if t >= 30:
        return

    if v in vc:
        yield (
            (v, vc.difference([v]), t + 1),
            sum(valves[w].rate for w in vc if w != v),
        )
    else:
        yield ((v, vc, 30), sum(valves[w].rate for w in vc if w != v) * (30 - t))

        for w in vc:
            if v != w and t + all_dists[v, w] <= 30:
                yield (
                    (w, vc, t + all_dists[v, w]),
                    sum(valves[w].rate for w in vc) * all_dists[v, w],
                )


base_flow = sum(valves[v].rate for v in nonzero_valves)


dists1 = dijkstra(("AA", nonzero_valves, 1), get_neighbors)
p1 = 29 * base_flow - min(d for s, d in dists1.items() if s[-1] == 30)


dists2 = dijkstra(("AA", nonzero_valves, 5), get_neighbors)
possible_visits = [
    (nonzero_valves.difference(s[1]), 25 * base_flow - d)
    for s, d in dists2.items()
    if s[-1] == 30
]
p2 = max(
    d1 + d2
    for (s1, d1), (s2, d2) in it.combinations(possible_visits, 2)
    if s1.isdisjoint(s2)
)

from typing import NamedTuple
from aocd import lines
from utils import shortest_paths, Vec2, CharGrid


grid = CharGrid(line[1:-1] for line in lines[1:-1])
start_pos = Vec2(-1, lines[0].index(".") - 1)
end_pos = Vec2(grid.nrows, lines[-1].index(".") - 1)


class State(NamedTuple):
    pos: Vec2
    t: int = 0
    end_reached: bool = False
    did_return: bool = False

    def is_snowy(self):
        if not (0 <= self.pos.x < grid.nrows and 0 <= self.pos.y < grid.ncols):
            return False
        for i, c in enumerate(grid.rows[self.pos.x]):
            if c == ">" and (i + self.t) % grid.ncols == self.pos.y:
                return True
            elif c == "<" and (i - self.t) % grid.ncols == self.pos.y:
                return True
        for i, c in enumerate(grid.cols[self.pos.y]):
            if c == "v" and (i + self.t) % grid.nrows == self.pos.x:
                return True
            elif c == "^" and (i - self.t) % grid.nrows == self.pos.x:
                return True
        return False


def get_neighbors(s: State):
    if s.pos.dist1(end_pos) == 1:
        yield s._replace(pos=end_pos, t=s.t + 1, end_reached=True)
    elif s.pos.dist1(start_pos) == 1 and s.end_reached:
        yield s._replace(pos=start_pos, t=s.t + 1, did_return=True)

    for n in grid.neighbors4(*s.pos):
        s_next = s._replace(pos=n, t=s.t + 1)
        if not s_next.is_snowy():
            yield s_next

    s_next = s._replace(t=s.t + 1)
    if not s_next.is_snowy():
        yield s_next


dists = shortest_paths(
    State(pos=start_pos),
    get_neighbors,
    stop_condition=lambda s: s.pos == end_pos and s.did_return,
)
p1 = min(dist for state, dist in dists.items() if state.end_reached)
p2 = max(dists.values())

import more_itertools as mit
import numpy as np
from parse import parse
from queue import SimpleQueue
from typing import Callable, Iterable, Optional, TypeVar


def split_lines(lines: Iterable[str], separator: str = ""):
    """
    Split list of lines at a separator. Default is to split at empty lines.
    """
    return list(mit.split_at(lines, lambda l: l == separator))


def split_numbers(lines: Iterable[str], separator: str = ""):
    """
    Split list of lines at a separator and convert to numbers. Default is to split at empty lines.
    """
    return [
        [int(line) for line in line_group]
        for line_group in mit.split_at(lines, lambda l: l == separator)
    ]


def parse_lines(lines: Iterable[str], fmt: str):
    """
    Parse lines according to a format string.
    """
    return [parse(fmt, line) for line in lines]


def parse_line_groups(lines: Iterable[str], fmts: Iterable[str], separator=""):
    """
    Split list of lines at a separator, and parse each group of lines according to the
    provided format strings.
    """
    return tuple(
        parse_lines(line_group, fmt) if fmt else line_group
        for fmt, line_group in zip(fmts, split_lines(lines, separator), strict=True)
    )


def bitsum(n: int) -> int:
    p = 0
    while n > 0:
        p += n & 1
        n >>= 1
    return p


V = TypeVar("V")


class NodeUnreachableError(Exception):
    ...


def shortest_paths(
    s: V,
    get_neighbors: Callable[[V], Iterable[V]],
    dist_max: int = -1,
    stop_condition: Callable[[dict[V, int]], bool] = lambda _: False,
) -> dict[V, int]:
    """
    Compute length of shortest path from source `s` to every other node visitable from `s`.
    If `t` is provided, stop after reaching node `t`.
    If `dist_max` is provided, only find paths of length <= dist_max.
    """
    q: SimpleQueue[V] = SimpleQueue()
    q.put(s)
    dists = {s: 0}
    while not q.empty():
        v = q.get()
        for w in get_neighbors(v):
            if w not in dists:
                dists[w] = dists[v] + 1
                if stop_condition(dists):
                    return dists
                if dist_max < 0 or dists[w] < dist_max:
                    q.put(w)
    return dists


def shortest_path(s: V, t: V, get_neighbors: Callable[[V], Iterable[V]]) -> int:
    """
    Compute length of shortest path from source `s` to target `t`.
    """
    dists = shortest_paths(s, get_neighbors, stop_condition=lambda dists: t in dists)
    if t in dists:
        return dists[t]
    else:
        raise NodeUnreachableError(f"{t} is not reachable from {s}")


class Grid:
    def __init__(self, data):
        self.data = np.array(data)
        assert len(self.data.shape) == 2

    @property
    def ncols(self):
        return self.data.shape[1]

    @property
    def nrows(self):
        return self.data.shape[0]

    @property
    def rows(self):
        return self.data

    @property
    def cols(self):
        return self.data.T

    def __getitem__(self, key):
        return self.data[key]

    def find(self, val) -> tuple[int, int]:
        i, j = np.where(self.data == val)
        return i[0], j[0]

    def find_all(self, val) -> list[tuple[int, int]]:
        return list(zip(*np.where(self.data == val)))

    def neighbors4(self, i: int, j: int) -> list[tuple[int, int]]:
        return [
            (i + di, j + dj)
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= i + di < self.nrows and 0 <= j + dj < self.ncols
        ]

    def neighbors8(self, i: int, j: int) -> list[tuple[int, int]]:
        return [
            (i + di, j + dj)
            for di, dj in [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
            ]
            if 0 <= i + di < self.nrows and 0 <= j + dj < self.ncols
        ]


class CharGrid(Grid):
    def __init__(self, data: list[str]):
        super().__init__([list(s) for s in data])


def parse_digit_grid(lines: Iterable[str]) -> Grid:
    """
    To parse stuff like this:

    30373
    25512
    65332
    33549
    35390
    """
    ...
    return Grid([[int(digit) for digit in line] for line in lines])


T = TypeVar("T")


def find_index(iter: Iterable[T], pred: Callable[[T], bool]) -> int:
    for i, item in enumerate(iter):
        if pred(item):
            return i
    return -1


def find(iter: Iterable[T], pred: Callable[[T], bool]) -> Optional[T]:
    for item in iter:
        if pred(item):
            return item
    return None


def find_last_index(iter: Iterable[T], pred: Callable[[T], bool]) -> int:
    for i, item in reversed(enumerate(iter)):
        if pred(item):
            return i
    return -1


def find_last(iter: Iterable[T], pred: Callable[[T], bool]) -> Optional[T]:
    for item in reversed(iter):
        if pred(item):
            return item
    return None


def columns_to_rows(lines: list[str], start_at_bottom: bool = False):
    """
    To help parse nonsense like this:

        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3
    """
    max_len = max(len(line) for line in lines)
    if start_at_bottom:
        lines = reversed(lines)
    return ["".join(line[i] for line in lines) for i in range(max_len)]

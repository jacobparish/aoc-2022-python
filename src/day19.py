from aocd import lines
import functools as ft
import utils
from typing import NamedTuple


class Blueprint(NamedTuple):
    id: int
    ore_bot_ore_cost: int
    clay_bot_ore_cost: int
    obsidian_bot_ore_cost: int
    obsidian_bot_clay_cost: int
    geode_bot_ore_cost: int
    geode_bot_obsidian_cost: int


class State(NamedTuple):
    t: int = 0
    ore_bots: int = 1
    clay_bots: int = 0
    obsidian_bots: int = 0
    geode_bots: int = 0
    ore_count: int = 0
    clay_count: int = 0
    obsidian_count: int = 0
    geode_count: int = 0

    def next_state(self):
        return self._replace(
            t=self.t + 1,
            ore_count=self.ore_count + self.ore_bots,
            clay_count=self.clay_count + self.clay_bots,
            obsidian_count=self.obsidian_count + self.obsidian_bots,
            geode_count=self.geode_count + self.geode_bots,
        )

    def buy_ore_bot(self, bp: Blueprint):
        return self._replace(
            ore_bots=self.ore_bots + 1,
            ore_count=self.ore_count - bp.ore_bot_ore_cost - 1,
        )

    def buy_clay_bot(self, bp: Blueprint):
        return self._replace(
            clay_bots=self.clay_bots + 1,
            ore_count=self.ore_count - bp.clay_bot_ore_cost,
            clay_count=self.clay_count - 1,
        )

    def buy_obsidian_bot(self, bp: Blueprint):
        return self._replace(
            obsidian_bots=self.obsidian_bots + 1,
            ore_count=self.ore_count - bp.obsidian_bot_ore_cost,
            clay_count=self.clay_count - bp.obsidian_bot_clay_cost,
            obsidian_count=self.obsidian_count - 1,
        )

    def buy_geode_bot(self, bp: Blueprint):
        return self._replace(
            geode_bots=self.geode_bots + 1,
            ore_count=self.ore_count - bp.geode_bot_ore_cost,
            obsidian_count=self.obsidian_count - bp.geode_bot_obsidian_cost,
            geode_count=self.geode_count - 1,
        )


@ft.cache
def find_max_geodes(bp: Blueprint, state: State, tmax: int):
    if state.t == tmax:
        return state.geode_count
    ore_prev = state.ore_count >= bp.ore_bot_ore_cost
    clay_prev = state.ore_count >= bp.clay_bot_ore_cost
    obsidian_prev = (
        state.ore_count >= bp.obsidian_bot_ore_cost
        and state.clay_count >= bp.obsidian_bot_clay_cost
    )
    geode_prev = (
        state.ore_count >= bp.geode_bot_ore_cost
        and state.obsidian_count >= bp.geode_bot_obsidian_cost
    )
    state = state.next_state()
    best = find_max_geodes(bp, state, tmax)
    if not ore_prev and state.ore_count >= bp.ore_bot_ore_cost:
        best = max(best, find_max_geodes(bp, state.buy_ore_bot(bp), tmax))
    if not clay_prev and state.ore_count >= bp.clay_bot_ore_cost:
        best = max(best, find_max_geodes(bp, state.buy_clay_bot(bp), tmax))
    if (
        not obsidian_prev
        and state.ore_count >= bp.obsidian_bot_ore_cost
        and state.clay_count >= bp.obsidian_bot_clay_cost
    ):
        best = max(best, find_max_geodes(bp, state.buy_obsidian_bot(bp), tmax))
    if (
        not geode_prev
        and state.ore_count >= bp.geode_bot_ore_cost
        and state.obsidian_count >= bp.geode_bot_obsidian_cost
    ):
        best = max(best, find_max_geodes(bp, state.buy_geode_bot(bp), tmax))
    return best


bps = [
    Blueprint(*fields)
    for fields in utils.parse_lines(
        lines,
        "Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.",
    )
]


p1 = 0

for bp in bps:
    p1 += bp.id * find_max_geodes(bp, State(), 24)
    find_max_geodes.cache_clear()


p2 = 1

for bp in bps[:3]:
    p2 *= find_max_geodes(bp, State(), 32)
    find_max_geodes.cache_clear()

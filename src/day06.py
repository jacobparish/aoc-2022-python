from aocd import data, submit
import more_itertools as mit
import utils


def find_first_marker(data: str, target_len: int) -> int:
    windows = mit.sliding_window(data, target_len)
    return (
        utils.find_index(windows, lambda chars: len(set(chars)) == target_len)
        + target_len
    )


def part_a() -> int:
    return find_first_marker(data, 4)


def part_b() -> int:
    return find_first_marker(data, 14)


if __name__ == "__main__":
    submit(part_a(), part="a", day=6, year=2022)
    submit(part_b(), part="b", day=6, year=2022)

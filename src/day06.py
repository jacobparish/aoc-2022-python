from aocd import data
import more_itertools as mit


def find_first_marker(data: str, target_len: int) -> int:
    windows = mit.sliding_window(data, target_len)
    return (
        next(i for i, chars in enumerate(windows) if len(set(chars)) == target_len)
        + target_len
    )


p1 = find_first_marker(data, 4)
p2 = find_first_marker(data, 14)

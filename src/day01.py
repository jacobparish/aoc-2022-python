from aocd import lines, submit
import heapq
import utils


def part_a() -> int:
    return max(sum(calories) for calories in utils.split_numbers(lines))


def part_b() -> int:
    return sum(
        heapq.nlargest(3, (sum(calories) for calories in utils.split_numbers(lines)))
    )


if __name__ == "__main__":
    submit(part_a(), part="a", day=1, year=2022)
    submit(part_b(), part="b", day=1, year=2022)

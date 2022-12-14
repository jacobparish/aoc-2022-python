import importlib
import argparse
import sys


class AocdMock:
    def __init__(self, day: int):
        with open(f"data/examples/day{day:02d}/input.txt", "r") as f:
            self.data = f.read()
        self.lines = self.data.splitlines()
        try:
            self.numbers = [int(line) for line in self.lines]
        except ValueError:
            self.numbers = None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    sys.modules["aocd"] = AocdMock(args.day)
    day_module = importlib.import_module(f"day{args.day:02d}")
    print("p1:", day_module.p1)
    print("p2:", day_module.p2)

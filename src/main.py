from aocd import submit
import importlib
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        sys.modules["aocd"] = __import__("mock_B")
        day_module = importlib.import_module(f"day{args.day:02d}")
    else:
        day_module = importlib.import_module(f"day{args.day:02d}")
        submit(day_module.p1, part="a", day=args.day, year=2022)
        submit(day_module.p2, part="b", day=args.day, year=2022)

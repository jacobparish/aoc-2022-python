from aocd import submit
import importlib
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    day_module = importlib.import_module(f"day{args.day:02d}")
    print("p1:", day_module.p1)
    submit(day_module.p1, part="a", day=args.day, year=2022)
    print("p2:", day_module.p2)
    submit(day_module.p2, part="b", day=args.day, year=2022)

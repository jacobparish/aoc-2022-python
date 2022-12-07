from aocd import lines, submit
from parse import parse
from functools import cached_property
from typing import Dict, Iterable, Optional


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"]):
        self.name = name
        self.parent = parent
        self.files: Dict[str, "File"] = {}
        self.dirs: Dict[str, "Directory"] = {}

    def add_file(self, name: str, file: "File"):
        if name not in self.files:
            self.files[name] = file

    def add_dir(self, name: str, dir: "Directory"):
        if name not in self.dirs:
            self.dirs[name] = dir

    @cached_property
    def size(self) -> int:
        return sum(file.size for file in self.files.values()) + sum(
            dir.size for dir in self.dirs.values()
        )

    def calc_sum_below(self, max_size: int) -> int:
        my_contribution = self.size if self.size <= max_size else 0
        child_contributions = sum(
            dir.calc_sum_below(max_size) for dir in self.dirs.values()
        )
        return my_contribution + child_contributions

    def find_delete_target(self, min_size: int) -> int:
        if self.size < min_size:
            return 0
        else:
            best = self.size
            for dir in self.dirs.values():
                curr = dir.find_delete_target(min_size)
                if 0 < curr < best:
                    best = curr
            return best


class File:
    def __init__(self, name: str, size: int, parent: Directory):
        self.name = name
        self.size = size
        self.parent = parent


def parse_file_tree(lines: Iterable[str]) -> Directory:
    root = Directory("/", None)
    cwd = root

    for line in lines:
        if line.startswith("$ "):
            line = line[2:]
            if line.startswith("cd"):
                line = line[3:]
                if line == "..":
                    cwd = cwd.parent
                elif line == "/":
                    cwd = root
                else:
                    cwd = cwd.dirs[line]
        elif line.startswith("dir"):
            name = line[4:]
            cwd.add_dir(name, Directory(name, cwd))
        else:
            size, name = parse("{:d} {}", line)
            cwd.add_file(name, File(name, size, cwd))

    return root


def part_a() -> int:
    root = parse_file_tree(lines)
    return root.calc_sum_below(100000)


def part_b() -> int:
    root = parse_file_tree(lines)
    return root.find_delete_target(root.size - 40000000)


if __name__ == "__main__":
    submit(part_a(), part="a", day=7, year=2022)
    submit(part_b(), part="b", day=7, year=2022)

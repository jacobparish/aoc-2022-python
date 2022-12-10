from aocd import lines
from functools import cached_property
from typing import Dict, Iterable, Optional


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"]):
        self.name = name
        self.parent = parent
        self.files: Dict[str, "File"] = {}
        self.dirs: Dict[str, "Directory"] = {}

    def add_file(self, file: "File"):
        if file.name not in self.files:
            self.files[file.name] = file

    def add_dir(self, dir: "Directory"):
        if dir.name not in self.dirs:
            self.dirs[dir.name] = dir

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
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


def parse_file_tree(lines: Iterable[str]) -> Directory:
    root = Directory("/", None)
    cwd = root

    for line in lines:
        tokens = line.split(" ")
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    cwd = cwd.parent
                elif tokens[2] == "/":
                    cwd = root
                else:
                    cwd = cwd.dirs[tokens[2]]
        elif tokens[0] == "dir":
            name = tokens[1]
            cwd.add_dir(Directory(name, cwd))
        else:
            size = int(tokens[0])
            name = tokens[1]
            cwd.add_file(File(name, size))

    return root


root = parse_file_tree(lines)
p1 = root.calc_sum_below(100000)
p2 = root.find_delete_target(root.size - 40000000)

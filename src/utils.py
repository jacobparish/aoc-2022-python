import more_itertools as mit
from parse import parse
from typing import Callable, Iterable, List, TypeVar


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


T = TypeVar("T")


def find_index(iter: Iterable[T], pred: Callable[[T], bool]) -> int:
    for i, item in enumerate(iter):
        if pred(item):
            return i
    return -1


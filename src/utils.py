import more_itertools as mit
from parse import parse
from typing import Iterable


def split_lines(lines: Iterable[str], separator: str = ""):
    """
    Split list of lines at a separator. Default is to split at empty lines.
    """
    return mit.split_at(lines, lambda l: l == separator)


def split_numbers(lines: Iterable[str], separator: str = ""):
    """
    Split list of lines at a separator and convert to numbers. Default is to split at empty lines.
    """
    return map(
        lambda line_group: list(map(int, line_group)),
        mit.split_at(lines, lambda l: l == separator),
    )


def parse_lines(lines: Iterable[str], format: str):
    """
    Parse lines according to a format string.
    """
    return map(lambda line: parse(format, line), lines)

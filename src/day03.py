from aocd import lines
import more_itertools as mit
import string


alphabet = string.ascii_lowercase + string.ascii_uppercase


def score_line(line: str):
    c1, c2 = mit.divide(2, line)
    item = set(c1).intersection(c2).pop()
    return alphabet.index(item) + 1


def score_line_group(line_group):
    item = set.intersection(*map(set, line_group)).pop()
    return alphabet.index(item) + 1


p1 = sum(map(score_line, lines))
p2 = sum(map(score_line_group, mit.chunked(lines, 3)))

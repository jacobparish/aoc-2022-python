from aocd import lines
import functools
import utils


def compare(l1, l2) -> int:
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        if l1 > l2:
            return 1
        return 0
    elif isinstance(l1, int) and isinstance(l2, list):
        return compare([l1], l2)
    elif isinstance(l1, list) and isinstance(l2, int):
        return compare(l1, [l2])
    else:
        for m1, m2 in zip(l1, l2):
            r = compare(m1, m2)
            if r != 0:
                return r
        if len(l1) < len(l2):
            return -1
        if len(l1) > len(l2):
            return 1
        return 0


p1 = 0
divider1 = [[2]]
divider2 = [[6]]
packets = [divider1, divider2]

for n, (line1, line2) in enumerate(utils.split_lines(lines), start=1):
    l1 = eval(line1)
    l2 = eval(line2)
    if compare(l1, l2) == -1:
        p1 += n
    packets.append(l1)
    packets.append(l2)

packets.sort(key=functools.cmp_to_key(compare))
i1 = packets.index(divider1) + 1
i2 = packets.index(divider2) + 1
p2 = i1 * i2

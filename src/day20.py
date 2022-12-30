from aocd import numbers
from utils import invert_perm


def mix_indices(indices, amounts):
    for i, n in enumerate(amounts):
        ii = indices[i]

        if ii + n <= 0:
            n %= len(indices) - 1
        if ii + n >= len(indices) - 1:
            n = (n + ii) % (len(indices) - 1) - ii

        for j, ij in enumerate(indices):
            if n > 0 and ii < ij <= ii + n:
                indices[j] -= 1
                assert indices[j] >= 0
            elif n < 0 and ii + n <= ij < ii:
                indices[j] += 1
                assert indices[j] < len(indices)

        indices[i] += n
        assert 0 <= indices[i] < len(indices)


def find_coords(result):
    i0 = result.index(0)
    return sum(result[(i0 + 1000 * j) % len(result)] for j in [1, 2, 3])


indices1 = list(range(len(numbers)))
amounts1 = numbers
mix_indices(indices1, amounts1)
p1 = find_coords([amounts1[k] for k in invert_perm(indices1)])

indices2 = list(range(len(numbers)))
amounts2 = [n * 811589153 for n in numbers]
for _ in range(10):
    mix_indices(indices2, amounts2)
p2 = find_coords([amounts2[k] for k in invert_perm(indices2)])

from aocd import data

rocks = [
    {(0, 2), (0, 3), (0, 4), (0, 5)},
    {(2, 3), (1, 2), (1, 3), (1, 4), (0, 3)},
    {(2, 4), (1, 4), (0, 2), (0, 3), (0, 4)},
    {(3, 2), (2, 2), (1, 2), (0, 2)},
    {(1, 2), (1, 3), (0, 2), (0, 3)},
]
grid = set()
n = 0
i = 0
h = 0
flat_states = {}
p1 = 0
p2 = 0

while n < 10**12:
    rock = {(r + h + 4, c) for r, c in rocks[n % 5]}
    n += 1

    while True:
        dc = " >".find(data[i % len(data)])
        i += 1
        if all(0 <= c + dc < 7 and (r, c + dc) not in grid for r, c in rock):
            rock = {(r, c + dc) for r, c in rock}
        if all(r - 1 >= 1 and (r - 1, c) not in grid for r, c in rock):
            rock = {(r - 1, c) for r, c in rock}
        else:
            break

    grid.update(rock)
    h = max(h, *(r for r, _ in rock))

    if n == 2022:
        p1 = h

    if all((h, c) in grid for c in range(7)):
        if (n % 5, i % len(data)) in flat_states:
            nprev, hprev = flat_states[n % 5, i % len(data)]
            cycles = (10**12 - n) // (n - nprev)
            n += (n - nprev) * cycles
            p2 += (h - hprev) * cycles
        else:
            flat_states[n % 5, i % len(data)] = (n, h)

p2 += h

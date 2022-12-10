from aocd import lines
import numpy as np

cycle = 1
x = 1
p1 = 0
crt = np.zeros(40 * 6, dtype=bool)


def do_cycle():
    global cycle, p1
    if cycle % 40 == 20:
        p1 += cycle * x
    if x - 1 <= (cycle - 1) % 40 <= x + 1:
        crt[cycle] = True
    cycle += 1


for line in lines:
    tokens = line.split()
    if tokens[0] == "noop":
        do_cycle()
    elif tokens[0] == "addx":
        do_cycle()
        do_cycle()
        x += int(tokens[1])


for row in crt.reshape((6, 40)):
    print("".join("*" if p else " " for p in row))

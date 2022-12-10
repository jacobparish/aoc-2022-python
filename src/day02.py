from aocd import lines


def calc_score_1(line):
    [abc, xyz] = line.split(" ")
    num1 = "ABC".index(abc)
    num2 = "XYZ".index(xyz)
    return 3 * ((num2 - num1 + 1) % 3) + num2 + 1


def calc_score_2(line):
    [abc, xyz] = line.split(" ")
    num1 = "ABC".index(abc)
    result = "XYZ".index(xyz)
    return 3 * result + (num1 + result - 1) % 3 + 1


p1 = sum(map(calc_score_1, lines))
p2 = sum(map(calc_score_2, lines))

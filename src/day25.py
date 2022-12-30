from aocd import lines


def snafu_to_decimal(s: str):
    n = 0
    for c in s:
        n *= 5
        n += "=-012".index(c) - 2
    return n


def decimal_to_snafu(n: int):
    s = ""
    while n != 0:
        s = "012=-"[n % 5] + s
        n = (n // 5) + (n % 5 > 2)
    return s


p1 = decimal_to_snafu(sum(map(snafu_to_decimal, lines)))

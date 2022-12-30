from aocd import lines
from fractions import Fraction
from utils import parse_lines


monkeys: dict[str, str] = {name: expr for name, expr in parse_lines(lines, "{}: {}")}


def build_expr(name: str, vars=[]) -> str | Fraction | tuple:
    if name in vars:
        return name

    try:
        return Fraction(monkeys[name])
    except ValueError:
        pass

    a, op, b = monkeys[name].split()
    ae = build_expr(a, vars)
    be = build_expr(b, vars)
    if isinstance(ae, Fraction) and isinstance(be, Fraction):
        match op:
            case "*":
                return ae * be
            case "/":
                return ae / be
            case "+":
                return ae + be
            case "-":
                return ae - be
    else:
        return (ae, op, be)


def solve_eqn(lhs: str | tuple, rhs: Fraction):
    if isinstance(lhs, str):
        return rhs

    a, op, b = lhs
    match op:
        case "*":
            if isinstance(a, Fraction):
                return solve_eqn(b, rhs / a)
            elif isinstance(b, Fraction):
                return solve_eqn(a, rhs / b)
        case "/":
            if isinstance(a, Fraction):
                return solve_eqn(b, a / rhs)
            elif isinstance(b, Fraction):
                return solve_eqn(a, rhs * b)
        case "+":
            if isinstance(a, Fraction):
                return solve_eqn(b, rhs - a)
            elif isinstance(b, Fraction):
                return solve_eqn(a, rhs - b)
        case "-":
            if isinstance(a, Fraction):
                return solve_eqn(b, a - rhs)
            elif isinstance(b, Fraction):
                return solve_eqn(a, rhs + b)

    # Turns out this is good enough to solve my input
    raise NotImplementedError("cannot solve: variable is referenced more than once")


root_val = build_expr("root")
assert isinstance(root_val, Fraction)
assert root_val.denominator == 1
p1 = root_val.numerator

lhs_name, _, rhs_name = monkeys["root"].split()
lhs = build_expr(lhs_name, ["humn"])
rhs = build_expr(rhs_name, ["humn"])
assert isinstance(rhs, Fraction)
humn_val = solve_eqn(lhs, rhs)
assert humn_val.denominator == 1
p2 = humn_val.numerator

from aocd import lines
from parse import parse
from dataclasses import dataclass
import math
import heapq
import numexpr
import utils
from typing import Callable, List


@dataclass
class Monkey:
    items: List[int]
    op_str: str
    divisor: int
    true_monkey: int
    false_monkey: int
    num_inspections: int = 0


def parse_monkeys(lines: List[str]) -> List[Monkey]:
    monkeys: List[Monkey] = []
    for line_group in utils.split_lines(lines):
        (items_str,) = parse("Starting items: {}", line_group[1].lstrip())
        items = [int(item_str) for item_str in items_str.split(", ")]
        (op_str,) = parse("Operation: new = {}", line_group[2].lstrip())
        (divisor,) = parse("Test: divisible by {:d}", line_group[3].lstrip())
        (true_monkey,) = parse("If true: throw to monkey {:d}", line_group[4].lstrip())
        (false_monkey,) = parse(
            "If false: throw to monkey {:d}", line_group[5].lstrip()
        )
        monkeys.append(Monkey(items, op_str, divisor, true_monkey, false_monkey))
    return monkeys


def calc_monkey_business(
    monkeys: List[Monkey], nrounds: int, reduce_worry_level: Callable[[int], int]
) -> int:
    for _ in range(nrounds):
        for monkey in monkeys:
            monkey.num_inspections += len(monkey.items)
            for item in monkey.items:
                new_item = numexpr.evaluate(monkey.op_str.replace("old", str(item)))
                new_item = reduce_worry_level(new_item)
                if new_item % monkey.divisor == 0:
                    monkeys[monkey.true_monkey].items.append(new_item)
                else:
                    monkeys[monkey.false_monkey].items.append(new_item)
            monkey.items = []
    x, y = heapq.nlargest(2, (monkey.num_inspections for monkey in monkeys))
    return x * y


monkeys1 = parse_monkeys(lines)
p1 = calc_monkey_business(monkeys1, 20, lambda item: item // 3)


monkeys2 = parse_monkeys(lines)
modulus = math.prod(monkey.divisor for monkey in monkeys2)
p2 = calc_monkey_business(monkeys2, 10000, lambda item: item % modulus)

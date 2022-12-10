from aocd import lines
import heapq
import utils


calorie_totals = [sum(calories) for calories in utils.split_numbers(lines)]
p1 = max(calorie_totals)
p2 = sum(heapq.nlargest(3, calorie_totals))

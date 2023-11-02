from pathlib import Path
from utils import answer

example = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]

def get_input(lines):
    return [[int(num) for num in line.strip()] for line in lines]

assert(get_input(example)[4][4] == 0)

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    my_input = f.readlines()

def part1():
    return 111

answer(part1(get_input(example)), "Example 1", 111)
answer(part1(get_input(my_input)), "Part 1", 111)
answer(part2(get_input(example)), "Example 2", 111)
answer(part2(get_input(my_input)), "Part 2", 111)

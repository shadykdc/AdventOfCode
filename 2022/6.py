from pathlib import Path
from utils import answer
import re

example = [
    "1",
    "2",
    "3",
]

def get_input(lines):
    return [int(line.strip()) for line in lines]

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = get_input(f.readlines())

assert(get_input(example) == [1, 2, 3])

def part1(nums):
    return 1

def part2(nums):
    return 1


answer(part1(get_input(example)), "Example 1")
answer(part1(puzzle_input), "Part 1")
answer(part2(get_input(example)), "Example 2")
answer(part2(puzzle_input), "Part 2")

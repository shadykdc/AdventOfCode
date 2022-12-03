from pathlib import Path
from utils import answer

example = [
    1,
    2,
    3,
]

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = [int(line.strip()) for line in f.readlines()]

def part1(nums):
    return sum(nums)

def part2(nums):
    return sum(nums)


answer(part1(example), "Example 1")
answer(part1(puzzle_input), "Part 1")
answer(part2(example), "Example 1")
answer(part2(puzzle_input), "Part 2")

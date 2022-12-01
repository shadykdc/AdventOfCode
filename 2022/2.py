from pathlib import Path
from utils import answer

example = [
    "hello"
]

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    nums = [int(line.strip()) for line in f.readlines()]

def part1(ins):
    return sum(ins)

def part2(ins):
    return sum(ins)


answer(part1(nums), "Part 1")
answer(part2(nums), "Part 2")

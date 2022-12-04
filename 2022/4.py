from pathlib import Path
from utils import answer
import re

example = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]

def get_input(lines):
    return [[int(d) for d in re.split(',|-', line.strip())] for line in lines]

assert(get_input(["2-4,6-8"]) == [[2, 4, 6, 8]])

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = get_input(f.readlines())

def inside(pair):
    return (pair[0] <= pair[2] and pair[1] >= pair[3]) or (pair[0] >= pair[2] and pair[1] <= pair[3])

def part1(pairs):
    return sum([inside(pair) for pair in pairs])

def overlap(pair):
    return not (pair[1] < pair[2] or pair[3] < pair[0])

def part2(pairs):
    return sum([overlap(pair) for pair in pairs])


answer(part1(get_input(example)), "Example 1", 2)
answer(part1(puzzle_input), "Part 1")
answer(part2(get_input(example)), "Example 2", 4)
answer(part2(puzzle_input), "Part 2")

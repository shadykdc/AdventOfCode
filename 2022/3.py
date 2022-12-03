from pathlib import Path
from utils import answer

example = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

def get_score(ch):
    if ord(ch) >= 97:
        return ord(ch) - 96
    return ord(ch) - 38

assert(get_score('a') == 1)
assert(get_score('z') == 26)
assert(get_score('A') == 27)
assert(get_score('Z') == 52)

def get_input(lines):
    return [[get_score(ch) for ch in line.strip()] for line in lines]

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = get_input(f.readlines())

def part1(nums):
    score = 0
    for items in nums:
        half = int(len(items)/2)
        comp1 = set(items[:half])
        comp2 = set(items[half:])
        score += sum(comp1.intersection(comp2))
    return score

def part2(nums):
    score = 0
    for i, _ in enumerate(nums):
        if i % 3 == 0:
            comp1 = set(nums[i])
            comp2 = set(nums[i + 1])
            comp3 = set(nums[i + 2])
            score += sum(comp1.intersection(comp2).intersection(comp3))
    return score

answer(part1(get_input(example)), "Example 1", 157)
answer(part1(puzzle_input), "Part 1", 7826)
answer(part2(get_input(example)), "Example 2", 70)
answer(part2(puzzle_input), "Part 2", 2577)

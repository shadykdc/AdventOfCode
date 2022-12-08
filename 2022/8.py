from pathlib import Path
from utils import answer
import re
from functools import lru_cache
import math

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

def part1(nums):
    count = [ [False for _ in range(len(nums[0]))] for _ in range(len(nums)) ]
    for r, row in enumerate(nums):
        biggest = -1
        # left to right
        for c, num in enumerate(row):
            if num > biggest:
                count[r][c] = True
                biggest = num
        biggest = -1
        # right to left
        for c, num in reversed(list(enumerate(row))):
            if num > biggest:
                count[r][c] = True
                biggest = num
    for c in range(len(nums[0])):
        biggest = -1
        # bottom to top
        for r in reversed(range(len(nums))):
            if nums[r][c] > biggest:
                count[r][c] = True
                biggest = nums[r][c]
        biggest = -1
        # top to bottom
        for r in range(len(nums)):
            if nums[r][c] > biggest:
                count[r][c] = True
                biggest = nums[r][c]
    return sum([sum(row) for row in count])


answer(part1(get_input(example)), "Example 1", 21)
answer(part1(get_input(my_input)), "Part 1", 1546)


def get_dists(row, col, nums):
    dists = [ 0, 0, 0, 0]
    # up
    for r in range(row-1, -1, -1):
        dists[0] += 1
        if nums[row][col] <= nums[r][col]:
            break
    # down
    for r in range(row+1, len(nums)):
        dists[1] += 1
        if nums[row][col] <= nums[r][col]:
            break
    # left
    for c in range(col-1, -1, -1):
        dists[2] += 1
        if nums[row][col] <= nums[row][c]:
            break
    # right
    for c in range(col+1, len(nums[0])):
        dists[3] += 1
        if nums[row][col] <= nums[row][c]:
            break
    return dists

def part2(nums):
    scores = [ [
        math.prod(get_dists(r, c, nums)) for c, num in enumerate(row)
    ] for r, row in enumerate(nums)]
    return max([max(row) for row in scores])

answer(part2(get_input(example)), "Example 2", 8)
answer(part2(get_input(my_input)), "Part 2", 519064)

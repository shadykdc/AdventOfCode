from typing import List

# Advent of Code 2017 Day 2

with open('input2.txt') as f:
    rows = f.readlines()
spreadsheet = [[int(num.strip()) for num in row.split("\t")] for row in rows]

# Part 1

example1 = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8],
]

def part_one(spreadsheet: List[List[int]]) -> int:
    total: int = 0
    for row in spreadsheet:
        total += max(row) - min(row)
    return total

assert(part_one(example1) == 18)
print(part_one(spreadsheet))

# Part 2

example2 = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5],
]

def evenly_divides(row: List[int]) -> int:
    row.sort()
    for idx1 in range(len(row)):
        for idx2 in range(idx1 + 1, len(row)):
            if row[idx2] % row[idx1] == 0:
                return int(row[idx2] / row[idx1])
    raise RuntimeError("Failed to find two numbers that evenly divide.")

def part_two(spreadsheet: List[List[int]]) -> int:
    total: int = 0
    for row in spreadsheet:
        total += evenly_divides(row)
    return total

assert(part_two(example2) == 9)
print(part_two(spreadsheet))

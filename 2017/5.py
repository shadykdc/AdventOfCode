from typing import List

with open('input5.txt', 'r') as f:
    instructions = [int(num) for num in f.readlines()]

def part_one(instrs: List[int]) -> int:
    i = 0
    count = 0
    while i < len(instrs):
        count += 1
        instrs[i] += 1
        i += instrs[i]-1

    return count

assert(part_one([0, 3, 0, 1, -3]) == 5)
print(f"Part 1: {part_one(instructions)}")

with open('input5.txt', 'r') as f:
    instructions = [int(num) for num in f.readlines()]

def part_two(instrs: List[int]) -> int:
    i = 0
    count = 0
    while i < len(instrs):
        count += 1
        offset = 1 if instrs[i] < 3 else -1
        instrs[i] += offset
        i += instrs[i] - offset

    return count

assert(part_two([0, 3, 0, 1, -3]) == 10)
print(f"Part 2: {part_two(instructions)}")

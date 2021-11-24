# Advent of Code 2017 Day 1 https://adventofcode.com/2017/day/3

with open('input1.txt') as f:
    digits: str = f.readline().strip()

# Part 1

def part_one(digits: str) -> int:
    end: int = len(digits) - 1
    total: int = 0
    for idx in range(end):
        if digits[idx] == digits[idx+1]:
            total += int(digits[idx])
    if digits[end] == digits[0] and end > 0:
        total += int(digits[0])
    return total

assert(part_one("1122") == 3)
assert(part_one("1111") == 4)
assert(part_one("1234") == 0)
assert(part_one("91212129") == 9)

print(f"Part 1: {part_one(digits)}")

# Part 2

def part_two(digits: str) -> int:
    half = int(len(digits) / 2)
    total: int = 0
    for idx in range(half):
        if digits[idx] == digits[idx + half]:
            total += int(digits[idx])
    return total * 2

assert(part_two("1212") == 6)
assert(part_two("1221") == 0)
assert(part_two("123425") == 4)
assert(part_two("123123") == 12)
assert(part_two("12131415") == 4)

print(f"Part 2: {part_two(digits)}")

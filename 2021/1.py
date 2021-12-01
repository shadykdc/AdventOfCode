from typing import List

example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open('input1.txt', 'r') as f:
    nums = [int(line.strip()) for line in f.readlines()]

def part_one(nums: List[int]) -> int:
    return len([idx for idx in range(1, len(nums)) if nums[idx] > nums[idx-1]])

assert(part_one(example) == 7)
print(f"Part One: {part_one(nums)}")

def part_two(nums: List[int]) -> int:
    return len([idx for idx in range(3, len(nums)) if nums[idx] > nums[idx-3]])

assert(part_two(example) == 5)
print(f"Part Two: {part_two(nums)}")

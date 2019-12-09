# Advent of Code Day 10

# Parse Input
with open('input10.txt') as f:
    lines = f.readlines()

nums = [int(string) for string in lines[0].strip().split(',')]
print(nums)
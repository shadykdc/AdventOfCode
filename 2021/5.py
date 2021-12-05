import re
from collections import defaultdict

with open('input5.txt', 'r') as f:
    lines = f.readlines()
    coords = [[int(num) for num in re.findall(r'\d+', line.strip())] for line in lines]

example = [
    [0, 9, 5, 9],
    [8, 0, 0, 8],
    [9, 4, 3, 4],
    [2, 2, 2, 1],
    [7, 0, 7, 4],
    [6, 4, 2, 0],
    [0, 9, 2, 9],
    [3, 4, 1, 4],
    [0, 0, 8, 8],
    [5, 5, 8, 2],
]

def part_one(coords):
    x_dim = max([max(x1, x2) for x1, y1, x2, y2 in coords]) + 1
    y_dim = max([max(y1, y2) for x1, y1, x2, y2 in coords]) + 1
    vents = defaultdict(lambda: 0)
    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            for y in range(abs(y2-y1)+1):
                vents[(x1, min(y1, y2)+y)] += 1
        elif y1 == y2:
            for x in range(abs(x2-x1)+1):
                vents[(min(x1, x2)+x, y1)] += 1
    return sum([1 for coord in vents if vents[coord] > 1])

assert(part_one(example) == 5)
print(f"Part 1: {part_one(coords)}")
assert(part_one(coords) == 6461)

def part_two(coords):
    x_dim = max([max(x1, x2) for x1, y1, x2, y2 in coords]) + 1
    y_dim = max([max(y1, y2) for x1, y1, x2, y2 in coords]) + 1
    vents = defaultdict(lambda: 0)
    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            for y in range(abs(y2-y1)+1):
                vents[(x1, min(y1, y2)+y)] += 1
        elif y1 == y2:
            for x in range(abs(x2-x1)+1):
                vents[(min(x1, x2)+x, y1)] += 1
        elif abs(x1-x2) == abs(y1-y2): # we can assume this but checking anyhow
            if (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
                for i in range(abs(x2-x1) + 1):
                    vents[(min(x1, x2) + i, min(y2, y1) + i)] += 1
            elif (x1 < x2 and y1 > y2) or (x2 < x1 and y2 > y1):
                for i in range(abs(x2-x1) + 1):
                    vents[(min(x1, x2) + i, max(y2, y1) - i)] += 1
    return sum([1 for coord in vents if vents[coord] > 1])

assert(part_two(example) == 12)
print(f"Part 2: {part_two(coords)}")
assert(part_two(coords) == 18065)

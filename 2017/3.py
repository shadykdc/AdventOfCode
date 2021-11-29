# Advent of Code 2017 Day 3

"""
    https://adventofcode.com/2017/day/3
    37  36  35  34  33  32  31  56
    38  17  16  15  14  13  30  55
    39  18   5   4   3  12  29  54
    40  19   6   1   2  11  28  53
    41  20   7   8   9  10  27  52
    42  21  22  23  24  25  26  51
    43  44  45  46  47  48  49  50
                                81

"""

num = 265149

# Part 1

def part_one(num: int) -> int:
    if num == 1:
        return 0
    size: int = 1
    while pow(size, 2) < num:
        size = size + 2
    ring = int((size + 1)/2) - 1
    low = pow(size - 2, 2) + 1
    high = pow(size, 2)

    x, y = ring, -ring
    current = high
    # traverse left
    while current > num and x > -ring:
        current = current - 1
        x = x - 1
    # traverse up
    while current > num and y < ring:
        current = current - 1
        y = y + 1
    # traverse right
    while current > num and x < ring:
        current = current - 1
        x = x + 1
    # traverse down
    while current > num and y > -ring:
        current = current - 1
        y = y - 1
    return abs(x) + abs(y)


assert(part_one(1) == 0)
assert(part_one(12) == 3)
assert(part_one(23) == 2)
assert(part_one(1024) == 31)

print(f"Part 1: {part_one(num)}")

# Part 2

"""
    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...

    What is the first value written that is larger than your puzzle input?
"""

from typing import Dict, Tuple


def sum_neighbors(x: int, y: int, graph: Dict[Tuple[int, int], int]) -> int:
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            coord = (x+i, y+j)
            if coord in graph:
                total += graph[coord]
    return total

def part_two(num: int) -> int:
    graph: Dict[Tuple[int, int], int] = {}
    edge = 1
    x, y = 0, 0
    graph[(x, y)] = 1

    while True:
        if graph[(x, y)] > num:
            return graph[(x, y)]

        while abs(x) < abs(edge) or -x == edge:
            x = x + 1 if edge > 0 else x - 1
            graph[(x, y)] = sum_neighbors(x, y, graph)
            if graph[(x, y)] > num:
                return graph[(x, y)]

        while abs(y) < abs(edge) or -y == edge:
            y = y + 1 if edge > 0 else y - 1
            graph[(x, y)] = sum_neighbors(x, y, graph)
            if graph[(x, y)] > num:
                return graph[(x, y)]

        edge *= -1
        edge += 1 if edge > 0 else 0

    return graph[(x, y)]

assert(part_two(747) == 806)
print(f"Part 2: {part_two(num)}")

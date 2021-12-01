from typing import List, Tuple, Set

with open('input1.txt') as f:
    directions: List[str] = [
        direction.strip()
        for direction
        in f.readline().split(",")
    ]

def part_one(directions: List[Tuple[str, int]]) -> int:
    directions = [(direc[0], int(direc[1:])) for direc in directions]
    dirs = ["n", "e", "s", "w"]
    idx, x, y = 0, 0, 0
    for lr, dist in directions:
        if lr == 'L':
            idx = idx - 1 if idx > 0 else len(dirs) - 1
        else: # lr == 'R
            idx = idx + 1 if idx < len(dirs) - 1 else 0
        if dirs[idx] == "n":
            y += dist
        if dirs[idx] == "e":
            x += dist
        if dirs[idx] == "s":
            y -= dist
        if dirs[idx] == "w":
            x -= dist
    return abs(x) + abs(y)

assert(part_one(["R2", "L3"]) == 5)
assert(part_one(["R2", "R2", "R2"]) == 2)
assert(part_one(["R5", "L5", "R5", "R3"]) == 12)
print(f"Part 1: {part_one(directions)}")
assert(part_one(directions) == 146)

def part_two(directions: List[Tuple[str, int]]) -> int:
    directions = [(direc[0], int(direc[1:])) for direc in directions]
    dirs = ["n", "e", "s", "w"]
    idx, x, y = 0, 0, 0
    seen: Set[Tuple[int, int]] = set((0, 0))
    for lr, dist in directions:
        if lr == 'L':
            idx = idx - 1 if idx > 0 else len(dirs) - 1
        else: # lr == 'R
            idx = idx + 1 if idx < len(dirs) - 1 else 0
        while dist > 0:
            dist -= 1
            if dirs[idx] == "n":
                    y += 1
            if dirs[idx] == "e":
                    x += 1
            if dirs[idx] == "s":
                    y -= 1
            if dirs[idx] == "w":
                    x -= 1
            if (x, y) in seen:
                return abs(x) + abs(y)
            seen.add((x, y))
    return 0

assert(part_two(["R8", "R4", "R4", "R8"]) == 4)
print(f"Part 2: {part_two(directions)}")
assert(part_two(directions) == 131)

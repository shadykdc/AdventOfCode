import queue
from functools import reduce
from operator import mul

coords = dict()
example = dict()

with open('input9.txt', 'r') as f:
    lines = [[int(ch) for ch in line.strip()] for line in f.readlines()]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            coords[(x,y)] = lines[y][x]

with open('input9.1.txt', 'r') as f:
    lines = [[int(ch) for ch in line.strip()] for line in f.readlines()]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            example[(x,y)] = lines[y][x]

def low_point(x, y, coords):
    for i in [-1, 1]:
        for neighbor in [(x+i, y), (x, y+i)]:
            if neighbor in coords and coords[neighbor] <= coords[(x, y)]:
                return False
    return True

def part_one(coords):
    low_points = [coords[(x,y)] for (x, y) in coords.keys() if low_point(x, y, coords)]
    return sum(low_points) + len(low_points)

assert(part_one(example) == 15)
print(f"Part 1: {part_one(coords)}")
assert(part_one(coords) == 462)

def get_basin_size(coords, x, y):
    # get bfs area where boundaries are 9s or edges
    q = queue.Queue()
    q.put((x, y))
    seen = set()
    while not q.empty():
        i, j = q.get()
        seen.add((i, j))
        for off in [-1, 1]:
            for neighbor in [(i+off, j), (i, j+off)]:
                if neighbor in coords and coords[neighbor] != 9 and neighbor not in seen:
                    q.put(neighbor)
    return len(seen)

def part_two(coords):
    low_points = [(x, y) for (x, y) in coords.keys() if low_point(x, y, coords)]
    basin_sizes = [get_basin_size(coords, x, y) for (x, y) in low_points]
    three_biggest = sorted(basin_sizes)[-3:]
    return reduce(mul, three_biggest)

assert(part_two(example) == 1134)
print(f"Part 2: {part_two(coords)}")
assert(part_two(coords) == 1397760)

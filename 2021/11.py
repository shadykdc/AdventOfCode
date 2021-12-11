with open('input11.txt', 'r') as f:
    grid = [[int(ch) for ch in line.strip()] for line in f.readlines()]

with open('input11.1.txt', 'r') as f:
    example = [[int(ch) for ch in line.strip()] for line in f.readlines()]

def one_step(grid, part_two = False):
    new_grid = [[num + 1 for num in row] for row in grid]
    flash_spots = [(j, i) for i, row in enumerate(new_grid) for j, _ in enumerate(row) if new_grid[j][i] > 9]
    seen = set(flash_spots)
    count = 0
    while len(flash_spots):
        j, i = flash_spots.pop()
        count += 1
        for off1 in [-1, 0, 1]:
            for off2 in [-1, 0, 1]:
                y, x = j+off2, i+off1
                if (off1 == 0 and off2 == 0) or y not in range(len(new_grid)) or x not in range(len(new_grid[0])):
                    continue
                new_grid[y][x] += 1
                if (y, x) not in seen and new_grid[y][x] > 9:
                    flash_spots.append((y, x))
                    seen.add((y, x))
    if part_two and len(seen) == len(new_grid) * len(new_grid[0]):
        return True, new_grid
    while len(seen):
        j, i = seen.pop()
        new_grid[j][i] = 0
    if part_two:
        return False, new_grid
    return count, new_grid

def part_one(grid, steps):
    new_grid = [[num for num in row] for row in grid]
    total = 0
    for _ in range(steps):
        count, new_grid = one_step(new_grid)
        total += count
    return total

def part_two(grid):
    new_grid = [[num for num in row] for row in grid]
    step, found = 0, False
    while not found:
        found, new_grid = one_step(new_grid, True)
        step += 1
    return step

assert(part_one(example, 10) == 204)
assert(part_one(example, 100) == 1656)
print(f"Part One: {part_one(grid, 100)}")
assert(part_one(grid, 100) == 1747)

assert(part_two(example) == 195)
print(f"Part Two: {part_two(grid)}")
assert(part_two(grid) == 505)

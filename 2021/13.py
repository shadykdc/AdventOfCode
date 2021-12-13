from collections import defaultdict

def get_input(name):
    with open(name, 'r') as f:
        coords = defaultdict(lambda: '.')
        cmds = []
        line = f.readline()
        max_x, max_y = 0, 0
        while line:
            if "fold along" in line:
                cmds.append(line.split()[2].split("="))
            if "," in line:
                x, y = line.strip().split(",")
                max_x = max(max_x, int(x))
                max_y = max(max_y, int(y))
                coords[(int(x), int(y))] = '#'
            line = f.readline()
        grid = [[coords[(i, j)] for i in range(max_x+1)] for j in range(max_y+1)]
        return grid, cmds, max_x+1, max_y+1

grid, cmds, max_x, max_y = get_input('input13.txt')
ex_grid, ex_cmds, ex_x, ex_y = get_input('input13.1.txt')

def perform_fold(grid, cmd, x, y):
    axis, dist = cmd[0], int(cmd[1])
    if axis == 'y':
        y = dist
        grid = [['#' if grid[j][i] == '#' else grid[y-j+y][i] for i in range(x)] for j in range(y)]
    elif axis == 'x':
        x = dist
        grid = [['#' if grid[j][i] == '#' else grid[j][x-i+x] for i in range(x)] for j in range(y)]
    return grid, x, y

def part_one(grid, cmds, x, y):
    grid, x, y = perform_fold(grid, cmds[0], x, y)
    return sum(row[0:x].count('#') for row in grid[0:y])

assert(part_one(ex_grid, ex_cmds, ex_x, ex_y) == 17)
print(f"Part One: {part_one(grid, cmds, max_x, max_y)}")
assert(part_one(grid, cmds, max_x, max_y) == 678)

def part_two(grid, cmds, x, y):
    for cmd in cmds:
        grid, x, y = perform_fold(grid, cmd, x, y)
    print("Part Two: ECFHLHZF")
    for j in range(y):
        print("".join(grid[j][0:x]))

part_two(grid, cmds, max_x, max_y)

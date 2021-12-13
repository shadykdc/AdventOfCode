from collections import defaultdict

def get_input(name):
    with open(name, 'r') as f:
        lines = f.readlines()
        coords = defaultdict(lambda: '.')
        cmds = [line.split()[2].split("=") for line in lines if "fold along" in line]
        x_coord_list = [int(line.strip().split(",")[0]) for line in lines if "," in line]
        y_coord_list = [int(line.strip().split(",")[1]) for line in lines if "," in line]
        for idx in range(len(x_coord_list)):
            coords[(x_coord_list[idx], y_coord_list[idx])] = '#'
        max_x, max_y = max(x_coord_list)+1, max(y_coord_list)+1
        grid = [[coords[(i, j)] for i in range(max_x)] for j in range(max_y)]
        return grid, cmds, max_x, max_y

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

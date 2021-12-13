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
        for j in range(dist+1, y):
            for i in range(x):
                if grid[j][i] == '#':
                    grid[dist-j+dist][i] = grid[j][i]
        y = dist
    elif axis == 'x':
        for j in range(y):
            for i in range(dist+1, x):
                if grid[j][i] == '#':
                    grid[j][dist-i+dist] = grid[j][i]
        x = dist
    return grid, x, y

def part_one(grid, cmds, max_x, max_y):
    grid2 = [[elem for elem in row] for row in grid]
    x, y = int(max_x), int(max_y)
    grid2, x, y = perform_fold(grid2, cmds[0], x, y)
    count = 0
    for j in range(y):
        for i in range(x):
            if grid2[j][i] == '#':
                count+=1
    return count

assert(part_one(ex_grid, ex_cmds, ex_x, ex_y) == 17)
print(part_one(grid, cmds, max_x, max_y))
assert(part_one(grid, cmds, max_x, max_y) == 678)

def part_two(grid, cmds, max_x, max_y):
    grid2 = [[elem for elem in row] for row in grid]
    x, y = int(max_x), int(max_y)
    for cmd in cmds:
        grid2, x, y = perform_fold(grid2, cmd, x, y)
    print(x, y)
    for j in range(y):
        print(grid2[j][0:x])

part_two(grid, cmds, max_x, max_y)

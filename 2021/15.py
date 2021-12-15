import queue

def get_input(name):
    with open(name, 'r') as f:
        return [[int(num) for num in line.strip()] for line in f.readlines()]

grid = get_input('input15.txt')

example = get_input('input15.1.txt')

def bfs(grid):
    q = queue.Queue()
    q.put((0, 0))
    risk = {(0,0): 0}
    while not q.empty():
        i, j = q.get()
        for off in [-1, 1]:
            for x, y in [(i+off, j), (i, j+off)]:
                if (y in range(len(grid)) and
                    x in range(len(grid[0])) and
                    ((x, y) not in risk or risk[(x, y)] > risk[(i,j)] + grid[y][x])):
                        risk[(x, y)] = risk[(i,j)] + grid[y][x]
                        q.put((x, y))
    return risk[(len(grid[0])-1, len(grid)-1)]

def part_one(grid):
    return bfs(grid)

assert(part_one(example) == 40)
print(f"Part One: {part_one(grid)}")

def part_two(grid):
    width = len(grid[0])
    height = len(grid)
    new_grid = [[(grid[j][i] + w) % 9 or 9 for w in range(5) for i in range(width)] for j in range(height)]
    for j in range(height):
        for h in range(1, 5):
            new_grid.append([(new_grid[j][i] + h) % 9 or 9 for i in range(len(new_grid[0]))])
    for row in new_grid:
        print("".join([str(num) for num in row]))
    print(bfs(new_grid))

assert(part_two(example) == 315)
print(part_two(grid))

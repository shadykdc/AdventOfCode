import copy
with open('input8.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

screen = [["." for _ in range(50)] for _ in range(6)]

example_screen = [["." for _ in range(7)] for _ in range(3)]
example = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=0 by 4",
    "rotate column x=1 by 1",
]

def process(line, screen):
    cmd = line.split()[0]
    new_screen = copy.deepcopy(screen)
    if cmd == "rect":
        dim = line.split()[1].split('x')
        a, b = int(dim[0]), int(dim[1])
        for i in range(a):
            for j in range(b):
                new_screen[j][i] = '#'
    elif cmd == "rotate":
        cmd, colrow, eq, _, by = line.split()
        idx = int(eq.split("=")[1])
        dist = int(by)
        if colrow == "column":
            for j in range(len(screen)):
                new_screen[(j+dist)%len(new_screen)][idx] = screen[j][idx]
        if colrow == "row":
            for i in range(len(screen[0])):
                new_screen[idx][(i+dist)%len(new_screen[0])] = screen[idx][i]
    return new_screen

def part_one(lines, screen) -> int:
    for line in lines:
        screen = process(line, screen)
    for row in screen:
        print(row)
    return sum([sum([ch == '#' for ch in row]) for row in screen])

assert(part_one(example, example_screen) == 6)
print(f"Part One: {part_one(lines, screen)}")

""" Part 2
    ['#' '#' '#' '#' '.' '.' '.' '#' '#' '.' '#' '.' '.' '#' '.' '#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '.' '#' '#' '.' '.' '#' '#' '#' '.' '.' '#' '.' '.' '.' '.' '#' '.' '.' '.' '#' '.' '.' '#' '#' '.']
    ['.' '.' '.' '#' '.' '.' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '.' '#' '.' '.' '.' '#' '.']
    ['.' '.' '#' '.' '.' '.' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '.' '.' '#' '.' '#' '#' '.' '.' '.' '#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.']
    ['.' '#' '.' '.' '.' '.' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '#' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '.' '.' '#' '#' '#' '.' '.' '#' '.' '.' '.' '.' '.' '.' '#' '.' '.' '.' '.' '.' '#' '.']
    ['#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '.' '.' '.' '.' '#' '.' '.' '#' '.' '.' '#' '.']
    ['#' '#' '#' '#' '.' '.' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '#' '.' '.' '#' '.' '.' '.' '.' '#' '#' '#' '#' '.' '.' '.' '#' '.' '.' '.' '#' '#' '.' '.']
"""

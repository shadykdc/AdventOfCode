with open('input25.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

example = [
    "v...>>.vv>",
    ".vv>>.vv..",
    ">>.>v>...v",
    ">>v>>.>.v.",
    "v>v.vv.v..",
    ">.>>..v...",
    ".vv..>.>v.",
    "v.v..>>v.v",
    "....v..v.>",
]

def move_south(lines):
    out = False
    new_lines = [[ch for ch in line] for line in lines]
    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch == 'v' and lines[(r+1)%len(lines)][c] == '.':
                new_lines[r][c] = '.'
                new_lines[(r+1)%len(lines)][c] = 'v'
                out = True
    return out, new_lines

def move_east(lines):
    out = False
    new_lines = [[ch for ch in line] for line in lines]
    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch == '>' and lines[r][(c+1)%len(row)] == '.':
                new_lines[r][c] = '.'
                new_lines[r][(c+1)%len(row)] = '>'
                out = True
    return out, new_lines

def printl(lines):
    for line in lines:
        print("".join(line))
    print(" ")

def move(lines):
    out1, new_lines = move_east(lines)
    out2, new_lines = move_south(new_lines)
    return out1 or out2, new_lines

def part_one(lines):
    new_lines = [[ch for ch in row] for row in lines]
    count, out = 0, True
    while out:
        out, new_lines = move(new_lines)
        count+=1
    return count

assert(part_one(example) == 58)
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == 305)

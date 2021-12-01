with open('input2.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

example = [
    "ULL",
    "RRDDD",
    "LURDL",
    "UUUUD",
]


PAD1 = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

PAD2 = [
    ["",  "",  "1", "",  ""],
    ["",  "2", "3", "4", ""],
    ["5", "6", "7", "8", "9"],
    ["",  "A", "B", "C", ""],
    ["",  "",  "D", "",  ""],
]

def solution(lines, x, y, pad):
    code = ""
    for line in lines:
        for move in line:
            if move == 'U' and y > 0 and pad[y-1][x]:
                y -= 1
            if move == 'D' and y + 1 < len(pad) and pad[y+1][x]:
                y += 1
            if move == 'R' and x + 1 < len(pad[0]) and pad[y][x+1]:
                x += 1
            if move == 'L' and x > 0 and pad[y][x-1]:
                x -= 1
        code += pad[y][x]
    return code

assert(solution(example, 1, 1, PAD1) == "1985")
print(f"Part 1: {solution(lines, 1, 1, PAD1)}")
assert(solution(lines, 1, 1, PAD1) == "65556")

assert(solution(example, 0, 2, PAD2) == "5DB3")
print(f"Part 2: {solution(lines, 0, 2, PAD2)}")
assert(solution(lines, 0, 2, PAD2) == "CB779")

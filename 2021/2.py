with open('input2.txt', 'r') as f:
    lines = [[line.strip().split()[0], int(line.strip().split()[1])] for line in f.readlines()]

example = [
    ["forward", 5],
    ["down", 5],
    ["forward", 8],
    ["up", 3],
    ["down", 8],
    ["forward", 2],
]

def part_one(lines):
    depth, horiz = 0, 0
    for move, dist in lines:
        if move == "forward":
            horiz += dist
        if move == "up":
            depth -= dist
        if move == "down":
            depth += dist
    return depth * horiz

assert(part_one(example) == 150)
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == 1690020)


def part_two(lines):
    depth, horiz, aim = 0, 0, 0
    for move, dist in lines:
        if move == "forward":
            horiz += dist
            depth += aim * dist
        if move == "up":
            aim -= dist
        if move == "down":
            aim += dist
    return depth * horiz

assert(part_two(example) == 900)
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == 1408487760)

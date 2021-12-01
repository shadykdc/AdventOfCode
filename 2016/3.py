with open('input3.txt', 'r') as f:
    lines = [[int(num) for num in line.strip().split()] for line in f.readlines()]

example = [[5, 10, 25]]

def part_one(rows):
    return len([row for row in rows if sum(row) - 2 * max(row) > 0])

assert(part_one(example) == 0)
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == 869)

example2 = [
    [101, 301, 501],
    [102, 302, 502],
    [103, 303, 503],
    [201, 401, 601],
    [202, 402, 602],
    [203, 403, 603],
]
SIDES = 3

def part_two(rows):
    count = 0
    for r in [r*3 for r in range(int(len(rows)/SIDES))]:
        for c in range(len(rows[0])):
            sides = [rows[r+s][c] for s in range(SIDES)]
            if sum(sides) - max(sides) * 2 > 0:
                count += 1
    return count

assert(part_two(example2) == 6)
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == 1544)

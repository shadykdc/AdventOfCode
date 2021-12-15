def get_input(name):
    with open(name, 'r') as f:
        return [line.strip() for line in f.readlines()]

lines = get_input('input16.txt')
example = get_input('input16.1.txt')

def part_one(lines):
    return 0

assert(part_one(example) == 0)
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == 0)


def part_two(lines):
    return 0

assert(part_two(example) == 0)
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == 0)

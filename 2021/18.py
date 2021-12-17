def get_input(name):
    with open(name, 'r') as f:
        return [[int(num) for num in line.strip()] for line in f.readlines()]

my_input = get_input('input18.txt')
example = get_input('input18.1.txt')

def part_one(my_input):
    return 0

assert(part_one(example) == 0)
print(f"Part 1: {part_one(my_input)}")
assert(part_one(my_input) == 0)

def part_two(my_input):
    return 0

assert(part_two(example) == 0)
print(f"Part 2: {part_two(my_input)}")
assert(part_two(my_input) == 0)

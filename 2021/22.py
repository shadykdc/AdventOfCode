def get_input(name):
    with open(name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return lines

my_input = get_input('input22.txt')
example = get_input('input22.1.txt')

def part_one(something):
    return 0

assert(part_one(example) == 0)
print(f"Part One: {part_one(my_input)}")

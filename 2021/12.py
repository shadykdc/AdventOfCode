from collections import defaultdict

def get_input(f):
    caves = defaultdict(list)
    for line in f.readlines():
        cave1, cave2 = line.strip().split("-")
        caves[cave1].append(cave2)
        caves[cave2].append(cave1)
    return caves

with open('input12.txt', 'r') as f:
    caves = get_input(f)

with open('input12.1.txt', 'r') as f:
    example1 = get_input(f)

with open('input12.2.txt', 'r') as f:
    example2 = get_input(f)

with open('input12.3.txt', 'r') as f:
    example3 = get_input(f)

START = 'start'
END = 'end'

def traverse(caves, path, paths):
    cave = path[-1]
    if cave == END:
        paths.add("".join(path))
        return
    for child in caves[cave]:
        if not child.lower() == child or child not in path:
            traverse(caves, path + [child], paths)

def part_one(caves):
    paths = set()
    traverse(caves, [START], paths)
    return len(paths)

assert(part_one(example1) == 10)
assert(part_one(example2) == 19)
assert(part_one(example3) == 226)
print(f"Part One: {part_one(caves)}")
assert(part_one(caves) == 3856)

def traverse2(caves, path, paths, found):
    cave = path[-1]
    if cave == END:
        paths.add("-".join(path))
        return
    for child in caves[cave]:
        if child not in path or child.lower() != child:
            traverse2(caves, path + [child], paths, found)
        elif child != START and path.count(child) < 2 and not found:
            traverse2(caves, path + [child], paths, True)

def part_two(caves):
    paths = set()
    found = False
    traverse2(caves, [START], paths, found)
    return len(paths)

print(part_two(example1))
assert(part_two(example1) == 36)
assert(part_two(example2) == 103)
assert(part_two(example3) == 3509)
print(f"Part Two: {part_two(caves)}")
assert(part_two(caves) == 116692)

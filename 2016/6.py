from collections import defaultdict

with open('input6.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

example = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar",
]

def part_one(lines):
    output = ["_"] * len(lines[0])
    for idx in range(len(lines[0])):
        count = defaultdict(lambda: 0)
        for line in lines:
            count[line[idx]] += 1
        output[idx] = max(count, key=count.get)
    return "".join(output)

assert(part_one(example) == "easter")
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == "asvcbhvg")

def part_two(lines):
    output = ["_"] * len(lines[0])
    for idx in range(len(lines[0])):
        count = defaultdict(lambda: 0)
        for line in lines:
            count[line[idx]] += 1
        output[idx] = min(count, key=count.get)
    return "".join(output)

assert(part_two(example) == "advent")
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == "odqnikqv")

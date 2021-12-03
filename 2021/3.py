import copy

with open('input3.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

example = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

def part_one(lines):
    gamma = ["_"] * len(lines[0])
    epsilon = ["_"] * len(lines[0])
    for idx in range(len(lines[0])):
        total = sum([int(line[idx]) for line in lines])
        count = {'0': len(lines) - total, '1': total}
        gamma[idx] = max(count, key=count.get)
        epsilon[idx] = min(count, key=count.get)
    return int("".join(gamma), 2) * int("".join(epsilon), 2)

assert(part_one(example) == 198)
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == 1082324)

def part_two(lines):
    oxy_lines, co2_lines = get_lines(lines, '1'), get_lines(lines, '0')
    return int("".join(oxy_lines[0]), 2) * int("".join(co2_lines[0]), 2)

def get_lines(lines, default):
    out_lines = copy.copy(lines)
    for idx in range(len(lines[0])):
        if len(out_lines) == 1:
            return out_lines
        total = sum([int(line[idx]) for line in out_lines])
        count = {'0': len(out_lines) - total, '1': total}
        max_key = max(count, key=count.get)
        min_key = min(count, key=count.get)
        keep = default if max_key == min_key else (min_key if default == '0' else max_key)
        out_lines = [l for l in out_lines if l[idx] == keep]
    return out_lines

assert(part_two(example) == 230)
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == 1353024)

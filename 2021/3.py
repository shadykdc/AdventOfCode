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
    oxy_lines, co2_lines = copy.copy(lines), copy.copy(lines)
    for idx in range(len(lines[0])):
        oxy_total = sum([int(line[idx]) for line in oxy_lines])
        co2_total = sum([int(line[idx]) for line in co2_lines])
        oxy_count = {'0': len(oxy_lines) - oxy_total, '1': oxy_total}
        co2_count = {'0': len(co2_lines) - co2_total, '1': co2_total}
        oxy_keep = '1' if max(oxy_count, key=oxy_count.get) == min(oxy_count, key=oxy_count.get) else max(oxy_count, key=oxy_count.get)
        co2_keep = '0' if max(co2_count, key=co2_count.get) == min(co2_count, key=co2_count.get) else min(co2_count, key=co2_count.get)
        if len(oxy_lines) > 1:
            oxy_lines = [l for l in oxy_lines if l[idx] == oxy_keep]
        if len(co2_lines) > 1:
            co2_lines = [l for l in co2_lines if l[idx] == co2_keep]
    return int("".join(oxy_lines[0]), 2) * int("".join(co2_lines[0]), 2)

assert(part_two(example) == 230)
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == 1353024)

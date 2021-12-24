def get_input(name):
    with open(name, 'r') as f:
        return [line.strip().split() for line in f.readlines()]

monad = get_input('input24.txt')

from bisect import bisect_left

def run(model, monad):
    alu = dict({'w': 0, 'x': 0, 'y': 0, 'z': 0})
    for instr in monad:
        cmd = instr[0]
        a = instr[1]
        b = 0
        if len(instr) == 3:
            try:
                b = int(instr[2])
            except Exception:
                b = alu[instr[2]]
        if instr[0] == 'inp':
            alu[a] = model.pop(0)
        elif instr[0] == 'add':
            alu[a] = alu[a] + b
        elif instr[0] == 'mod':
            assert(alu[a] >=0 and b > 0)
            alu[a] = alu[a] % b
        elif instr[0] == 'div':
            assert(b > 0)
            alu[a] = int(alu[a] / b)
        elif instr[0] == 'mul':
            alu[a] = alu[a] * b
        elif instr[0] == 'eql':
            alu[a] = 1 if alu[a] == b else 0
    # print(f"monad ended: {alu}")
    return alu

def part_one(monad):
    for model in reversed(range(11111111111111, 100000000000000)):
        if model % 10000 == 0:
            print(model)
        digits = [int(d) for d in str(model)]
        if 0 in digits:
            continue
        if run(digits, monad)['z'] == 0:
            return model
    return 0

print(f"Part 1: {part_one(monad)}")


def part_two(monad):
    return 0

print(f"Part 2: {part_two(monad)}")
assert(part_two(monad) == 0)

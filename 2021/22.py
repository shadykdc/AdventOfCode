import re

class RebootStep:
    def __init__(self, on, nums):
        self.on = on
        assert(len(nums) == 6)
        self.x1 = int(nums[0])
        self.x2 = int(nums[1])
        self.y1 = int(nums[2])
        self.y2 = int(nums[3])
        self.z1 = int(nums[4])
        self.z2 = int(nums[5])

    def out_of_bounds(self):
        return abs(self.x1) > 50 or abs(self.x2) > 50
        or abs(self.y1) > 50 or abs(self.y2) > 50
        or abs(self.z1) > 50 or abs(self.z2) > 50

    def get_volume(self):
        return abs(self.x1-self.x2) * abs(self.y1-self.y2) * abs(self.z1-self.z2)

    def get_shared_volume(self, step):
        return max(min(self.x2, step.x2))-max(self.x1, step.x1), 0)
            * max(min(self.y2, step.y2))-max(self.y1, step.y1), 0)
            * max(min(self.z2, step.z2))-max(self.z1, step.z1), 0)

def get_input(name):
    with open(name, 'r') as f:
        steps = [
            RebootStep(line[1] == 'n', re.findall('[-]?\d+', line.strip()))
            for line in f.readlines()
        ]
        return steps

steps = get_input('input22.txt')
example1 = get_input('input22.1.txt')
example2 = get_input('input22.2.txt')

def part_one(steps):
    on_cubes = set()
    for step in steps:
        if not step.out_of_bounds():
            for x in range(step.x1, step.x2+1):
                for y in range(step.y1, step.y2+1):
                    for z in range(step.z1, step.z2+1):
                        if step.on:
                            on_cubes.add((x, y, z))
                        elif (x, y, z) in on_cubes:
                            on_cubes.remove((x, y, z))
    return len(on_cubes)

assert(part_one(example1) == 590784)
print(f"Part One: {part_one(steps)}")
assert(part_one(steps) == 612714)

def part_two(steps):
    on_count
    for idx, step in enumerate(steps):
        if step.on:
            on_count += step.get_volume()
            for prev in steps[0:idx]:
                if prev.on:
                    on_count -= step.get_shared_volume(prev)
        else:
            for prev in steps[0:idx]:
                on_count -= step.get_shared_volume(prev)
    return on_count

print(part_two(example2))
assert(part_two(example2) == 2758514936282235)
print("assert passed...")
print(f"Part Two: {part_two(steps)}")

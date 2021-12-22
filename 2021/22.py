import re

class Cube:
    def __init__(self, on, nums):
        self.on = on
        assert(len(nums) == 6)
        self.x1 = int(nums[0])
        self.x2 = int(nums[1])
        self.y1 = int(nums[2])
        self.y2 = int(nums[3])
        self.z1 = int(nums[4])
        self.z2 = int(nums[5])
        self.off = []

    def __str__(self):
        return f"{'on' if self.on else 'off'} {self.x1} {self.x2}"

    def subtract(self, cube):
        if self.get_shared_volume(cube):
            for off_cube in self.off:
                off_cube.subtract(cube)
            self.off.append(Cube(False, self.get_shared_coords(cube)))

    def get_coords(self):
        return [self.x1, self.x2, self.y1, self.y2, self.z1, self.z2]

    def get_shared_coords(self, cube):
        if self.get_shared_volume(cube):
            return [
                max(self.x1, cube.x1), min(self.x2, cube.x2),
                max(self.y1, cube.y1), min(self.y2, cube.y2),
                max(self.z1, cube.z1), min(self.z2, cube.z2)
            ]
        return None

    def out_of_bounds(self):
        return abs(self.x1) > 50 or abs(self.x2) > 50 \
            or abs(self.y1) > 50 or abs(self.y2) > 50 \
            or abs(self.z1) > 50 or abs(self.z2) > 50

    def calculate_volume(self):
        return abs(self.x2-self.x1+1) \
             * abs(self.y2-self.y1+1) \
             * abs(self.z2-self.z1+1) \
             - sum([cube.calculate_volume() for cube in self.off])

    def get_shared_volume(self, cube):
        return max(min(self.x2, cube.x2)-max(self.x1, cube.x1)+1, 0) \
             * max(min(self.y2, cube.y2)-max(self.y1, cube.y1)+1, 0) \
             * max(min(self.z2, cube.z2)-max(self.z1, cube.z1)+1, 0)

def get_input(name):
    with open(name, 'r') as f:
        steps = [
            Cube(line[1] == 'n', re.findall('[-]?\d+', line.strip()))
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
p1 = part_one(steps)
print(f"Part One: {p1}")
assert(p1 == 612714)

def part_two(steps):
    steps = [step for step in steps]
    cubes = []
    for step in steps:
        for cube in cubes:
            cube.subtract(step)
        if step.on:
            cubes.append(step)
    return sum([cube.calculate_volume() for cube in cubes])

p2_ex = part_two(example2)
assert(p2_ex == 2758514936282235)
p2 = part_two(steps)
print(f"Part Two: {p2}")
assert(p2 == 1311612259117092)

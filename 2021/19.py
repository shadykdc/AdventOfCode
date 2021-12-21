import itertools
from collections import defaultdict

def get_input(name):
    with open(name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        scanners = []
        num = 0
        for line in lines:
            if "---" in line:
                num = int(line.split()[2])
                scanners.append([])
            elif "," in line:
                scanners[num].append([int(num) for num in line.split(",")])
    return scanners

scanners = get_input('input19.txt')
example = get_input('input19.1.txt')

SHARED = 12

def check_for_overlap(scanner, beacons):
    combos = list(itertools.product(scanner, [list(t) for t in beacons]))
    for combo in combos:
        sx, sy, sz = combo[0]
        bx, by, bz = combo[1]
        i, j, k = bx-sx, by-sy, bz-sz
        scan = {(coord[0]+i, coord[1]+j, coord[2]+k) for coord in scanner}
        if len(scan.intersection(set(beacons.keys()))) >= SHARED:
            return True, i, j, k
    return False, 0, 0, 0

def rotate(coord, axis):
    axes = [num for num in [0, 1, 2] if num != axis]
    temp = coord[axes[0]]
    coord[axes[0]] = coord[axes[1]]
    coord[axes[1]] = -temp
    return coord

AXES = 3
ROTATIONS = 4
ORIENTATIONS = 2 * AXES * ROTATIONS

def facing_options(coord):
    return [
        [coord[2], coord[1], -coord[0]],  # face left (rotate about x-axis)
        [coord[0], coord[2], -coord[1]],  # face up (rotate about y-axis)
        [coord[0], coord[1], coord[2]],   # face forward (rotate about z-axis)
        [-coord[2], coord[1], coord[0]],  # face right (rotate about x-axis)
        [coord[0], -coord[2], coord[1]],  # face down (rotate about y-axis)
        [-coord[0], coord[1], -coord[2]], # face back (rotate about z-axis)
    ]

def get_orientations(scanner):
    rotated_scanners = [[] for _ in range(ORIENTATIONS)]
    for coord in scanner:
        for axis, to_rotate in enumerate(facing_options(coord)):
            for idx in range(ROTATIONS):
                orientation = ROTATIONS*axis+idx
                rotated_scanners[orientation].append(
                    [num for num in rotate(to_rotate, axis%3)]
                )
    return rotated_scanners

def try_scanner(scanners, beacons, locations):
    scanner = scanners.pop(0)
    print(f"Trying scanner with {scanner[0]} ({len(scanners)} left)")
    for orientation in get_orientations(scanner):
        overlap, x, y, z = check_for_overlap(orientation, beacons)
        if overlap:
            locations.add((x, y, z))
            print(f"Success at {x} {y} {z}")
            for i, j, k in orientation:
                beacons[(i+x, j+y, k+z)] += 1
            return
    scanners.append(scanner)

def populate_beacons(scanners, beacons, locations):
    for coord in scanners.pop(0):
        beacons[tuple(coord)] += 1
    while len(scanners) > 0:
        try_scanner(scanners, beacons, locations)

def part_one(scanners):
    scanners = [l for l in scanners]
    beacons = defaultdict(int)
    locations = set()
    populate_beacons(scanners, beacons, locations)
    return len(list(beacons.keys()))

assert(part_one(example) == 79)
print(f"Part 1: {part_one(scanners)}")

def distance(loc1, loc2):
    x1, y1, z1 = loc1
    x2, y2, z2 = loc2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

def part_two(scanners):
    scanners = [l for l in scanners]
    beacons = defaultdict(int)
    locations = set() # keep track of the scanner coordinates we find
    populate_beacons(scanners, beacons, locations)
    return max([
        distance(loc1, loc2)
        for loc1, loc2
        in list(itertools.combinations(locations, 2))
    ])

assert(part_two(example) == 3621)
print(part_two(scanners))

import itertools

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
        if len(scan.intersection(beacons)) >= SHARED:
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

def get_orientations(scanner):
    rotated_scanners = [[] for _ in range(ORIENTATIONS)]
    for coord in scanner:
        for posneg in [-1, 1]:
            to_rotate = [num * posneg for num in coord]
            for axis in range(AXES):
                for idx in range(ROTATIONS):
                    orientation = ROTATIONS*axis+idx + (12 if posneg > 0 else 0)
                    rotated_scanners[orientation].append(
                        [num for num in rotate(to_rotate, axis)]
                    )
    return rotated_scanners

def try_scanner(scanners, beacons):
    scanner = scanners.pop(0)
    print(f"Trying scanner with {scanner[0]}")
    for orientation in get_orientations(scanner):
        overlap, x, y, z = check_for_overlap(orientation, beacons)
        if overlap:
            print(f"Success {x} {y} {z}")
            for i, j, k in orientation:
                beacons.add((i+x, j+y, k+z))
            return
    scanners.append(scanner)

def populate_beacons(scanners, beacons):
    first_scanner = scanners.pop(0)
    print(f"First scanner has {first_scanner[0]}")
    beacons = {tuple(coord) for coord in first_scanner}
    while len(scanners) > 0:
        try_scanner(scanners, beacons)

def part_one(scanners):
    scanners = [l for l in scanners]
    beacons = set()
    populate_beacons(scanners, beacons)
    return len(beacons)

# test to make sure my code works
s = [[
    [-618,-824,-621],
    [-537,-823,-458],
    [-447,-329,318],
    [404,-588,-901],
    [544,-627,-890],
    [528,-643,409],
    [-661,-816,-575],
    [390,-675,-793],
    [423,-701,434],
    [-345,-311,381],
    [459,-707,401],
    [-485,-357,347],
]]
b = [
    (686,422,578),
    (605,423,415),
    (515,917,-361),
    (-336,658,858),
    (-476,619,847),
    (-460,603,-452),
    (729,430,532),
    (-322,571,750),
    (-355,545,-477),
    (413,935,-424),
    (-391,539,-444),
    (553,889,-390),
]
x, y, z = 68,-1246,-43
# try_scanner(s, set(b))
# assert(len(s) == 0)

print(f"Example: {part_one(example)}")
# print(f"Part 1: {part_one(scanners)}")

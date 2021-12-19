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

def get_orientations(scanner):
    rotated_scanners = [[] for _ in range(ORIENTATIONS)]
    for coord in scanner:
        for posneg in [-1, 1]:
            for axis in range(AXES):
                to_rotate = [num * posneg for num in coord]
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
                beacons[(i+x, j+y, k+z)] += 1
            return
    scanners.append(scanner)

def populate_beacons(scanners, beacons):
    for coord in scanners.pop(0):
        beacons[tuple(coord)] += 1
    while len(scanners) > 0:
        try_scanner(scanners, beacons)

def part_one(scanners):
    scanners = [l for l in scanners]
    beacons = defaultdict(int)
    populate_beacons(scanners, beacons)
    return len(list(beacons.keys()))

# test to make sure my code works
s = [[ # s4
    [727,592,562],
    [-293,-554,779],
    [441,611,-461],
    [-714,465,-776],
    [-743,427,-804],
    [-660,-479,-426],
    [832,-632,460],
    [927,-485,-438],
    [408,393,-506],
    [466,436,-512],
    [110,16,151],
    [-258,-428,682],
    [-393,719,612],
    [-211,-452,876],
    [808,-476,-593],
    [-575,615,604],
    [-485,667,467],
    [-680,325,-822],
    [-627,-443,-432],
    [872,-547,-609],
    [833,512,582],
    [807,604,487],
    [839,-516,451],
    [891,-625,532],
    [-652,-548,-490],
    [30,-46,-14],
]]
# s 0, 1, and 3 (missing 2 and 4)
b = {(404, -588, -901): 2, (528, -643, 409): 2, (-838, 591, 734): 1, (390, -675, -793): 2, (-537, -823, -458): 2, (-485, -357, 347): 2, (-345, -311, 381): 2, (-661, -816, -575): 2, (-876, 649, 763): 1, (-618, -824, -621): 2, (553, 345, -567): 1, (474, 580, 667): 1, (-447, -329, 318): 2, (-584, 868, -557): 1, (544, -627, -890): 2, (564, 392, -477): 1, (455, 729, 728): 1, (-892, 524, 684): 1, (-689, 845, -530): 1, (423, -701, 434): 2, (7, -33, -71): 1, (630, 319, -379): 1, (443, 580, 662): 1, (-789, 900, -551): 1, (459, -707, 401): 2, (-27, -1108, -65): 1, (408, -1815, 803): 2, (-499, -1607, -770): 2, (-601, -1648, -643): 2, (568, -2007, -577): 2, (534, -1912, 768): 2, (497, -1838, -617): 2, (-635, -1737, 486): 2, (396, -1931, -563): 2, (-518, -1681, -600): 2, (432, -2009, 850): 2, (-739, -1745, 668): 2, (-687, -1600, 576): 2, (-697, -3072, -689): 1, (366, -3059, 397): 1, (-430, -3130, 366): 1, (-620, -3212, 371): 1, (-654, -3158, -753): 1, (846, -3110, -434): 1, (12, -2351, -103): 1, (-470, -3283, 303): 1, (686, -3108, -505): 1, (346, -2985, 342): 1, (377, -2827, 367): 1, (776, -3184, -501): 1, (-706, -3180, -659): 1}
try_scanner(s, dict(b))
# assert(len(s) == 0)

print(f"Example: {part_one(example)}")
# print(f"Part 1: {part_one(scanners)}")

def part_two(scanners):
    scanners = [l for l in scanners]
    beacons = defaultdict(int)
    populate_beacons(scanners, beacons)
    count = 0
    for key in beacons:
        if beacons[key] == 1:
            count += 1
    return count

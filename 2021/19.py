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

RANGE = 1000
SHARED = 12
ORIENTATIONS = 24

def check_for_overlap(scanner, beacons):
    beacon_list = [list(t) for t in beacons]
    combos = list(itertools.product(scanner, beacon_list))
    for combo in combos:
        sx, sy, sz = combo[0]
        bx, by, bz = combo[1]
        i, j, k = bx-sx, by-sy, bz-sz
        scan = {(coord[0]+i, coord[1]+j, coord[2]+k) for coord in scanner}
        overlap = len(scan.intersection(beacons))
        if overlap >= 12:
            return True, i, j, k
    return False, 0, 0, 0

def rotate(coord, axis):
    axies = [num for num in [0, 1, 2] if num != axis]
    temp = coord[axies[0]]
    coord[axies[0]] = coord[axies[1]]
    coord[axies[1]] = -temp

def get_orientations(scanner):
    orientations = [[] for _ in range(ORIENTATIONS)]
    for i in range(ORIENTATIONS):
        for coord in scanner:
            coord1 = [num for num in coord]
            coord2 = [-num for num in coord]
            for idx in range(3):
                for _ in range(4):
                    orientations[i].append(coord1)
                    rotate(coord1, idx)
                    orientations[i].append(coord2)
                    rotate(coord2, idx)
    return orientations

def try_scanner(scanners, beacons):
    scanner = scanners.pop()
    for rotated in get_orientations(scanner):
        overlap, x, y, z = check_for_overlap(rotated, beacons)
        if overlap:
            for i, j, k in rotated:
                beacons.add((i+x, j+y, k+z))
            return
    scanners.append(scanner)

def populate_beacons(scanners, beacons):
    beacons = {tuple(coord) for coord in scanners.pop(0)}
    while len(scanners) > 0:
        try_scanner(scanners, beacons)

def part_one(scanners):
    scanners = [l for l in scanners]
    beacons = set()
    populate_beacons(scanners, beacons)
    return len(beacons)

print(f"Example: {part_one(example)}")
print(f"Part 1: {part_one(scanners)}")

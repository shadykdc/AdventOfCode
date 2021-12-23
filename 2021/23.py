def get_input(diagram):
    return [[ch for ch in line.strip()] for line in diagram.split()]

ENERGY = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

ROOMS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9,
}

diagram = get_input("""\
#############
#...........#
###B#A#B#C###
###D#A#D#C###
#############""")

example = get_input("""\
#############
#...........#
###B#C#B#D###
###A#D#C#A###
#############""")

def get_state(diagram):
    return "".join(["".join(row) for row in diagram])

def complete(state):
    return state == "##############...........####A#B#C#D######A#B#C#D################"

def enter_moves(diagram, letter, i, j):
    moves = []
    for off in range(-10, 11):
        if i+off in range(len(diagram[0]))\
        and diagram[j+1][i+off] == '.'\
        and i+off == ROOMS[letter]\
        and row_is_clear(diagram, i, j, off):
            if diagram[j+2][i+off] == '.':
                moves.append((off+i, j+2, ENERGY[letter] * (abs(off) + 2)))
            if diagram[j+2][i+off] in ROOMS and ROOMS[diagram[j+2][i+off]] == off+i:
                moves.append((off+i, j+1, ENERGY[letter] * (abs(off) + 1)))
    return moves

def row_is_clear(diagram, i, j, off):
    if off < 0:
        for o in range(off, 0):
            if diagram[j][i+o] != '.':
                return False
    elif off > 0:
        for o in range(1, off+1):
            if diagram[j][i+o] != '.':
                return False
    return True

def exit_moves(diagram, letter, i, j):
    exits = []
    if j != 1 and ROOMS[letter] != i or diagram[j+1][i] in ROOMS and ROOMS[diagram[j+1][i]] != i:
        for off in range(-10, 11):
            if i+off in range(len(diagram[0]))\
            and off+i not in ROOMS.values():
                if diagram[j-1][i+off] == '.' and row_is_clear(diagram, i, j-1, off):
                    exits.append((i+off, j-1, ENERGY[letter] * (abs(off) + 1)))
                if diagram[j-2][i+off] == '.' and diagram[j-1][i] == '.' and row_is_clear(diagram, i, j-2, off):
                    exits.append((i+off, j-2, ENERGY[letter] * (abs(off) + 2)))
    return exits

def printd(diagram):
    for row in diagram:
        print("".join(row))
    print(" ")

def get_solutions(diagram, solutions, seen, energy):
    # if energy in [40, 440, 3030+440, 3030+440+40, 3030+440+40+2003, 3030+440+40+2003+7000, 3030+440+40+2003+7000+8]:
    if energy == 40:
        print(f"energy: {energy};")
        print(diagram)
        printd(diagram)
        import time
        time.sleep(0.2)
    diagram = [[ch for ch in row] for row in diagram]
    if complete(get_state(diagram)):
        solutions.append(energy)
        return
    for y1 in [1, 2, 3]:
        for x1 in range(1, 12) if y1 == 1 else list(ROOMS.values()):
            ch = diagram[y1][x1]
            if ch in ENERGY:
                moves = enter_moves(diagram, ch, x1, y1) if y1 == 1 else exit_moves(diagram, ch, x1, y1)
                for x2, y2, e in moves:
                    if energy + e <= min(solutions):
                        diagram[y1][x1], diagram[y2][x2] = '.', ch
                        state = get_state(diagram)
                        if state not in seen or complete(state):
                            seen.add(state)
                            get_solutions(diagram, solutions, seen, energy + e)
                        diagram[y1][x1], diagram[y2][x2] = ch, '.'

def part_one(diagram):
    solutions = [999999999]
    seen = {get_state(diagram)}
    get_solutions(diagram, solutions, seen, 0)
    return min(solutions)

print(part_one(example))
assert(part_one(example) == 12521)
p1 = part_one(diagram)
assert(p1 < 56612)
print(p1)

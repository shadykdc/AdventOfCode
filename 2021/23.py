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
    for x in [1, -1]:
        if diagram[j][i+x] == '.'\
        and diagram[j+1][i+x] == '.'\
        and i+x == ROOMS[letter]:
            if diagram[j+2][i+x] == '.':
                moves.append((x+i, j+2, ENERGY[letter] * 3))
            if diagram[j+2][i+x] in ROOMS and ROOMS[diagram[j+2][i+x]] == x+i:
                moves.append((x+i, j+1, ENERGY[letter] * 2))
    return moves

def lat_enter_moves(diagram, letter, i, j):
    moves = []
    for x2, y2, e2 in lateral_moves(diagram, letter, i, j):
        diagram[j][i] = '.'
        diagram[y2][x2] = letter
        moves.extend(enter_moves(diagram, letter, x2, y2))
        moves = [(x, y, e2+e1) for x, y, e1 in moves]
        diagram[j][i] = letter
        diagram[y2][x2] = '.'
    return moves

def row_is_clear(diagram, i, j, off):
    if off < 0:
        for o in range(off, 0):
            if diagram[j][i+o] != '.':
                return False
    if off > 0:
        for o in range(1, off+1):
            if diagram[j][i+o] != '.':
                return False
    return True

def lateral_moves(diagram, letter, i, j):
    moves = []
    if j == 1:
        for off in range(-10, 11): # standing still is okay
            if off+i in range(1, 12)\
            and off+i not in ROOMS.values()\
            and row_is_clear(diagram, i, j, off):
                moves.append((off+i, j, ENERGY[letter] * abs(off)))
    return moves

def exit_moves(diagram, letter, i, j):
    exits = []
    if j != 1 and ROOMS[letter] != i or diagram[j+1][i] in ROOMS and ROOMS[diagram[j+1][i]] != i:
        for x in [1, -1]:
            if diagram[j-1][i+x] == '.':
                exits.append((x+i, j-1, ENERGY[letter] * 2))
            if diagram[j-2][i+x] == '.' and diagram[j-1][i] == '.':
                exits.append((x+i, j-2, ENERGY[letter] * 3))
    return exits

def exit_lat_moves(diagram, letter, i, j):
    moves = []
    for x2, y2, e2 in exit_moves(diagram, letter, i, j):
        diagram[j][i] = '.'
        diagram[y2][x2] = letter
        moves.extend(lateral_moves(diagram, letter, x2, y2))
        moves = [(x, y, e2+e1) for x, y, e1 in moves]
        diagram[j][i] = letter
        diagram[y2][x2] = '.'
    return moves

def printd(diagram):
    for row in diagram:
        print("".join(row))
    print(" ")

def get_solutions(diagram, solutions, seen, energy):
    # print(energy)
    # print(diagram)
    # printd(diagram)
    # import time
    # time.sleep(1)
    diagram = [[ch for ch in row] for row in diagram]
    if complete(get_state(diagram)):
        solutions.append(energy)
        return
    for y1 in [2, 1, 3]:
        for x1 in range(1, 12) if y1 == 1 else list(ROOMS.values()):
            ch = diagram[y1][x1]
            if ch in ENERGY:
                moves = lat_enter_moves(diagram, ch, x1, y1) if y1 == 1 else exit_lat_moves(diagram, ch, x1, y1)
                for x2, y2, e in moves:
                    if energy + e < min(solutions):
                        diagram[y1][x1] = '.'
                        diagram[y2][x2] = ch
                        state = get_state(diagram)
                        if state not in seen or complete(state):
                            seen.add(state)
                            get_solutions(diagram, solutions, seen, energy + e)
                        diagram[y1][x1] = ch
                        diagram[y2][x2] = '.'

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

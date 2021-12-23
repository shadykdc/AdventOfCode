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

diagram_p1 = get_input("""\
#############
#...........#
###B#A#B#C###
###D#A#D#C###
#############""")

example_p1 = get_input("""\
#############
#...........#
###B#C#B#D###
###A#D#C#A###
#############""")

diagram_p2 = get_input("""\
#############
#...........#
###B#A#B#C###
###D#C#B#A###
###D#B#A#C###
###D#A#D#C###
#############""")

example_p2 = get_input("""\
#############
#...........#
###B#C#B#D###
###D#C#B#A###
###D#B#A#C###
###A#D#C#A###
#############""")

def get_state(diagram):
    return f"".join(["".join(row) for row in diagram])

COMPLETE = "##############...........####A#B#C#D######A#B#C#D################"
def complete(state):
    return state == COMPLETE

def row_is_clear(diagram, i, j, off):
    assert(i+off in range(0, len(diagram[0])))
    if off < 0:
        for o in range(off, 0):
            if diagram[j][i+o] != '.':
                return False
    elif off > 0:
        for o in range(1, off+1):
            if diagram[j][i+o] != '.':
                return False
    return True

def col_is_clear(diagram, i, j, off):
    if off < 0:
        for o in range(off, 0):
            if diagram[j+o][i] != '.':
                return False
    elif off > 0:
        for o in range(1, off+1):
            if diagram[j+o][i] != '.':
                return False
    return True

def enter_moves(diagram, i, j):
    moves = []
    xoff = ROOMS[diagram[j][i]] - i
    if j == 1 and row_is_clear(diagram, i, j, xoff):
        for yoff in reversed(range(1, len(diagram)-2)): # start with bottom
            if j+yoff in range(2, len(diagram)-1)\
            and diagram[yoff+j][xoff+i] == '.'\
            and col_is_clear(diagram, i+xoff, j, yoff)\
            and not bad_letters_in_col(diagram, i+xoff):
                moves.append(
                    (xoff+i, j+yoff, ENERGY[diagram[j][i]] * (abs(xoff) + abs(yoff)))
                )
                break # always go to the bottom
    return moves

def bad_letters_in_col(diagram, i):
    for j in range(2, len(diagram)-1):
        letter = diagram[j][i]
        if letter != '.' and ROOMS[letter] != i:
            return True
    return False

def exit_moves(diagram, i, j):
    exits = []
    if j != 1 and bad_letters_in_col(diagram, i) and col_is_clear(diagram, i, j, 1-j):
        for xoff in range(1-i, len(diagram[0])-1-i):
            if xoff+i not in ROOMS.values()\
            and row_is_clear(diagram, i, 1, xoff):
                exits.append((i+xoff, 1, ENERGY[diagram[j][i]] * (abs(xoff) + abs(1-j))))
    return exits

def printd(diagram):
    for row in diagram:
        print("".join(row))
    print(" ")

def get_solutions(diagram, seen, energy):
    print(f"energy: {energy};")
    print(diagram)
    printd(diagram)
    import time
    time.sleep(0.02)
    diagram = [[ch for ch in row] for row in diagram]
    for y1 in range(1, len(diagram)-1): # greedy - always try to enter first
        for x1 in range(1, 12) if y1 == 1 else list(ROOMS.values()):
            letter = diagram[y1][x1]
            if letter in ROOMS:
                moves = enter_moves(diagram, x1, y1) if y1 == 1 else exit_moves(diagram, x1, y1)
                for x2, y2, e in moves:
                    if COMPLETE not in seen or energy + e < seen[COMPLETE]:
                        diagram[y1][x1], diagram[y2][x2] = '.', letter
                        state = get_state(diagram)
                        if state not in seen or seen[state] > energy + e:
                            seen[state] = energy + e
                            if state != COMPLETE:
                                get_solutions(diagram, seen, energy + e)
                        diagram[y1][x1], diagram[y2][x2] = letter, '.'

def solution(diagram):
    seen = {get_state(diagram): 0}
    get_solutions(diagram, seen, 0)
    return seen[COMPLETE] if COMPLETE in seen else -1

# assert(solution(example_p1) == 12521)
# p1 = solution(diagram_p1)
# print(f"Part One: {p1}")
# assert(p1 == 16506)

ex_p2 = solution(example_p2)
print(ex_p2)
assert(ex_p2 == 44169)
p2 = solution(diagram_p2)
print(f"Part Two: {p2}")
# assert(p2 == 16506)

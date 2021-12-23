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

def complete(state):
    return state == "##############...........####A#B#C#D######A#B#C#D################"

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
    assert(i in list(ROOMS.values()))
    if off < 0:
        for o in range(off, 0):
            if diagram[j+o][i] != '.':
                return False
    elif off > 0:
        for o in range(1, off+1):
            if diagram[j+o][i] != '.':
                return False
    return True

def enter_moves(diagram, letter, i, j):
    moves = []
    if j != 1:
        return moves
    for xoff in range(-10, 11):
        if i+xoff in range(len(diagram[0]))\
        and diagram[j+1][i+xoff] == '.'\
        and i+xoff == ROOMS[letter]\
        and row_is_clear(diagram, i, j, xoff):
            for yoff in reversed(range(1, 5)):
                if yoff+j in range(2, len(diagram)-1)\
                and diagram[yoff+j][xoff+i] == '.'\
                and col_is_clear(diagram, i+xoff, j, yoff)\
                and no_bad_letters_in_col(diagram, i+xoff):
                    moves.append((xoff+i, j+yoff, ENERGY[letter] * (abs(xoff) + abs(yoff))))
                    break # always go to the bottom
    return moves

def no_bad_letters_in_col(diagram, i):
    for j in range(2, len(diagram)-1):
        letter = diagram[j][i]
        if letter != '.' and ROOMS[letter] != i:
            return False
    return True

def exit_moves(diagram, letter, i, j):
    exits = []
    if j != 1 and not no_bad_letters_in_col(diagram, i):
        for xoff in range(-10, 11):
            if i+xoff in range(1, len(diagram[0])-1)\
            and xoff+i not in ROOMS.values():
                yoff = 1-j
                if col_is_clear(diagram, i, j, yoff)\
                and row_is_clear(diagram, i, j+yoff, xoff):
                    exits.append((i+xoff, j+yoff, ENERGY[letter] * (abs(xoff) + abs(yoff))))
    return exits

def printd(diagram):
    for row in diagram:
        print("".join(row))
    print(" ")

def get_solutions(diagram, solutions, seen, energy):
    print(f"energy: {energy};")
    print(diagram)
    printd(diagram)
    import time
    time.sleep(0.2)
    diagram = [[ch for ch in row] for row in diagram]
    if complete(get_state(diagram)):
        solutions.append(energy)
        return
    for y1 in range(1, len(diagram)-1):
        for x1 in range(1, 12) if y1 == 1 else list(ROOMS.values()):
            ch = diagram[y1][x1]
            if ch in ENERGY:
                moves = enter_moves(diagram, ch, x1, y1) if y1 == 1 else exit_moves(diagram, ch, x1, y1)
                for x2, y2, e in moves:
                    if energy + e < min(solutions):
                        diagram[y1][x1], diagram[y2][x2] = '.', ch
                        state = get_state(diagram)
                        if state not in seen or seen[state] > energy + e or complete(state):
                            seen[state] = energy + e
                            get_solutions(diagram, solutions, seen, energy + e)
                        diagram[y1][x1], diagram[y2][x2] = ch, '.'

def solution(diagram):
    solutions = [999999999]
    seen = {get_state(diagram): 0}
    get_solutions(diagram, solutions, seen, 0)
    return min(solutions)

# assert(solution(example_p1) == 12521)
# p1 = solution(diagram_p1)
# print(f"Part One: {p1}")
# assert(p1 == 16506)

print(solution(example_p2))
assert(solution(example_p2) == 44169)
p2 = solution(diagram_p2)
print(f"Part Two: {p2}")
# assert(p2 == 16506)

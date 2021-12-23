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

def complete(diagram):
    return get_state(diagram) == """\
#############
#...........#
###A#B#C#D###
###A#B#C#D###
#############"""

def legal_move(diagram, i, j, x, y):
    if x+i in range(len(diagram[0]))\
    and y+j in range(len(diagram))\
    and diagram[y+j][x+i] == "."\
    and not (j == 1 and x+i not in ROOMS.values())\
    and not (y+j >= 2 and x+i != ROOMS[letter]\
    and not (y+j == 2 and diagram[3][x+i] not in {letter, '.'})):
        return True
    return False

def moves(diagram, letter, i, j):
    moves = []
    if j == 1:
        # enter room if correct home
        for x in [1, -1]:
            if diagram[j][i+x] == '.'\
            and diagram[j+1][i+x] == '.'\
            and i+x == ROOMS[letter]:
                if diagram[j+2][i+x] == '.':
                    moves.append((x+i, j+2, ENERGY[letter] * 3))
                else:
                    if diagram[j+2][i+x] in ROOMS and ROOMS[diagram[j+2][i+x]] == x+i:
                        moves.append((x+i, j+1, ENERGY[letter] * 2))
                # greedy, if we can move into a room, just do that
                return moves
        # lateral move
        for x in [-1, 1, 2, -2]:
            if x+i in range(1, 12)\
            and x+i not in ROOMS.values()\
            and diagram[j][x+i] == '.':
                # big lateral move
                if abs(x) == 2:
                    if diagram[j][x+i+(1 if x == -2 else -1)] == '.':
                        moves.append((x+i, j, ENERGY[letter] * 2))
                else: # small lateral move
                    moves.append((x+i, j, ENERGY[letter]))
    # exit room if not in its home
    elif ROOMS[diagram[j][i]] != i:
        for x in [1, -1]:
            if diagram[j-1][i+x] == '.':
                moves.append((x+i, j-1, ENERGY[letter] * 2))
            if diagram[j-2][i+x] == '.' and diagram[j-1][i] == '.':
                moves.append((x+i, j-2, ENERGY[letter] * 3))
    return moves

def printd(diagram):
    for row in diagram:
        print("".join(row))
    print(" ")
import time
def get_solutions(diagram, solutions, seen, energy):
    diagram = [[ch for ch in row] for row in diagram]
    printd(diagram)
    time.sleep(1)
    if complete(diagram):
        solutions.append(energy)
        return
    for y1, row in enumerate(diagram):
        for x1, ch in enumerate(row):
            if ch in ENERGY:
                for x2, y2, e in moves(diagram, ch, x1, y1):
                    diagram[y1][x1] = '.'
                    diagram[y2][x2] = ch
                    state = get_state(diagram)
                    if state in seen:
                        diagram[y1][x1] = ch
                        diagram[y2][x2] = '.'
                    else:
                        seen.add(state)
                        if energy + e < min(solutions):
                            get_solutions(diagram, solutions, seen, energy + e)
                            diagram[y1][x1] = ch
                            diagram[y2][x2] = '.'

def part_one(diagram):
    solutions = [999999999]
    seen = {get_state(diagram)}
    get_solutions(diagram, solutions, seen, 0)
    return min(solutions)

print(part_one(example))
print(part_one(diagram))

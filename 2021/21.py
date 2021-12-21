# my input
p1 = 3
p2 = 10

# example
p1_2 = 4
p2_2 = 8

ROLLS = 3

def get_roll(num):
    return sum([num % 100 for num in [num + i for i in range(3)]])

def move(pos, move):
    return (pos + move - 1) % 10 + 1

def take_turn(p, score, roll):
    p = move(p, get_roll(roll+1))
    return p, score + p, roll + 3

def part_one(p1, p2):
    roll, p1_score, p2_score, limit = 0, 0, 0, 1000
    while p1_score < limit and p2_score < limit:
        p1, p1_score, roll = take_turn(p1, p1_score, roll)
        if p1_score >= limit:
            return p2_score * roll
        p2, p2_score, roll = take_turn(p2, p2_score, roll)
    return p1_score * roll

assert(part_one(p1_2, p2_2) == 739785)
print(f"Part One: {part_one(p1, p2)}")

def take_turns(pos, score):
    for roll in range(1, 4):
        pos = move(pos, roll)
        yield pos, score + pos

def play(p1, p2, p1_score, p2_score, limit, p1_turn, wins):
    if p1_turn:
        for pos, score in take_turns(p1, p1_score):
            if score >= limit:
                wins['p1'] += 1
                return
            play(pos, p2, score, p2_score, limit, False, wins)
    else:
        for pos, score in take_turns(p2, p2_score):
            if score >= limit:
                wins['p2'] += 1
                return
            play(p1, pos, p1_score, score, limit, True, wins)

def part_two(p1, p2):
    wins = {'p1': 0, 'p2': 0}
    play(p1, p2, 0, 0, 21, True, wins)
    return max(wins['p1'], wins['p2'])

print(part_two(p1_2, p2_2))

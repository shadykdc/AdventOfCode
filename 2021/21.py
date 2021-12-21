from functools import lru_cache
from itertools import product

p1 = 3
p2 = 10
p1_ex = 4
p2_ex = 8

def move(pos, move):
    return (pos + move - 1) % 10 + 1

def get_roll(num):
    return sum([num % 100 for num in [num + i for i in range(3)]])

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

assert(part_one(p1_ex, p2_ex) == 739785)
print(f"Part One: {part_one(p1, p2)}")
assert(part_one(p1, p2) == 713328)

def get_possible_rolls():
    return [sum(list(t)) for t in product([1, 2, 3], repeat=3)]

def take_turns(pos, score):
    return [
        (move(pos, roll), move(pos, roll) + score)
        for roll in get_possible_rolls()
    ]

@lru_cache(maxsize=None)
def play(p1, p2, p1_score, p2_score, limit, p1_turn):
    if p1_score >= limit:
        return (1, 0)
    if p2_score >= limit:
        return (0, 1)
    p1_wins, p2_wins = 0, 0
    for pos, score in take_turns(
        p1 if p1_turn else p2, p1_score if p1_turn else p2_score
    ):
        a, b = play(
            pos if p1_turn else p1,
            p2 if p1_turn else pos,
            score if p1_turn else p1_score,
            p2_score if p1_turn else score,
            limit, not p1_turn
        )
        p1_wins += a
        p2_wins += b
    return (p1_wins, p2_wins)

def part_two(p1, p2):
    return max(play(p1, p2, 0, 0, 21, True))

assert(part_two(p1_ex, p2_ex) == 444356092776315)
print(f"Part Two: {part_two(p1, p2)}")
assert(part_two(p1, p2) == 92399285032143)

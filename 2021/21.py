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

ROLLS = [sum(list(t)) for t in product([1, 2, 3], repeat=3)]

@lru_cache(maxsize=None)
def play(p1, p2, p1_score, p2_score, limit):
    if p1_score >= limit:
        return (1, 0)
    if p2_score >= limit:
        return (0, 1)
    p1_wins, p2_wins = 0, 0
    for pos in [move(p1, roll) for roll in ROLLS]:
        a, b = play(p2, pos, p2_score, pos + p1_score, limit)
        p2_wins += a
        p1_wins += b
    return (p1_wins, p2_wins)

def part_two(p1, p2):
    return max(play(p1, p2, 0, 0, 21))

assert(part_two(p1_ex, p2_ex) == 444356092776315)
print(f"Part Two: {part_two(p1, p2)}")
assert(part_two(p1, p2) == 92399285032143)

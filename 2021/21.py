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
    score += p
    roll += 3
    return p, score, roll

def part_one(p1, p2):
    roll, p1_score, p2_score = 0, 0, 0
    while p1_score < 1000 and p2_score < 1000:
        p1, p1_score, roll = take_turn(p1, p1_score, roll)
        if p1_score >= 1000:
            break
        p2, p2_score, roll = take_turn(p2, p2_score, roll)
    return min(p1_score, p2_score) * roll

assert(part_one(p1_2, p2_2) == 739785)
print(f"Part One: {part_one(p1, p2)}")

def part_two(p1, p2):
    pass

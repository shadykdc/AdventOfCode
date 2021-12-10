with open('input10.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

with open('input10.1.txt', 'r') as f:
    example = [line.strip() for line in f.readlines()]

openers = set(['{', '(', '[', '<'])
closers = set(['}', ')', ']', '>'])
match = {'(': ')', '[': ']', '{': '}', '<': '>'}

def part_one(lines):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    count = 0
    for line in lines:
        stack = []
        for ch in line:
            if ch in openers:
                stack.append(ch)
            elif ch in closers:
                opener = stack.pop()
                if ch != match[opener]:
                    count += scores[ch]
    return count

assert(part_one(example) == 26397)
print(f"Part 1: {part_one(lines)}")
assert(part_one(lines) == 290691)

points = {')': 1, ']': 2, '}': 3, '>': 4}

def get_score(line):
    stack = []
    for ch in line:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            opener = stack.pop()
            if ch != match[opener]:
                return 0
    score = 0
    while len(stack) > 0:
        score = score * 5 + points[match[stack.pop()]]
    return score


def part_two(lines):
    scores = [get_score(line) for line in lines if get_score(line) > 0]
    scores = sorted(scores)
    return scores[int(len(scores)/2)]

assert(part_two(example) == 288957)
print(f"Part 2: {part_two(lines)}")
assert(part_two(lines) == 2768166558)

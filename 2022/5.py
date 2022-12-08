import re
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from utils import answer

example = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

def get_input(lines):
    stacks = defaultdict(lambda: [])
    begin = 0
    for i, line in enumerate(lines):
        if "1" in line:
            begin = i
            break
        for idx, ch in enumerate(line):
            if ch.isalpha():
                stacks[int(idx/4) + 1].append(ch)
    moves = [re.findall(r'\b\d+\b', line) for line in lines[begin+2:]]
    for k in stacks:
        stacks[k].reverse()
    return stacks, moves

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = get_input(f.readlines())

def part1(stks, mvs):
    for move in mvs:
        for _ in range(int(move[0])):
            stks[int(move[2])].append(stks[int(move[1])].pop())
    return "".join([stks[key].pop() for key in sorted(stks)])

def part2(stks, mvs):
    for move in mvs:
        count = int(move[0])
        mv_from = int(move[1])
        stks[int(move[2])].extend(stks[mv_from][-count:])
        stks[mv_from] = stks[mv_from][:-count]
    return "".join(
        [stks[key].pop() if len(stks[key]) else "" for key in sorted(stks)]
    )

answer(part1(*get_input(example)), "Example 1", "CMZ")
answer(part1(*deepcopy(puzzle_input)), "Part 1", "FJSRQCFTN")
answer(part2(*get_input(example)), "Example 2", "MCD")
answer(part2(*deepcopy(puzzle_input)), "Part 2", "CJVLJQPHS")

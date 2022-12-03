from pathlib import Path
from utils import answer

example = [
    ['A', 'Y'],
    ['B', 'X'],
    ['C', 'Z'],
]

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = [line.split() for line in f.readlines()]

def get_score(their_move, our_move):
    move_score = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    win = {
        ('A', 'X'): 3,
        ('B', 'X'): 0,
        ('C', 'X'): 6,
        ('A', 'Y'): 6,
        ('B', 'Y'): 3,
        ('C', 'Y'): 0,
        ('A', 'Z'): 0,
        ('B', 'Z'): 6,
        ('C', 'Z'): 3,
    }
    return win[(their_move, our_move)] + move_score[our_move]

def part1(moves):
    return sum([get_score(move[0], move[1]) for move in moves])


def get_score_2(their_move, require):
    requires = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    win = {
        ('A', 'X'): 3,
        ('B', 'X'): 1,
        ('C', 'X'): 2,
        ('A', 'Y'): 1,
        ('B', 'Y'): 2,
        ('C', 'Y'): 3,
        ('A', 'Z'): 2,
        ('B', 'Z'): 3,
        ('C', 'Z'): 1,
    }
    return requires[require] + win[(their_move, require)]

def part2(moves):
    return sum([get_score_2(move[0], move[1]) for move in moves])


answer(part1(example), "Example 1", 15)
answer(part1(puzzle_input), "Part 1", 14827)
answer(part2(example), "Example 2", 12)
answer(part2(puzzle_input), "Part 2", 13889)

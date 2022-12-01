from pathlib import Path
from utils import answer

example = [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000]
]

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    elves_snacks = []
    calories = []
    for line in f.readlines():
        if line.strip():
            calories.append(int(line.strip()))
        else:
            elves_snacks.append(calories)
            calories = []


def get_k_snackiest_calories(elves, k):
    return sum(sorted(sum(cals) for cals in elves)[-k:])

answer(get_k_snackiest_calories(example, 1), "Example 1", 24000)
answer(get_k_snackiest_calories(elves_snacks, 1), "Part 1", 71924)
answer(get_k_snackiest_calories(example, 3), "Example 2", 45000)
answer(get_k_snackiest_calories(elves_snacks, 3), "Part 2", 210406)

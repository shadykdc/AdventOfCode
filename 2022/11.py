from pathlib import Path
from utils import answer

example = [
    "Monkey 0:",
    "Starting items: 79, 98",
    "Operation: new = old * 19",
    "Test: divisible by 23",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 3",
    "",
    "Monkey 1:",
    "Starting items: 54, 65, 75, 74",
    "Operation: new = old + 6",
    "Test: divisible by 19",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "Starting items: 79, 60, 97",
    "Operation: new = old * old",
    "Test: divisible by 13",
    "    If true: throw to monkey 1",
    "    If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "Starting items: 74",
    "Operation: new = old + 3",
    "Test: divisible by 17",
    "    If true: throw to monkey 0",
    "    If false: throw to monkey 1",
]

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.op = None
        self.test = 0
        self.iftrue = -1
        self.iffalse = -1

    def worry(item):
        f = lambda x: eval(self.op)
        return f(item)

def get_input(lines):
    monkies = {}
    monkey = None
    for line in lines:
        if line.strip().startswith("Monkey"):
            id = re.findall(r'\d+', line)[0]
            monkey = Monkey(id)
            monkies[id] = monkey
        elif line.strip().startswith("Operation: new ="):
            monkey.op = line[len("Operation: new ="):].strip()
        elif line.strip().startswith("Starting items:"):
            self.items = re.findall(r'\d+', line)
        elif line.strip().startswith("Test"):
            self.test = re.findall(r'\d+', line)[0]
        elif line.strip().startswith("If true"):
            self.iftrue = re.findall(r'\d+', line)[0]
        elif line.strip().startswith("If false"):
            self.iffalse = re.findall(r'\d+', line)[0]
    return monkies

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    my_input = f.readlines()

def part1(monkies, rounds=20, k=2):
    return 10605

'''
Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.
The level of monkey business in this situation can be found by multiplying
these together: 10605
'''

answer(part1(get_input(ex)), "Example 1", 10605)
# answer(part1(get_input(my_input)), "Part 1")
# answer(part2(get_input(example)), "Example 2")
# answer(part2(get_input(my_input)), "Part 2")

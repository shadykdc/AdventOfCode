import re
from typing import Dict, List, Set, Tuple

class Program:
    def __init__(self, name: str, weight: int, programs: List[str] = []) -> None:
        self.name: str = name
        self.weight: int = weight
        self.programs: List[str] = programs

    def total_weight(self, tower: Dict[str, "Program"]) -> int:
        return sum([tower[prog].total_weight(tower) for prog in self.programs]) + self.weight

    def __str__(self) -> str:
        return f"{self.name} - {self.programs}"

with open('input7.2.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

def get_tower(lines) -> Tuple[Dict[str, Program], Set[str]]:
    tower: Dict[str, Program] = {}
    children: Set[str] = set()
    for line in lines:
        name = line.split(" ")[0]
        weight = int(line.split("(")[1].split(")")[0])
        programs = []
        if "->" in line:
            programs = [name.strip() for name in line.split("->")[1].split(", ")]
            for program in programs:
                children.add(program)
        tower[name] = Program(name, weight, programs)
    return tower, children

tower, children = get_tower(data)

def part_one(tower: Dict[str, Program], children) -> str:
    return [key for key in tower.keys() if key not in children][0]

root_name = part_one(tower, children)
print(f"Part 1: {root_name}")

def weight_difference(tower: Dict[str, Program], name: str) -> int:
    weights = [tower[child].total_weight(tower) for child in tower[name].programs]
    if len(set(weights)) != 1:
        for idx, weight in enumerate(weights):
            if weights.count(weight) == 1 and len(weights) > 1:
                program = tower[tower[name].programs[idx]]
                if idx == 0:
                    return weights[1] - weight + program.weight
                return weights[0] - weight + program.weight
    return 0


def part_two(tower: Dict[str, Program], name: str) -> int:
    for child in tower[name].programs:
        if weight_difference(tower, child) > 0:
            return part_two(tower, child)
    return weight_difference(tower, name)

print(f"Part Two: {part_two(tower, root_name)}")
assert(part_two(tower, root_name) == 1275)

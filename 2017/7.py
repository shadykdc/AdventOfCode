import re
from typing import Dict, List, Set

class Program:
    def __init__(self, name: str, weight: int, programs: List[str] = []) -> None:
        self.name: str = name
        self.weight: int = weight
        self.programs: List[str] = programs

    def total_weight(self, tower: Dict[str, "Program"]) -> int:
        return sum([tower[prog].weight for prog in programs]) + self.weight

    def __str__(self) -> str:
        return f"{self.name} - {self.programs}"

with open('input7.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

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

def part_one(tower: Dict[str, Program]) -> str:
    return [key for key in tower.keys() if key not in children][0]

root_name = part_one(tower)
print(f"Part 1: {root_name}")

def balanced(tower: Dict[str, Program], name: str) -> bool:
    weights = [tower[prog].total_weight(tower) for prog in tower[name].programs]
    if len(set(weights)) != len(weights):
        weights.sort()
        if weights.count(weights[0]) == 1:
            return weights[1] - weights[0]
        end = len(weights)-1
        if weights.count(weights[end]) == 1:
            return weights[end] - weights[end-1]


def part_two(tower: Dict[str, Program], root_name: str) -> int:
    if len(tower[root_name].programs) == 0:
        return 0
    return balaned(tower, root_name)

part_two(tower, root_name)

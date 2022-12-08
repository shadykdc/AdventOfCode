from pathlib import Path
from utils import answer
import re
from functools import lru_cache

example = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


class Directory:
    def __init__(self, name):
        self.name = name
        self.dirs = {}
        self.files = {}
        self.parent = None

    def __str__(self):
        return str(self.dirs)

    def add_file(self, name, size):
        self.files[name] = size

    def add_dir(self, d):
        d.parent = self
        self.dirs[d.name] = d

    def get_dir(self, name):
        return self.dirs[name]

    @lru_cache(maxsize=None)
    def get_size(self):
        return sum([self.dirs[d].get_size() for d in self.dirs]) + sum([self.files[f] for f in self.files])

    def get_root(self):
        root = self
        while root.parent is not None:
            root = self.parent
        return root

    @lru_cache(maxsize=None)
    def part1(self, limit = 100000):
        output = self.get_size() if self.get_size() < limit else 0
        for d in self.dirs:
            size = self.dirs[d].part1(limit)
            if size < limit:
                output += size
        return output

def get_input(lines):
    cd = None
    for line in lines:
        if line.startswith("$ cd"):
            if line.strip() == "$ cd ..":
                cd = cd.parent
            else:
                name = line[5:].strip()
                if cd:
                    cd = cd.get_dir(name)
                else:
                    cd = Directory(name)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            cd.add_dir(Directory(line[4:].strip()))
        else:
            size, name = line.strip().split()
            cd.add_file(name, int(size))
    return cd.get_root()


with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    my_input = f.readlines()

answer(get_input(example).part1(), "Example 1", 95437)
answer(get_input(my_input).part1(), "Part 1")

# Advent of Code Day 11

# Parse Input
with open('input11.txt') as f:
    lines = f.readlines()

original_program = [int(string) for string in lines[0].strip().split(',')]

ast_map = [list(line.strip()) for line in lines]

def PrintMap(m):
    for j in range(len(ast_map)):
        for i in range(len(ast_map[0])):
            print(m[j][i], end="")
        print("")
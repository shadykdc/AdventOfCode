# Advent of Code Day 10

import math

# Parse Input
with open('input10.txt') as f:
    lines = f.readlines()

ast_map = [list(line.strip()) for line in lines]
print(ast_map)

def PrintMap(m, width, height):
    for j in range(height):
        for i in range(width):
            print(m[j][i], end="")
        print("")

def CountVisible(x, y, ast_map):
    ang_to_d = {}
    for j in range(len(ast_map)): # height
        for i in range(len(ast_map[0])): # width
            if ast_map[j][i] != "." and not (j==y and i==x):
                d = ((i-x)**2 + (j-y)**2)**(0.5)
                ang = math.degrees(math.atan2((x-i), (y-j)))
                if ang not in ang_to_d or ang_to_d[ang] > d:
                    ang_to_d[ang] = d
    return(len(list(ang_to_d)))


width = len(ast_map[0])
height = len(ast_map)

best_asteroid = (0, 0, 0) # x, y, asteroids visible

for j in range(height):
    for i in range(width):
        if ast_map[j][i] != ".":
            print(i, j)
            num = CountVisible(i, j, ast_map)
            ast_map[j][i] = num
            if best_asteroid[2] < num:
                best_asteroid = (i, j, num)

PrintMap(ast_map, width, height)
print(best_asteroid)
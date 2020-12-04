# Advent of Code Day 10

import math
from itertools import dropwhile

# Parse Input
with open('input10.txt') as f:
    lines = f.readlines()

ast_map = [list(line.strip()) for line in lines]

def GetAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def PrintMap(m):
    for j in range(len(ast_map)):
        for i in range(len(ast_map[0])):
            print(m[j][i], end="")
        print("")

def CountVisible(x, y, ast_map):
    ang_to_d = {}
    for j in range(len(ast_map)): # height
        for i in range(len(ast_map[0])): # width
            if ast_map[j][i] != "." and not (j==y and i==x):
                d = ((i-x)**2 + (j-y)**2)**(0.5)
                ang = GetAngle((i-x,y-j), (0,0), (1,0))
                if ang not in ang_to_d or ang_to_d[ang] > d:
                    ang_to_d[ang] = d
    return(len(list(ang_to_d)))


width = len(ast_map[0])
height = len(ast_map)

best_asteroid = (0, 0, 0) # x, y, asteroids visible

for j in range(height):
    for i in range(width):
        if ast_map[j][i] != ".":
            num = CountVisible(i, j, ast_map)
            if best_asteroid[2] < num:
                best_asteroid = (i, j, num)

print("Best: ", best_asteroid)

# Part 2
x = best_asteroid[0]
y = best_asteroid[1]
ast_map[y][x] = "X"

ang_to_d = {}
for j in range(len(ast_map)): # height
    for i in range(len(ast_map[0])): # width
        if ast_map[j][i] != "." and not (j==y and i==x):
            d = ((i-x)**2 + (j-y)**2)**(0.5)
            ang = GetAngle((i-x,y-j), (0,0), (1,0))
            if ang < 0:
                ang = 360 + ang
            if ang not in ang_to_d:
                ang_to_d[ang] = [(d, i, j)]
            else:
                ang_to_d[ang].append((d, i, j))
                sorted(ang_to_d[ang], key=lambda x: x[0])

vaporize_list = []
print("vaporizing...")
while len(ang_to_d) != 0:
    keys_to_delete = []
    sorted_angs = sorted(ang_to_d.keys())
    angs = []
    for key in sorted_angs:
        if key < 270:
            continue
        angs.append(key)
    for key in sorted_angs:
        if key >= 270:
            continue
        angs.append(key)
    for key in angs:
        tuple_list = ang_to_d[key]
        vaporize_list.append((tuple_list[-1][1], tuple_list[-1][2]))
        if len(tuple_list) == 1:
            keys_to_delete.append(key)
        else:
            tuple_list.pop()
    for key in keys_to_delete:
        del ang_to_d[key]

print(vaporize_list[199])
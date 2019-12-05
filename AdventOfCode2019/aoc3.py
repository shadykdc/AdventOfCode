# Advent of Code Day 3 - Crossed Wires

# Parse Input
with open('input3.txt') as f:
    lines = f.readlines()

str1 = lines[0]
str2 = lines[1]
wire1=str1.split(",") 
wire2=str2.split(",")

# Part 1
x1_sum = 0
x2_sum = 0
y1_sum = 0
y2_sum = 0
shortest_distance = 10000000

wire1_coords = []
wire2_coords = []
steps1 = 0
steps2 = 0
stepsmap1 = {}
stepsmap2 = {}

# Note: not proud of this one
for cmd1 in wire1:
    cmd_num = int(cmd1[1:])
    for move in range(1, cmd_num + 1):
        steps1 = steps1 + 1
        if cmd1[0] is 'D':
            wire1_coords.append((x1_sum, y1_sum - move))
            stepsmap1[(x1_sum, y1_sum-move)] = steps1
        elif cmd1[0] is 'R':
            wire1_coords.append((x1_sum + move, y1_sum))
            stepsmap1[(x1_sum + move, y1_sum)] = steps1
        elif cmd1[0] is 'U':
            wire1_coords.append((x1_sum, y1_sum + move))
            stepsmap1[(x1_sum, y1_sum + move)] = steps1
        elif cmd1[0] is 'L':
            wire1_coords.append((x1_sum - move, y1_sum))
            stepsmap1[(x1_sum - move, y1_sum)] = steps1
    if cmd1[0] is 'D':
        y1_sum = y1_sum - cmd_num
    if cmd1[0] is 'R':
        x1_sum = x1_sum + cmd_num
    if cmd1[0] is 'U':
        y1_sum = y1_sum + cmd_num
    if cmd1[0] is 'L':
        x1_sum = x1_sum - cmd_num

for cmd2 in wire2:
    cmd_num = int(cmd2[1:])
    for move in range(1, cmd_num + 1):
        steps2 = steps2 + 1
        if cmd2[0] is 'D':
            wire2_coords.append((x2_sum, y2_sum - move))
            stepsmap2[(x2_sum, y2_sum - move)] = steps2
        elif cmd2[0] is 'R':
            wire2_coords.append((x2_sum + move, y2_sum))
            stepsmap2[(x2_sum + move, y2_sum)] = steps2
        elif cmd2[0] is 'U':
            wire2_coords.append((x2_sum, y2_sum + move))
            stepsmap2[(x2_sum, y2_sum + move)] = steps2
        elif cmd2[0] is 'L':
            wire2_coords.append((x2_sum - move, y2_sum))
            stepsmap2[(x2_sum - move, y2_sum)] = steps2
    if cmd2[0] is 'D':
        y2_sum = y2_sum - cmd_num
    if cmd2[0] is 'R':
        x2_sum = x2_sum + cmd_num
    if cmd2[0] is 'U':
        y2_sum = y2_sum + cmd_num
    if cmd2[0] is 'L':
        x2_sum = x2_sum - cmd_num

first_set = set(wire1_coords)
second_set = set(wire2_coords)
least_steps = 100000000

intersections = first_set & second_set
for intersection in intersections:
    # distance = abs(intersection[0]) + abs(intersection[1]) - Part 1
    steps = stepsmap1[intersection] + stepsmap2[intersection]
    if steps < least_steps:
        least_steps = steps

print(least_steps)

# Part 1 Answer: 3247

# Part 2 Answer: 48054

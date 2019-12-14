# Advent of Code Day 11

import math
import copy

# Parse Input
with open('input11.txt') as f:
    lines = f.readlines()

class Moon:
    def __init__(self,x,y,z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]
        self.pot = 0
        self.kin = 0
        self.energy = self.pot + self.kin

class Node:
    def __init__(self, v, d):
        self.val = v
        self.depth = d
        self.children = {} # key=val, value=Node

# My Input
moon1 = Moon(-9,10,-1)
moon2 = Moon(-14,-8,14)
moon3 = Moon(1,5,6)
moon4 = Moon(-19,7,8)
xs = "-9,0,-14,0,1,0,-19,0,"
ys = "10,0,-8,0,5,0,7,0,"
zs = "-1,0,14,0,6,0,8,0,"

# Example 1
# moon1 = Moon(-1,0,2)
# moon2 = Moon(2,-10,-7)
# moon3 = Moon(4,-8,8)
# moon4 = Moon(3,5,-1)
# xs = "-1,0,2,0,4,0,3,0,"
# ys = "0,0,-10,0,-8,0,5,0,"
# zs = "2,0,-7,0,8,0,-1,0,"

# Example 2
# moon1 = Moon(-8,-10,0)
# moon2 = Moon(5,5,10)
# moon3 = Moon(2,-7,3)
# moon4 = Moon(9,-8,-3)

a = [xs, ys, zs]
old_moons = [moon1, moon2, moon3, moon4]

def Move(moon1, moon2, i):
    if moon1.pos[i] < moon2.pos[i]:
        moon2.vel[i] -= 1
        moon1.vel[i] += 1
    elif moon1.pos[i] > moon2.pos[i]:
        moon2.vel[i] += 1
        moon1.vel[i] -= 1

def UpdateVelocity(moons, i):
    for k in range(len(moons)):
        j = k + 1
        while j < len(moons):
            moon1 = moons[k]
            moon2 = moons[j]
            Move(moon1, moon2, i)
            j+=1

def UpdatePosition(moons, i):
    for moon in moons:
        moon.pos[i] += moon.vel[i]

def BackAtTheStart(moons, i):
    position = ""
    for moon in moons:
        position += str(moon.pos[i]) + ","
        position += str(moon.vel[i]) + ","
    if position == a[i]:
        return True
    return False

# Part 2
times = [0, 0, 0]
for i in range(3): # each axis
    moons = copy.deepcopy(old_moons)
    while True:
        times[i] += 1
        position = ""
        for moon in moons:
            position += str(moon.pos[i]) + ","
            position += str(moon.vel[i]) + ","
        UpdateVelocity(moons, i)
        UpdatePosition(moons, i)
        if BackAtTheStart(moons, i):
            print(times[i])
            break

times = [times[0], times[1], times[2]]
out = times[0]*times[1]/math.gcd(times[0], times[1])
out = int(out)*times[2]/math.gcd(int(out), times[2])
print(int(out))

# Part 1
# total_energy = 0
# for moon in moons:
#     moon.pot = abs(moon.pos[0]) + abs(moon.pos[1]) + abs(moon.pos[2])
#     moon.kin = abs(moon.vel[0]) + abs(moon.vel[1]) + abs(moon.vel[2])
#     moon.energy = moon.pot * moon.kin
#     total_energy += moon.energy
# print(total_energy)

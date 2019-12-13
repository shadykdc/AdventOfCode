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
# moon1 = Moon(-9,10,-1)
# moon2 = Moon(-14,-8,14)
# moon3 = Moon(1,5,6)
# moon4 = Moon(-19,7,8)

# Example 1
moon1 = Moon(-1,0,2)
moon2 = Moon(2,-10,-7)
moon3 = Moon(4,-8,8)
moon4 = Moon(3,5,-1)

# Example 2
# moon1 = Moon(-8,-10,0)
# moon2 = Moon(5,5,10)
# moon3 = Moon(2,-7,3)
# moon4 = Moon(9,-8,-3)

old_moons = [moon1, moon2, moon3, moon4]

def Move(moon1, moon2, i):
    if moon1.pos[i] < moon2.pos[i]:
        moon2.vel[i] -= 1
        moon1.vel[i] += 1
    elif moon1.pos[i] > moon2.pos[i]:
        moon2.vel[i] += 1
        moon1.vel[i] -= 1

def UpdateVelocity(moons, i):
    for i in range(len(moons)):
        j = i + 1
        while j < len(moons):
            moon1 = moons[i]
            moon2 = moons[j]
            Move(moon1, moon2, i)
            j+=1

def UpdatePosition(moons, i):
    for moon in moons:
        moon.pos[i] += moon.vel[i]

def PositionIsOld(moons, d, i):
    position = ""
    for moon in moons:
        position += str(moon.pos[i]) + ","
        position += str(moon.vel[i]) + ","
    if position in d:
        return True
    d[position] = True
    return False

# Part 2
times = [0, 0, 0]
for i in range(3): # each axis
    d = {}
    moons = copy.deepcopy(old_moons)
    while True:
        times[i] += 1
        if(times[i] == 2):
            position = ""
            for moon in moons:
                position += str(moon.pos[i]) + ","
                position += str(moon.vel[i]) + ","
            print(position)
        UpdateVelocity(moons, i)
        UpdatePosition(moons, i)
        if PositionIsOld(moons, d, i):
            break
err = 1
times = [times[0]-err, times[1]-err, times[2]-err]
out = times[0]*times[1]/math.gcd(times[0], times[1])
out = int(out)*times[2]/math.gcd(int(out), times[2])
print(times)
print(out)

# Part 1
# total_energy = 0
# for moon in moons:
#     moon.pot = abs(moon.pos[0]) + abs(moon.pos[1]) + abs(moon.pos[2])
#     moon.kin = abs(moon.vel[0]) + abs(moon.vel[1]) + abs(moon.vel[2])
#     moon.energy = moon.pot * moon.kin
#     total_energy += moon.energy
# print(total_energy)

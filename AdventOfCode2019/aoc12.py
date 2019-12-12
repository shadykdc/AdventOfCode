# Advent of Code Day 11

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

moons = [moon1, moon2, moon3, moon4]

def Move(moon1, moon2):
    if moon1.pos[0] < moon2.pos[0]:
        moon2.vel[0] -= 1
        moon1.vel[0] += 1
    elif moon1.pos[0] > moon2.pos[0]:
        moon2.vel[0] += 1
        moon1.vel[0] -= 1
    if moon1.pos[1] < moon2.pos[1]:
        moon2.vel[1] -= 1
        moon1.vel[1] += 1
    elif moon1.pos[1] > moon2.pos[1]:
        moon2.vel[1] += 1
        moon1.vel[1] -= 1
    if moon1.pos[2] < moon2.pos[2]:
        moon2.vel[2] -= 1
        moon1.vel[2] += 1
    elif moon1.pos[2] > moon2.pos[2]:
        moon2.vel[2] += 1
        moon1.vel[2] -= 1

# Update Velocity (Gravity)
def UpdateVelocity(moons):
    for i in range(4):
        j = i + 1
        while j < 4:
            moon1 = moons[i]
            moon2 = moons[j]
            Move(moon1, moon2)
            j+=1

def UpdatePosition(moons):
    for moon in moons:
        moon.pos[0] += moon.vel[0]
        moon.pos[1] += moon.vel[1]
        moon.pos[2] += moon.vel[2]

def NewNode(vals, depth):
    if depth < len(vals)-1:
        new_node = Node(vals[depth], depth)
        new_node.children[vals[depth]] = NewNode(vals, depth+1)
        return new_node
    return None

def CheckChildren(kids, vals, depth):
    val = vals[depth]
    if val in kids:
        if depth == 21:
            return False
        return CheckChildren(kids[val].children, vals, depth+1)
    kids[val] = NewNode(vals, depth)
    return True

# Part 2
time = 0
children = {}
keep_going = True
while keep_going:
    time += 1
    vals = [moons[0].pos[0], moons[0].pos[1], moons[0].pos[2], \
            moons[0].vel[0], moons[0].vel[1], moons[0].vel[2], \
            moons[1].pos[0], moons[1].pos[1], moons[1].pos[2], \
            moons[1].vel[0], moons[1].vel[1], moons[1].vel[2], \
            moons[2].pos[0], moons[2].pos[1], moons[2].pos[2], \
            moons[2].vel[0], moons[2].vel[1], moons[2].vel[2], \
            moons[3].pos[0], moons[3].pos[1], moons[3].pos[2], \
            moons[3].vel[0], moons[3].vel[1], moons[3].vel[2]]
    keep_going = CheckChildren(children, vals, 0)
    UpdateVelocity(moons)
    UpdatePosition(moons)
print(time)

# Part 1
# total_energy = 0
# for moon in moons:
#     moon.pot = abs(moon.pos[0]) + abs(moon.pos[1]) + abs(moon.pos[2])
#     moon.kin = abs(moon.vel[0]) + abs(moon.vel[1]) + abs(moon.vel[2])
#     moon.energy = moon.pot * moon.kin
#     total_energy += moon.energy
# print(total_energy)

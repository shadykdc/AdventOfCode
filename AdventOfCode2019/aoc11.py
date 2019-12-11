# Advent of Code Day 11

# Parse Input
with open('input11.txt') as f:
    lines = f.readlines()

original_program = [int(string) for string in lines[0].strip().split(',')]
for i in range(100000):
    original_program.append(0)

from itertools import permutations 

class Computer:
    def __init__(self, prog):
        self.program = prog.copy()
        self.in_put = 0
        self.out_put = []
        self.ip = 0 # instruction pointer
        self.halt = False
        self.rb = 0 # relative base
    
    def RunProgram(self):
        self.out_put = []
        while self.ip < len(self.program):
            modes = [] # modes: 0 = position, 1 = value, 2 = relative base
            opcode = self.program[self.ip]
            if opcode in {1, 2, 3, 4, 5, 6, 7, 8, 9, 99}:
                # Position Mode (Default)
                modes = [0, 0, 0]
            else:
                # Immediate (Value) or Relative Base Mode
                li = [int(d) for d in str(self.program[self.ip])]
                while len(li) < 5:
                    li = [0] + li
                opcode = abs(self.program[self.ip]%100)
                modes = [li[-3], li[-4], li[-5]]
            if opcode not in {1, 2, 3, 4, 5, 6, 7, 8, 9, 99}:
                print("ERROR op code: ", opcode)
                return
            self.PerformOpCode(opcode, modes)
            if opcode == 99 or len(self.out_put) == 2:
                return self.out_put

    # Returns true if it hit a HALT
    def PerformOpCode(self, opcode, modes):
        a = 0
        if (self.ip < len(self.program) - 1):
            a = self.program[self.ip+1]
        b = 0
        if (self.ip < len(self.program) - 2):
            b = self.program[self.ip+2]
        c = 0
        if (self.ip < len(self.program) - 3):
            c = self.program[self.ip+3]
            if modes[2] == 2:
                c = c + self.rb
        if opcode == 1:
            # Add and Store
            if modes[0] == 0:
                a = self.program[a]
            elif modes[0] == 2:
                a = self.program[a + self.rb]
            if modes[1] == 0:
                b = self.program[b]
            elif modes[1] == 2:
                b = self.program[b + self.rb]
            self.program[c] = a + b
            self.ip = self.ip + 4
        elif opcode == 2:
            # Multiply and Store
            if modes[0] == 0:
                a = self.program[a]
            elif modes[0] == 2:
                a = self.program[a + self.rb]
            if modes[1] == 0:
                b = self.program[b]
            elif modes[1] == 2:
                b = self.program[b + self.rb]
            self.program[c] = a * b
            self.ip = self.ip + 4
        elif opcode == 3:
            # Input
            if modes[0] == 2:
                a = a + self.rb
            self.program[a] = self.in_put
            self.ip = self.ip + 2
        elif opcode == 4:
            # out_put
            if modes[0] == 1:
                self.out_put.append(a)
            elif modes[0] == 2:
                self.out_put.append(self.program[a + self.rb])
            else:
                self.out_put.append(self.program[a])
            self.ip = self.ip + 2
            if (len(self.out_put) == 2):
                return self.out_put
        elif opcode == 5:
            # Jump if true
            if modes[0] == 0:
                a = self.program[a]
            elif modes[0] == 2:
                a = self.program[a + self.rb]
            if a != 0:
                if modes[1] == 0:
                    b = self.program[b]
                if modes[1] == 2:
                    b = self.program[b + self.rb]
                self.ip = b
            else:
                self.ip = self.ip + 3
        elif opcode == 6:
            # Jump if false
            if modes[0] == 0:
                a = self.program[a]
            elif modes[0] == 2:
                a = self.program[a + self.rb]
            if a == 0:
                if modes[1] == 0:
                    b = self.program[b]
                if modes[1] == 2:
                    b = self.program[b + self.rb]
                self.ip = b
            else:
                self.ip = self.ip + 3
        elif opcode == 7:
            # less than
            if modes[0] == 0:
                a = self.program[a]
            elif modes[0] == 2:
                a = self.program[a + self.rb]
            if modes[1] == 0:
                b = self.program[b]
            elif modes[1] == 2:
                b = self.program[b + self.rb]
            if a < b:
                self.program[c] = 1
            else:
                self.program[c] = 0
            self.ip = self.ip + 4
        elif opcode == 8:
            # equals
            if modes[0] == 0:
                a = self.program[a]
            elif modes[0] == 2:
                a = self.program[a + self.rb]
            if modes[1] == 0:
                b = self.program[b]
            elif modes[1] == 2:
                b = self.program[b + self.rb]
            if a == b:
                self.program[c] = 1
            else:
                self.program[c] = 0
            self.ip = self.ip + 4
        elif opcode == 9:
            # Relative Base
            if modes[0] == 0:
                a = self.program[a]
            if modes[0] == 2:
                a = self.program[a + self.rb]
            self.rb = self.rb + a
            self.ip += 2
        elif opcode == 99:
            # Halt
            self.halt = True
            return

def Move(pos, dir):
    if dir == 0:
        pos = (pos[0] + 1, pos[1])
    elif dir == 90 or dir == -270:
        pos = (pos[0], pos[1] + 1)
    elif dir == 180 or dir == -180:
        pos = (pos[0] - 1, pos[1])
    elif dir == 270 or dir == -90:
        pos = (pos[0], pos[1] - 1)
    return pos

def PrintMap(m):
    for j in range(len(m)):
        for i in range(len(m[0])):
            print(m[j][i], end="")
        print("")

# Part 1
pos = (0, 0)
intcomp = Computer(original_program)
count = 0
dir = 90
mp = {}
mp[pos] = '.'
while not intcomp.halt:
    intcomp.in_put = 0 # '.'
    if pos not in mp:
        mp[pos] = '.'
    if mp[pos] == '#':
        intcomp.in_put = 1
    out = intcomp.RunProgram()
    # Paint
    if len(out) != 2:
        break
    if out[0] == 0:
        mp[pos] = '.'
    elif out[0] == 1:
        mp[pos] = '#'
    # Move
    if out[1] == 0:
        # Turn Left
        dir = dir + 90
    elif out[1] == 1:
        # Turn Right
        dir = dir - 90
    if dir == -360 or dir == 360:
        dir = 0
    pos = Move(pos, dir)

print(len(mp.keys()))
# 1565 is wrong
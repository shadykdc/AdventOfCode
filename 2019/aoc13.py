#Advent of Code Day 13

# Parse Input
with open('input13.txt') as f:
    lines = f.readlines()

original_program = [int(string) for string in lines[0].strip().split(',')]
for i in range(100000):
    original_program.append(0)

def PrintMap(m):
    for j in range(len(m)):
        for i in range(len(m[0])):
            print(m[j][i], end="")
        print("")

class Computer:
    def __init__(self, prog):
        self.program = prog.copy()
        self.in_put = 0
        self.out_put = []
        self.ip = 0 # instruction pointer
        self.halt = False
        self.rb = 0 # relative base
        self.score = 0
        self.mp = [[" " for i in range(100)] for _ in range(100)]
        self.px = 0
        self.bx = 0
    
    def RunProgram(self):
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
            if len(self.out_put) == 3:
                print(self.out_put)
                self.bx = self.out_put[0]
                self.score += self.out_put[2]
                return self.out_put
            if opcode == 99:
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
            self.in_put = 0
            if self.bx < self.px:
                self.in_put = -1
            elif self.bx > self.px:
                self.in_put = 1
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
            if (len(self.out_put) == 3):
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
    
    def AdjustMap(self):
        x = comp.out_put[0]
        y = comp.out_put[1]
        tile_id = comp.out_put[2]
        if self.mp[y][x] in {"W","P"}:
            return
        elif tile_id == 0 and (x,y) not in self.mp: # empty
            self.mp[y][x] = " "
        elif tile_id == 1: # wall
            self.mp[y][x] = "W"
        elif tile_id == 2: # block
            self.mp[y][x] = "B"
        elif tile_id == 3: #horizontal paddle
            self.mp[y][x] = "P"
            self.px = x
        elif tile_id == 4: # ball
            self.mp[y][x] = "."
            self.bx = x


comp = Computer(original_program)

# Part 1
while comp.halt == False:
    out = comp.out_put
    if len(comp.out_put) == 3:
        comp.AdjustMap()
        comp.out = []
    comp.RunProgram()

count = 0
for i in range(100):
    for j in range(100):
        if comp.mp[i][j] == 2:
            count += 1

# Part 2
comp2 = Computer(original_program)
comp2.program[0] = 2
comp2.mp = comp.mp
while comp2.halt == False:
    comp2.out_put = []
    comp2.RunProgram()
PrintMap(comp2.mp)
print(comp2.score)
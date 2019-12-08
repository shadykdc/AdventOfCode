from itertools import permutations 

with open('C:\\Users\\kathr\\Code\\AdventOfCode\\AdventOfCode2019\\input7.txt') as f:
    lines = f.readlines()

original_program = [int(c) for c in lines[0].strip().split(",")]
in_put = 0

class Amplifier:
    def __init__(self, prog):
        self.program = prog.copy()
        self.in_put = 0
        self.out_put = 0
        self.ip = 2
        self.halt = False
    
    def RunProgram(self):
        while self.ip < len(self.program):
            modes = []
            opcode = self.program[self.ip]
            if opcode in {1, 2, 3, 4, 5, 6, 7, 8, 99}:
                # Position Mode
                modes = [0, 0, 0]
            else:
                # Immediate Mode
                li = [int(d) for d in str(self.program[self.ip])]
                while len(li) < 5:
                    li = [0] + li
                opcode = abs(self.program[self.ip]%100)
                modes = [li[-3], li[-4], li[-5]]
            if opcode not in {1, 2, 3, 4, 5, 6, 7, 8, 99}:
                print("ERROR op code: ", opcode)
                return
            self.PerformOpCode(opcode, modes)
            if opcode == 99 or opcode == 4:
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
        if opcode == 1:
            # Add and Store
            if modes[0] == 0:
                a = self.program[a]
            if modes[1] == 0:
                b = self.program[b]
            self.program[c] = a + b
            self.ip = self.ip + 4
        elif opcode == 2:
            # Multiply and Store
            if modes[0] == 0:
                a = self.program[a]
            if modes[1] == 0:
                b = self.program[b]
            self.program[c] = a * b
            self.ip = self.ip + 4
        elif opcode == 99:
            # Halt
            self.halt = True
            return
        elif opcode == 3:
            # Input
            self.program[a] = self.in_put
            self.ip = self.ip + 2
        elif opcode == 4:
            # out_put
            if modes[0] == 1:
                self.out_put = a
            else:
                self.out_put = self.program[a]
            self.ip = self.ip + 2
        elif opcode == 5:
            # Jump if true
            if modes[0] == 0:
                a = self.program[a]
            if a != 0:
                if modes[1] == 0:
                    b = self.program[b]
                self.ip = b
            else:
                self.ip = self.ip + 3
        elif opcode == 6:
            # Jump if false
            if modes[0] == 0:
                a = self.program[a]
            if a == 0:
                if modes[1] == 0:
                    b = self.program[b]
                self.ip = b
            else:
                self.ip = self.ip + 3
        elif opcode == 7:
            # less than
            if modes[0] == 0:
                a = self.program[a]
            if modes[1] == 0:
                b = self.program[b]
            self.program[c] = 0
            if a < b:
                self.program[c] = 1
            self.ip = self.ip + 4
        elif opcode == 8:
            # equals
            if modes[0] == 0:
                a = self.program[a]
            if modes[1] == 0:
                b = self.program[b]
            self.program[c] = 0
            if a == b:
                self.program[c] = 1
            self.ip = self.ip + 4
       
# Part 1
"""
phases = permutations([0, 1, 2, 3, 4])
max_output = 0
for phase_tuple in phases:
    in_put = 0
    amplifiers = [Amplifier(original_program, list(phase_tuple)[0]), \
        Amplifier(original_program, list(phase_tuple)[1]), \
        Amplifier(original_program, list(phase_tuple)[2]), \
        Amplifier(original_program, list(phase_tuple)[3]), \
        Amplifier(original_program, list(phase_tuple)[4])]
    for idx in range(5):
        phase = list(phase_tuple)[idx]
        amp = amplifiers[idx]
        amp.in_put.append(phase)
        print(amp.program)
        amp.RunProgram()
        amp.ip = 2
        in_put = amplifiers[idx].out_put
    if amplifiers[4].out_put > max_output:
        max_output = in_put
print(max_output)
"""

# Part 2
phases = permutations([5, 6, 7, 8, 9])
max_output = 0
ret = -1
for phase_tuple in phases:
    phase_list = list(phase_tuple)
    amplifiers = [Amplifier(original_program.copy()) for _ in range(5)]
    for amp, phase in zip(amplifiers, phase_list):
        amp.program[amp.program[1]] = phase
    in_put = 0
    while(not amplifiers[-1].halt):
        for idx, amp in enumerate(amplifiers):
            amp.in_put = in_put
            in_put = amp.RunProgram()
        max_output = max(amp.out_put, max_output)
print(max_output)
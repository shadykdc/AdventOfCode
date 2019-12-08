from itertools import permutations 

with open('input7.txt') as f:
    lines = f.readlines()

original_program = [int(c) for c in lines[0].strip().split(",")]
in_put = 0

class Amplifier:
    def __init__(self, prog):
        self.program = prog
        self.input = 0
        self.output = 0
        self.ip = 0
    
    def RunProgram():
        ip = 0
        while ip < len(program):
            modes = []
            opcode = program[ip]
            if opcode in {1, 2, 3, 4, 5, 6, 7, 8, 99}:
                # Position Mode
                modes = [0, 0, 0]
            else:
                # Immediate Mode
                li = [int(d) for d in str(program[ip])]
                while len(li) < 5:
                    li = [0] + li
                opcode = abs(program[ip]%100)
                modes = [li[-3], li[-4], li[-5]]
            if opcode not in {1, 2, 3, 4, 5, 6, 7, 8, 99}:
                # Error
                return 0
            if PerformOpCode(opcode, modes):
                # HALT
                return 1
        # Keep going?
        return 2

    # Returns true if it hit a HALT
    def PerformOpCode(opcode, modes):
        a = 0
        if (i < len(nums) - 1):
            a = nums[i+1]
        b = 0
        if (i < len(nums) - 2):
            b = nums[i+2]
        c = 0
        if (i < len(nums) - 3):
            c = nums[i+3]
        if opcode == 1:
            # Add and Store
            if modes[0] == 0:
                a = nums[a]
            if modes[1] == 0:
                b = nums[b]
            nums[c] = a + b
            i = i + 4
        elif opcode == 2:
            # Multiply and Store
            if modes[0] == 0:
                a = nums[a]
            if modes[1] == 0:
                b = nums[b]
            nums[c] = a * b
            i = i + 4
        elif opcode == 99:
            # Halt
            return True
        elif opcode == 3:
            # Input 
            nums[a] = in_put
            i = i + 2
        elif opcode == 4:
            # Output
            if modes[0] == 1:
                out_put = a
            else:
                out_put = nums[a]
            i = i + 2
        elif opcode == 5:
            # Jump if true
            if modes[0] == 0:
            a = nums[a]
            if a != 0:
                if modes[1] == 0:
                    b = nums[b]
                i = b
            else:
                i = i + 3
        elif opcode == 6:
            # Jump if false
            if modes[0] == 0:
                a = nums[a]
            if a == 0:
                if modes[1] == 0:
                    b = nums[b]
                i = b
            else:
                i = i + 3
        elif opcode == 7:
            # less than
            if modes[0] == 0:
                a = nums[a]
            if modes[1] == 0:
                b = nums[b]
            nums[c] = 0
            if a < b:
                nums[c] = 1
            i = i + 4
        elif opcode == 8:
            # equals
            if modes[0] == 0:
                a = nums[a]
            if modes[1] == 0:
                b = nums[b]
            nums[c] = 0
            if a == b:
                nums[c] = 1
            i = i + 4
        return False

def Amplify(amp, phase, in_put):
    amp.program[1] = phase
    amp.input = in_put
    return amp.RunProgram()

# Part 1
phases = permutations([0, 1, 2, 3, 4])
Apmlifier a = Amplifier(original_program)
Apmlifier b = Amplifier(original_program)
Apmlifier c = Amplifier(original_program)
Apmlifier d = Amplifier(original_program)
Apmlifier e = Amplifier(original_program)
amplifiers = [a, b, c, d, e]

for idx, phase in enumerate(phases):
    phase = list(phase)
    Amplify(amplifiers[idx], phase, in_put)

def FeedbackLoop(init):
    phases = permutations([5, 6, 7, 8, 9])
    for phase in phases:
        phase = list(phase)
        phase = [9, 8, 7, 6, 5]
        out_put = init
        for idx in range(0,5):
            in_put = out_put
            nums = amplifiers_nums[idx]
            nums[nums[1]] = phase[idx]
            i = 2
            print(nums)
            ret = RunProgram()
            if ret == 0:
                print("Error")
                return
            elif ret == 1:
                print("HALT")
                if out_put > max_out_put:
                    max_out_put = out_put
                    return
            elif ret == 2:
                print("Amplifying")
                Amplify(out_put)

# Part 2
phases = permutations([5, 6, 7, 8, 9])
Apmlifier a = Amplifier(original_program)
Apmlifier b = Amplifier(original_program)
Apmlifier c = Amplifier(original_program)
Apmlifier d = Amplifier(original_program)
Apmlifier e = Amplifier(original_program)
amplifiers = [a, b, c, d, e]

for amp in amplifiers:

print(max_out_put)
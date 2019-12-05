# Advent of Code Day 5

# Parse Input
with open('input5.txt') as f:
    lines = f.readlines()

# Globals
nums = [int(char) for  char in lines[0].split(",")]
in_put = 5
out_put = 0
i = 0

def PerformOpCode(opcode, modes):
    global nums
    global in_put
    global out_put
    global i
    a = 0
    if (i < len(nums) - 1):
        a = nums[i+1]
    b = 0
    if (i < len(nums) - 2):
        b = nums[i+2]
    c = 0
    if (i < len(nums) - 3):
        c = nums[i+3]
    if (opcode == 6 and a == 12 and b == 15 and c == 1 and i == 2):
        return True
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
        print("HALT")
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

def IntCompute():
    global nums
    global in_put
    global out_put
    global i
    while i < len(nums):
        modes = []
        opcode = nums[i]
        if opcode in {1, 2, 3, 4, 5, 6, 7, 8, 99}:
            # Position Mode
            modes = [0, 0, 0]
        else:
            # Immediate Mode
            li = [int(d) for d in str(nums[i])]
            while len(li) < 5:
                li = [0] + li
            opcode = abs(nums[i]%100)
            modes = [li[-3], li[-4], li[-5]]
        if PerformOpCode(opcode, modes):
            return True
    return False

if IntCompute():
    print(out_put)
else:
    print("error?")

# 16209841 was the answer to Part 1
# 8834787 is the answer to Part 2
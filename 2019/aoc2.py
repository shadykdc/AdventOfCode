# Advent of Code Day 2 - Intcode Computers

# Parse Input
with open('input2.txt') as f:
    text = f.readlines()

string = text[0]
str_nums=string.split(",")

nums = []
for char in str_nums:
    nums.append(int(char))

def IntCompute(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 1:
            # Add and Store
            idx1 = nums[i + 1]
            idx2 = nums[i + 2]
            idx3 = nums[i + 3]
            nums[idx3] = nums[idx1] + nums[idx2]
            i = i + 4
        elif nums[i] == 2:
            # Multiply and Store
            idx1 = nums[i + 1]
            idx2 = nums[i + 2]
            idx3 = nums[i + 3]
            nums[idx3] = nums[idx1] * nums[idx2]
            i = i + 4
        elif nums[i] == 99:
            # Halt
            return nums[0]
        else:
            return -1

    # Not sure what to do without a halt, throw error?
    return nums[0]

# Part 1
nums[1] = 12
nums[2] = 2
copy = nums.copy()
print("PART 1")
print("Solution: " + str(IntCompute(copy)))
# Answer: 3790645

# Part 2
print("PART 2")
magic_num = 19690720
for noun in range(0, 100):
    for verb in range(0, 100):
        nums[1] = noun
        nums[2] = verb
        copy = nums.copy()
        IntCompute(copy)
        if (copy[0] == magic_num):
            print("Zero Position: " + str(copy[0]))
            print("Noun: " + str(noun))
            print("Verb: " + str(verb))
            # Solution is 100 * noun + verb = 6577
            print("Solution: " + str(noun * 100 + verb))
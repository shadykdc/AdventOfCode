# Advent of Code Day 4 - Secure Container

def NumHasPair(n):
    # convert num to list of digits
    l = [int(d) for d in str(n)]
    # check for pairs
    for i in range(0, 5):
        if l[i] == l[i+1]:
            # For Part 2, add these two if statements
            if i > 0 and l[i-1] == l[i]:
                continue
            if i < 4 and l[i+1] == l[i+2]:
                continue
            return True
    return False

def NoDecreasing(n):
    # convert num to list of digits
    l = [int(d) for d in str(n)]
    # check for decreasing digits
    for i in range(0, 5):
        if l[i] > l[i+1]:
            return False
    return True

# Input
minimum = 245318
maximum = 765747

count = 0
for num in range(minimum, maximum + 1):
    if NumHasPair(num) and NoDecreasing(num):
        count = count + 1

print(count)
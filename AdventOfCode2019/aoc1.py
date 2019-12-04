# Advent of Code Day 1

with open('input1.txt') as f:
    lines = f.readlines()

# Part 2
def CalculateModuleFuelFuel(mass):
    fuel = mass
    plus_fuel = (fuel // 3) - 2
    while (plus_fuel > 0):
        fuel = fuel + plus_fuel
        plus_fuel = (plus_fuel//3) - 2
    return fuel - mass

# Part 1
out = 0
for line in lines:
    mass = int(line.strip())
    module_fuel = (mass // 3) - 2
    out = out + module_fuel
    # Part 1 Solution: 3229279
    # Part 2
    out = out + CalculateModuleFuelFuel(module_fuel)
    # Part 2 Solution: 4841054

print(out)

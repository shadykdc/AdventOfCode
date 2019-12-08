# Advent of Code Day 9

# Parse Input
with open('input9.txt') as f:
    lines = f.readlines()

list_of_digits = [int(ch) for ch in lines[0].strip()]
# Advent of Code Day 8 - Space Image Format

# Parse Input
with open('input8.txt') as f:
    lines = f.readlines()

password = [int(ch) for ch in lines[0].strip()]

width = 25
height = 6
total = len(password)
layers = int(total / width / height)

def Multiply(layer):
    ones_count = 0
    twos_count = 0
    for pixel in layer:
        if pixel == 1:
            ones_count = ones_count + 1
        elif pixel == 2:
            twos_count = twos_count + 1
    return ones_count * twos_count

min_zero_count_layer = [None, 100000000] # layer, count

for idx in range(0, layers):
    start = idx * width * height
    end = (idx + 1) * width * height
    layer = password[start:end]
    zeroes_count = 0
    for pixel in layer:
        if pixel == 0:
            zeroes_count = zeroes_count + 1
    if min_zero_count_layer[1] > zeroes_count:
        min_zero_count_layer[0] = layer
        min_zero_count_layer[1] = zeroes_count

# Part 1 = 1848
print(Multiply(min_zero_count_layer[0]))


def PrintImage(image):
    for idx, ch in enumerate(image):
        if idx%width == 0:
            print(' ')
        if ch == "0":
            print(' ', end=" ")
        else:
            print(ch, end=" ")

def Decode(password):
    image = [" " for i in range(width*height)]
    # 0 = black, 1 = white, 2 = transparent
    for i in range(height * width):
        idx = 0
        while idx < layers:
            pw_idx = i + idx * width * height
            img_idx = i
            current_value = password[pw_idx]
            if current_value == 2:
                idx = idx + 1
            else:
                image[img_idx] = str(current_value)
                break
    PrintImage(image)

# Part 2 = FGJUZ
Decode(password)
def get_input(name):
    with open(name, 'r') as f:
        line = f.readline().strip()
        f.readline()
        img = [[ch for ch in row.strip()] for row in f.readlines()]
    return line, img

img_algo, img = get_input('input20.txt')
ex_algo, ex_img = get_input('input20.1.txt')

def print_img(img):
    for row in img:
        print("".join(row))
    print(" ")

def get_number(img, i, j, zero='.', one='#'):
    hashdots = [
        zero
        if x < 0 or x >= len(img[0]) or y < 0 or y >= len(img)
        else img[y][x]
        for y in range(j-1, j+2)
        for x in range(i-1, i+2)
    ]
    return int("".join(hashdots).replace(zero, "0").replace(one, "1"), 2)

assert(get_number(ex_img, 2, 2) == 34)

def enhance(img_algo, img, zero='.', one='#'):
    return [[
        img_algo[get_number(img, i, j, zero, one)]
        for i in range(len(img[0]))
        ] for j in range(len(img))
    ]

def count_pixels(img, val="#"):
    count = 0
    for row in img:
        count += row.count(val)
    return count

assert(count_pixels([["#", ".", "."],[".", "#", "."]]) == 2)

def pad_image(img, pad=2, val="."):
    pad = [val] * pad
    for idx, row in enumerate(img):
        img[idx] = pad + row + pad
    for _ in range(len(pad)):
        img.insert(0, [val for _ in range(len(img[0]))])
        img.append([val for _ in range(len(img[0]))])

def depad_image(img, pad=1):
    for idx, row in enumerate(img):
        img[idx] = row[pad:len(row)-pad]
    img = img[pad:len(img)-pad]

def solution(algo, in_img, steps=2):
    img = [[ch for ch in row] for row in in_img]
    print_img(img)
    zero, one = '.', '#'
    for step in range(steps):
        zero = algo[-1] if steps % 2 else algo[0]
        one = algo[0] if steps % 2 else algo[-1]
        pad_image(img, 1, zero)
        print_img(img)
        img = enhance(algo, img, zero, one)
        print_img(img)
    return count_pixels(img, one)

assert(solution(ex_algo, ex_img, 2) == 35)
assert(solution(ex_algo, ex_img, 50) == 3351)
p1 = solution(img_algo, img)
print(p1)
assert(p1 == 5379)

# print(f"Part One: {p1}")
# p2 = solution(img_algo, img, 50)
# print(f"Part Two: {p2}")
# assert(p2 < 19343)

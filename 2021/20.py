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

def get_number(img, i, j, zero):
    hashdots = [
        img[y][x]
        for y in range(j-1, j+2)
        for x in range(i-1, i+2)
    ]
    return int("".join(hashdots).replace('.', "0").replace('#', "1"), 2)

def enhance(img_algo, img, zero):
    return [[
        img_algo[get_number(img, i, j, zero)]
        for i in range(1, len(img[0])-1)
        ] for j in range(1, len(img)-1)
    ]

def count_pixels(img, val="#"):
    count = 0
    for row in img:
        count += row.count(val)
    return count

def pad_image(img, pad=2, val="."):
    pad = [val] * pad
    for idx, row in enumerate(img):
        img[idx] = pad + row + pad
    for _ in range(len(pad)):
        img.insert(0, [val for _ in range(len(img[0]))])
        img.append([val for _ in range(len(img[0]))])

def solution(algo, in_img, steps=2):
    img = [[ch for ch in row] for row in in_img]
    for step in range(steps):
        print(f"step {step}")
        zero = '#' if not steps % 2 and algo[0] == '#' else '.'
        pad_image(img, 2, zero)
        print_img(img)
        img = enhance(algo, img, zero)
        print_img(img)
    return count_pixels(img)

assert(solution(ex_algo, ex_img, 2) == 35)
p1 = solution(img_algo, img)
print(f"Part One: {p1}")
assert(p1 == 5379)

assert(solution(ex_algo, ex_img, 50) == 3351)
p2 = solution(img_algo, img, 50)
print(f"Part Two: {p2}")
assert(p2 < 19343)
assert(p2 > 17704)

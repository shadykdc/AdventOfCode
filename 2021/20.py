ZERO = '0'
ONE = '1'

def get_input(name):
    with open(name, 'r') as f:
        line = [ZERO if ch == "." else ONE for ch in f.readline().strip()]
        f.readline()
        img = [[ZERO if ch == "." else ONE for ch in row.strip()] for row in f.readlines()]
    return line, img

img_algo, img = get_input('input20.txt')
ex_algo, ex_img = get_input('input20.1.txt')

def print_img(img):
    for row in img:
        print("".join(['.' if ch == ZERO else '#' for ch in row]))
    print(" ")

def get_number(img, i, j, default):
    binarystr = [
        default if x not in range(0, len(img[0])) or y not in range(0, len(img))
        else img[y][x]
        for y in range(j-1, j+2)
        for x in range(i-1, i+2)
    ]
    return int("".join(binarystr), 2)

def enhance(img_algo, img, default):
    return [
        [img_algo[get_number(img, i, j, default)] for i in range(len(img[0]))]
        for j in range(len(img))
    ]

def count_pixels(img):
    return sum([sum([int(ch) for ch in row]) for row in img])

def pad_image(img, val=ZERO, times=1):
    pad = [val] * times
    for idx, row in enumerate(img):
        img[idx] = pad + row + pad
    for _ in range(len(pad)):
        img.insert(0, [val for _ in range(len(img[0]))])
        img.append([val for _ in range(len(img[0]))])

def solution(algo, in_img, steps=2):
    img = [[ch for ch in row] for row in in_img]
    pad_image(img, val=ZERO, times=steps)
    for step in range(steps):
        default = ZERO if not step % 2 or algo[0] == ZERO else ONE
        img = enhance(algo, img, default)
    return count_pixels(img)

assert(solution(ex_algo, ex_img) == 35)
p1 = solution(img_algo, img)
print(f"Part One: {p1}")
assert(p1 == 5379)

assert(solution(ex_algo, ex_img, 50) == 3351)
p2 = solution(img_algo, img, 50)
print(f"Part Two: {p2}")
assert(p2 == 17917)

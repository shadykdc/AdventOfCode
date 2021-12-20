def get_input(name):
    with open(name, 'r') as f:
        line = f.readline()
        f.readline()
        img = [[ch for ch in row.strip()] for row in f.readlines()]
    return line, img

img_algo, img = get_input('input20.txt')
ex_algo, ex_img = get_input('input20.1.txt')

def get_number(img, i, j):
    hashdots = []
    for y in range(j-1, j+2):
        for x in range(i-1, i+2):
            if x < 0 or x >= len(img[0]) or y < 0 or y >= len(img):
                hashdots.append(".")
            else:
                hashdots.append(img[y][x])
    binstr = "".join(hashdots).replace(".", "0").replace("#", "1")
    print(binstr)
    return int(binstr, 2)

assert(get_number(ex_img, 2, 2) == 34)

def pad_image(img):
    for idx, row in enumerate(img):
        img[idx] = ['.', '.'] + row + ['.', '.']
    img.insert(0, ['.' for _ in range(len(img[0]))])
    img.append(['.' for _ in range(len(img[0]))])

def enhance(img_algo, img):
    out_img = [['.' for ch in row] for row in img]
    for j in range(len(img)):
        for i in range(len(img[0])):
            idx = get_number(img, i, j)
            out_img[j][i] = img_algo[idx]
    return out_img

def count_lit_pixels(img):
    count = 0
    for row in img:
        count += row.count("#")
    return count

assert(count_lit_pixels([["#", ".", "."],[".", "#", "."]]) == 2)

def part_one(img_algo, img, steps=2):
    out_img = img
    for _ in range(steps):
        out_img = enhance(img_algo, out_img)
    for row in out_img:
        print("".join(row))
    return count_lit_pixels(out_img)

print(part_one(ex_algo, ex_img))
assert(part_one(ex_algo, ex_img) == 35)
# print(f"Part One: {part_one(img_algo, img)}")

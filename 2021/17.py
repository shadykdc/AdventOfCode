def process(target):
    x_min = int(target.split("=")[1].split("..")[0])
    x_max = int(target.split("=")[1].split("..")[1].split(",")[0])
    y_min = int(target.split("=")[2].split("..")[0])
    y_max = int(target.split("=")[2].split("..")[1])
    return x_min, x_max, y_min, y_max

example = "target area: x=20..30, y=-10..-5"
my_input = "target area: x=94..151, y=-156..-103"

def step(x_pos, y_pos, vx, vy):
    x_pos += vx
    y_pos += vy
    if vx < 0:
        vx += 1
    elif vx > 0:
        vx -= 1
    return x_pos, y_pos, vx, vy-1

def soltuion(target):
    x1, x2, y1, y2 = process(target)
    ys = []
    for vx in range(500):
        for vy in range(-500, 500):
            x_pos, y_pos, max_y, velx, vely = 0, 0, 0, vx, vy
            while abs(x_pos) <= abs(x2) and y_pos >= min([y1, 0]):
                x_pos, y_pos, velx, vely = step(x_pos, y_pos, velx, vely)
                max_y = max(max_y, y_pos)
                if x_pos in range(x1, x2+1) and y_pos in range(y1, y2+1):
                    ys.append(max_y)
                    break
    return ys

assert(max(soltuion(example)) == 45)
print(f"Part One: {max(soltuion(my_input))}")
assert(max(soltuion(my_input)) == 12090)
assert(len(soltuion(example)) == 112)
print(f"Part Two: {len(soltuion(my_input))}")
assert(len(soltuion(my_input)) == 5059)

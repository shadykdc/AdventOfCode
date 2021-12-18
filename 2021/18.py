import ast
import itertools
import math
import re

def get_input(name):
    with open(name, 'r') as f:
        return [ast.literal_eval(line.strip()) for line in f.readlines()]

snailfish = get_input('input18.txt')
example = get_input('input18.1.txt')

def magnitude(numbers):
    if isinstance(numbers, int):
        return numbers
    return magnitude(numbers[0]) * 3 + magnitude(numbers[1]) * 2

assert(magnitude([[1,2],[[3,4],5]]) == 143)
assert(magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384)
assert(magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445)
assert(magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791)
assert(magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137)
assert(magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488)
assert(magnitude([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]) == 4140)

def convert_to_strlist(numbers):
    numstr = re.split(r'(\d+|\[|\]|\,)', numbers.__repr__().replace(" ", ""))
    return list(filter(None, numstr))

assert(convert_to_strlist([[1, 23], 34]) == ["[", "[", "1", ",", "23", "]", ",", "34", "]"])

def explode(numbers, level=0):
    numstr = convert_to_strlist(numbers)
    level, idx, last_num_idx = 0, 0, -1
    while idx < len(numstr):
        item = numstr[idx]
        if item == ',':
            pass
        elif item == '[':
            level += 1
        elif item == ']':
            level -= 1
        else:
            if level == 5:
                if last_num_idx != -1:
                    numstr[last_num_idx] = str(int(numstr[last_num_idx]) + int(item))
                right = int(numstr[idx+2])
                del numstr[idx-1:idx+4]
                numstr.insert(idx-1, '0')
                while idx < len(numstr) and numstr[idx] in [',', '[', ']']:
                    idx+= 1
                if idx < len(numstr):
                    numstr[idx] = str(right + int(numstr[idx]))
                numbers = ast.literal_eval("".join(numstr))
                return True, numbers
            else: # a number
                last_num_idx = idx
        idx += 1
    return False, numbers

assert(explode([[[[[9,8],1],2],3],4]) == (True, [[[[0,9],2],3],4]))
assert(explode([7,[6,[5,[4,[3,2]]]]]) == (True, [7,[6,[5,[7,0]]]]))
assert(explode([[6,[5,[4,[3,2]]]],1]) == (True, [[6,[5,[7,0]]],3]))
assert(explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == (True, [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]))
assert(explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == (True, [[3,[2,[8,0]]],[9,[5,[7,0]]]]))
assert(explode([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]) == (True, [[[[0,7],4],[7,[[8,4],9]]],[1,1]]))

def split(numbers):
    if isinstance(numbers, list):
        for idx, item in enumerate(numbers):
            if isinstance(numbers, int) and item >= 10:
                numbers[idx] = [math.floor(item/2), math.ceil(item/2)]
                return True
            if split(item):
                return True
    return False

ex = [[[[0,7],4],[15,[0,13]]],[1,1]]
assert(split(ex) == True)
assert(ex == [[[[0,7],4],[[7,8],[0,13]]],[1,1]])
assert(split(ex) == True)
assert(ex == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
assert(split(ex) == False)

def reduction(numbers):
    exploded, numbers = explode(numbers)
    if exploded:
        return reduction(numbers)
    if split(numbers):
        return reduction(numbers)
    return numbers

def add(numbers1, numbers2):
    numbers = [[item for item in numbers1], [item for item in numbers2]]
    return reduction(numbers)

ex1 = [[[[4,3],4],4],[7,[[8,4],9]]]
ex2 = [1,1]
assert(add(ex1, ex2) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]])

def part_one(snailfish):
    num_list = [item for item in snailfish]
    numbers = num_list[0]
    for idx in range(1, len(num_list)):
        numbers = add(numbers, num_list[idx])
    return magnitude(numbers)

assert(part_one(example) == 4140)
p1 = part_one(snailfish)
print(f"Part One: {p1}")
assert(p1 == 3305)

def part_two(snailfish):
    max_sum = 0
    for combo in itertools.combinations(snailfish, 2):
        max_sum = max(magnitude(add(combo[0], combo[1])), max_sum)
        max_sum = max(magnitude(add(combo[1], combo[0])), max_sum)
    return max_sum

assert(part_two(example) == 3993)
print(f"Part Two: {part_two(snailfish)}")

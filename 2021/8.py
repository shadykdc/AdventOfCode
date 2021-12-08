with open('input8.txt', 'r') as f:
    lines = f.readlines()
    tens = [[word.strip() for word in line.strip().split("|")[0].split()] for line in lines]
    outs = [[word.strip() for word in line.strip().split("|")[1].split()] for line in lines]

with open('input8.1.txt', 'r') as f:
    lines = f.readlines()
    example_tens = [[word.strip() for word in line.strip().split("|")[0].split()] for line in lines]
    example_outs = [[word.strip() for word in line.strip().split("|")[1].split()] for line in lines]


def part_one(outs):
    count = 0
    for out in outs:
        for word in out:
            if len(word) in [2, 3, 4, 7]:
                count+=1
    return count

print(f"Part One: {part_one(outs)}")
assert(part_one(outs) == 532)

def get_decoder(out):
    decoder = dict()
    int_to_word = dict()
    words = ["".join(sorted(word)) for word in out]
    # easy ones
    while len(words) > 6:
        for word in words:
            if len(word) in [2, 3, 4, 7]:
                len_to_int = {2: 1, 3: 7, 4:4, 7:8}
                decoder[word] = len_to_int[len(word)]
                int_to_word[len_to_int[len(word)]] = word
                words.remove(word)

    # get the three_letters that are in 8 but not 0, 6, and 9
    words_for_069 = [word for word in words if len(word) == 6]
    three_letters = []
    for word in words_for_069:
        for letter in int_to_word[8]:
            if letter not in word:
                three_letters.append(letter)

    # left_bottom = of those three_letters, the one that's not in 4
    left_bottom = [letter for letter in three_letters if letter not in int_to_word[4]][0]

    # 9 = 8 - left_bottom
    nine = int_to_word[8].replace(left_bottom, '')
    decoder[nine] = 9
    int_to_word[9] = nine
    words.remove(nine)

    # two_letters = three_letters - left_bottom
    two_letters = [letter for letter in three_letters if letter != left_bottom]

    # right_top = letter from two_letters that is in 1
    right_top = [letter for letter in two_letters if letter in int_to_word[1]][0]

    # middle = letter from two_letters that is not in 1
    middle = [letter for letter in two_letters if letter not in int_to_word[1]][0]

    # 0 = 8 - middle
    zero = int_to_word[8].replace(middle, '')
    decoder[zero] = 0
    int_to_word[0] = zero
    words.remove(zero)

    # 6 = 8 - right_top
    six = int_to_word[8].replace(right_top, '')
    decoder[six] = 6
    int_to_word[6] = six
    words.remove(six)

    # 5 = 8 - left_bottom - right_top
    five = int_to_word[8].replace(right_top, '').replace(left_bottom, '')
    decoder[five] = 5
    int_to_word[5] = five
    words.remove(five)

    # only 2 and 3 are left
    assert(len(words) == 2)

    # 3 = whatever is left that has 1 inside of it
    three = [word for word in words if int_to_word[1][0] in word and int_to_word[1][1] in word][0]
    decoder[three] = 3
    int_to_word[3] = three
    words.remove(three)

    # 2 = whatever is left
    two = words[0]
    decoder[two] = 2
    int_to_word[2] = two
    words.remove(two)
    return decoder

def decode(out, decoder):
    return int("".join([str(decoder["".join(sorted(word))]) for word in out]))

def part_two(tens, outs):
    total = 0
    for idx in range(len(tens)):
        decoder = get_decoder(tens[idx])
        total += decode(outs[idx], decoder)
    return total


assert(part_two([["acedgfb","cdfbe","gcdfa","fbcad","dab","cefabd","cdfgeb","eafb","cagedb","ab"]], [["cdfeb","fcadb","cdfeb","cdbaf"]]) == 5353)
assert(part_two(example_tens, example_outs) == 61229)
print(f"Part Two: {part_two(tens, outs)}")
assert(part_two(tens, outs) == 1011284)

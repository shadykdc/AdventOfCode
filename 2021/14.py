from collections import Counter, defaultdict

def get_input(name):
    with open(name, 'r') as f:
        return {line.split("->")[0].strip(): line.split("->")[1].strip() for line in f.readlines()}

template = "NBOKHVHOSVKSSBSVVBCS"
pairs = get_input('input14.txt')

ex_template = "NNCB"
ex_pairs = get_input('input14.1.txt')


def do_step(template, pairs):
    new_template = [template[0]]
    for idx in range(len(template) - 1):
        pair = template[idx:idx+2]
        new_template.extend([pairs[pair], pair[1]])
    return "".join(new_template)

def do_steps(template, pairs, steps):
    for i in range(steps):
        template = do_step(template, pairs)
    return template

def part_one(template, pairs, steps):
    counter = Counter(do_steps(template, pairs, steps))
    return counter.most_common(1)[0][1] - counter.most_common()[-1][1]

assert(len(do_steps(ex_template, ex_pairs, 5)) == 97)
assert(len(do_steps(ex_template, ex_pairs, 10)) == 3073)
assert(do_steps(ex_template, ex_pairs, 10).count("B") == 1749)
assert(do_steps(ex_template, ex_pairs, 10).count("C") == 298)
assert(do_steps(ex_template, ex_pairs, 10).count("H") == 161)
assert(do_steps(ex_template, ex_pairs, 10).count("N") == 865)
assert(part_one(ex_template, ex_pairs, 10) == 1588)
print(f"Part 1: {part_one(template, pairs, 10)}")
assert(part_one(template, pairs, 10) == 3342)

def part_two(template, pairs, steps):
    count_letters = Counter(template)
    count_pairs = Counter([template[idx:idx+2] for idx in range(len(template) - 1)])
    for i in range(steps):
        for pair, val in list(count_pairs.items()):
            count_pairs[pair] -= val
            count_pairs[pair[0] + pairs[pair]] += val
            count_pairs[pairs[pair] + pair[1]] += val
            count_letters[pairs[pair]] += val
    return count_letters.most_common(1)[0][1] - count_letters.most_common()[-1][1]

assert(part_two(ex_template, ex_pairs, 40) == 2188189693529)
print(f"Part 2: {part_two(template, pairs, 40)}")

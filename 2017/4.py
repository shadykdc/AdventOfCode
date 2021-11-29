from typing import List

with open('input4.txt', 'r') as f:
    passwords = [[word for word in pw.strip().split(" ")] for pw in f.readlines()]

def part_one(passwords: List[List[str]]) -> int:
    # a valid password is one where len(pw) == len(set(pw))
    return len([pw for pw in passwords if len(pw) == len(set(pw))])

assert(part_one([["aa", "bb", "cc", "dd", "ee"]]) == 1)
assert(part_one([["aa", "bb", "cc", "dd", "aa"]]) == 0)
assert(part_one([["aa", "bb", "cc", "dd", "aaa"]]) == 1)
assert(part_one(passwords) == 337)
print(f"Part 1: {part_one(passwords)}")

def valid_password(pw: List[str]) -> bool:
    pw_set = {"".join(sorted(word)) for word in pw}
    return len(pw) == len(pw_set)

def part_two(passwords: List[List[str]]) -> int:
    return len([pw for pw in passwords if valid_password(pw)])

assert(part_two(["abcde fghij".split(' ')]) == 1)
assert(part_two(["abcde xyz ecdab".split(' ')]) == 0)
assert(part_two(["a ab abc abd abf abj".split(' ')]) == 1)
assert(part_two(["iiii oiii ooii oooi oooo".split(' ')]) == 1)
assert(part_two(["oiii ioii iioi iiio".split(' ')]) == 0)
print(f"Part 2: {part_two(passwords)}")

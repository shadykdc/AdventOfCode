from collections import defaultdict

fish_ages = [1,4,1,1,1,1,1,1,1,4,3,1,1,3,5,1,5,3,2,1,1,2,3,1,1,5,3,1,5,1,1,2,1,2,1,1,3,1,5,1,1,1,3,1,1,1,1,1,1,4,5,3,1,1,1,1,1,1,2,1,1,1,1,4,4,4,1,1,1,1,5,1,2,4,1,1,4,1,2,1,1,1,2,1,5,1,1,1,3,4,1,1,1,3,2,1,1,1,4,1,1,1,5,1,1,4,1,1,2,1,4,1,1,1,3,1,1,1,1,1,3,1,3,1,1,2,1,4,1,1,1,1,3,1,1,1,1,1,1,2,1,3,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,5,1,1,1,2,2,1,1,3,5,1,1,1,1,3,1,3,3,1,1,1,1,3,5,2,1,1,1,1,5,1,1,1,1,1,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,5,1,4,3,3,1,3,4,1,1,1,1,1,1,1,1,1,1,4,3,5,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,1,4,4,1,1,1,1,1,1,1,5,1,1,2,5,1,1,4,1,3,1,1]
example = [3,4,3,1,2]

def age_one_day(ages):
    new_ages = defaultdict(lambda: 0)
    for key in range(1, max(ages.keys())+ 1):
        new_ages[key-1] = ages[key]
    new_ages[8] = ages[0]
    new_ages[6] += ages[0]
    return new_ages

def solution(fish_ages, days):
    ages = {age: fish_ages.count(age) for age in range(max(fish_ages)+1)}
    for _ in range(days):
        ages = age_one_day(ages)
    return sum(ages.values())

assert(solution(example, 18) == 26)
assert(solution(example, 80) == 5934)
print(f"Part 1: {solution(fish_ages, 80)}")
assert(solution(fish_ages, 80) == 393019)

assert(solution(example, 256) == 26984457539)
print(f"Part 2: {solution(fish_ages, 256)}")
assert(solution(fish_ages, 256) == 1757714216975)

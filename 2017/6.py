from typing import List, Set

nums = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
example = [0, 2, 7, 0]

def part_one(nums: List[int]) -> int:
    seen: Set[str] = set()
    nums_to_str = "".join([str(num) for num in nums])
    while nums_to_str not in seen:
        seen.add(nums_to_str)
        max_num = nums[0]
        index = 0
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                index = idx
        blocks = nums[index]
        nums[index] = 0
        while blocks > 0:
            index = index + 1 if index + 1 < len(nums) else 0
            nums[index] += 1
            blocks -= 1
        nums_to_str = "".join([str(num) for num in nums])
    return len(seen)

assert(part_one(example) == 5)
p1 = part_one(nums)
assert(p1 == 11137)
print(f"Part 1: {p1}")

assert(part_one(example) == 4)
p2 = part_one(nums)
assert(p2 == 1037)
print(f"Part 2: {p2}")

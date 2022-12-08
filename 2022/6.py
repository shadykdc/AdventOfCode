from pathlib import Path
from utils import answer

p1_examples = {
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
    "nppdvjthqldpwncqszvftbrmjlhg": 6,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
}

p2_examples = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
    "nppdvjthqldpwncqszvftbrmjlhg": 23,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26,

}

with open(f'input{Path(__file__).stem}.txt', 'r') as f:
    puzzle_input = f.readlines()[0]

def solution(letters, count=4):
    idx = count
    while len(set(letters[idx-count:idx])) != count:
        idx+=1
    return idx

for key in p1_examples:
    answer(solution(key), "Example 1", p1_examples[key])
answer(solution(puzzle_input), "Part 1", 1175)
for key in p2_examples:
    answer(solution(key, 14), "Example 2", p2_examples[key])
answer(solution(puzzle_input, 14), "Part 2", 3217)

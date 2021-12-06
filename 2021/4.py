import copy

BOARD_SIZE = 5

with open('input4.txt', 'r') as f:
    nums = [int(num.strip()) for num in f.readline().split(",")]
    line = f.readline()
    boards = []
    while line:
        board = [[[int(num.strip()), False] for num in f.readline().split()] for r in range(BOARD_SIZE)]
        boards.append(board)
        line = f.readline()

example = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
example_boards = [
    [
        [[22, False],[13, False],[17, False],[11, False],[ 0, False]],
        [[8, False],[2, False],[ 23, False],[  4, False],[ 24, False]],
        [[21, False],[9, False],[ 14, False],[ 16, False],[  7, False],],
        [[6, False],[10, False],[  3, False],[ 18, False],[  5, False]],
        [[1, False],[12, False],[ 20, False],[ 15, False],[ 19, False]],
    ],
    [
        [[3, False], [15, False],  [0, False],  [2, False], [22, False]],
        [[9, False], [18, False], [13, False], [17, False],  [5, False]],
        [[19, False],  [8, False],  [7, False], [25, False], [23, False]],
        [[20, False], [11, False], [10, False], [24, False],  [4, False]],
        [[14, False], [21, False], [16, False], [12, False],  [6, False]],
    ],
    [
        [[14, False], [21, False], [17, False], [24, False],  [4, False]],
        [[10, False], [16, False], [15, False],  [9, False], [19, False]],
        [[18, False],  [8, False], [23, False], [26, False], [20, False]],
        [[22, False], [11, False], [13, False],  [6, False],  [5, False]],
        [[2, False],  [0, False], [12, False],  [3, False],  [7, False]],
    ],
]

boards2 = copy.copy(boards)
example_boards2 = copy.copy(example_boards)

def is_win(board, j, i):
    return (
        len([1 for y in range(BOARD_SIZE) if board[y][i][1]]) == BOARD_SIZE
        or len([1 for x in range(BOARD_SIZE) if board[j][x][1]]) == BOARD_SIZE
    )

def play_bingo(num, boards, winners):
    for idx, board in enumerate(boards):
        for j in range(BOARD_SIZE):
            for i in range(BOARD_SIZE):
                if board[j][i][0] == num:
                    board[j][i][1] = True
                    if is_win(board, j, i) and idx not in winners.values():
                        winners[len(winners)+1] = idx

def sum_unused(board) -> int:
    return sum([sum(
        [board[j][i][0]
        for j in range(BOARD_SIZE)
        if not board[j][i][1]]
    ) for i in range(BOARD_SIZE)])

def solution(nums, boards, place) -> int:
    winners = dict()
    for num in nums:
        play_bingo(num, boards, winners)
        if len(winners) == place:
            return sum_unused(boards[winners[place]]) * num
    return 0

assert(solution(example, example_boards, 1) == 4512)
print(f"Part 1: {solution(nums, boards, 1)}") # 64084

assert(solution(example, example_boards2, len(example_boards2)) == 1924)
print(f"Part 2: {solution(nums, boards2, len(boards2))}") # 12833

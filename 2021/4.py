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
    win = True
    for y in range(BOARD_SIZE):
        if not board[y][i][1]:
            win = False
            break
    if win:
        return win
    win = True
    for x in range(BOARD_SIZE):
        if not board[j][x][1]:
            win = False
            break
    return win

def play_bingo(num, boards):
    """Return the winning board and num"""
    for idx, board in enumerate(boards):
        for j in range(BOARD_SIZE):
            for i in range(BOARD_SIZE):
                if board[j][i][0] == num:
                    board[j][i][1] = True
                    if is_win(board, j, i):
                        return idx, num
    return -1, -1


def play_bingo2(num, boards, winners):
    """Return the winning board and num"""
    for idx, board in enumerate(boards):
        for j in range(BOARD_SIZE):
            for i in range(BOARD_SIZE):
                if board[j][i][0] == num:
                    board[j][i][1] = True
                    if is_win(board, j, i):
                        winners[idx] = True
                        if False not in winners:
                            return sum_unused(boards[idx]) * num
    return -1

def sum_unused(board) -> int:
    count = 0
    for j in range(BOARD_SIZE):
        for i in range(BOARD_SIZE):
            if not board[j][i][1]:
                count+=board[j][i][0]
    return count

def part_one(nums, boards):
    for num in nums:
        idx, num = play_bingo(num, boards)
        if idx != -1 or num != -1:
            return sum_unused(boards[idx]) * num
    return 0

assert(part_one(example, example_boards) == 4512)
print(f"Part 1: {part_one(nums, boards)}") # 64084

def part_two(nums, boards):
    winners = [False for board in boards]
    for num in nums:
        res = play_bingo2(num, boards, winners)
        if res != -1:
            return res
    return 0

assert(part_two(example, example_boards2) == 1924)
print(f"Part 2: {part_two(nums, boards2)}")

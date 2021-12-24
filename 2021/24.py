def get_input(name):
    with open(name, 'r') as f:
        return [line.strip().split() for line in f.readlines()]

monad = get_input('input24.txt')

def run(monad):
    ws_big = [0 for _ in range(14)]
    ws_small = [0 for _ in range(14)]
    stack = []
    for i in range(int(len(monad)/18)):
        a = int(monad[18*i+4][2])
        assert(a == 1 or a == 26)
        if a == 1:
            # store the y value and our index (for ws)
            stack.append((int(monad[18*i+15][2]), i))
        else:
            # pop y and index and add y to x to get w
            y, j = stack.pop()
            w = y + int(monad[18*i+5][2])
            assert(w in range(-9, 10))
            if w < 0:
                i, j, w = j, i, -w
            ws_big[i] = 9
            ws_big[j] = 9 - w
            ws_small[i] = 1 + w
            ws_small[j] = 1
    print("".join([str(num) for num in ws_big])) # 94992992796199
    print("".join([str(num) for num in ws_small])) # 11931881141161

run(monad)

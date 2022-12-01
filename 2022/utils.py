def answer(guess, part, ans = None):
    if ans:
        print(f"{part}: {guess}")
        assert(guess == ans)
    else:
        print(f"{part}? {guess}")

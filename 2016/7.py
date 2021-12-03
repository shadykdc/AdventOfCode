with open('input7.txt', 'r') as f:
    ip_addrs = [ip_addr.strip() for ip_addr in f.readlines()]

def is_abba(line: str) -> bool:
    for i in range(len(line) - 3):
        if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
            return True
    return False

def valid(ip_addr: str) -> bool:
    found_abba = False
    start = 0
    for idx in range(len(ip_addr)):
        if ip_addr[idx] == "[" or idx == len(ip_addr) - 1:
            if not found_abba:
                found_abba = is_abba(ip_addr[start:idx+1])
            start = idx + 1
        elif ip_addr[idx] == "]":
            if is_abba(ip_addr[start:idx]):
                return False
            start = idx + 1
    return found_abba

def part_one(ip_addrs) -> int:
    return len([ip_addr for ip_addr in ip_addrs if valid(ip_addr)])

assert(part_one(["abba[mnop]qrst"]) == 1)
assert(part_one(["abcd[bddb]xyyx"]) == 0)
assert(part_one(["aaaa[qwer]tyui"]) == 0)
assert(part_one(["ioxxoj[asdfgh]zxcvbn"]) == 1)
print(f"Part One: {part_one(ip_addrs)}")
assert(part_one(ip_addrs) == 115)

def get_abas(line):
    return {
        line[i:i+3]
        for i in range(len(line) - 2)
        if line[i] == line[i+2] and line[i] != line[i+1]
    }

def valid2(ip_addr) -> bool:
    start = 0
    abas = set()
    babs = set()
    for idx in range(len(ip_addr)):
        if ip_addr[idx] == "[" or idx == len(ip_addr) - 1:
            abas = abas.union(get_abas(ip_addr[start:idx+1]))
            start = idx + 1
        elif ip_addr[idx] == "]":
            babs = babs.union(get_abas(ip_addr[start:idx+1]))
            start = idx + 1
    for aba in abas:
        if "".join([aba[1], aba[0], aba[1]]) in babs:
            return True
    return False

def part_two(ip_addrs) -> int:
    return len([ip_addr for ip_addr in ip_addrs if valid2(ip_addr)])

assert(part_two(["aba[bab]xyz"]) == 1)
assert(part_two(["xyx[xyx]xyx"]) == 0)
assert(part_two(["aaa[kek]eke"]) == 1)
assert(part_two(["zazbz[bzb]cdb"]) == 1)
print(f"Part Two: {part_two(ip_addrs)}")
# assert(part_two(ip_addrs) == 561) too high

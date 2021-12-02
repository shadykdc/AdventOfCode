import hashlib

door_id = "uqwqemis"
example = "abc"
PW_LEN = 8
LEAD = 5

def part_one(door_id: str) -> str:
    num = 0
    password = ""
    while len(password) < PW_LEN:
        num += 1
        result = hashlib.md5(f"{door_id}{num}".encode('utf-8'))
        if str(result.hexdigest())[0:LEAD] == "00000":
            password += str(result.hexdigest())[LEAD]
    return password

assert(part_one(example) == "18f47a30")
p1 = part_one(door_id)
print(f"Part One: {p1}")
assert(p1 == "1a3099aa")

def part_two(door_id: str) -> str:
    num = 0
    empty = "_"
    password = [empty] * PW_LEN
    while empty in password:
        num += 1
        result = hashlib.md5(f"{door_id}{num}".encode('utf-8'))
        val = str(result.hexdigest())
        if (
            val[0:LEAD] == '0' * LEAD
            and len(val) > LEAD + 1
            and val[LEAD] < str(PW_LEN)
            and val[LEAD] >= '0'
            and password[int(val[LEAD])] == empty
        ):
            password[int(val[LEAD])] = val[LEAD + 1]
    return "".join(password)

assert(part_two(example) == "05ace8e3")
p2 = part_two(door_id)
print(f"Part Two: {p2}")
assert(p2 == "694190cd")

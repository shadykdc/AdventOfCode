class Room:
    def __init__(self, name, id, checksum):
        self.name: str = name
        self.id: int = id
        self.checksum: str = checksum

    @classmethod
    def from_line(self, line) -> "Room":
        first_split = line.split("[") # aaaaa-bbb-z-y-x-123, abxyz]
        name = "".join([c for c in first_split[0] if c.isalpha() or c == "-"])
        name = name.replace("-", " ").strip()
        id = int(first_split[0].split("-")[-1])
        checksum = first_split[1][:-1]
        return Room(name, id, checksum)

    def __str__(self) -> str:
        return f"Name: {self.name} | ID: {self.id} | Checksum: {self.checksum}"

    def is_valid(self) -> bool:
        counts = {c: self.name.count(c) for c in set(self.name) if c != " "}
        for letter in self.checksum:
            if letter not in counts or counts[letter] != max(counts.values()):
                return False
            for num in range(ord('a'), ord(letter)):
                if chr(num) in counts and counts[chr(num)] == counts[letter]:
                    return False
            del counts[letter]
        return True

    def decrypt(self) -> str:
        offset = self.id % 26
        new_name = ""
        for letter in self.name:
            if letter.isalpha():
                if ord(letter) + offset > ord('z'):
                    letter = chr(offset + ord(letter) - 26)
                else:
                    letter = chr(ord(letter) + offset)
            new_name += letter
        return new_name


with open('input4.txt', 'r') as f:
    rooms = [Room.from_line(line.strip()) for line in f.readlines()]

example1 = [Room.from_line("aaaaa-bbb-z-y-x-123[abxyz]")]
example2 = [Room.from_line("a-b-c-d-e-f-g-h-987[abcde]")]
example3 = [Room.from_line("not-a-real-room-404[oarel]")]
example4 = [Room.from_line("totally-real-room-200[decoy]")]

def part_one(rooms):
    return sum([room.id for room in rooms if room.is_valid()])

assert(part_one(example1) == 123)
assert(part_one(example2) == 987)
assert(part_one(example3) == 404)
assert(part_one(example4) == 0)
print(f"Part 1: {part_one(rooms)}")
assert(part_one(rooms) == 173787)


def part_two(rooms):
    for room in rooms:
        if room.decrypt() == "northpole object storage":
            return room.id
    return 0

print(f"Part 2: {part_two(rooms)}")
assert(part_two(rooms) == 548)

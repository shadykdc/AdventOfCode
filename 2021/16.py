from textwrap import dedent

my_input = "A20D74AFC6C80CEA7002D4009202C7C00A6830029400F500218080C3002D006CC2018658056E7002DC00C600E75002ED6008EDC00D4003E24A13995080513FA309482649458A054C6E00E6008CEF204BA00B080311B21F4101006E1F414846401A55002F53E9525B845AA7A789F089402997AE3AFB1E6264D772D7345C6008D8026200E41D83B19C001088CB04A294ADD64C0129D818F802727FFF3500793FFF9A801A801539F42200DC3801A39C659ACD3FC6E97B4B1E7E94FC1F440219DAFB5BB1648E8821A4FF051801079C379F119AC58ECC011A005567A6572324D9AE6CCD003639ED7F8D33B8840A666B3C67B51388440193E003413A3733B85F2712DEBB59002B930F32A7D0688010096019375300565146801A194844826BB7132008024C8E4C1A69E66108000D39BAD950802B19839F005A56D9A554E74C08028992E95D802D2764D93B27900501340528A7301F2E0D326F274BCAB00F5009A737540916D9A9D1EA7BD849100425D9E3A9802B800D24F669E7691E19CFFE3AF280803440086C318230DCC01E8BF19E33980331D631C593005E80330919D718EFA0E3233AE31DF41C67F5CB5CAC002758D7355DD57277F6BF1864E9BED0F18031A95DDF99EB7CD64626EF54987AE007CCC3C4AE0174CDAD88E65F9094BC4025FB2B82C6295F04100109263E800FA41792BCED1CC3A233C86600B48FFF5E522D780120C9C3D89D8466EFEA019009C9600A880310BE0C47A100761345E85F2D7E4769240287E80272D3CEFF1C693A5A79DFE38D27CCCA75E5D00803039BFF11F401095F714657DC56300574010936491FBEC1D8A4402234E1E68026200CC5B8FF094401C89D12E14B803325DED2B6EA34CA248F2748834D0E18021339D4F962AB005E78AE75D08050E10066114368EE0008542684F0B40010B8AB10630180272E83C01998803104E14415100623E469821160"


def hex_to_binary(hex_string):
    binary = [str(bin(int(hex_digit, 16))[2:].zfill(4)) for i in range(0, len(hex_string), 4) for hex_digit in hex_string[i:i+4]]
    return "".join(binary)

class Packet:
    def __init__(self, binary_string, idx=0):
        self.binstr = binary_string
        self.idx = idx
        self.version = -1
        self.type_id = -1
        self.packets = []
        self.value = 0

    def __str__(self):
        return dedent(
            f"""
            Version: {self.version}
            Type Id: {self.type_id}
            Value: {self.value}
            Idx: {self.idx}
            Len Bin Str: {len(self.binstr)}
            Packets: {[packet.version for packet in self.packets]}
            {[str(packet) for packet in self.packets]}
            """
        )

    def get_literal(self):
        literals = []
        while self.idx + 5 <= len(self.binstr):
            literals.append(self.binstr[self.idx+1:self.idx+5])
            self.idx += 5
            if self.binstr[self.idx-5] == '0':
                break
        self.value = int("".join(literals), 2)

    def process_operator(self):
        if self.binstr[self.idx-1] == '0':
            len_in_bits = int(self.binstr[self.idx:self.idx+15], 2)
            self.idx += 15
            stop = self.idx + len_in_bits
            while self.idx < stop:
                self.add_sub_packet()
        else:
            num_sub_packets = int(self.binstr[self.idx:self.idx+11], 2)
            self.idx += 11
            for packet in range(num_sub_packets):
                self.add_sub_packet()

    def add_sub_packet(self):
        packet = Packet(self.binstr, self.idx)
        packet.create()
        self.idx = packet.idx
        self.packets.append(packet)

    def create(self):
        self.version = int(self.binstr[self.idx:self.idx+3], 2)
        self.type_id = int(self.binstr[self.idx+3:self.idx+6], 2)
        self.idx += 6
        if self.type_id == 4:  # literal
            self.get_literal()
            return
        # operator
        self.idx += 1
        self.process_operator()
        if self.type_id == 0:  # sum
            self.value = sum([pack.value for pack in self.packets])
        if self.type_id == 1:  # product
            prod = 1
            for pack in self.packets:
                prod *= pack.value
            self.value = prod
        if self.type_id == 2:  # minimum
            self.value = min([pack.value for pack in self.packets])
        if self.type_id == 3:  # maximum
            self.value = max([pack.value for pack in self.packets])
        if self.type_id == 5:  # greater than
            self.value = 1 if self.packets[0].value > self.packets[1].value else 0
        if self.type_id == 6:  # less than
            self.value = 1 if self.packets[0].value < self.packets[1].value else 0
        if self.type_id == 7:  # equal to
            self.value = 1 if self.packets[0].value == self.packets[1].value else 0

    def get_version_sum(self):
        child_sum = sum([pack.get_version_sum() for pack in self.packets])
        return self.version + child_sum


def part_one(hex_string):
    packet = Packet(hex_to_binary(hex_string))
    packet.create()
    return packet.get_version_sum()


assert(hex_to_binary("D2FE28") == "110100101111111000101000")
assert(part_one("D2FE28") == 6)
assert(part_one("8A004A801A8002F478") == 16)
assert(part_one("620080001611562C8802118E34") == 12)
assert(part_one("C0015000016115A2E0802F182340") == 23)
assert(part_one("A0016C880162017C3686B18A3D4780") == 31)
print(f"Part 1: {part_one(my_input)}")
assert(part_one(my_input) == 891)

def part_two(hex_string):
    packet = Packet(hex_to_binary(hex_string))
    packet.create()
    return packet.value

assert(part_two("C200B40A82") == 3)
assert(part_two("04005AC33890") == 54)
assert(part_two("880086C3E88112") == 7)
assert(part_two("CE00C43D881120") == 9)
assert(part_two("D8005AC2A8F0") == 1)
print(f"Part 2: {part_two(my_input)}")
assert(part_two(my_input) == 673042777597)

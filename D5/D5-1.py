import math

class MD5:
    def __init__(self):
        self.shift = [
            7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
            5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
            4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
            6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
        ]
        self.K = [0x0] * 64
        for i in range(0,64):
            self.K[i] = int(math.floor(pow(2,32) * abs(math.sin(i+1))))

        self.A = int(0x67452301)
        self.B = int(0xefcdab89)
        self.C = int(0x98badcfe)
        self.D = int(0x10325476)
        self.ChunkSize = int(512/8)
        self.PadMod = int(448/8)

    def calculate(self, string):
        byteArray = bytearray(string, encoding='ascii')
        original_len = int((len(string)*8)%pow(2,64)) & 0xffffffffffffffff

        byteArray.append(0x80)
        while len(byteArray) % self.ChunkSize != self.PadMod:
            byteArray.append(0)

        byteArray += (original_len.to_bytes(8, 'little'))

        for chunkIndex in range(0, len(byteArray), self.ChunkSize):
            chunk = byteArray[chunkIndex:chunkIndex+self.ChunkSize]




input = 'abbhdwsy'


checkInput = 0
passwordCount = 0

while passwordCount < 8:
    #print(input + str(checkInput))
    byteinput = bytearray(input, 'ascii');
    print(byteinput)
    print((int.from_bytes(byteinput[0:4],byteorder='little')))

    test = MD5();
    test.calculate(input)


    checkInput += 1
    break

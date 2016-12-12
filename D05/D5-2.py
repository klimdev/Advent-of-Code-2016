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

    def _lefrRotate(self, value, shift):
        value &= 0xffffffff
        return ((value<<shift) | (value>> (32-shift))) & 0xffffffff

    def calculate(self, string):
        A = self.A
        B = self.B
        C = self.C
        D = self.D

        byteArray = bytearray(string, encoding='ascii')
        #print(byteArray)
        original_len = int((len(string)*8)) & 0xffffffffffffffff

        byteArray.append(0x80)#1000 0000
        while len(byteArray) % self.ChunkSize != self.PadMod:
            byteArray.append(0)

        byteArray += original_len.to_bytes(8, 'little')

        for chunkIndex in range(0, len(byteArray), self.ChunkSize):
            chunk = byteArray[chunkIndex:chunkIndex+self.ChunkSize]
            M = [ int.from_bytes(chunk[4*i:4*(i+1)], 'little') for i in range(0,16) ]
            #print(M)
            a0 = A
            b0 = B
            c0 = C
            d0 = D

            for i in range(0,self.ChunkSize):
                if i < 16:
                    F = (b0 & c0) | ((~b0) & d0)
                    g = i
                elif i < 32:
                    F = (d0 & b0) | ((~d0) & c0)
                    g = (5*i + 1)%16
                elif i < 48:
                    F = b0 ^ c0 ^ d0
                    g = (3*i + 5)%16
                else:
                    F = c0 ^ (b0 | (~d0))
                    g = (7*i)%16

                dTemp = d0
                d0 = c0
                c0 = b0
                b0 = (b0 + self._lefrRotate((a0 + F + self.K[i] + M[g]),self.shift[i]))&0xffffffff
                a0 = dTemp

            A += a0
            A &= 0xffffffff
            B += b0
            B &= 0xffffffff
            C += c0
            C &= 0xffffffff
            D += d0
            D &= 0xffffffff

        #md5_raw = sum([self.A, self.B << 32, self.C <<64, self.D <<96])
        md5_raw = A.to_bytes(4, 'little')
        md5_raw += B.to_bytes(4, 'little')
        md5_raw += C.to_bytes(4, 'little')
        md5_raw += D.to_bytes(4, 'little')
        #print(md5_raw)
        md5_string = ''.join([ '{:0>2}'.format(str(((hex(value)))).replace('0x','')) for value in md5_raw])
        return md5_string




input = 'abbhdwsy'


checkInput = 1910966
password = '        '
passwordPosition = {0,1,2,3,4,5,6,7}
passwordCount = 0
md5 = MD5()

#test
#print(md5.calculate(''))
#print(md5.calculate("The quick brown fox jumps over the lazy dog."))
#print(md5.calculate("The quick brown fox jumps over the lazy dog"))

while len(passwordPosition):
    #print(input + str(checkInput))
    inputCount = input + str(checkInput)

    test = md5.calculate(inputCount)
    #print(test)
    if test[:5] == '00000':
        position = ord(test[5])-ord('0')
        if position in passwordPosition:
            password = password[:position] + test[6] + password[position+1:]
            passwordPosition.remove(position)
            print('found at {} password {} ::: hash :::{}'.format(checkInput, password, test))

    checkInput += 1
    if checkInput % 10000 == 0:
        print(checkInput)

print(password)

#found at 1910966 password 4        ::: hash :::0000004ed0ede071d293b5f33de2dc2f
#found at 1997199 password 42       ::: hash :::0000012be6057b2554c26bfddab18b08
#found at 2963716 password 42   1   ::: hash :::00000512874cc40b764728993dd71ffb
#found at 3237361 password 42   19  ::: hash :::0000069710beec5f9a1943a610be52d8
#found at 7777889 password 42   197 ::: hash :::00000776b6ff41a7e30ed2d4b6663351
#found at 12850790 password 424  197 ::: hash :::0000024cc74f8456ee0a717f3d9446c3
#found at 12942170 password 424 0197 ::: hash :::0000040cbee050fc9d43ebef7823c70e
#found at 25651067 password 424a0197 ::: hash :::000003af31f09c411f2d74a7c8f41831
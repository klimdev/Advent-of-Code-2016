
from Decompressor import Decompressor

inputFile = open('test.txt', 'r')
print("without memory save \n\n")
for input in inputFile:
    decomp = Decompressor(input.replace('\n',''))
    decomp.decompress()
    print(decomp.input)

inputFile = open('test2.txt', 'r')
print("with memory save \n\n")
for input in inputFile:
    decomp = Decompressor(input.replace('\n', ''), True)
    decomp.decompress()
    print(decomp.count)
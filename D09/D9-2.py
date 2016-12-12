
from Decompressor import Decompressor

inputFile = open('D9.txt', 'r')
inputString = inputFile.readline()

decomp = Decompressor(inputString.replace('\n',''), True)
decomp.decompress()
print(decomp.count)
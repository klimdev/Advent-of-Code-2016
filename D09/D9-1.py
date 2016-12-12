
from Decompressor import Decompressor

inputFile = open('D9.txt', 'r')
inputString = inputFile.readline()

decomp = Decompressor(inputString.replace('\n',''))
decomp.decompress()
print(len(decomp.input))
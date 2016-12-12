
ordA = ord('a')

inputFile = open('D6.txt', 'r')


inputStrings = [line.replace('\n','') for line in inputFile]
print(inputStrings)

frequencyGrid = [ [ 0 for i in range(26)] for i in range(8) ]
print(frequencyGrid)
print(frequencyGrid[0])

for string in inputStrings:
    for i in range(0,8):
        char = ord(string[i]) - ordA
        frequencyGrid[i][char] += 1
        print('{} and {}'.format(string[i],frequencyGrid[i]))

for i in range(0,8):
    #print(max(frequencyGrid[i]))
    #print(frequencyGrid[i].index(max(frequencyGrid[i])))
    print(chr(frequencyGrid[i].index(max(frequencyGrid[i])) + ordA), end='')
    #print()

print()
print(frequencyGrid)

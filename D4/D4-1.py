
answerCount = 0

inputFile = open('D4.txt', 'r')

for inputLine in inputFile:
    room = inputLine[0:inputLine.rfind('-')].replace('-','')
    sectorID = inputLine[inputLine.rfind('-')+1:inputLine.find('[')]
    checksum = inputLine[inputLine.find('[')+1:inputLine.find(']')]

    letterCount = dict()
    for char in room:
        if char not in letterCount:
            letterCount[char] = 0

        letterCount[char] += 1

    print(letterCount)
    sortedLetterSet = dict()
    for key, value in letterCount.items():
        if value not in sortedLetterSet:
            sortedLetterSet[value] = set()
        sortedLetterSet[value].add(key)

    print(sortedLetterSet)
    realChecksum = ''
    for key in sorted(sortedLetterSet.keys(), reverse=True):
        realChecksum += ''.join(sorted(sortedLetterSet[key]))
        if len(realChecksum) > len(checksum):
            break;

    print(realChecksum)
    realChecksum = realChecksum[0:len(checksum)]
    print(checksum)
    print(realChecksum)
    print()
    if checksum == realChecksum:
        answerCount += int(sectorID)
    #break

print(answerCount)
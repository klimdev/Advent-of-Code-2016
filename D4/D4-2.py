
def decypher(roomName, sectorID):
    rotation = int(sectorID % 26)#a~z 26 letter
    for i in range(0, len(roomName)):
        if roomName[i] != '-':
            roomName = roomName[:i] + chr(ord('a') + ((ord(roomName[i]) - ord('a') + rotation)%26)) + roomName[i+1:]

    print(str(sectorID) + ' :' + roomName)
    return


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

    sortedLetterSet = dict()
    for key, value in letterCount.items():
        if value not in sortedLetterSet:
            sortedLetterSet[value] = set()
        sortedLetterSet[value].add(key)

    realChecksum = ''
    for key in sorted(sortedLetterSet.keys(), reverse=True):
        realChecksum += ''.join(sorted(sortedLetterSet[key]))
        if len(realChecksum) > len(checksum):
            break;


    realChecksum = realChecksum[0:len(checksum)]

    if checksum == realChecksum:
        decypher(inputLine[0:inputLine.rfind('-')], int(sectorID))
        answerCount += int(sectorID)
    #break

print(answerCount)

inputFile = open('D7.txt', 'r')
#inputFile = open('test.txt', 'r')

found = 0

def hasABBA(string):
    print(string)
    for i in range(0,len(string)-4 + 1):
        if string[i] != string[i+1] and string[i] == string[i+3] and string[i+1] == string[i+2]:
            print(string[i:i+4])
            return True
    return False





for inputLine in inputFile:
    inputLine = inputLine.replace('\n','')
    #print(inputLine[:inputLine.find('[')])
    #print(inputLine[inputLine.find(']')+1:])
    #print(inputLine[inputLine.find('[')+1:inputLine.find(']')])
    print(inputLine)

    index = 0
    outBracket = False
    inBracket = False
    split = inputLine.count(']') + 1
    while split:

        leftBracket = inputLine.find('[', index)
        rightBracket = inputLine.find(']', index)

        if leftBracket != -1:
            outBracket |= hasABBA(inputLine[index:leftBracket])
            inBracket |= hasABBA(inputLine[leftBracket + 1:rightBracket])
        else:
            outBracket |= hasABBA(inputLine[index:])

        index = rightBracket+1
        split -= 1

    found += 1 if outBracket and not inBracket else 0


    #found += 1 if (hasABBA(inputLine[:inputLine.find('[')]) or hasABBA(inputLine[inputLine.find(']')+1:])) \
    #              and not hasABBA(inputLine[inputLine.find('[')+1:inputLine.find(']')]) \
    #            else 0
    print()
print(found)
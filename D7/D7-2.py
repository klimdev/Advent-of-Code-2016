
inputFile = open('D7.txt', 'r')
#inputFile = open('test.txt', 'r')

found = 0

def hasABA(string):
    for i in range(0,len(string)-3 + 1):
        if string[i] != string[i+1] and string[i] == string[i+2]:
            return True, i

    return False, -1

def hasABABAB(outBrackets, inBrackets):
    for outBracket in outBrackets:
        i = 0
        while i < len(outBracket):
            has, where = hasABA(outBracket[i:])
            if where == -1:
                break
            else:
                where += i

            if has:
                BAB = outBracket[where+1] + outBracket[where] + outBracket[where+1]
                for inBracket in inBrackets:
                    if inBracket.find(BAB) != -1:
                        print(outBracket[where:where + 3])
                        print(BAB)
                        return True

            i = where + 1

    return False



for inputLine in inputFile:
    inputLine = inputLine.replace('\n','')
    print(inputLine)

    index = 0
    outBrackets = list()
    inBrackets = list()
    split = inputLine.count(']') + 1
    while split:

        leftBracket = inputLine.find('[', index)
        rightBracket = inputLine.find(']', index)

        if leftBracket != -1:
            outBrackets.append(inputLine[index:leftBracket])
            inBrackets.append(inputLine[leftBracket + 1:rightBracket])
        else:
            outBrackets.append(inputLine[index:])

        index = rightBracket+1
        split -= 1

    found += 1 if hasABABAB(outBrackets, inBrackets) else 0
    print()

print(found)
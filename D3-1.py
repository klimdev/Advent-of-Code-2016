
def IsTriangle(a, b, c):
    return (a+b>c) and (b+c>a) and (c+a>b)


triangleCount = 0
inputFile = open('D3.txt', 'r')

for inputLine in inputFile:
    cleanedUpInputLine = inputLine.replace('  ',' ')
    while cleanedUpInputLine is not inputLine:
        inputLine = cleanedUpInputLine
        cleanedUpInputLine = inputLine.replace('  ',' ')


    numbers = cleanedUpInputLine[1:].split(' ',3)
    a, b, c = numbers
    a = float(a); b = float(b); c = float(c)

    if IsTriangle(a,b,c):
        triangleCount += 1


print(triangleCount)





def IsTriangle(a, b, c):
    return 1 if ((a+b>c) and (b+c>a) and (c+a>b)) else 0


triangleCount = 0
inputFile = open('D3.txt', 'r')
checker = 0
a =[0.0,0.0,0.0]
b =[0.0,0.0,0.0]
c =[0.0,0.0,0.0]

for inputLine in inputFile:
    cleanedUpInputLine = inputLine.replace('  ',' ')
    while cleanedUpInputLine is not inputLine:
        inputLine = cleanedUpInputLine
        cleanedUpInputLine = inputLine.replace('  ',' ')

    numbers = cleanedUpInputLine[1:].split(' ',3)
    num1, num2, num3 = numbers
    num1 = float(num1); num2 = float(num2); num3 = float(num3)
    if checker is 0:
        a[0] = num1
        a[1] = num2
        a[2] = num3
    elif checker is 1:
        b[0] = num1
        b[1] = num2
        b[2] = num3
    elif checker is 2:
        c[0] = num1
        c[1] = num2
        c[2] = num3
        triangleCount += IsTriangle(a[0],b[0],c[0]) + IsTriangle(a[1],b[1],c[1]) + IsTriangle(a[2],b[2],c[2])

    checker = (checker+1)%3


print(triangleCount)




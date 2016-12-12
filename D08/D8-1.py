
from Display import Display

inputFile = open('D8.txt', 'r')

display = Display(50,6)
print(display)

for input in inputFile:
    display.Instruction(input)
    print(display)

print(display.Count())
print(str(display).replace(',','').replace(' ','').replace('0',' '))


from Display import Display

inputFile = open('test.txt', 'r')

display = Display(7,3)
print(display)

for input in inputFile:
    display.Instruction(input)
    print(display)

print(display)
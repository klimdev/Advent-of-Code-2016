

inputString = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"
#inputString = "R5, L5, R5, R3"

#R +1, L -1
totalStep = [0, 0, 0, 0]  # N R S L
currentDirection = 0

inputString = inputString.replace(' ', '')
#print(inputString)
commands = inputString.split(',')


for command in commands:
    command = command.replace(',', '')
    if command[0] == 'L':
        currentDirection = (4 + currentDirection - 1) % 4
        command = command.strip('L')
    else:
        currentDirection = (currentDirection + 1) % 4
        command = command.strip('R')

    totalStep[currentDirection] += int(command)

print(abs(totalStep[0] - totalStep[2]) + abs(totalStep[1] - totalStep[3]))

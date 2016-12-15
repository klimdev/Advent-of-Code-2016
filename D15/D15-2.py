

class Disc:
    def __init__(self, index, cycle, start):
        self.index = index
        self.cycle = cycle
        self.start = start

    def position(self, time):
        return ((self.start + self.index + time) % self.cycle)

    def check(self, time):
        return ((self.start + self.index + time) % self.cycle) == 0

inputFile = open('D15.txt','r')

discs = list()

for inputLine in inputFile:
    index = int(inputLine.split('#')[1].split(' ')[0])
    cycle = int(inputLine.split('has ')[1].split(' ')[0])
    start = int(inputLine.split('position ')[1].split('.')[0])
    discs.append(Disc(index, cycle, start))

prevAnswer = 400589
lastDisc = Disc(len(discs)+1, 11, 0)
discs.append(lastDisc)

time = 0
passed = False
while not passed:
    passed = True
    for disc in discs:
        passed &= disc.check(time)

    time += 1

print(time-1)
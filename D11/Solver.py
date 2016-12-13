
import queue
import copy

class Me:
    def __init__(self, floors):
        self.hold = list()
        self.floors = copy.deepcopy(floors)
        self.floor = 0
        self.step = 0
        self.diff = 0
        self.calcDiff()
        return

    def __lt__(self, other):
        #return self.step < other.step
        #return self.step**2 + self.diff < other.step**2 + other.diff
        #return self.diff < other.diff
        myFactor = float(self.diff)/other.diff
        return (myFactor * self.step) < (other.step / myFactor)

    def __gt__(self, other):
        #return self.step > other.step
        #return self.step**2 + self.diff > other.step**2 + other.diff
        myFactor = float(self.diff)/other.diff
        return (myFactor * self.step) > (other.step / myFactor)


    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
        #result = True
        #for floor in range(0, len(self.floors)):
        #    result &= str(self.floors[floor]) == str(other.floors[floor])
        #    if not result:
        #        break
        #return result

    def __hash__(self):
        hash = ''
        for floor in range(0, len(self.floors)):
            hash += self.floors[floor].strHash()
        #print(hash)
        return int(hash)

    def take(self, component):
        floor = self.floors[self.floor]
        if component.isGen() and component.name in floor.gens:
            #print(floor.gens)
            self.hold.append(floor.gens.pop(component.name))
            #print(floor.gens)
        elif component.isChip() and component.name in floor.chips:
            self.hold.append(floor.chips.pop(component.name))
        return

    def move(self, change):
        self.floor += change
        self.step += 1
        floor = self.floors[self.floor]
        for comp in self.hold:
            if comp.isGen():
                floor.gens.setdefault(comp.name, comp)
            else:
                floor.chips.setdefault(comp.name, comp)
        self.calcDiff()
        return

    def calcDiff(self):
        self.diff = 0
        i = 0
        for floor in self.floors:
            if i < self.floor:
                self.diff += (4 + self.floor - 2 * i) * len(floor.gens)
                self.diff += (4 + self.floor - 2 * i) * len(floor.chips)
            else:
                self.diff += (4 - i) * len(floor.gens)
                self.diff += (4 - i) * len(floor.chips)
        #self.diff /= 2
        return

    def createSets(self):
        floor = self.floors[self.floor]
        sets = list()
        for component in floor.gens.values():
            Set = set()
            Set.add(component)
            sets.append(Set)
        for component in floor.chips.values():
            Set = set()
            Set.add(component)
            sets.append(Set)
        size = len(sets)
        for i in range(0,size):
            for j in range(i+1,size):
                sets.append(sets[i].union(sets[j]))

        return sets

    def isValid(self):
        return self.floors[self.floor].checkFloor()

    def isDone(self):
        return self.floors[0].isEmpty() and self.floors[1].isEmpty() and self.floors[2].isEmpty()

    def canGoUp(self):
        return self.floor < len(self.floors)-1

    def canGoDown(self):
        return self.floor > 0 and not self.floors[self.floor].isEmpty()

    def showStatus(self):
        print('F4 {01}: {}{}{}{}{} | {}{}{}{}{}'.format())
        print('F3 {01}: {}{}{}{}{} | {}{}{}{}{}'.format())
        print('F2 {01}: {}{}{}{}{} | {}{}{}{}{}'.format())
        print('F1 {01}: {}{}{}{}{} | {}{}{}{}{}'.format())

class Component:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        return

    def isGen(self):
        return self.type == 'g'

    def isChip(self):
        return self.type == 'c'

class Generator(Component):
    def __init__(self, name):
        super(Generator, self).__init__(name, 'g')
        return

    def __str__(self):
        return '{}'.format(self.name) + ' gen'

    def __repr__(self):
        return self.__str__()


class Chip(Component):
    def __init__(self, name):
        super(Chip, self).__init__(name, 'c')
        return

    def __str__(self):
        return '{}'.format(self.name) + ' chip'

    def __repr__(self):
        return self.__str__()

class Floor:
    def __init__(self):
        self.gens = dict()
        self.chips = dict()
        return

    def __str__(self):
        return str(self.gens) + ' -- ' + str(self.chips)

    def __repr__(self):
        return self.__str__()

    def strHash(self):
        str = ''
        for i in range(0,5):
            if i in self.gens:
                str += '{}'.format(i)
            else:
                str += '{}'.format(5+i)
        for i in range(0, 5):
            if i in self.chips:
                str += '{}'.format(i)
            else:
                str += '{}'.format(5 + i)
        return str

    def checkFloor(self):
        if len(self.gens):
            for chip in self.chips.keys():
                if chip not in self.gens:
                    return False
        return True

    def isEmpty(self):
        return len(self.gens) == len(self.chips) and len(self.gens) == 0


class Solver:
    def __init__(self, floors):
        self.pq = queue.PriorityQueue()
        self.floors = copy.deepcopy(floors)
        self.visited = set()
        #print(x for x in floors)
        #print(x for x in self.floors)
        self.addToQueue(Me(self.floors))
        return

    def solve(self):
        prevStep = 0
        while not self.pq.empty():
            top = self.pq.get()

            if top.step != prevStep:
                prevStep = top.step
                print(prevStep)

            if top.isDone():
                print('--------------- done ---------------------')
                print(top.step)
                print('------------------------------------------')
                break

            sets = top.createSets()

            for Set in sets:
                topCopy = copy.deepcopy(top)
                #print(topCopy)
                #print(Set)
                for comp in Set:
                    #print(comp)
                    topCopy.take(comp)
                if topCopy.isValid():
                    #move up
                    if topCopy.canGoUp():
                        upCopy = copy.deepcopy(topCopy)
                        upCopy.move(1)
                        if not self.addToQueue(upCopy):
                            del upCopy
                    #move down
                    if topCopy.canGoDown():
                        downCopy = copy.deepcopy(topCopy)
                        downCopy.move(-1)
                        if not self.addToQueue(downCopy):
                            del downCopy
                del topCopy
        return

    def addToQueue(self, capture):
        if capture.isValid() and capture not in self.visited:
            self.pq.put(capture)
            self.visited.add(capture.__hash__())
            return True
        return False

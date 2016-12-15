
import queue
import copy

class Me:
    def __init__(self, floors, floor = 0):
        self.hold = list()
        self.floors = copy.deepcopy(floors)
        self.floor = floor
        self.step = 0
        self.hashString = ''
        self.hash()
        return

    def __lt__(self, other):
        return self.step < other.step
        #return self.step**2 + self.diff < other.step**2 + other.diff
        #return self.diff < other.diff
        #myFactor = float(self.diff)/other.diff
        #return (myFactor * self.step) < (other.step / myFactor)

    def __gt__(self, other):
        return self.step > other.step
        #return self.step**2 + self.diff > other.step**2 + other.diff
        #myFactor = float(self.diff)/other.diff
        #return (myFactor * self.step) > (other.step / myFactor)


    def __eq__(self, other):
        return self.hashString == other.hashString
        #result = True
        #for floor in range(0, len(self.floors)):
        #    result &= str(self.floors[floor]) == str(other.floors[floor])
        #    if not result:
        #        break
        #return result

    #def __hash__(self):
    #    hash = ''
    #    for floor in range(0, len(self.floors)):
    #        hash += self.floors[floor].strHash()
    #    #print(hash)
    #    return int(hash)

    def hash(self):
        self.hashString = '{}'.format(self.floor)
        for floor in range(0, len(self.floors)):
            self.hashString += self.floors[floor].strHash()
        return

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
        self.hold.clear()
        self.hash()
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

    def canGoUp(self):
        return self.floor < len(self.floors)-1

    def canGoDown(self):
        return self.floor > 0

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
    def __init__(self, size):
        self.size = size
        self.gens = dict()
        self.chips = dict()
        return

    def __str__(self):
        return str(self.gens) + ' -- ' + str(self.chips)

    def __repr__(self):
        return self.__str__()

    def strHash(self):
        str = ''
        for i in range(0, self.size):
            if i in self.gens:
                str += '{}'.format(i)
            else:
                str += '{}'.format(self.size+i)
        for i in range(0, self.size):
            if i in self.chips:
                str += '{}'.format(i)
            else:
                str += '{}'.format(self.size + i)
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
    def __init__(self, start):
        self.pq = queue.PriorityQueue()
        self.visited = set()
        self.addToQueue(start)
        return

    def solve(self, done):
        prevStep = 0
        while not self.pq.empty():
            top = self.pq.get()

            if top.step != prevStep:
                prevStep = top.step
                print(prevStep)

            if top == done:
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
            del top
        return

    def addToQueue(self, capture):
        if capture.isValid() and capture.hashString not in self.visited:
            self.pq.put(capture)
            self.visited.add(capture.hashString)
            return True
        return False

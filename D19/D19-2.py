import math

class Elves:
    def __init__(self, number):
        self.elves = [i + 1 for i in range(0, number)]
        return

    #Last man standing
    def lms(self):
        size = len(self.elves)
        index = 0
        while size > 1:
            target = math.floor(index + size/2.0)%size
            self.elves = self.elves[:target] + self.elves[target+1:]
            index += 1
            size -= 1
            #print(index)
            if index >= size:
                index = 0
                print(size)
        print()
        return self.elves[0]



print(Elves(3017957).lms())

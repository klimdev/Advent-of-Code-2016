
class Elves:
    def __init__(self, number):
        self.elves = [i + 1 for i in range(0, number)]
        return

    #Last man standing
    def lms(self):
        while len(self.elves) > 1:
            even = len(self.elves)%2 == 0
            self.elves = [ self.elves[i] for i in range(0, len(self.elves),2) ]
            if not even:
                self.elves.pop(0)

        print(len(self.elves))
        return self.elves[0]



print(Elves(3017957).lms())

import queue
import hashlib
import copy

class Board:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.xMin = xMin;
        self.xMax = xMax;
        self.yMin = yMin;
        self.yMax = yMax;
        return


class Me:
    def __init__(self, passcode):
        self.x = 0
        self.y = 0
        self.passcode = passcode
        self.step = 0
        self.path = ''
        return

    def __lt__(self, other):
        return self.step < other.step

    def __gt__(self, other):
        return self.step > other.step

    def up(self, board):
        if self.y > board.yMin:
            self.y -= 1
            self.path += 'U'
            self.step += 1
            return True
        return False

    def down(self, board):
        if self.y < board.yMax:
            self.y += 1
            self.path += 'D'
            self.step += 1
            return True
        return False

    def left(self, board):
        if self.x > board.xMin:
            self.x -= 1
            self.path += 'L'
            self.step += 1
            return True
        return False

    def right(self, board):
        if self.x < board.xMax:
            self.x += 1
            self.path += 'R'
            self.step += 1
            return True
        return False

    def getNewPasscode(self):
        return format('{}{}'.format(self.passcode,self.path)).encode('utf-8')

    def arrived(self, board):
        return self.x == board.xMax and self.y == board.yMax

def checkDoors(str):
    return [ False if str[i].isnumeric() or str[i] == 'a' else True for i in range(0,4) ]


board = Board(0,3,0,3)
pq = queue.PriorityQueue()
current = me = Me('gdjjyniy')
pq.put(me)
maxPath = None

while pq.not_empty:
    current = pq.get()
    if current.arrived(board):
        if maxPath:
            if current > maxPath:
                maxPath = current
                print(maxPath.step)
        else:
            maxPath = current
        continue

    h = hashlib.md5()
    h.update(current.getNewPasscode())

    doorOpen = checkDoors(h.hexdigest()[:4])
    nextMove = [ copy.deepcopy(current) for i in range(0,4) ]
    func = [ nextMove[0].up, nextMove[1].down, nextMove[2].left, nextMove[3].right ]
    for i in range(0,4):
        if doorOpen[i] and func[i](board):
            pq.put(nextMove[i])

print(maxPath.step)
print(maxPath.path)
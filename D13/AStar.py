import sys
import queue

class MazeBoard:
    def __init__(self, code):
        self.code = code
        self.w = -1
        self.h = -1
        self.board = list()
        self.increaseBoard()

    def calc(self, x, y):
        xy = x+y
        number = x*(xy+3) + y*(xy+1) + self.code
        #odd = wall
        return ("{0:b}".format(number).count('1')) % 2

    def increaseBoard(self):
        self.w += 1
        for y in range(0,self.h+1):
            self.board[y].append(self.calc(self.w, y))
        self.h += 1
        newRow = list()
        for x in range(0, self.w+1):
            newRow.append(self.calc(x, self.h))
        self.board.append(newRow)
        return

    def isWall(self,x,y):
        if y < 0 or x < 0:
            return True
        while y >= self.h or x >= self.w:
            self.increaseBoard()
        return self.board[y][x] == 1

class AStar:

    class Cell:
        def __init__(self, x,y, destCell = None, fromCell = None):
            self.x = x
            self.y = y
            if destCell:
                self.destCell = destCell
            self.fromCell = fromCell
            if fromCell:
                self.min = fromCell.min + 1
            else:
                self.min = sys.maxsize
            return

        def setMin(self, newCell):
            if self.fromCell:
                if newCell.min < self.fromCell.min:
                    self.fromCell = newCell
                    self.min = newCell.min + 1
                    return True
            else:
                self.fromCell = newCell
                self.min = newCell.min + 1
                return True
            return False

        def minDist(self):
            return self.min + abs(self.destCell.x - self.x) + abs(self.destCell.y - self.y)

        def __lt__(self, other):
            return self.minDist() < other.minDist()

        def __gt__(self, other):
            return self.minDist() > other.minDist()

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __hash__(self):
            return int(str(self.x) + '00' + str(self.y))

    def __init__(self, board):
        self.board = board
        return

    def findPath(self, startX, startY, destX, destY, maxStep = sys.maxsize):
        if self.board.isWall(destX, destY):
            return sys.maxsize

        visited = dict()
        pq = queue.PriorityQueue()
        destCell = self.Cell(destX,destY)
        cell = self.Cell(startX,startY,destCell)
        cell.min = 0
        visited.setdefault(cell.__hash__(),cell)
        pq.put(cell)

        direction = [ [-1,0], [0,-1], [1,0], [0,1]]

        while pq.not_empty:
            cell = pq.get()
            if cell == destCell:
                break
            if cell.min >= maxStep:
                return sys.maxsize
            for d in direction:
                newX = cell.x + d[0]
                newY = cell.y + d[1]

                if self.board.isWall(newX, newY):
                    continue

                newCell = self.Cell(newX, newY, destCell, cell)
                add = True
                if newCell.__hash__() in visited:
                    add = visited[newCell.__hash__()].setMin(newCell)

                if add:
                    visited.setdefault(newCell.__hash__(), newCell)
                    pq.put(newCell)

        print(visited[destCell.__hash__()].min)
        return visited[destCell.__hash__()].min


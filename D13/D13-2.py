
from AStar import MazeBoard, AStar

board = MazeBoard(1350)

solver = AStar(board)

maxStep = 50
count = 0
for y in range(0,maxStep+1):
    for x in range(0,maxStep+1):
        if solver.findPath(1, 1, x, y, maxStep) <= maxStep:
            count += 1

print('count!')
print(count)
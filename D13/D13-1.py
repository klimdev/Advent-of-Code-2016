
from AStar import MazeBoard, AStar

board = MazeBoard(1350)

solver = AStar(board)

solver.findPath(1,1,31,39)
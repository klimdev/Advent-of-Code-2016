
from AStar import MazeBoard, AStar

board = MazeBoard(10)

solver = AStar(board)

solver.findPath(1,1,7,4)
import copy
from minimax import calculateMoves

from game import calculateMoves

class Node:
    def __init__(self, board, turn, parent = None, move = None):
        self.board = copy.copy(board)
        self.turn = turn
        self.parent = parent
        self.move = move
        self.visits = 0
        self.wins = 0
        self.children = []
        self.unvisitedMoves = calculateMoves(board)
        
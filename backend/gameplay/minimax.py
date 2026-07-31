from game import initBoard, validateMove, makeMove, checkWin, undoMove, TOKENS
import random

def boardFull(board):
    if " " not in board:
        return True
    return False

def calculateMoves(board):
    moves = []
    for column in range(7):
        row = validateMove(board, column)
        if row != -1:
            moves.append([int(row), int(column)])

    return moves

def randomMove(board, turn):
    possibleMoves = calculateMoves(board)
    move = random.choice(possibleMoves)
    row, column = move[0], move[1]
    makeMove(board, row, column, turn)
    return 

def minimax(board, depth, isMaximising):
    if depth == 0 or boardFull(board):
        return evaluateBoard(board)

    possibleMoves = calculateMoves(board)

    if isMaximising:
        weight = float("inf")
        for move in possibleMoves:
            # check for immediate wins and deal with that
            weight = max(weight, minimax(board, depth -1, False))
        return weight

    else:
        weight = float("-inf")
        for move in possibleMoves:
            # check for immediate wins and deal with that
            weight = min(weight, minimax(board, depth -1, False))
        return weight

def evaluateBoard(board):
    # some evaluation function
    pass

'''
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
'''

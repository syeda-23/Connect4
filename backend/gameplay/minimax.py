from game import initBoard, validateMove, makeMove, checkWin, undoMove,TOKENS
import random

def showBoard(board):
    print("   0    1    2    3    4    5    6 ")
    for row in range(6):
        print(row, board[row])
        

def boardFull(board):
    if len(calculateMoves(board)) == 0:
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

def minimax(board, depth, isMaximising, turn):
    #print("minimax called with depth:", depth, "isMaximising:", isMaximising, "turn:", turn)

    if depth == 0 or boardFull(board):
        return evaluateBoard(board), None

    possibleMoves = calculateMoves(board)
    bestMoves= []
    if turn == 1:
        opponent = 2
    else:
        opponent = 1

    if isMaximising:
        bestWeight = float("-inf")
        for move in possibleMoves:
            row, column = move[0], move[1]
            makeMove(board, row, column, turn)
            if checkWin(board, row, column, turn):
                undoMove(board, row, column)
                weight = 100000 + depth
            else:
                weight =  minimax(board, depth -1, False, opponent)[0]
                undoMove(board, row, column)
                
            if weight > bestWeight:
                bestWeight = weight
                bestMoves = [[row, column]]
            elif weight == bestWeight:
                bestMoves.append([row, column])
            
        return bestWeight, bestMoves

    else:
        bestWeight = float("inf")
        for move in possibleMoves:
            row, column = move[0], move[1]
            makeMove(board, row, column, turn)
            if checkWin(board, row, column, turn):
                undoMove(board, row, column)
                weight = -100000 - depth
            else:
                weight = minimax(board, depth -1, True, opponent)[0]
                undoMove(board, row, column)
            if weight < bestWeight:
                bestWeight = weight
                bestMoves = [[row, column]]
            elif weight == bestWeight:
                bestMoves.append([row, column])

        return bestWeight, bestMoves

def evaluateBoard(board):
    weights = {"꩜":-1, "⬤":1}
    evaluationMatrix = [[3, 4, 5, 7, 5, 4, 3],
                        [4, 6, 8, 10, 8, 6, 4],
                        [5, 8, 11, 13, 11, 8, 5],
                        [5, 8, 11, 13, 11, 8, 5],
                        [4, 6, 8, 10, 8, 6, 4],
                        [3, 4, 5, 7, 5, 4, 3]]

    score = 0
    for row in range(6):
        for column in range(7):
            if board[row][column] != " ":
                score += weights[board[row][column]]*evaluationMatrix[row][column]

    return score


def makeMinimaxMove(board, depth, turn):
    moves, croves = minimax(board, depth, True, 2)
    print(moves, croves)
    move = random.choice(croves)
    print("MOVE", move)
    makeMove(board, move[0], move[1], turn)
    return move[0], move[1]

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

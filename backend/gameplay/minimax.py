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

def minimax(board, depth, isMaximising, turn, nodesExplored):

    print("\n minimax(", depth, "," ,isMaximising, ",", turn, ")")
    if depth == 0 or boardFull(board):
        print("Max depth reached at score:", evaluateBoard(board))
        return evaluateBoard(board), None, nodesExplored

    possibleMoves = calculateMoves(board)
    print("Possible Moves:", possibleMoves)
    bestMoves= []
    if turn == 1:
        opponent = 2
    else:
        opponent = 1

    if isMaximising:
        bestWeight = float("-inf")
        for move in possibleMoves:
            print("Checking", move)
            row, column = move[0], move[1]
            makeMove(board, row, column, turn)
            nodesExplored += 1
            if checkWin(board, row, column, turn):
                print("Win for player", turn, "at depth", depth, "detected")
                weight = 100000 + depth
                undoMove(board, row, column)
            else:
                weight, score, nodesExplored =  minimax(board, depth -1, False, opponent, nodesExplored)
                undoMove(board, row, column)
                
            if weight > bestWeight:
                bestWeight = weight
                bestMoves = [[row, column]]
            elif weight == bestWeight:
                bestMoves.append([row, column])

        print("Returning moves", bestMoves, "score", bestWeight)
        
            
        return bestWeight, bestMoves, nodesExplored

    else:
        bestWeight = float("inf")
        for move in possibleMoves:
            print("Checking", move)
            row, column = move[0], move[1]
            makeMove(board, row, column, turn)
            nodesExplored += 1
            if checkWin(board, row, column, turn):
                print("Win for player", turn, "at depth", depth, "detected")
                      
                weight = -100000 - depth
                undoMove(board, row, column)
            else:
                weight, score, nodesExplored = minimax(board, depth -1, True, opponent, nodesExplored)
                undoMove(board, row, column)
            if weight < bestWeight:
                bestWeight = weight
                bestMoves = [[row, column]]
            elif weight == bestWeight:
                bestMoves.append([row, column])

        print("returning moves", bestMoves, "score", bestWeight, "from minimax depth", depth, "turn", turn)

        return bestWeight, bestMoves, nodesExplored

def alphabeta(board, depth, isMaximising, turn, alpha, beta, nodesExplored):

    if depth == 0 or boardFull(board):
        return evaluateBoard(board), None, nodesExplored
        
    possibleMoves = calculateMoves(board)
    print("Possible Moves:", possibleMoves)
    bestMoves= []
    if turn == 1:
        opponent = 2
    else:
        opponent = 1

    if isMaximising:
            bestWeight = float("-inf")
            for move in possibleMoves:
                print("Checking", move)
                row, column = move[0], move[1]
                makeMove(board, row, column, turn)
                nodesExplored += 1
                if checkWin(board, row, column, turn):
                    print("Win for player", turn, "at depth", depth, "detected")
                    weight = 100000 + depth
                    undoMove(board, row, column)
                else:
                    weight , score, nodesExplored =  alphabeta(board, depth -1, False, opponent, alpha, beta, nodesExplored)
                    undoMove(board, row, column)
                    
                if weight > bestWeight:
                    bestWeight = weight
                    bestMoves = [[row, column]]
                elif weight == bestWeight:
                    bestMoves.append([row, column])

                if bestWeight >= beta:
                    break
                alpha = max(alpha, bestWeight)

            print("Returning moves", bestMoves, "score", bestWeight)
             
            return bestWeight, bestMoves, nodesExplored
    
    else:
        bestWeight = float("inf")
        for move in possibleMoves:
            print("Checking", move)
            row, column = move[0], move[1]
            makeMove(board, row, column, turn)
            nodesExplored += 1
            if checkWin(board, row, column, turn):
                print("Win for player", turn, "at depth", depth, "detected")
                        
                weight = -100000 - depth
                undoMove(board, row, column)
            else:
                weight , score, nodesExplored = alphabeta(board, depth -1, True, opponent, alpha, beta, nodesExplored)
                undoMove(board, row, column)
            if weight < bestWeight:
                bestWeight = weight
                bestMoves = [[row, column]]
            elif weight == bestWeight:
                bestMoves.append([row, column])

            if bestWeight <= alpha:
                break
            beta = min(beta, bestWeight)

        print("returning moves", bestMoves, "score", bestWeight, "from minimax depth", depth, "turn", turn)

        return bestWeight, bestMoves, nodesExplored
    
    

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

def makeMinimaxMove(board, depth, turn, pruning):
    if not pruning:
        moves, score, nodesExplored = minimax(board, depth, True, 2, 0)
    else:
        moves, score, nodesExplored = alphabeta(board, depth, True, 2, float("-inf"), float("inf"), 0)[1]

    print("Nodes explored:", nodesExplored)
    move = random.choice(moves)
    makeMove(board, move[0], move[1], turn)
    return move[0], move[1]

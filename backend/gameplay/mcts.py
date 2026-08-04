from minimax import calculateMoves

def makeMCTSMove():
    pass

def MCTS(board):
    possibleMoves = calculateMoves(board)

'''
mcts(root, simulations)

    for each child node:
        weight = expand(child)
        root.value += score

    nextNode = selection(tree)

    mcts(nextNode)

selection(tree):
    calculation function to determine which child node to investigate further

expand(root):
    
    possibleMoves = calculateMoves(root)

    if not possibleMoves:
        if checkWin(board, row ,column, turn):
            return 1
        else:
            return 0

    move = random.choice(possibleMoves)
    board = makeMove(move, board)
    expand(board)



    
'''


def comparisonMode(board, turn, pruning, depth, rollouts, exploration, firstTurn):

    


    makeMinimaxMove(board, depth, turn, pruning)

    mcts(board, rollouts, turn)
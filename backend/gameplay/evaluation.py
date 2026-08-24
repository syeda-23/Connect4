import time
from game import checkGameOver, TOKENS, OPPONENTS
from minimax import makeMinimaxMove
from mcts import mcts

def displayBoard(board):
    print("   0    1    2    3    4    5    6 ")
    for row in range(6):
        print(row, board[row])

def comparisonMode(board, turn, pruning, depth, rollouts, exploration, firstTurn):

    displayBoard(board)
    turn = firstTurn
    turns = {1: "Minimax", 2: "MCTS"}

    while True:

        print(turns[turn] + "'s turn...")

        start = time.time()
        if turn == 1:
            row, column = makeMinimaxMove(board, depth, turn, pruning)
        else:
            row, column = mcts(board, rollouts, turn)
        end = time.time()
        print("Time taken:", end-start)
        displayBoard(board)

        if checkGameOver(board, row, column, turn):
            print(turns[turn], "wins!")
            return
        
        turn = OPPONENTS[turn]
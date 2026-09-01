import time
from game import checkGameOver, TOKENS, OPPONENTS, initGame
from minimax import makeMinimaxMove
from mcts import mcts
from minimax import randomMove


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
            row, column, nodesExplored = makeMinimaxMove(board, depth, turn, pruning)
            print("Nodes Explored:", nodesExplored)
        else:
            row, column = mcts(board, rollouts, turn)
        end = time.time()
        print("Time taken:", end-start)
        displayBoard(board)

        if checkGameOver(board, row, column, turn):
            print(turns[turn], "wins!")
            return
        
        turn = OPPONENTS[turn]

def simulateGame(choice1, choice2, p1, p2, p3, p4):

    #print("Parameters:", p1, p2, p3, p4)
    
    turns = {1: "Minimax", 2: "MCTS"}
    board, turn, count = initGame()

    while True:

        if choice1 == 1:
            row, column, nodesExplored = makeMinimaxMove(board, p2, turn, p1)
        elif choice1 == 2:
            print("\n\n\nBOARD\n\n\n", board)
            row, column = mcts(board, p1, turn)
        elif choice1 == 3:
            row, column = randomMove(board, turn)
        if checkGameOver(board, row, column, turn):
            return 1

        turn = OPPONENTS[turn]

        if choice2 == 1:
            row, column, nodesExplored = makeMinimaxMove(board, p4, turn, p3)
        elif choice2 == 2:
            print("\n\n\nboard\n\n\n", board)
            row, column = mcts(board, p3, turn)
        elif choice2 == 3:
            row, column = randomMove(board, turn)
        if checkGameOver(board, row, column, turn):
            return 2
            
        turn = OPPONENTS[turn]



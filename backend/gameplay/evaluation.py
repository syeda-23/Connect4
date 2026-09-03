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
    average_time = {1:0, 2:0}
    average_nodes = {1:0, 2:0}
    counts = {1:0, 2:0}

    while True:

        start1 = time.time()

        if choice1 == 1:
            row, column, nodesExplored = makeMinimaxMove(board, p2, turn, p1)
            average_nodes[1] += nodesExplored
            
        elif choice1 == 2:
            print("\n\n\nBOARD\n\n\n", board)
            row, column = mcts(board, p1, turn)
        elif choice1 == 3:
            row, column = randomMove(board, turn)

        end1 = time.time()
        

        average_time[1] += end1 - start1
        counts[1] += 1
        
        if checkGameOver(board, row, column, turn):
            average_time[1], average_time[2] = average_time[1]/counts[1] , average_time[2]/counts[2]
            average_nodes[1], average_nodes[2] = average_nodes[1]/counts[1] ,average_nodes[2]/counts[2]
            #print("Nodes",average_nodes)
            #print("Times",average_time)
            
            return 1, average_time, average_nodes

        turn = OPPONENTS[turn]

        start2 = time.time()

        if choice2 == 1:
            row, column, nodesExplored = makeMinimaxMove(board, p4, turn, p3)
            average_nodes[2] += nodesExplored
        elif choice2 == 2:
            print("\n\n\nboard\n\n\n", board)
            row, column = mcts(board, p3, turn)
        elif choice2 == 3:
            row, column = randomMove(board, turn)

        end2 = time.time()
        average_time[2] += end2 - start2
        counts[2] += 1

        if checkGameOver(board, row, column, turn):
            average_time[1], average_time[2] = average_time[1]/counts[1] , average_time[2]/counts[2]
            average_nodes[1], average_nodes[2] = average_nodes[1]/counts[1] ,average_nodes[2]/counts[2]
            #print("Nodes",average_nodes)
            #print("Times",average_time)
            return 2, average_time, average_nodes
            
        turn = OPPONENTS[turn]



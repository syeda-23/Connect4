from game import initGame, validateMove, makeMove, checkGameOver, TOKENS, OPPONENTS
from minimax import calculateMoves, randomMove, makeMinimaxMove, alphabeta
from mcts import mcts
from evaluation import comparisonMode, simulateGame

def displayBoard(board):
    print("   0    1    2    3    4    5    6 ")
    for row in range(6):
        print(row, board[row])

def getMove(board):
    column = int(input("Enter column to drop token into: "))
    row = int(validateMove(board, column))
    while row == -1:
        column = int(input("Enter column to drop token into: "))
        row = int(validateMove(board, column))
    return(row, column)

def Menu():
    mode = input("**MENU**\n1. Multiplayer (Human v Human)\n2. Play against computer opponent(non intelligent)\n3. Play against minimax\n4. Play against MCTS\n5. Observe MCTS vs Minimax\n6. Stats mode\nEnter choice: ")
    if mode == "6":
        statsMode()
    else:
        play(mode)

def userPlay(board, turn):
    print("\n" + TOKENS[turn] + "'s turn")
    row, column =  getMove(board)
    makeMove(board, row, column, turn)
    displayBoard(board)
    return row, column

def getParameters(mode):
    if mode == 1:
        pruning = input("Enable Alpha-Beta pruning (Y/N): ").lower()
        pruning = (pruning == "y")
        depth = int(input("Select minimax depth (1-5): "))
        return (pruning, depth)

    if mode == 2:
        rollouts = int(input("Enter desired number of rollouts (100-1000): "))
        exploration = int(input("Enter desired exploration factor (Default value is 1): "))
        return (rollouts, exploration)

    return None, None
    

def statsMode():
    print("Use this mode to run a number of simulations")
    simulations = int(input("Enter number of simulations you'd like to run: "))
    choice1 = int(input("\n1. Minimax \n2. MCTS \n3. Random\nChoose settings for first player: "))
    
    p1, p2 = getParameters(choice1)

    choice2 = int(input("\n1. Minimax \n2. MCTS \n3. Random\nChoose settings for second player: "))
    
    p3, p4 = getParameters(choice2)
    

    wins = {1:0, 2:0}

    for i in range(simulations):
        wins[simulateGame(choice1, choice2, p1, p2, p3, p4)] += 1

    print("Player 1 win rate:", wins[1]/simulations)
    print("Player 2 win rate:", wins[2]/simulations)

    return 


def play(mode):
    board, turn, count = initGame()
    displayBoard(board)

    if mode == "5":
        pruning, depth = getParameters(1)
        rollouts, exploration = getParameters(2)
        firstTurn = int(input("Enter 1 for minimax to go first, 2 for mcts to go first: "))
        comparisonMode(board, turn, pruning, depth, rollouts, exploration, firstTurn)

    else:

        while True:
            if turn == 1:
                row, column = userPlay(board, turn)
            elif turn == 2:
                if mode == "1":
                    row, column = userPlay(board, turn)
                elif mode == "2":
                    row, column = randomMove(board, turn)
                elif mode == "3":
                    depth = 3
                    row, column = makeMinimaxMove(board, depth, turn, True)
                elif mode == "4":
                    row, column = mcts(board, 500, turn)

                displayBoard(board)

            if checkGameOver(board, row, column, turn):
                return 

            turn = OPPONENTS[turn]

if __name__ == "__main__":
    Menu()
    '''
    board = [['⬤', 'X', 'X', '⬤', '⬤', '⬤', 'X'], 
             ['X', 'X', 'X', 'X', 'X', 'X', '⬤'],
            ['⬤', '⬤', 'X', '⬤', '⬤', '⬤', 'X'], 
            ['X', 'X', '⬤', 'X', 'X', '⬤', 'X'], 
            ['⬤', 'X', '⬤', 'X', '⬤', '⬤', '⬤'], 
            ['⬤', 'X', '⬤', 'X', '⬤', 'X', '⬤']]
    print(checkGameOver(board, row, column, turn))
    '''

from game import initBoard, validateMove, makeMove, checkWin, TOKENS
from minimax import calculateMoves, randomMove, makeMinimaxMove, alphabeta

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
    mode = input("**MENU**\n1. Multiplayer (Human v Human)\n2. Play against computer opponent(non intelligent)\n3. Play against minimax\n4. Play against MCTS\nEnter choice: ")
    if mode == "1":
        playMultiplayer()
    if mode == "2":
        playRandomly()
    if mode == "3":
        depth = int(input("Enter depth for minimax to use: "))
        playMinimax(depth)
    if mode == "4":
        playMCTS()

def userPlay():
    pass
    
def playMultiplayer(): 
    turn = 1
    count = 0
    board = initBoard()
    displayBoard(board)

    while True:
        print("\n" + TOKENS[turn] + "'s turn")
        row, column = getMove(board)
        makeMove(board, row, column, turn)
        count += 1
        displayBoard(board)

        if checkWin(board, row, column, turn):
            print("Player", turn, "wins!")
            return

        if count == 42:
            print("Draw - Game Over!")
            return

        if turn == 1:
            turn = 2
        else:
            turn = 1

def playRandomly():
    turn = 1
    count = 0
    board = initBoard()
    displayBoard(board)

    while True:
        if turn == 1:
            print("\n" + TOKENS[turn] + "'s turn")
            row, column =  getMove(board)
            makeMove(board, row, column, turn)
            count += 1
            displayBoard(board)
            turn = 2
        elif turn == 2:
            randomMove(board, turn)
            displayBoard(board)
            turn = 1

        if checkWin(board, row, column, turn):
            print("Player", turn, "wins!")
            return

        elif count == 42:
            print("Draw - Game Over!")
            return 

def playMinimax(depth):

    turn = 1
    count = 0
    board = initBoard()
    displayBoard(board)

    while True:
        if turn == 1:
            print("\n" + TOKENS[turn] + "'s turn")
            row, column =  getMove(board)
            makeMove(board, row, column, turn)
        elif turn == 2:
            row, column = makeMinimaxMove(board, depth, turn, True)

        count += 1
        displayBoard(board)
        if checkWin(board, row, column, turn):
            print("Player", turn, "wins!")
            return
        elif count == 42:
            print("DRAW - Game Over!!")
            return

        if turn == 1:
            turn = 2
        else:
            turn = 1

def playMCTS():
    print("MCTS")


if __name__ == "__main__":
    Menu()

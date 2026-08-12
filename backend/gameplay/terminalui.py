from game import initGame, validateMove, makeMove, checkGameOver, TOKENS, OPPONENTS
from minimax import calculateMoves, randomMove, makeMinimaxMove, alphabeta
from mcts import mcts

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
    play(mode)

def userPlay(board, turn):
    print("\n" + TOKENS[turn] + "'s turn")
    row, column =  getMove(board)
    makeMove(board, row, column, turn)
    displayBoard(board)
    return row, column
    

def play(mode):
    board, turn, count = initGame()
    displayBoard(board)

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
                row, column = mcts(board, 100, turn)

            displayBoard(board)

        turn = OPPONENTS[turn]

        if checkGameOver(board, row, column, turn):
            return 

if __name__ == "__main__":
    Menu()

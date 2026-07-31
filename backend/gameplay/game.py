
def initBoard():
    board = []
    for row in range(6):
        r = []
        for col in range(7):
            r.append(" ")
        board.append(r)
    print(board)
    return board

def displayBoard(board):
    print("   0    1    2    3    4    5    6 ")
    for row in range(6):
        print(row, board[row])

def validateMove(board, column):
    row = 5
    while row >= 0:
        if board[row][column] == " ":
            return row
        row -= 1
    return -1

def getMove(board):
    column = int(input("Enter column to drop token into: "))
    row = int(validateMove(board, column))
    while row == -1:
        column = int(input("Enter column to drop token into: "))
        row = int(validateMove(board, column))
    return(row, column)

def makeMove(board, row, column, turn, tokens):
    board[row][column] = tokens[turn]

def consecutiveRun(sequence, turn, tokens):
    count = 0
    i = 0
    while i < len(sequence):
        if count == 4:
            return True
        if sequence[i] == tokens[turn]:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        i += 1
    return False
    

def checkWin(board, row, column, turn, tokens):
    # check diagonally
    diag1, diag2 = [], []
    i, j = row, column

    while i != 5 and j != 6:
        i += 1
        j += 1
    
    while i >= 0 and j >= 0:
        
        diag1.append(board[i][j])
        i -= 1
        j -= 1

    i,j = row, column

    while i != 0 and j != 6:
            i -= 1
            j += 1
        
    while i <= 5 and j >= 0:
        diag2.append(board[i][j])
        i += 1
        j -= 1

    if consecutiveRun(diag1, turn, tokens) or consecutiveRun(diag2, turn, tokens): 
        return True 

    # check horizontally
    if consecutiveRun(board[row], turn, tokens): 
        return True

    # check vertically
    col = []
    for i in range(6):
        col.append(board[i][column])
    if consecutiveRun(col, turn, tokens):
        return True
    
    return False

def playGame():
    
    tokens = {1: "꩜", 2: "⬤"}
    turn = 1
    gameOver = False

    board = initBoard()
    displayBoard(board)
    while not gameOver:
        print(tokens[turn] + "'s turn")
        row, column =  getMove(board)
        makeMove(board, row, column, turn, tokens)
        displayBoard(board)
        if checkWin(board, row, column, turn, tokens):
            print("Player", turn, "wins!")
            gameOver = True
            return
        if turn == 1:
            turn = 2
        else:
            turn = 1


playGame()


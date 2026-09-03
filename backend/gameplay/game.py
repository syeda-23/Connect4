

TOKENS = {1: "X", 2: "⬤"}
OPPONENTS = {1:2, 2:1}

def initGame():
    turn = 1
    count = 0
    board = []
    for row in range(6):
        r = []
        for col in range(7):
            r.append(" ")
        board.append(r)
    return board, turn, count

def validateMove(board, column):
    row = 5
    while row >= 0:
        if board[row][column] == " ":
            return row
        row -= 1
    return -1

def makeMove(board, row, column, turn):
    board[row][column] = TOKENS[turn]

def undoMove(board, row, column):
    board[row][column] = " "

def consecutiveRun(sequence, turn):
    count = 0
    i = 0
    while i < len(sequence):
        if count == 4:
            return True
        if sequence[i] == TOKENS[turn]:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        i += 1
    return False
    

def checkWin(board, row, column, turn):
    
    # check diagonally
    ranges = [[[5,6,1,1], [0,0,-1,-1]], [[0,6,-1,1], [5,0,1,-1]]]

    for i in range(2):
        r,c, sequence = row, column, []
        indices = ranges[i]

        while r != indices[0][0] and c != indices[0][1]:
            r += indices[0][2]
            c += indices[0][3]

        while r != indices[1][0] and c != indices[1][1]:
            sequence.append(board[r][c])
            r += indices[1][2]
            c += indices[1][3]
        sequence.append(board[r][c])  

        if consecutiveRun(sequence, turn):
            return True

    # check horizontally
    if consecutiveRun(board[row], turn): 
        return True

    # check vertically
    col = []
    for i in range(6):
        col.append(board[i][column])
    if consecutiveRun(col, turn):
        return True
    
    return False

def calculateMoves(board):
    moves = []
    for column in range(7):
        row = validateMove(board, column)
        if row != -1:
            moves.append([int(row), int(column)])

    return moves

def checkGameOver(board, row, column, turn):
    if checkWin(board, row, column, turn):
        #print("Player", turn, "won!")
        return True
    elif not calculateMoves(board):
        #print("Draw - Game Over")
        return True
    else:
        return False


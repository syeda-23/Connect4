from minimax import calculateMoves
from Node import Node
import math

def mcts2(root):
    while count <= simulations:
        child = traverse(root)
        weight = expand(child)
        backpropagate(child, weight)
    return bestMove(root)

def mcts(board, turn, simulations, count = 0):
    if turn == 1:
        opponent = 2
    else:
        opponent = 1

    root = Node(board, turn)

    while count <= simulations:
        if not node.children:

            moves = calculateMoves(board)
            for move in moves:
                board = makeMove(move[0], move[1])
                child = Node(board, opponent, root, move)
                root.children.append(child)
                undoMove(move[0], moves[1])

        child = select(root)
        expand(child)

    return bestMove(root)

def select(root):
    ## root.children might be empty!?
    ## child here is an OBJECT - where has this been declared though??
    best = 0 
    selection = None
    for child in root.children:
        if uct(child) > best:
            max = uct(child)
            selection = child

    return selection

def uct(node):
    ## will crash due to 0s on the denominator
    ## where have i updated wins/visits in the code for this to work??
    c = 1
    return (node.wins/node.visits) + c*math.sqrt(math.log(node.parent.visits)/node.visits)

def expand(root):
    ## are we wure this root properly exists?
    ## this base case is NOT CORRECT, also possibleMoves isnt even a thing yet
    ## do we ever update unvisitedMoves once we've visited a move?
    while not root.unvisitedMoves:
        expand(root.random.choice(root.possibleMoves))

    backpropagate(result, root.parent)

    if not root.unvisitedMoves:
        backpropagate(result)


    # choose a random child node
    # make a Node out of it
    # choose another child node from there

    move = random.choice(root.unvisitedMoves)

    
    possibleMoves = calculateMoves(root)

    if not possibleMoves:
        if checkWin(board, row ,column, turn):
            return 1
        else:
            return 0

    move = random.choice(possibleMoves)
    board = makeMove(move, board)
    expand(board)

def bestMove(root):
    mostVisits = 0
    moves = None
    for child in root.children:
        if child.visits > mostVisits:
            mostVisits = child.visits
            move = child.move

    return move



    

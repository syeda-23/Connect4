
from Node import Node
import math
import random
from game import makeMove, undoMove, checkWin, TOKENS, OPPONENTS, calculateMoves

def mcts(board, rollouts, turn):
    global_turn = turn
    root = Node(board, turn)

    for r in range(rollouts):
        if root.children and not root.unvisitedMoves:
            node = select(root)
        else:
            node = root

        child = expand(board, node, node.turn)
        score, next_turn = simulate(child.board, child, child.turn, global_turn)

        if child.turn == global_turn:
            start_score = 1 - score
        else:
            start_score = score
        backpropagate(start_score, child)

    row, column = bestMove(root)
    makeMove(board, row, column, turn)
    return row, column

def select(root):
    while root.children and not root.unvisitedMoves:

        bestUCT = float("-inf")
        selected_node = None

        for child in root.children:
            uct = calculateUCT(child)
            if uct > bestUCT:
                selected_node = child
                bestUCT = uct

        root = selected_node

    return root

def calculateUCT(node):
    c = 1
    exploitation = node.wins/node.visits
    exploration = math.sqrt(math.log(node.parent.visits)/node.visits)

    return exploitation + c*exploration


def expand(board, root, turn):

    move = random.choice(root.unvisitedMoves)
    makeMove(board, move[0], move[1], turn)
    child = Node(board, OPPONENTS[turn], root, move)
    undoMove(board, move[0], move[1])

    root.children.append(child)
    root.unvisitedMoves.remove(move)

    return child

def simulate(board, root, turn, global_turn, previous_move = None):

    score = isTerminalState(board, previous_move, turn, global_turn)

    if score is False:
        if not previous_move:
            move = random.choice(root.unvisitedMoves)
        else:
            move = random.choice(calculateMoves(board))

        makeMove(board, move[0], move[1], turn)
        score, turn = simulate(board, root, OPPONENTS[turn], global_turn, move)
        undoMove(board, move[0], move[1])

    return score, turn

def isTerminalState(board, previous_move, turn, global_turn):
    if not previous_move:
        return False

    mover = OPPONENTS[turn]
    
    if checkWin(board, previous_move[0], previous_move[1], mover):
        if mover == global_turn:
            return 1
        return 0

    if not calculateMoves(board):
        return 0
    

    return False

def backpropagate(score, node):
    node.visits += 1
    node.wins += score
    if node.parent:
        backpropagate(1-score, node.parent)

    return

def bestMove(root):
    max_visits = float("-inf")
    best_child = None
    for child in root.children:
        if child.visits > max_visits:
            max_visits = child.visits
            best_child = child

    best_move = best_child.move
    return best_move[0], best_move[1]


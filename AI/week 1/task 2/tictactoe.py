"""
Tic Tac Toe Player
"""

import math
import copy


X = "X"
O = "O"
EMPTY = None

PLAYERS = (X, O)

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    
    for row in board:
        countX += row.count(X)
        countO += row.count(O)
        
    return X if (countX + countO) % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    
    # Iterating the field.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in PLAYERS: # If the cell is empty add it to action.
                actionsSet.add((i, j))
    
    return actionsSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copiedBoard = copy.deepcopy(board)
    
    if copiedBoard[action[0]][action[1]] in PLAYERS:
        raise Exception("The action cannot be applied. Func \"result\"")
    else:
        copiedBoard[action[0]][action[1]] = player(board)
    
    return copiedBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check rows and columns.
    for i in range(len(board)):
        if (board[i][0] in PLAYERS) and (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
        if (board[0][i] in PLAYERS) and (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]
    
    # Check diagonals.
    if (board[0][0] in PLAYERS) and (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    if (board[0][2] in PLAYERS) and (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) in PLAYERS:
        return True
    
    for row in board:
        for cell in row:
            if cell not in PLAYERS: # We have an empty space.
                return False
    
    return True # Draw


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if playerWin := winner(board):
        return 1 if playerWin == X else -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    
    currentPlayer = player(board)
    posiableActs = actions(board)
    minActs = dict()
    maxActs = dict()
    
    for act in posiableActs:
        if currentPlayer == X:
            maxActs[utility(result(board, act))] = act
        else:
            minActs[utility(result(board, act))] = act
    
    if currentPlayer == X:
        return maxActs[max(maxActs.keys())]
    else:
        return minActs[min(minActs.keys())]
    
    return None

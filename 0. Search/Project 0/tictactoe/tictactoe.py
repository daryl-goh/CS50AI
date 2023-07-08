"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                allPossibleActions.add((row, col))

    return allPossibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)

    return board_copy

# Create function to check if there is a winner in row
def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] ==  player and board[row][1] == player and board[row][2] == player:
            return True
    return False

# Create function to check if there is a winner in col
def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] ==  player and board[1][col] == player and board[2][col] == player:
            return True
    return False

# Create function to check if there is a winner in first diag
def checkFirstDiag(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count +=  1
    if count == 3:
        return True
    else:
        return False

# Create function to check if there is a winner in second diag  
def checkSecondDiag(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count +=  1
    if count == 3:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkFirstDiag(board, X) or checkSecondDiag(board, X):
        return X
    elif checkRow(board, O) or checkRow(board, O) or checkFirstDiag(board, O) or checkSecondDiag(board, O):
        return O
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

# Create max_value function

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

# Create min_value function

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # Case of player is X (max-player)
    elif player(board) == X:
        plays = []
        # Loop over the possible actions
        for action in actions(board):
            # Add in plays list a tuple with the min_value and the action that results to its value
            plays.append([min_value(result(board, action)), action])
        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    # Case of player is O (min-player)
    elif player(board) == O:
        plays = []
        # Loop over the possible actions
        for action in actions(board):
            # Add in plays list a tuple with the max_value and the action that results to its value
            plays.append([max_value(result(board, action)), action])
        # Sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0], reverse=False)[0][1]
    


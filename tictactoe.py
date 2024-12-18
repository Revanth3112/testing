"""
Tic Tac Toe Player
"""

import math,copy,random

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
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count+=1
    if count%2 == 0:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    poss_actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                poss_actions.add((i,j))
    return poss_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    valid_actions = actions(board)
    if action not in valid_actions:
        raise IndexError
    dup_board = copy.deepcopy(board)
    if player(dup_board) == X:
        dup_board[action[0]][action[1]] = X
    else:
        dup_board[action[0]][action[1]] = O
    return dup_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[0][0] == board[1][1] and board[1][1] == board[2][2])or (board[0][2] == X and board[0][2] == board[1][1] and board[1][1] == board[2][0]) or (board[0][0] == X and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or (board[1][0] ==X and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or (board[2][0] == X and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or (board[0][0] ==X and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or (board[0][1] ==X and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or (board[0][2] == X and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return X
    elif (board[0][0] == O and board[0][0] == board[1][1] and board[1][1] == board[2][2])or (board[0][2] == O and board[0][2] == board[1][1] and board[1][1] == board[2][0]) or (board[0][0] == O and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or (board[1][0] ==O and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or (board[2][0] == 0 and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or (board[0][0] ==O and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or (board[0][1] ==O and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or (board[0][2] == O and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return O
    else:
        return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if ((board[0][0] != EMPTY) and board[0][0] == board[1][1] and board[1][1] == board[2][2])or (board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]) or (board[0][0] != EMPTY and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or (board[1][0] != EMPTY and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or (board[2][0] !=EMPTY and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or (board[0][0] != EMPTY and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or (board[0][1] != EMPTY and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or (board[0][2] != EMPTY and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if  win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    
    raise NotImplementedError

def Maxvalue(state):
    if terminal(state):
        return utility(state)
    v=-999
    for action in actions(state):
        v=max(v,Minvalue(result(state,action)))
    return v

def Minvalue(state):
    if terminal(state):
        return utility(state)
    v=999
    for action in actions(state):
        v=min(v,Maxvalue(result(state,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        possible_actions = actions(board)
        possible_actions = list(possible_actions)
        possible_states = []
        possible_scores = []

        for action in possible_actions:
            x=result(board,action)
            possible_states.append(x)

        for state in possible_states:   
            
            score = Minvalue(state)
        
            possible_scores.append(score)
        max_score_index = []

        m = max(possible_scores)
        for i in range(len(possible_scores)):
            if possible_scores[i]==m:
                max_score_index.append(i)
        r=random.choice(max_score_index)
        return possible_actions[r]
    else:
        possible_actions = actions(board)
        possible_actions = list(possible_actions)
        possible_states = []
        possible_scores = []

        for action in possible_actions:
            x=result(board,action)
            possible_states.append(x)

        for state in possible_states:   
            
            score = Maxvalue(state)
        
            possible_scores.append(score)
        max_score_index = []

        m = min(possible_scores)
        for i in range(len(possible_scores)):
            if possible_scores[i]==m:
                max_score_index.append(i)
        r=random.choice(max_score_index)
        return possible_actions[r]

    raise NotImplementedError

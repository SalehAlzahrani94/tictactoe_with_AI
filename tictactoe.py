"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    # variables
    Player_X = 0
    Player_O = 0
    # the idea is count how many x and y
    for i in board:
        Player_X+= i.count( X )
        Player_O+= i.count( O )

    if Player_X<=Player_O :
        return X
    else :
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()
    #nedted loop to check

    for index ,row in enumerate( board ) :
        for index_for_Column, i in enumerate( row ) :
            if i ==None :
                moves.add( ( index ,index_for_Column) )
    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if the player has 3 X in vertical
    # i is a player
    move=player( board)

    new_board=deepcopy( board)
    i ,j =action

    if board[ i ][ j ]!= None :
        raise Exception
    else :
        new_board[i][j ]=move

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for play in ( X, O ) :
        #         # check if the player has 3 X in  vertical
        # first_row is a row in board
        for first_row in board:
            if first_row == [ play] * 3 :
                return play
        # check if the player has 3 X in horizontal
        for player in range (3 ) :
            column=[board[ x ][player ] for x in range(3) ] # take all board x i index
            if column==[play ] * 3 :# check if is a wien ( 3 x )
                return play

        # check if the player has 3 X in diagonal
        if [board[player][player ] for player in range(0, 3)] == [play] * 3:# take all board i i index
            return play

        elif [board[player][~player] for player in range( 0, 3) ]==[play]* 3 :
            return play
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if wons by players
    if winner(board )!= None:
        return True

    # moves  possible
    # nested loops for check rows
    for i in board:
        if EMPTY in i :
            return False

    # no more moves can be done
    return True
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winerPlayer = winner(board) # call winner method we make UP
    # check how is the winner and return a value
    if winerPlayer==X :
        return 1
    elif winerPlayer==O :
        return -1
    else :
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxmize(board) :
        move  =()
        if terminal(board ) :
            return utility(board ) ,move
        else:
            v=-5
            for i in actions( board) : # class actions
                minval=minnmaze(result( board , i ) ) [0 ] #call minnmaze and result methods
                if minval > v :
                    v= minval
                    move=i
            return v,move

    def minnmaze (board) :
        move= ()
        if terminal(board): #call terminal method
            return utility(board ) , move # using utility method
        else :
            v=5
            for j in actions( board) :
                maxval = maxmize (result ( board , j) )[0 ]
                if maxval <v :
                    v=maxval
                    move = j
            return v , move

    current_player =player(board)

    if terminal(board):
        return None

    if current_player  ==X :
        return maxmize( board ) [1]

    else :
        return minnmaze ( board) [1]
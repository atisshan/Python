import numpy as np #to use the arrays for the game
import random 
from time import sleep  #to pause the game 




def empty_board():
    board = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]]
    )

    return board

# print(empty_board())

def Check_empty_board(board):
    lst=[]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                lst.append((i,j))

    return lst

# print(Check_empty_board(board))

# select a random place for the player on the board

def random_place(board, player):
    select=Check_empty_board(board)
    current_location=random.choice(select)
    board[current_location]=player

    return board

# print(random_place(board, 1))

# checking for the row match
def row_check(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x,y] != player:
                win=False

                continue
        if win == True:
            return win
        
    return(win)

# print(row_check(board, 1))


def column_check(board, player):
    for y in range(len(board)):
        win=True

        for x in range(len(board)):
            if board[x,y] !=player:
                win=False
                continue
        if win == True:
            return(win)
    return(win)

# print(column_check(board, 1))

def check_diag(board, player):
    
    main_win=True
    for i in range(len(board)):
        if board[i,i] != player:
            main_win=False

            break
    if main_win == True:

         return main_win

    anti_diag_win= True

    for i in range(len(board)):
        if board[i, (len(board))-1-i] != player:
            anti_diag_win=False
            break
    if anti_diag_win == True:  

        return anti_diag_win
# print(check_diag(board,2))


def evaluate_winner(board):
    winner = 0

    for player in [1,2]:
        if(row_check(board,player) or column_check(board,player) or check_diag(board,player)):

            winner=player

    if np.all(board !=0) and winner == 0:
        winner=-1

    return winner
# print(evaluate_winner(board))

def tic_tac_toe():
    board=empty_board()
    winner=0
    counter=1
    print(board)
    sleep(5)

    while winner == 0:
        for player in [1,2]:
            brd=random_place(board, player)
            print("Board after " +  str(counter) + " move")
            print(brd)
            sleep(5)
            winner=evaluate_winner(brd)


            if winner !=0:
                break

    return(winner)

print("The winner is " + str(tic_tac_toe()))

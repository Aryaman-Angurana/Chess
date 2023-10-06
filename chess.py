# chess game

import os

# External file to check the validity of moves
from move_check import movecorrect, castling, enpassant

# We need to create variables to check if castling is valid for a side
check_king_1 = True
check_king_2 = True
pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]


player = 1

# Martix of the chess board
board =[["Rk", "Kt", "Bs", "Kn", "Qn", "Bs", "Kt", "Rk"],
        ["Pn", "Pn", "Pn", "Pn", "Pn", "Pn", "Pn", "Pn"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["pn", "pn", "pn", "pn", "pn", "pn", "pn", "pn"],
        ["rk", "kt", "bs", "kn", "qn", "bs", "kt", "rk"]]


# A function to draw the chess board 
def draw():
    os.system('cls')
    print("    1    2    3    4    5    6    7    8")
    print("  -----------------------------------------")
    coor = ["A", "B", "C", "D", "E", "F", "G", "H"]
    k = 0
    for i in board:
        print(coor[k], end = " | ")
        for j in i:
            if (j == ""):
                print ("   ", end = "| ")
            else:
                print(j, end = " | ")
        print(coor[k])
        print("  -----------------------------------------")
        k+=1
    print("    1    2    3    4    5    6    7    8")


# Function to input the coordinates of initial and final position of a piece and checking its validity
def inputPos():

    global pawns
    invar = ""
    while True:
        global player
        global check_king_1
        global check_king_2

        # Input paremeters
        initial = input ("Enter the starting position of the piece: ")
        final = input ("Enter the final position of the piece: ")

        # Checking if the input lies in the correct range
        if (len(initial) != 2 or len(final) != 2 or ord(initial[0]) not in [i for i in range(65,90)] or ord(final[0]) not in [i for i in range(65,90)] or int(initial[1]) not in [i for i in range(1,9)] or int(final[1]) not in [i for i in range(1,9)]):
            print("-------Incorrect coordinates-------")
            continue

        # Checking if the right player makes the move
        if (board[ord(initial[0])-65][int(initial[1])-1] == "" or ( player == 1 and board[ord(initial[0])-65][int(initial[1])-1][0].islower())):
            print("-------Wrong piece moved-------")
            continue
        if (board[ord(initial[0])-65][int(initial[1])-1] == "" or ( player == 2 and board[ord(initial[0])-65][int(initial[1])-1][0].isupper())):
            print("-------Wrong piece moved-------")
            continue
        
        invar = board[ord(initial[0])-65][int(initial[1])-1]

        # Checking if the move made by the player is correct
        if (movecorrect(initial, final, board)):
            if (initial == "A4" or initial == "A1"):
                check_king_1 = False
            if (initial == "H4" or initial == "H1"):
                check_king_2 = False

            board[ord(final[0])-65][int(final[1])-1] = board[ord(initial[0])-65][int(initial[1])-1]
            board[ord(initial[0])-65][int(initial[1])-1] = ""
            break
        elif ( castling(initial, final, board, check_king_1, check_king_2)):
            board[ord(final[0])-65][1] = board[ord(initial[0])-65][0]
            board[ord(final[0])-65][0] = board[ord(initial[0])-65][3]
            board[ord(final[0])-65][2] = ""
            board[ord(final[0])-65][3] = ""
            break
        elif (enpassant(initial, final, board, pawns)):
            board[ord(final[0])-65][int(final[1])-1] = board[ord(initial[0])-65][int(initial[1])-1]
            board[ord(initial[0])-65][int(initial[1])-1] = ""
            if (ord(initial[0])-65 == 4):
                board[4][int(final[1])-1] = ""
            if (ord(initial[0])-65 == 3):
                board[3][int(final[1])-1] = ""
            break
        else:
            print("-------Wrong move-------")
    if (invar == "Pn" and ord(final[0])-ord(initial[0]) == 2):
        pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        pawns[0][int(final[1])-1] = 1
    elif (invar == "pn" and ord(initial[0])-ord(final[0]) == 2):
        pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        pawns[1][int(final[1])-1] = 1
    else:
        pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]


    # Switching the players for the next move
    if (player == 1):
        player = 2
    else:
        player =1

    #change of pawns into queens
    for i in range (0,8):
        if (board[0][i] == "pn"):
            board[0][i] = "qn"
        if (board[7][i] == "Pn"):
            board[7][i] = "Qn"


# Function to check for gameover
def gameover():
    flag = False
    for i in board:
        for j in i:
            if (j == "Kn"):
                flag = True
                break
        if (flag):
            break
    else:
        draw()
        print("-------Game over-------")
        print("-----Player 2 wins-----")
        return False
    
    for i in board:
        for j in i:
            if (j == "kn"):
                return True
    draw()
    print("-------Game over-------")
    print("-----Player 1 wins-----")
    return False


# Main function loop
while (gameover()):
    draw()
    inputPos()
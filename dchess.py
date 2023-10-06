# External file to check the validity of moves
from move_check import movecorrect, castling, enpassant

# We need to create variables to check if castling is valid for a side
check_king_1 = True
check_king_2 = True


# We need to keep a check on the movement of pawns for the enpassant
pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]


# Function to input the coordinates of initial and final position of a piece and checking its validity
def inputPos(initial,final,board,player):
    global pawns
    global check_king_1
    global check_king_2

        # Checking if the right player makes the move
    if (board[ord(initial[0])-65][int(initial[1])-1] == "" or ( player == 1 and board[ord(initial[0])-65][int(initial[1])-1][0].islower())):
        print("-------Wrong piece moved-------")
        return board
    if (board[ord(initial[0])-65][int(initial[1])-1] == "" or ( player == 2 and board[ord(initial[0])-65][int(initial[1])-1][0].isupper())):
        print("-------Wrong piece moved-------")
        return board
    
    invar = board[ord(initial[0])-65][int(initial[1])-1]

    # Checking if the move made by the player is correct
    if (movecorrect(initial, final, board)):
        if (invar == "Pn" and ord(final[0])-ord(initial[0]) == 2):
            pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
            pawns[0][int(final[1])-1] = 1
        elif (invar == "pn" and ord(initial[0])-ord(final[0]) == 2):
            pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
            pawns[1][int(final[1])-1] = 1
        else:
            pawns = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        
        if (initial == "A4" or initial == "A1"):
            check_king_1 = False
        if (initial == "H4" or initial == "H1"):
            check_king_2 = False

        board[ord(final[0])-65][int(final[1])-1] = board[ord(initial[0])-65][int(initial[1])-1]
        board[ord(initial[0])-65][int(initial[1])-1] = ""
        return board
    elif ( castling(initial, final, board, check_king_1, check_king_2)):
        board[ord(final[0])-65][1] = board[ord(initial[0])-65][0]
        board[ord(final[0])-65][0] = board[ord(initial[0])-65][3]
        board[ord(final[0])-65][2] = ""
        board[ord(final[0])-65][3] = ""
        return board
    elif (enpassant(initial, final, board, pawns)):
        board[ord(final[0])-65][int(final[1])-1] = board[ord(initial[0])-65][int(initial[1])-1]
        board[ord(initial[0])-65][int(initial[1])-1] = ""
        if (ord(initial[0])-65 == 4):
            board[4][int(final[1])-1] = ""
        if (ord(initial[0])-65 == 3):
            board[3][int(final[1])-1] = ""
        return board
    else:
        return board


# Function to check for gameover
def gameover(board):
    flag = False
    for i in board:
        for j in i:
            if (j == "Kn"):
                flag = True
                break
        if (flag):
            break
    else:

        return True
    
    for i in board:
        for j in i:
            if (j == "kn"):
                return False
    return True
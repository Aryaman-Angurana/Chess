def movecorrect(initial, final, board):
    i_pos = [ord(initial[0])-65, int(initial[1])-1]
    f_pos = [ord(final[0])-65, int(final[1])-1]
    
    # For the pawn of the upper letter
    if (board[i_pos[0]][i_pos[1]] == "Pn"):
        if ((f_pos[0]-i_pos[0] == 1 or (f_pos[0]-i_pos[0] == 2 and i_pos[0] == 1 and board[f_pos[0] - 1][f_pos[1]] == "")) and f_pos[1]-i_pos[1] == 0 and board[f_pos[0]][f_pos[1]] == ""):
            return True
        if ((f_pos[0]-i_pos[0] == 1 and (f_pos[1]-i_pos[1] == 1 or f_pos[1]-i_pos[1] == -1)) and board[f_pos[0]][f_pos[1]] != "" and board[f_pos[0]][f_pos[1]][0].islower()):
            return True
    
    # For the pawn of the lower letter
    elif (board[i_pos[0]][i_pos[1]] == "pn"):
        if ((f_pos[0]-i_pos[0] == -1 or (f_pos[0]-i_pos[0] == -2 and i_pos[0] == 6 and board[f_pos[0] + 1][f_pos[1]] == "")) and f_pos[1]-i_pos[1] == 0 and board[f_pos[0]][f_pos[1]] == ""):
            return True
        if ((f_pos[0]-i_pos[0] == -1 and (f_pos[1]-i_pos[1] == 1 or f_pos[1]-i_pos[1] == -1)) and board[f_pos[0]][f_pos[1]] != "" and board[f_pos[0]][f_pos[1]][0].isupper()):
            return True
    
    # For the kings of both
    elif (board[i_pos[0]][i_pos[1]].lower() == "kn"):
        if (f_pos[0]-i_pos[0] in [-1,0,1] and f_pos[1]-i_pos[1] in [-1,0,1] and (board[f_pos[0]][f_pos[1]] == "" or (board[f_pos[0]][f_pos[1]].islower() != board[i_pos[0]][i_pos[1]].islower()))):
            return True
    
    # For knights of both
    elif (board[i_pos[0]][i_pos[1]].lower() == "kt"):
        if (board[f_pos[0]][f_pos[1]] == "" or (board[f_pos[0]][f_pos[1]].islower() != board[i_pos[0]][i_pos[1]].islower())):
            if ((f_pos[0]-i_pos[0] in [1,-1] and f_pos[1]-i_pos[1] in [2,-2]) or (f_pos[1]-i_pos[1] in [1,-1] and f_pos[0]-i_pos[0] in [2,-2])):
                return True
    
    # For rooks of both
    elif (board[i_pos[0]][i_pos[1]].lower() == "rk"):
        if (board[f_pos[0]][f_pos[1]] == "" or (board[f_pos[0]][f_pos[1]].islower() != board[i_pos[0]][i_pos[1]].islower())):
            if (f_pos[1]-i_pos[1] == 0):
                for i in range (i_pos[0],f_pos[0],int((f_pos[0]-i_pos[0])/(abs(f_pos[0]-i_pos[0])))):
                    if (board[i][f_pos[1]] != "" and i_pos[0] != i):
                        return False
                return True
            if (f_pos[0]-i_pos[0] == 0):
                for i in range (i_pos[1],f_pos[1],int((f_pos[1]-i_pos[1])/(abs(f_pos[1]-i_pos[1])))):
                    if (board[f_pos[0]][i] != "" and i_pos[1] != i):
                        return False
                return True
    
    # For bishops of both
    elif (board[i_pos[0]][i_pos[1]].lower() == "bs"):
        if (board[f_pos[0]][f_pos[1]] == "" or (board[f_pos[0]][f_pos[1]].islower() != board[i_pos[0]][i_pos[1]].islower())):
            if (f_pos[0]-i_pos[0] == f_pos[1]-i_pos[1] or f_pos[0]-i_pos[0] == i_pos[1]-f_pos[1]):
                k = 1
                while (i_pos[0] != f_pos[0]):
                    if k == 1:
                        k=0
                        i_pos[0] += int((f_pos[0]-i_pos[0])/(abs(f_pos[0]-i_pos[0])))
                        i_pos[1] += int((f_pos[1]-i_pos[1])/(abs(f_pos[1]-i_pos[1])))
                        continue
                    else:
                        if (board[i_pos[0]][i_pos[1]] != ""):
                            return False
                    i_pos[0] += int((f_pos[0]-i_pos[0])/(abs(f_pos[0]-i_pos[0])))
                    i_pos[1] += int((f_pos[1]-i_pos[1])/(abs(f_pos[1]-i_pos[1])))
                return True

    # For queens of both        
    elif (board[i_pos[0]][i_pos[1]].lower() == "qn"):
        if (board[f_pos[0]][f_pos[1]] == "" or (board[f_pos[0]][f_pos[1]].islower() != board[i_pos[0]][i_pos[1]].islower())):
            flag = True
            if (f_pos[0]-i_pos[0] == f_pos[1]-i_pos[1] or f_pos[0]-i_pos[0] == i_pos[1]-f_pos[1]):
                k = 1
                while (i_pos[0] != f_pos[0]):
                    if k == 1:
                        k=0
                        i_pos[0] += int((f_pos[0]-i_pos[0])/(abs(f_pos[0]-i_pos[0])))
                        i_pos[1] += int((f_pos[1]-i_pos[1])/(abs(f_pos[1]-i_pos[1])))
                        continue
                    else:
                        if (board[i_pos[0]][i_pos[1]] != ""):
                            flag = False
                            break
                    i_pos[0] += int((f_pos[0]-i_pos[0])/(abs(f_pos[0]-i_pos[0])))
                    i_pos[1] += int((f_pos[1]-i_pos[1])/(abs(f_pos[1]-i_pos[1])))
                if (flag == True):
                    return True
            flag = True
            if (f_pos[1]-i_pos[1] == 0):
                for i in range (i_pos[0],f_pos[0],int((f_pos[0]-i_pos[0])/(abs(f_pos[0]-i_pos[0])))):
                    if (board[i][f_pos[1]] != "" and i_pos[0] != i):
                        flag = False
                if (flag == True):
                    return True
            if (f_pos[0]-i_pos[0] == 0):
                for i in range (i_pos[1],f_pos[1],int((f_pos[1]-i_pos[1])/(abs(f_pos[1]-i_pos[1])))):
                    if (board[f_pos[0]][i] != "" and i_pos[1] != i):
                        flag = False
                if (flag == True):
                    return True
    return False



# Checking for castling conditions
def castling(initial, final, board, move_king_1, move_king_2):
    i_pos = [ord(initial[0])-65, int(initial[1])-1]
    f_pos = [ord(final[0])-65, int(final[1])-1]
    if (i_pos == [0,3] and f_pos == [0,1] and board[0][2] == "" and board[0][1] == "" and move_king_1):
        return True
    if (i_pos == [7,3] and f_pos == [7,1] and board[7][2] == "" and board[7][1] == "" and move_king_2):
        return True
    return False

# Checking for enpassant condition
def enpassant(initial, final, board, pawns):
    i_pos = [ord(initial[0])-65, int(initial[1])-1]
    f_pos = [ord(final[0])-65, int(final[1])-1]
    if (board[i_pos[0]][i_pos[1]] == "pn" and i_pos in [[3,i] for i in range(0,8)] and f_pos in [[2,i_pos[1]-1],[2,i_pos[1]+1]] and pawns[0][f_pos[1]] == 1):
        return True
    if (board[i_pos[0]][i_pos[1]] == "Pn" and i_pos in [[4,i] for i in range(0,8)] and f_pos in [[5,i_pos[1]-1],[5,i_pos[1]+1]] and pawns[1][f_pos[1]] == 1):
        return True
    return False
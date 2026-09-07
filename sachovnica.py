import tkinter as tk
chessboard = []
def create_chessboard():
    global chessboard
    
    for i in range(8):
        row = [0] * 8 
        chessboard.append(row)


def chectit(x,y):
    
    for i in range(0,8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8): #y
        for j in range(0,8): #x
            if i + j == x+y:
                if chessboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chessboard[i][j] == 1:
                    return False
    return True

create_chessboard()
#prva dama
chessboard[2][3] = 1
print(chessboard)

print(chectit(4,3))
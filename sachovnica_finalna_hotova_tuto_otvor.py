import tkinter as tk
chessboard = []
counter_solutions = 0



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

def queens(n):
    global chessboard
    global counter_solutions
    if n  == 8:
        counter_solutions += 1
        createImage(counter_solutions)
        print(chessboard)
        print('--------------------')
        print(counter_solutions)

        root, canvas = createImage(400, 8)
        draw_queens(canvas, 8, 400)
        root.mainloop()
    else:
        for i in range(8):
            if chectit(i,n) == True:
                chessboard[n][i] = 1
                queens(n+1)
                chessboard[n][i] = 0

def createImage(size=400, squares=8):

    root = tk.Tk()
    root.title("8 Queens")
    
    square_size = size // squares
    canvas = tk.Canvas(root, width=size, height=size)
    canvas.pack()

    # Draw the chessboard squares
    for row in range(squares):
        for col in range(squares):
            color = "white" if (row + col) % 2 == 0 else "gray"
            
            x1 = col * square_size 
            y1 = row * square_size  
            x2 = x1 + square_size
            y2 = y1 + square_size

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
            
    return root, canvas

def draw_queens(canvas, squares=8, size=400):
    global chessboard
    square_size = size // squares
    
    for row in range(squares):
        for col in range(squares):
            if chessboard[row][col] == 1:
                # Calculate coordinates for the queen marker (a red circle with a 'Q')
                x1 = col * square_size + square_size * 0.15
                y1 = row * square_size + square_size * 0.15
                x2 = col * square_size + square_size * 0.85
                y2 = row * square_size + square_size * 0.85
                
                canvas.create_oval(x1, y1, x2, y2, fill="crimson", outline="black", width=2)
                canvas.create_text(
                    col * square_size + square_size / 2, 
                    row * square_size + square_size / 2, 
                    text="Q", 
                    fill="white", 
                    font=("Arial", int(square_size * 0.4), "bold")
                )
create_chessboard()
queens(0)
from PIL import Image, ImageDraw
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
    else:
        for i in range(8):
            if chectit(i,n) == True:
                chessboard[n][i] = 1
                queens(n+1)
                chessboard[n][i] = 0

def createImage(size=400, squares = 8):
    square_size = size // squares
    im = Image.new(mode="RGB", size=(size,size), color="white")
    draw = ImageDraw.Draw(im)

    black = (0,0,0)
    white = (255,255,255)

    for row in range(squares):
        for collum in range(squares):
            color = white if (row + collum) % 2 == 0 else black

            x1 = collum * square_size 
            y1 = row * square_size  
            x2 = x1 * square_size +50
            y2 = y1 * square_size +50

            draw.rectangle([x1,y1,x2,y2], fill=color)
    return im
a = createImage(400)
a.save("Chessboard.png")
#create_chessboard()
#queens(0)
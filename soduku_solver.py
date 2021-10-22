board = [
    [6,4,7,9,1,5,3,8,2],
    [3,9,5,2,8,4,7,6,1],
    [0,2,0,3,0,0,5,4,9],
    [0,0,0,0,3,0,0,0,6],
    [0,0,0,5,0,1,0,0,0],
    [9,0,0,0,4,0,0,0,0],
    [0,8,6,0,5,0,0,2,3],
    [5,0,2,6,0,3,0,0,0],
    [0,3,9,0,2,8,6,7,5]
]

def print_board(board:list):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- "*10)

        for j in range(len(board[0])):
            if j % 3 == 0 and j !=0:
                print("|", end="")

            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)

def find_empty(board:list):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]== 0:
                return(i,j)
    return None

def Checker(board:list, num:int ,pos:list):
    #check rows
    for i in range(len(board[0])):
        if board[pos[0]][i]== num and pos[0]!=i:
            return False
    #check colmuns

    for i in range(len(board)):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False

    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3,box_y*3 +3):
        for j in range(box_x*3 ,box_x*3 +3 ):
            if board[i][j]==num and (i,j) !=pos:
                return False

    return True

def solver(board:list):
    finder=find_empty(board)
    if not finder:
        return True
    else:
        rows,colmuns=finder

    for i in range(1,10):
        if Checker(board,i,(rows,colmuns)):
            board[rows][colmuns]=i

            if solver(board):
                return True

            board[rows][colmuns]=0
    return False


solver(board)
print("\n" ,"_ "*10)

print_board(board)

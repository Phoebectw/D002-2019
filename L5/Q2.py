# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
        return False   
    

def check_row(cells):
    for i in range(0, 3):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
        return False   
    
def check_diagonal(cells):
    
    if cells[0][0] == cells[1][1] == cells[2][2] != ' ' or cells[2][0] == cells[1][1] == cells[0][2] != ' ':
        return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
xo=0
printcell(cells)
while (check(cells) == False):
    if xo%2 == 0:
        print("player 1 please input your choice")
    else:
        print("player 2 please input your choice")
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row][col] == ' ':
        if xo%2 == 0:
            cells[row][col] = 'x'
        else:
            cells[row][col] = 'o'
    else:
        print("It is taken already")
    xo=xo+1        
    printcell(cells)


    if xo >8:
        print('game over')
        print("it is a draw")
        break
    if check(cells):
        print('game over')
       
        if xo%2 == 0:
            print("player 2 wins")
        
        else:
            print("player 1 wins")
        print("please press F5 to play again")
        break

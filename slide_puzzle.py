def make_board(n):
    """
    n is an integer between 3 and 9.  makes a board which is a list of n lists, each list representing a row in the board.  assigns a value from the (n*n - 1) to 0 to each tile.  if n is even, the 2 and 1 tiles are swapped.
    """
    val = n*n-1
    for i in range(n):
        board.append([])
    for i in range(n):
        for j in range(n):
            board[i].append(val)
            val-=1
    if n % 2 == 0:
        board[n-1][n-3], board[n-1][n-2] = board[n-1][n-2], board[n-1][n-3]
        

def display_board():
    n = len(board)
    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num == 0: print("  ", end = " ")
            elif num < 10: print(" " + str(num), end = " ")
            else: print(str(num), end = " ")
        print()
            
def find_blank():
    '''
    returns a list which contains the row, column location of the blank tile
    0 represents the blank tile in the board
    '''
    for row in range(board):
        for tile in range(row):
            if board[row][tile] == 0:
                return [row, tile]

def find_tile(tile):
    '''
    returns a list which contains the row, column location of the tile
    entered as the parameter(chosen by  the user)
    '''
    #TODO

def valid_move(bRow, bCol, tRow, tCol):
    '''
    compares the blank row, column location with the tile row, culumn location
    returns True if it is a valid move and False if it is not a valid move
    '''
    #TODO


def swap_tile(bRow, bCol, tRow, tCol):
    '''
    updates the board so that the value in the tile row, column location
    switches with the value in the blank row, column location (0)
    '''
    #TODO

def check_win():
    '''
    checks to see if the tiles are in order from least to greatest
    returns True if they are all in order.  False otherwise
    '''
    #TODO




board = [] 	 #global variable - can be seen inside and outside functions
num_rows = 4

#num_rows = valid_input()
make_board(num_rows)
display_board()
print(board)
print(find_blank())
##
##while True:
##    tile = int(input("Tile: "))
##    blankLoc = find_blank()
##    tileLoc = find_tile(tile)
##    if valid_move(blankLoc[0], blankLoc[1], tileLoc[0], tileLoc[1]):
##        swap_tile(blankLoc[0], blankLoc[1], tileLoc[0], tileLoc[1])
##    else:
##        print("not a valid move")
##    display_board()
##    if check_win():
##        print("Yay!!!")



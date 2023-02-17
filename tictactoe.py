import random
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        

def print_board():
    line_nums = [0, 1, 3, 4, 6, 7]
    for square in range(len(board)):
        print(board[square], end=' ')
        if square in line_nums:
            print('|', end=' ')
        if square==2 or square==5:
            print('\n---------')
    print('\n')

def check_tie():
    letter_sum = 0
    for square in board:
        if isinstance(square, int) == False:
            letter_sum+=1
    if letter_sum == 9:
        return True
    return False


def check_win():
    no_win = 0
    p1_win = 1
    p2_win = 2
    
    #Horizontal Win
    if board[0:3] == ['x','x','x'] or \
       board[3:6] == ['x','x','x'] or \
       board[6:8] == ['x','x','x']:
        return p1_win
    if board[0:3] == ['o','o','o'] or \
         board[3:6] == ['o','o','o'] or \
         board[6:8] == ['o','o','o']:
        return p2_win
    
    #Vertical Win
    if (board[0] == board[3] == board[6] == 'x') or \
         (board[1] == board[4] == board[7] == 'x') or \
         (board[2] == board[5] == board[8] == 'x'):
        return p1_win
    if (board[0] == board[3] == board[6] == 'o') or \
         (board[1] == board[4] == board[7] == 'o') or \
         (board[2] == board[5] == board[8] == 'o'):
        return p2_win

    #Diagonal Win
    if (board[0] == board[4] == board[8] == 'x') or \
         (board[2] == board[4] == board[6] == 'x'):
        return p1_win
    if (board[0] == board[4] == board[8] == 'o') or \
         (board[2] == board[4] == board[6] == 'o'):
        return p2_win
    
    return no_win

def two_player():
    player = random.randint(0,1)
    xo = ['x', 'o']
    game = True
    while game:
        print_board()
        invalid_move = True
        while invalid_move:
            move = input(xo[player] + ' move: ')
            if move.isdigit()==False or int(move)>9 or isinstance(board[int(move)-1], str):
                print('Illegal move. Try again.')
            else:
                board[int(move)-1] = xo[player]
                invalid_move = False
        if player == 0:
            player = 1
        else:
            player = 0
        if check_win():
            print_board()
            if check_win() == 1:
                print('x wins')
            if check_win() == 2:
                print('o wins')
            game = False
        if check_tie():
            print_board()
            print('Game tied')
            game = False

def random_move():
    available_moves = []
    for square in board:
        if isinstance(square,int):
            available_moves.append(square)
    if available_moves:
        return random.choice(available_moves)
    else:
       return random.randint(1,9)
        
    

def one_player():
    player = random.randint(0,1)
    xo = ['x', 'o']
    game = True
    while game:
        print_board()
        invalid_move = True
        while invalid_move and player:
            move = input('player move (o): ')
            if move.isdigit()==False or int(move)>9 or isinstance(board[int(move)-1], str):
                print('Illegal move. Try again.')
            else:
                board[int(move)-1] = xo[player]
                invalid_move = False
        if not player:
            random_value = random_move()
            board[random_value-1] = xo[player]
            print('cpu move (x): ' + str(random_value))
        if player == 0:
            player = 1
        else:
            player = 0
        
        if check_win() == 1:
            print_board()
            print('cpu wins')
            game = False
        if check_win() == 2:
            print_board()
            print('user wins')
            game = False
        if check_tie():
            print_board()
            print('Game tied')
            game = False

while True:
    game_choice = input('Welcome to tic tac toe\ntype 1 for 1 player and 2 for 2 player: ')
    if game_choice == '1':
        one_player()
        y = input('press y to restart: ')
        if y == 'y':
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            continue
        break

    if game_choice == '2':
        two_player()
        y = input('press y to restart: ')
        if y == 'y':
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            continue
        break
    
    if (game_choice != '1') or (game_choice != '2'):
        print('Invalid input. Try again\n')

        
    





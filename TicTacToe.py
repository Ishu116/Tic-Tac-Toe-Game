import random 
from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    
    print('-----------')
    
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    
    print('-----------')
    
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        
        player_1=marker
    if player_1 == 'X':
        player_2='O'
    else:
        player_2='X'
    return (player_1,player_2)

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    
    flip = random.randint(0,1)
    if flip == 0:
        return 'player_1'
    else:
        return 'player_2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Y or N : ').lower().startswith('y')


print('Welcome To Tic Tac Toe')

while True:
    the_board=[' '] * 10
    player_1,player_2=player_input()
    turn = choose_first()
    print(turn + ' Will go first.')
    play_game = input('Ready to play the game ? y or n ?')
    if play_game.lower()[0] == 'y':
        game_on = True 
    else:
        game_on = False
        
    while game_on:
        if turn == 'player_1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player_1,position)
            
            if win_check(the_board,player_1):
                display_board(the_board)
                print('Congratulations! Player_1 have won the game!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn='player_2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player_2,position)
            
            if win_check(the_board,player_2):
                display_board(the_board)
                print('Congratulations! Player_2 have won the game!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn='player_1'
    if not replay():
        break
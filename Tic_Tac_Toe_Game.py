from IPython.display import clear_output
    

def display_board(board):
    clear_output()
    
    print("   |   |  ")
    print(' '+board[7]+' '+'|'+' '+ board[8]+' '+'|'+ ' '+board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(' '+board[4]+' '+'|'+' '+ board[5]+' '+'|'+ ' '+board[6])
    print("   |   |  ")
    print("-----------")
    print("   |   |")
    print(' '+board[1]+' '+'|'+' '+ board[2]+' '+'|'+ ' '+board[3])
    print("   |   |  ")
    
    
    
    
def player_input():
    
    marker = ''
    
    #Keep asking player 1 to choose a X or O
    while marker != 'X' and marker !='O':
        marker = input("Player 1, choose X or O:").upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')




def place_marker(board, marker, position):
    
    board[position] = marker
    
    
    
def win_check(board, mark):
    
    #win?
    
    #3 across
    return ((board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)or
    
    #3 in a row
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark)or
    #3 in column
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark))


import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    
    else:
        return 'Player 2'
    
    
    
def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        #Board is full if we return true
    return True



def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position :(1-9)'))
    
    return position



def replay():
    
    return input('Would you like to play again? Enter Yes or No:').lower().startswith('y')






print('Welcome to Tic Tac Toe!')

while True:
    
    
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn +' goes first ')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    #pass

    #while game_on:
    while game_on:
        
        #Player 1 Turn
        if turn == 'Player1':
            #show the board
            display_board(theBoard)
            #choose position
            position = player_choice(theBoard)
            #place marker on the position
            place_marker(theBoard, player1_marker, position)
            #check if they won
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('PLAYER 1 HAS WON !!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("IT'S A TIE !!")
                    game_on = False
                else:
                    turn = 'Player2'
            
            
        # Player2's turn.
        
        else:
            #show the board
            display_board(theBoard)
            #choose position
            position = player_choice(theBoard)
            #place marker on the position
            place_marker(theBoard, player2_marker, position)
            #check if they won
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('PLAYER 2 HAS WON !!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("IT'S A TIE !!")
                    game_on = False
                else:
                    turn = 'Player1'

    if not replay():
        break
""" Create a game Tic-tac-toe
Write a game. Input will be from two players x or o
Need to: draw a board
coordinate turns, check if board cell was used or not,
check after every turn if a move == victory

I will make the boartd using dictionary, each key in the board will be indicating a cell/location,
I will change the value of each cell to "x" or "o" according to player's choice of move
"""
board = {'1': '1', '2': '2', '3': '3',
         '4': '4', '5': '5', '6': '6',
         '7': '7', '8': '8', '9': '9'}
count = 0 #counts turns (max is 9)


def draw_board(board):
    """ to draw initial board 9x9 """
    print("\n")
    for i in range(3): #iterate through numbers 0,1,2 createing three rows
        str1 = " " # create emplty str 
        for j in range(3): #iterate through numbers 0,1,2 createing three columns
            str1 += board[str(i*3+j+1)] #taking 9 numbers from board one by one
            if j != 2: #adding | after each number but the last one
                str1 += " | "
        print(str1)
        if i != 2: #print separation lines after each row but the last one
            print("--- --- ---")
    print("\n")


def player_turn(board, player, coordinate):
    """ Updates board w/ "x" or "o", replacing a number on the board """
    board[coordinate] = player #updating board "x" or "o" 
    return(board)

def if_cell_is_empty(board, coordinate):
    """ Cheking for cell to have an original number """
    if board[coordinate] == 'x' or board[coordinate] == 'o': #checking board "x" or "o" 
        return False
    return True

def is_winning(board, player):
    """ Checks if "x" or "o" are next to each other"""
    if board['1'] == player and board['2'] == player and board['3'] == player:
        return True
    elif board['4'] == player and board['5'] == player and board['6'] == player:
        return True
    elif board['7'] == player and board['8'] == player and board['9'] == player:
        return True
    elif board['1'] == player and board['4'] == player and board['7'] == player:
        return True
    elif board['2'] == player and board['5'] == player and board['8'] == player:
        return True
    elif board['3'] == player and board['6'] == player and board['9'] == player:
        return True
    elif board['1'] == player and board['5'] == player and board['9'] == player:
        return True
    elif board['3'] == player and board['5'] == player and board['7'] == player:
        return True
    return False

def check_input(coordinate):
    """ Checks if input is a number from 1 to 9 """
    while coordinate not in "123456789": #untill input is correct asking for input and save it in coordinate
        coordinate = input('It is not a valid number. Enter a number from 1 to 9')
    return coordinate

player_names = ['Player1', 'Player2']
player_sumbol = ['x', 'o'] #defines a player

while True: #untill the game is over do this loop
    player = player_names[count%2] #player with index 0%2 will start ->player[0] | player with index 1%2 will continue ->player[1]
    char = player_sumbol[count%2] #player with index 0%2 will be "x" ->player[0] | player with index 1%2 will be "o" ->player[1]

    draw_board(board)
    coordinate = input(f'{player}: Enter next number')
    coordinate = check_input(coordinate) #gets str back


    while if_cell_is_empty(board, coordinate) == False: #untill player gives you a correct cell number 
        coordinate = input('This number has been used. Enter a different number')
        coordinate = check_input(coordinate)
    board = player_turn(board, char, coordinate) #updating board w/ new turn "x" or "o"
    
    draw_board(board)

    if count >= 4:
        if is_winning(board, char) == True: #check board for 3 "x" or 3 "o"
            print(f'{player} Won!')
            break

    if count == 8:
        print("\nGame Over\n")
        break

    count += 1
    print(count)


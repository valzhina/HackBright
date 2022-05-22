""" Create a game Tic-tac-toe
Write a game. Input will be from two players x or o
Need to: draw a board
coordinate turns, check if board cell was used or not,
check after every turn if a move == victory
"""

board = [[1,2,3],[4,5,6],[7,8,9]] #adds 9 coordinates to board 
player1 = "x"
player2 = "o"

def draw_board(board):
    """ to draw initial board 9x9 """
    print("\n")
    for i in range(3): #iterate through numbers 0,1,2 createing three rows
        str1 = " " # create emplty str 
        for j in range(3): #iterate through numbers 0,1,2 createing three columns
            str1 += str(board[i][j]) #taking three numbers from board one by one
            if j != 2: #adding | after each number but the last one
                str1 += " | "
        print(str1)
        if i != 2: #print separation lines after each row but the last one
            print("--- --- ---")
    print("\n")

def player_turn(board, player, coordinate):
    """ Current board, "x" or "o", number that was an input from 1 to 9 """
    coordinate = coordinate - 1 #correction for binary system 
    i = coordinate // 3 #check coordiante's row
    j = coordinate % 3 #check coordiante's position in a row
    board[i][j] = player #updating board "x" or "o" 
    return(board)

def if_cell_is_empty(board, coordinate):
    """ tbd """
    coordinate = coordinate - 1 #correction for binary system 
    i = coordinate // 3 #check coordiante's row
    j = coordinate % 3 #check coordiante's position in a row
    if board[i][j] == 'x' or board[i][j] == 'o': #checking board "x" or "o" 
        return False
    return True

def is_winning2(board, player): #when checking all the scenarios one by one
    """ Checks if "x" or "o" are next to each other"""
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False

def is_winning(board, player):
    """ Checks if "x" or "o" are next to each other"""
    win = None

    #checking rows
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != player: #[i]-row stays 3 times the same [j]iterates and should be all be == "x" or "o" to win
                win = False
                break
        if win == True:
            return win

    #checking columns
    for i in range(3):
        win = True # changing from None to True
        for j in range(3):
            if board[j][i] != player: #[j]-column stays 3 times the same [i]iterates and should be all be == "x" or "o" to win
                win = False
                break
        if win == True:
            return win

    #checking diagonal 1
    win = True #changing from Falce to True
    for i in range(3):
        if board[i][i] != player:
            win = False
            break
    if win == True:
        return win

    #checking diagonal 2
    win = True #changing from Falce to True
    for i in range(3):
        if board[i][3-1-i] != player:
            win = False
            break
    if win == True:
        return win
    return False #for all other scenarios 


def check_input(coordinate):
    """ Checks if input is a number from 1 to 9 """
    while coordinate not in "123456789": #untill input is correct asking for input and save it in coordinate
        coordinate = input('It is not a valid number. Enter a number from 1 to 9')
    return int(coordinate) #transfer to str to int
   
while True: #untill the game is over do this loop
    draw_board(board)
    coordinate1 = input('Player 1: Enter next number')
    coordinate1 = check_input(coordinate1) #gets int back

    while if_cell_is_empty(board, coordinate1) == False: #untill player1 gives you a correct cell number 
        
        coordinate1 = input('This number has been used. Enter a different number')
        coordinate1 = check_input(coordinate1)
    board = player_turn(board, player1, coordinate1) #updating board w/ new turn "x" or "o"
    draw_board(board)

    if is_winning(board, player1) == True: #check board for 3 "x" or 3 "o"
        print('Player 1 Won!')
        break
    # do the same for player 2
    coordinate2 = input('Player 2: Enter next number')
    coordinate2 = check_input(coordinate2)

    while if_cell_is_empty(board, coordinate2) == False:
        
        coordinate2 = input('This number has been used. Enter a different number')
        coordinate2 = check_input(coordinate2)
    board = player_turn(board, player2, coordinate2)
    draw_board(board)
    
    if is_winning(board, player2) == True:
        print('Player 2 Won!')
        break

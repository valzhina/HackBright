board = {'1': '1', '2': '2', '3': '3',
         '4': '4', '5': '5', '6': '6'
         '7': '7', '8': '8', '9': '9'}
player1 = "x"
player2 = "o"

def draw_board(board):
    """ tbd """
    print("\n")
    # for i in range(3):
    #     str1 = " "
    #     for j in range(3):
    #         str1 += str(board[i][j])
    #         if j != 2:
    #             str1 += " | "
    #     print(str1)
    #     if i != 2:
    #         print("--- --- ---")

    print("\n")


# def player_turn(board, player, coordinate):
#     """ tbd """
#     coordinate = coordinate - 1
#     i = coordinate // 3
#     j = coordinate % 3
#     board[i][j] = player
#     return(board)

# def if_cell_is_empty(board, coordinate):
#     """ tbd """
#     coordinate = coordinate - 1
#     i = coordinate // 3
#     j = coordinate % 3
#     if board[i][j] == 'x' or board[i][j] == 'o':
#         return False
#     return True

# def is_winning(board, player):
#     """ tbd """
#     if board[0][0] == player and board[0][1] == player and board[0][2] == player:
#         return True
#     elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
#         return True
#     elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
#         return True
#     elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
#         return True
#     elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
#         return True
#     elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
#         return True
#     elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True
#     elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
#         return True
#     return False

# def check_input(coordinate):
#     """ tbd """
#     while coordinate not in "123456789":
#         coordinate = input('It is not a valid number. Enter a number from 1 to 9')
#     return int(coordinate)
   
# while True:
#     draw_board(board)
#     coordinate1 = input('Player 1: Enter next number')
#     coordinate1 = check_input(coordinate1)

#     while if_cell_is_empty(board, coordinate1) == False:
        
#         coordinate1 = input('This number has been used. Enter a different number')
#         coordinate1 = check_input(coordinate1)
#     board = player_turn(board, player1, coordinate1)
#     draw_board(board)

#     if is_winning(board, player1) == True:
#         print('Player 1 Won!')
#         break

#     coordinate2 = input('Player 2: Enter next number')
#     coordinate2 = check_input(coordinate2)

#     while if_cell_is_empty(board, coordinate2) == False:
        
#         coordinate2 = input('This number has been used. Enter a different number')
#         coordinate2 = check_input(coordinate2)
#     board = player_turn(board, player2, coordinate2)
#     draw_board(board)
    
#     if is_winning(board, player2) == True:
#         print('Player 2 Won!')
#         break

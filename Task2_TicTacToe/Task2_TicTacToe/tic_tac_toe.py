import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax(is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    board[move] = 'O'

print("Tic Tac Toe")
print("You = X | Computer = O")

while True:
    print_board()
    user_move = int(input("Enter position (0-8): "))
    if board[user_move] == ' ':
        board[user_move] = 'X'
    else:
        print("Invalid move")
        continue

    if check_winner('X'):
        print_board()
        print("You win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    best_move()

    if check_winner('O'):
        print_board()
        print("Computer wins!")
        break

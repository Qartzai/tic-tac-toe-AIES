import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty.append((i, j))
    return empty

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid input! Choose from 1 to 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Cell already taken! Choose another.")
                continue
            board[row][col] = "X"
            break
        except ValueError:
            print("Please enter a valid number!")

def computer_move(board):
    empty = get_empty_cells(board)
    move = random.choice(empty)
    board[move[0]][move[1]] = "O"
    print(f"Computer chose position {move[0]*3 + move[1] + 1}")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("You are 'X' and Computer is 'O'.")
    print_board(board)
    
    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            computer_move(board)
        print_board(board)
        
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            return
        elif check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            return
    
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()

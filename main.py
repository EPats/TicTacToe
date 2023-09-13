# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Initialize an empty board
empty_board = [[" ", " ", " "] for _ in range(3)]

# Display the empty board
display_board(empty_board)

# Function to make a move on the board
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Cell is already occupied. Choose another cell.")
        return False

# Test the function
board = [[" ", " ", " "] for _ in range(3)]

# Player 'X' makes a move at (0, 0)
make_move(board, 0, 0, 'X')

# Player 'O' makes a move at (1, 1)
make_move(board, 1, 1, 'O')

# Player 'X' tries to make a move at (0, 0) again
make_move(board, 0, 0, 'X')

# Display the updated board
display_board(board)
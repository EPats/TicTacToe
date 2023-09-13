# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Initialize an empty board
empty_board = [[" ", " ", " "] for _ in range(3)]

# Display the empty board
display_board(empty_board)
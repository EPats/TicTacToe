X_SYMBOL = 'X'
O_SYMBOL = 'O'
BLANK_SYMBOL = ''
X_WIN = 'X wins'
O_WIN = 'O wins'
TIE = 'Game is tied'
NO_WIN_MET = 'No win condition met'

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 10)


# Function to make a move on the board
def make_move(board, row, col, player):
    if board[row][col] == BLANK_SYMBOL:
        board[row][col] = player
        return True
    else:
        print('Cell is already occupied. Choose another cell.')
        return False


# Test the function
# Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
            all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


# Function to check for a tie
def check_tie(board):
    return all([cell in [X_SYMBOL, O_SYMBOL] for row in board for cell in row])


def debug_check_board(board):
    if check_win(board, X_SYMBOL):
        return X_WIN
    elif check_win(board, O_SYMBOL):
        return O_WIN
    elif check_tie(board):
        return TIE
    return NO_WIN_MET



board = [[' ', ' ', ' '] for _ in range(3)]

tests = [
    {'board': [[X_SYMBOL, X_SYMBOL, X_SYMBOL], [BLANK_SYMBOL, O_SYMBOL, BLANK_SYMBOL], [BLANK_SYMBOL, BLANK_SYMBOL, O_SYMBOL]], 'result': X_WIN},
    {'board': [[X_SYMBOL, O_SYMBOL, X_SYMBOL], [O_SYMBOL, X_SYMBOL, O_SYMBOL], [O_SYMBOL, X_SYMBOL, X_SYMBOL]], 'result': X_WIN},
    {'board': [[X_SYMBOL, O_SYMBOL, X_SYMBOL], [O_SYMBOL, X_SYMBOL, O_SYMBOL], [O_SYMBOL, O_SYMBOL, O_SYMBOL]], 'result': O_WIN},
    {'board': [[X_SYMBOL, O_SYMBOL, X_SYMBOL], [O_SYMBOL, X_SYMBOL, O_SYMBOL], [O_SYMBOL, X_SYMBOL, O_SYMBOL]], 'result': TIE},
    {'board': [[X_SYMBOL, BLANK_SYMBOL, BLANK_SYMBOL], [O_SYMBOL, BLANK_SYMBOL, BLANK_SYMBOL], [BLANK_SYMBOL, X_SYMBOL, O_SYMBOL]], 'result': NO_WIN_MET}
]

checked_tests = [{'test_#': i, 'passed': test['result'] == debug_check_board(test['board']),
                  'expected': test['result'], 'received': debug_check_board(test['board']),
                  'board': test['board']} for i, test in enumerate(tests)]
if all([test['passed'] for test in checked_tests]):
    print(f'All {len(checked_tests)} passed.')
else:
    failed_tests = [test for test in checked_tests if not test['passed']]
    print(f'Failed {len(failed_tests)} of {len(checked_tests)} tests.')
    for failed_test in failed_tests:
        print('-'*30)
        print(f'Test {failed_test["test_#"]}')
        print(f'Expected {failed_test["expected"]}; got {failed_test["received"]}')
        display_board(failed_test['board'])
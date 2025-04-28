# logic.py
# This file contains all the game logic functions.
# It checks for win conditions, manages turns, validates moves, and handles game flow.
# Functions include checking for a winner, a draw, and making moves.
import random
import time

def check_win(board : list[str], symbol : str):
    """
This function checks rows, columns and diagonals for wins
    """
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row): # all function with a generator expression
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

def check_draw(board):
    """
    Returns True if there are no possible winning moves left for either player.
    """
    lines = []

    # adds Rows from board to lines
    lines.extend(board)

    print(lines)

    # adds Columns from board to lines
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    # adds Diagonals from board to lines
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if ' ' in line:  # Line is not full yet
            if not ('X' in line and 'O' in line):
                # This line could still be won by someone
                return False

    return True  # All lines are blocked

# def is_valid_move(board, row, col):
#     return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, position, symbol):
    """
    Places the symbol ('X' or 'O') on the board.
    `move` is an integer from 1 to 9.
    Returns True if the move was successful, otherwise False.
    """
    if position < 1 or position > 9: #accounts for invalid moves
        return False  # out of range

    row = (position - 1) // 3
    col = (position - 1) % 3

    if board[row][col] == ' ':
        board[row][col] = symbol
        return True
    return False  # cell already taken


def get_available_moves(board):
    return [r*3+c+1 for r in range(3) for c in range(3) if board[r][c] == ' '] 
    # the line above returns a list of all available positions

def switch_player(current_player, players):
    return players[1] if current_player == players[0] else players[0]

def create_empty_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def create_position_board(board):
    """Creates a board showing position numbers where spots are empty."""
    new_board = []
    pos = 1
    for row in board:
        new_row = []
        for cell in row:
            if cell == ' ':
                new_row.append(str(pos))
            else:
                new_row.append(cell)
            pos += 1
        new_board.append(new_row)
    return new_board

def computer_move(board, computer_symbol, human_symbol):
    """
    Make computer move smartly:
    1. Win if possible
    2. Block human's win
    3. Otherwise pick best available spot
    """

    # Short delay to simulate "thinking"
    print("\nComputer is thinking...")
    time.sleep(1.5)

    # Check if computer can win
    for move in get_available_moves(board):
        temp_board = [row[:] for row in board]
        make_move(temp_board, move, computer_symbol)
        if check_win(temp_board, computer_symbol):
            make_move(board, move, computer_symbol)
            return

    # Check if need to block human's win
    for move in get_available_moves(board):
        temp_board = [row[:] for row in board]
        make_move(temp_board, move, human_symbol)
        if check_win(temp_board, human_symbol):
            make_move(board, move, computer_symbol)
            return

    # Pick center if available
    if board[1][1] == ' ':
        make_move(board, 5, computer_symbol)
        return

    # Pick corners if available
    corners = [1, 3, 7, 9]
    available_corners = [pos for pos in corners if pos in get_available_moves(board)]
    random.shuffle(available_corners)
    for move in available_corners:
        if make_move(board, move, computer_symbol):
            return

    # Pick sides
    sides = [2, 4, 6, 8]
    available_sides = [pos for pos in sides if pos in get_available_moves(board)]
    random.shuffle(available_sides)
    for move in available_sides:
        if make_move(board, move, computer_symbol):
            return
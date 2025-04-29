# logic.py
# This file contains all the game logic functions.
# It checks for win conditions, manages turns, validates moves, and handles game flow.
# Functions include checking for a winner, a draw, and making moves.
import time
import random

def check_win(board: list[list[str]], symbol: str) -> bool:
    """
    Checks if the given symbol has a winning combination.

    board
        A 3x3 list of lists containing "X", "O", or " ".
    symbol
        The player's symbol to check for a win ("X" or "O").

    Returns
    -------
    bool
        True if the symbol has a winning line; otherwise False.
    """
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
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


def check_draw(board: list[list[str]]) -> bool:
    """
    Determines if the game is a draw.

    board
        A 3x3 list of lists representing the board.

    Returns
    -------
    bool
        True if no winning moves are left for either player; otherwise False.
    """
    lines : list[list[str]]= board[:] # adds rows to lines

    # adds columns to lines
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    # adds diagonals to 
    lines.append([board[i][i] for i in range(3)]) #list comprehension
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if " " in line and not ("X" in line and "O" in line):
            return False
    return True


def make_move(board: list[list[str]], position: int, symbol: str) -> bool:
    """
    Places a symbol at the specified board position.

    board
        A 3x3 list of lists.
    position
        Integer from 1 to 9 indicating the board cell.
    symbol
        The player's symbol to place ("X" or "O").

    Returns
    -------
    bool
        True if the move is valid and was made; otherwise False.
    """
    if position < 1 or position > 9:
        raise ValueError
    index : int = position - 1
    row : int = index // 3
    col : int = index % 3

    if board[row][col] == " ":
        board[row][col] = symbol
        return True
    print("❌ can't play in a taken spot!")
    return False


def get_available_moves(board: list[list[str]]) -> list[int]:
    """
    Returns a list of available move positions.

    board
        A 3x3 list of lists.

    Returns
    -------
    list[int]
        List of positions (1–9) that are currently unoccupied.
    """
    return [row * 3 + col + 1 for row in range(3) for col in range(3) if board[row][col] == " "]


def switch_player(current_player: str, players: list[dict[str,str]]) -> dict:
    """
    Switches to the other player.

    current_player
        The current player's symbol.
    players
        A list of player data (dictionaries) (e.g., [
            {"name": player1_name, "symbol": "X"},
            {"name": player2_name, "symbol": "O"}
        ]).

    Returns
    -------
    str
        The symbol of the next player.
    """
    return players[1] if current_player == players[0] else players[0]


def create_empty_board() -> list[list[str]]:
    """
    Creates an empty 3x3 Tic-Tac-Toe board.

    Returns
    -------
    list[list[str]]
        A 3x3 board filled with spaces.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def computer_move(board: list[list[str]], computer_symbol: str, human_symbol: str) -> None:
    """
    Makes a move for the computer:
    - Win if possible
    - Block human's win
    - Take center, corner, or side (in that order)

    board
        The current board.
    computer_symbol
        Symbol used by the computer.
    human_symbol
        Symbol used by the human player.

    Returns
    -------
    None
    """
    print("\nComputer is thinking...")
    time.sleep(1.5)

    for move in get_available_moves(board):
        temp_board : list = [row[:] for row in board] # making a copy of the original board
        # checks if move would be a win for the computer on the copy board and makes the move if it will be a win. 
        if make_move(temp_board, move, computer_symbol) and check_win(temp_board, computer_symbol):
            make_move(board, move, computer_symbol)
            return 

    for move in get_available_moves(board):
        temp_board : list = [row[:] for row in board]  # making a copy of the original board
        # checks if move would be a win for the human on the copy board and blocks the space if it will be a win. 
        if make_move(temp_board, move, human_symbol) and check_win(temp_board, human_symbol):
            make_move(board, move, computer_symbol)
            return

    if board[1][1] == " ": # makes the computer play at the centre if its empty
        make_move(board, 5, computer_symbol)
        return

    corners : list = [1, 3, 7, 9]
    random.shuffle(corners)
    for move in corners: # makes a random corner move
        if move in get_available_moves(board) and make_move(board, move, computer_symbol):
            return

    sides : list = [2, 4, 6, 8]
    random.shuffle(sides)
    for move in sides: # makes a random side move
        if move in get_available_moves(board) and make_move(board, move, computer_symbol):
            return

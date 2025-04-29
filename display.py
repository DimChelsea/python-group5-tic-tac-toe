# display.py
# This file is responsible for displaying the game board in the terminal.
# It uses ASCII characters to create the game grid and ANSI escape codes to add colors.
# It also handles updating the board after each move.

def display_board(game_board: list[list[str]]) -> None:
    """
    Displays a colored 3x3 Tic-Tac-Toe board in the console.

    game_board
        A 3x3 list of lists with values "X", "O", or " " (empty).
        X is shown in red, O in green, and empty spots as gray numbers (1–9).

    The board is printed directly with ANSI color formatting.

    Returns
    -------
    None
    """
    for row in range(3):
        row_display: list[str] = []
        for col in range(3):
            index: int = row * 3 + col
            cell: str = game_board[row][col]

            if cell == "X":
                row_display.append("\033[91mX\033[0m")
            elif cell == "O":
                row_display.append("\033[92mO\033[0m")
            else:
                row_display.append(f"\033[30m{index + 1}\033[0m")

        print(" | ".join(row_display))
        if row < 2:
            print("--+---+--")
            
if __name__ == "__main__":
    board : list = [
            ["X", "X", " "],
            ["X", "O", "O"],
            [" ", "O", "X"]
        ]

    display_board(board)    
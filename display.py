# display.py
# This file is responsible for displaying the game board in the terminal.
# It uses ASCII characters to create the game grid and ANSI escape codes to add colors.
# It also handles updating the board after each move.


def display_board(board_in_use : list[str]):
    """
    Displays the Tic-Tac-Toe board with numbers in unoccupied spots (1-9).
    X's are red, O's are green.
    """
    for row in range(3):  # Iterate over rows
        row_display : list[str] = []
        for col in range(3):  # Iterate over columns
            index : int = row * 3 + col  # Calculate the index in the flattened board
            cell : str = board_in_use[row][col]
            
            if cell == 'X':
                row_display.append("\033[91mX\033[0m")  # Red for X
            elif cell == 'O':
                row_display.append("\033[92mO\033[0m")  # Green for O
            else:
                # Display the number (1-9) in unoccupied spots
                row_display.append(f"\033[30m{index + 1}\033[0m")

        # Join the row and print it
        print(" | ".join(row_display))
        
        if row < 2:  # Print separator only between rows
            print("--+---+--")
if __name__ == "__main__":
    board : list = [
            ['X', 'O', 'X'],
            [' ', 'X', 'O'],
            ['O', ' ', 'X']
        ]

    display_board(board)
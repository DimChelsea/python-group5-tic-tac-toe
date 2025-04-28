# main.py
# This file contains the main script that runs the game.
# It integrates the game logic and the display functions.
# It also handles user input, game modes (Player vs Player or Player vs Computer),
# and the replay/quit system.

# from display import display_board
# from logic import *

# board : list = [
#         ['X', 'O', 'X'],
#         [' ', 'X', 'O'],
#         ['O', ' ', 'X']
#     ]
# print(get_available_moves(board))
# display_board(board)
# make_move(board,4,"O")
# display_board(board)
# print(check_win(board, "X"))
# check_draw(board)
import random
from display import display_board
from logic import *
import sys


def get_player_info(player_num : int):
    """Gets the name of a player"""
    name = input(f"Enter name for Player {player_num}: ").strip()
    return name

def choose_game_mode():
    """Gives users the oppourt"""
    print("Choose Game Mode:")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    choice : str = ''
    while choice not in ['1', '2']:
        choice : str = input("Enter your choice (1 or 2): ").strip()
    return choice

def choose_x_player_pvp():
    print("\nWho should be 'X' and start the game?")
    print("1. First Player")
    print("2. Second Player")
    print("3. Random Choice")
    choice : str = ''

    while choice not in ['1', '2', '3']:
        choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        return 0
    elif choice == '2':
        return 1
    else:
        return random.randint(0, 1)

def choose_symbol_player_vs_computer():
    print("\nDo you want to be 'X', 'O', or Random?")
    symbol : str = ''
    while symbol not in ['X', 'O', 'R']:
        symbol = input("Enter your choice (X/O/R for Random): ").strip().upper()

    if symbol == 'R':
        symbol = random.choice(['X', 'O'])

    return symbol

def main():
    print("🎮 Welcome to Tic-Tac-Toe! 🎮")

    game_mode = choose_game_mode()  # Choose Player vs Player or Player vs Computer

    if game_mode == '1':  # Player vs Player
        player1_name = get_player_info(1)
        player2_name = get_player_info(2)

        # Choose who gets 'X' (first player)
        x_player_index = choose_x_player_pvp()
        # o_player_index = 1 - x_player_index

        players = [
            {'name': player1_name, 'symbol': 'X' if x_player_index == 0 else 'O'},
            {'name': player2_name, 'symbol': 'O' if x_player_index == 0 else 'X'}
        ]

        # Game Loop
        while True:
            board = create_empty_board()
            move_count = 0
            current_player = players[x_player_index]  # Start with player who has 'X'

            while True:
                position_board = create_position_board(board)  # Create a board with positions
                display_board(position_board)  # Display board

                print(f"\n{current_player['name']}'s turn ({current_player['symbol']})")

                # Get player move
                try:
                    move = int(input("Enter your move (1-9): "))
                    if not make_move(board, move, current_player['symbol']):
                        print("❌ Invalid move! Try again.")
                        continue
                except ValueError:
                    print("❌ Please enter a valid number between 1 and 9.")
                    continue

                move_count += 1

                # Check for win or draw
                if move_count >= 5:
                    winning_line = check_win(board, current_player['symbol'])
                    if winning_line:
                        final_board = create_position_board(board)
                        display_board(final_board)
                        print(f"\n🎉 {current_player['name']} ({current_player['symbol']}) wins! 🎉")
                        break
                    if check_draw(board):
                        display_board(create_position_board(board))
                        print("\n🤝 It's a draw! Well played both!")
                        break

                current_player = switch_player(current_player, players)  # Switch players

            # Replay option
            play_again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\nThanks for playing! Goodbye! 👋")
                break

    else:  # Player vs Computer Mode
        player_name = get_player_info(1)
        human_symbol = choose_symbol_player_vs_computer()
        computer_symbol = 'O' if human_symbol == 'X' else 'X'

        if human_symbol == 'X':
            current_player = 'human'
        else:
            current_player = 'computer'

        print(f"\n{player_name} will be '{human_symbol}' and Computer will be '{computer_symbol}'.")

        # Game Loop
        while True:
            board = create_empty_board()
            move_count = 0

            while True:
                position_board = create_position_board(board)
                display_board(position_board)

                # Human move
                if current_player == 'human':
                    print(f"\n{player_name}'s turn ({human_symbol})")
                    try:
                        move = int(input("Enter your move (1-9): "))
                        if not make_move(board, move, human_symbol):
                            print("❌ Invalid move! Try again.")
                            continue
                    except ValueError:
                        print("❌ Please enter a valid number between 1 and 9.")
                        continue
                # Computer move
                else:
                    computer_move(board, computer_symbol, human_symbol)

                move_count += 1

                # Check for win or draw
                if move_count >= 5:
                    symbol = human_symbol if current_player == 'human' else computer_symbol
                    winning_line = check_win(board, symbol)
                    if winning_line:
                        final_board = create_position_board(board)
                        display_board(final_board)
                        if current_player == 'human':
                            print(f"\n🎉 {player_name} wins! 🎉")
                        else:
                            print("\n🤖 Computer wins! Better luck next time!")
                        break

                    if check_draw(board):
                        display_board(create_position_board(board))
                        print("\n🤝 It's a draw! Well played!")
                        break

                current_player = 'computer' if current_player == 'human' else 'human'

            # Replay option
            play_again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\nThanks for playing! Goodbye! 👋")
                sys.exit() # This stops the entire program immediately

if __name__ == "__main__":
    main()

main()

import sys
import random
from display import display_board
from logic import *


def get_player_info(player_num: int) -> str:
    """
    Prompts the user to enter a name for the specified player.

    Parameters
    ----------
    player_num : int
        The player number (1 or 2).

    Returns
    -------
    str
        The player's name as a string.
    """
    name: str = input(f"Enter name for Player {player_num}: ").strip()
    return name


def choose_game_mode() -> str:
    """
    Allows the user to select the game mode.

    Returns
    -------
    str
        "1" for Player vs Player or "2" for Player vs Computer.
    """
    print("Choose Game Mode:")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    choice: str = ""
    while choice not in ["1", "2"]:
        choice = input("Enter your choice (1 or 2): ").strip()
    return choice


def choose_x_player_pvp() -> int:
    """
    Lets users choose who plays as "X" in Player vs Player mode.

    Returns
    -------
    int
        0 if the first player is "X", 1 if the second, or randomly selected.
    """
    print("\nWho should be \"X\" and start the game?")
    print("1. First Player")
    print("2. Second Player")
    print("3. Random Choice")
    choice: str = ""

    while choice not in ["1", "2", "3"]:
        choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        return 0
    elif choice == "2":
        return 1
    else:
        return random.randint(0, 1)


def choose_symbol_player_vs_computer() -> str:
    """
    Lets the player choose their symbol for Player vs Computer mode.

    Returns
    -------
    str
        "X" or "O", randomly selected if user inputs "R".
    """
    print("\nDo you want to be \"X\", \"O\", or Random?")
    symbol: str = ""
    while symbol not in ["X", "O", "R"]:
        symbol = input("Enter your choice (X/O/R for Random): ").strip().upper()

    if symbol == "R":
        symbol = random.choice(["X", "O"])

    return symbol


def main() -> None:
    """
    Main function that runs the Tic-Tac-Toe game.
    Handles game mode selection, game logic, and replay option.

    Returns
    -------
    None
    """
    print("🎮 Welcome to Tic-Tac-Toe! 🎮")

    game_mode : str = choose_game_mode()

    if game_mode == "1":  # Player vs Player
        player1_name : str = get_player_info(1)
        player2_name : str = get_player_info(2)

        x_player_index : int = choose_x_player_pvp()

        players : list[dict[str]] = [
            {"name": player1_name, "symbol": "X" if x_player_index == 0 else "O"},
            {"name": player2_name, "symbol": "O" if x_player_index == 0 else "X"}
        ]

        while True:
            board : list[list[str]]= create_empty_board()
            move_count : int = 0
            current_player : dict = players[x_player_index]

            while True:
                display_board(board)
                print(f"\n{current_player["name"]}'s turn ({current_player["symbol"]})")

                try:
                    move : int = int(input("Enter your move (1-9): "))
                    if not make_move(board, move, current_player["symbol"]):
                        print("❌ Invalid move! Try again.")
                        continue
                except ValueError:
                    print("❌ Please enter a valid number between 1 and 9.")
                    continue

                move_count += 1

                if move_count >= 5:
                    winning_line = check_win(board, current_player["symbol"])
                    if winning_line:
                        display_board(board)
                        print(f"\n🎉 {current_player["name"]} ({current_player["symbol"]}) wins! 🎉")
                        break
                    if check_draw(board):
                        display_board(board)
                        print("\n🤝 It's a draw! Well played both!")
                        break

                current_player : str = switch_player(current_player, players)

            play_again : str = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
            if play_again != "y":
                print("\nThanks for playing! Goodbye! 👋")
                break

    else:  # Player vs Computer Mode
        player_name : str = get_player_info(1)
        human_symbol : str = choose_symbol_player_vs_computer()
        computer_symbol : str = "O" if human_symbol == "X" else "X"

        if human_symbol == "X":
            current_player : str = "human"
        else:
            current_player : str = "computer"

        print(f"\n{player_name} will be \"{human_symbol}\" and Computer will be \"{computer_symbol}\".")

        while True:
            board : list[list[str]]= create_empty_board()
            move_count : int = 0

            while True:
                display_board(board)
                if current_player == "human":
                    print(f"\n{player_name}'s turn ({human_symbol})")
                    try:
                        move = int(input("Enter your move (1-9): "))
                        if not make_move(board, move, human_symbol):
                            print("❌ Invalid move! Try again.")
                            continue
                    except ValueError:
                        print("❌ Please enter a valid number between 1 and 9.")
                        continue
                else:
                    computer_move(board, computer_symbol, human_symbol)

                move_count += 1

                if move_count >= 5:
                    symbol : str = human_symbol if current_player == "human" else computer_symbol
                    winning_line: bool = check_win(board, symbol)
                    if winning_line:
                        display_board(board)
                        if current_player == "human":
                            print(f"\n🎉 {player_name} wins! 🎉")
                        else:
                            print("\n💻 Computer wins! Better luck next time!")
                        break

                    if check_draw(board):
                        display_board(board)
                        print("\n🤝 It's a draw! Well played!")
                        break

                current_player : str = "computer" if current_player == "human" else "human"

            play_again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
            if play_again != "y":
                print("\nThanks for playing! Goodbye! 👋")
                sys.exit() # This stops the entire program immediately
            current_player = "human" if human_symbol == "X" else "computer"

if __name__ == "__main__":
    main()


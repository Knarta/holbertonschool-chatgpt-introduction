#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if a player has won the game.

    Returns:
    True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw(board):
    """
    Checks if the game is a draw (board is full and no winner).

    Returns:
    True if it's a draw, False otherwise.
    """
    for row in board:
        if " " in row:  # There are still empty spaces
            return False
    return True  # All spaces are filled and no winner


def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty 3x3 board
    player = "X"  # Start with player X
    last_player = None  # Track the last player who made a valid move

    while True:
        print_board(board)  # Display the current board

        # Ensure valid input for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

                if row not in range(3) or col not in range(3):  # Check bounds
                    print("Invalid input. Row and column must be between 0 and 2.")
                    continue
                if board[row][col] == " ":
                    board[row][col] = player  # Place the symbol
                    last_player = player  # Save the last player who made a valid move
                    break
                else:
                    print("That spot is already taken! Try again.")
            except ValueError:
                print("Invalid input. Please enter valid numeric values for row and column.")

        # Check for a winner or draw
        if check_winner(board):
            print_board(board)
            print(f"Player {last_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
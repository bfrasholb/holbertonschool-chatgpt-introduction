#!/usr/bin/env python3.8

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    # Rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Values must be 0, 1, or 2.")
                continue

            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = get_move(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player AFTER checking win
        player = "O" if player == "X" else "X"


tic_tac_toe()

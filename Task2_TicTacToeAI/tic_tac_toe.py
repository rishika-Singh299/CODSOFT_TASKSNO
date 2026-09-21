# CODSOFT AI Internship
# Task 2: Tic-Tac-Toe AI using Minimax

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


def is_board_full(board):
    return " " not in board


def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move(board):
    best_score = -1000
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    board = [" "] * 9

    print("================================")
    print("       Tic-Tac-Toe AI")
    print("================================")
    print("You are X")
    print("Computer is O")
    print("Computer uses Minimax AI.")
    print("Choose a position from 1 to 9.")

    print_board([str(i) for i in range(1, 10)])

    while True:
        try:
            move = int(input("Enter your position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please choose a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("That position is already occupied.")
                continue

            board[move] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        move = computer_move(board)
        board[move] = "O"

        print("Computer's move:")
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break


play_game()

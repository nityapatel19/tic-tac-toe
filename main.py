import random


def insert_letter(board, letter, pos):
    board[pos] = letter


def space_is_free(board, pos):
    return board[pos] == ' '


def print_board(board):
    print("""
     {} | {} | {} 
    -----------
     {} | {} | {} 
    -----------
     {} | {} | {} 
    """.format(*board[1:]))


def is_board_full(board):
    return board.count(' ') == 0


def is_winner(board, letter):
    return any(all([board[pos] == letter for pos in trio]) for trio in WINNING_TRIOS)


def player_move(board, letter):
    while True:
        try:
            move = int(input("Enter position (1-9): "))
            if move not in range(1, 10):
                print("Position out of range. Try again.")
            elif not space_is_free(board, move):
                print("Position already occupied. Try again.")
            else:
                insert_letter(board, letter, move)
                break
        except ValueError:
            print("Position not a number. Try again.")


def computer_move_easy(board):
    empty_spaces = [i for i in range(1, 10) if space_is_free(board, i)]
    move = random.choice(empty_spaces)
    insert_letter(board, 'O', move)


def computer_move_medium(board):
    possible_moves = {i for i in range(1, 10) if space_is_free(board, i)}

    # Check if computer can win in the next move, if yes, make that move
    # Or if player can win in the next move, block that move
    for letter in ['O', 'X']:
        for move in possible_moves:
            board_copy = board[:]
            insert_letter(board_copy, letter, move)
            if is_winner(board_copy, letter):
                insert_letter(board, 'O', move)
                return

    open_corners = list(possible_moves.intersection([1, 3, 7, 9]))
    if open_corners:
        move = random.choice(open_corners)
        insert_letter(board, 'O', move)
        return

    if 5 in possible_moves:
        insert_letter(board, 'O', 5)
        return

    open_edges = list(possible_moves.intersection([2, 4, 6, 8]))
    if open_edges:
        move = random.choice(open_edges)
        insert_letter(board, 'O', move)
        return


def minimax(board, maximize=True):
    letter = 'O' if maximize else 'X'
    win_score = 1 if maximize else -1

    if is_winner(board, letter):
        return win_score
    elif is_board_full(board):
        return 0

    possible_moves = {i for i in range(1, 10) if space_is_free(board, i)}
    best_score = float('-inf') if maximize else float('inf')
    for move in possible_moves:
        board[move] = letter
        score = minimax(board, not maximize)
        board[move] = ' '
        best_score = max(score, best_score) if maximize else min(score, best_score)

    return best_score


def computer_move_hard(board):
    possible_moves = {i for i in range(1, 10) if space_is_free(board, i)}
    best_score = float('-inf')
    best_move = None
    for move in possible_moves:
        board[move] = 'O'
        # O wants to maximize. O makes a move and checks the best minimized score that X can give.
        # Then chooses the maximum from those.
        score = minimax(board, maximize=False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    insert_letter(board, 'O', best_move)


def player_vs_player():
    print("PLAYER VS PLAYER")
    print("Player 1 is X and Player 2 is O.")

    board = ['#'] + [' '] * 9
    print_board(board)

    while True:
        if not is_winner(board, 'O'):
            player_move(board, 'X')
            print_board(board)
        else:
            print("Player 2 won!!!")
            break

        if is_board_full(board):
            print("The game is a draw.")
            break

        if not is_winner(board, 'X'):
            player_move(board, 'O')
            print_board(board)
        else:
            print("Player 1 won!!!")
            break


def player_vs_computer(level=1):
    computer_move = COMPUTER_MOVE[level]
    print("PLAYER VS COMPUTER")
    print("You are X and Computer is O.")

    board = ['#'] + [' '] * 9
    print_board(board)

    while True:
        if not is_winner(board, 'O'):
            player_move(board, 'X')
        else:
            print("You lost!")
            break

        if is_board_full(board):
            print("The game is a draw.")
            break

        if not is_winner(board, 'X'):
            computer_move(board)
            print_board(board)
        else:
            print_board(board)
            print("You won!!!")
            break


WINNING_TRIOS = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
COMPUTER_MOVE = {
    1: computer_move_easy,
    2: computer_move_medium,
    3: computer_move_hard
}


if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    play = input("Press p to play, anything else to quit: ").lower()
    while play == 'p':
        mode = input("Press 1 for Player vs Player, 2 for Player vs Computer: ")
        if mode == '1':
            player_vs_player()
            play = input("Press p to play again, q to quit: ").lower()

        elif mode == '2':
            try:
                level = int(input("Enter level of difficulty (1-3), anything else to quit: "))
                if 1 <= level <= 3:
                    player_vs_computer(level)
                else:
                    break
            except ValueError as e:
                print(e)
                break
            play = input("Press p to play again, anything else to quit: ").lower()

        else:
            print("Invalid Input.")

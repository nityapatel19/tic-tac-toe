# importing enum for enumerations
from enum import Enum
from typing import List
import random


class Status(Enum):
    DRAW = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2


SIZE = 3
solutions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def print_grid(grid: List[str]):
    print(f"""
 {grid[0]} | {grid[1]} | {grid[2]} 
-----------
 {grid[3]} | {grid[4]} | {grid[5]} 
-----------
 {grid[6]} | {grid[7]} | {grid[8]} 
""")


def check_winner(grid: List[str]):
    if any(all([grid[i] == 'X' for i in s]) for s in solutions):
        return Status.PLAYER_ONE
    elif any(all([grid[i] == 'O' for i in s]) for s in solutions):
        return Status.PLAYER_TWO
    elif ' ' not in grid:
        return Status.DRAW
    else:
        return None


def take_turn(grid: List[str], player: str, inp: List[int]) -> Status:
    grid[inp[0] * 3 + inp[1]] = player
    return check_winner(grid)


def validate_input(grid: List[str], s: str):
    s = list(map(int, s.strip().split()))
    if all([i in range(3) for i in s]) and len(s) == 2 and grid[s[0] * 3 + s[1]] == ' ':
        return s
    else:
        return False


def player_vs_player():
    grid = [' '] * SIZE * SIZE
    winner = None
    player = ['X', 'O']
    while winner is None:
        print_grid(grid)

        while not (
                inp := validate_input(grid, input(
                    f'Player {player[0]}, take your turn (Enter coordinates separated by spaces): '))):
            print("Invalid Input. Try again:")

        winner = take_turn(grid, player[0], inp)
        player.append(player.pop(0))

    print_grid(grid)
    if winner.name == "DRAW":
        print("The game is a draw.")
    else:
        print(f"{winner.name} wins!!!")


def player_vs_computer_easy():
    grid = [' '] * SIZE * SIZE
    empty_places = ["0 0", "0 1", "0 2", "1 0", "1 1", "1 2", "2 0", "2 1", "2 2"]
    winner = None
    player = ['X', 'O']
    while winner is None:
        print_grid(grid)

        if player[0] == 'X':
            while not (
                    inp := validate_input(grid, input(
                        f'Player {player[0]}, take your turn (Enter coordinates separated by spaces): '))):
                print("Invalid Input. Try again:")

            winner = take_turn(grid, player[0], inp)

        else:
            choice = random.choice(empty_places)
            turn = validate_input(grid, choice)
            winner = take_turn(grid, player[0], turn)
            empty_places.remove(choice)

        player.append(player.pop(0))

    print_grid(grid)
    if winner.name == "DRAW":
        print("The game is a draw.")
    elif winner == Status.PLAYER_ONE:
        print("Congratulations, you won!!!")
    else:
        print("You lost, better luck next time.")


def player_vs_computer_medium():
    ...


def player_vs_computer_hard():
    ...


def player_vs_computer():
    level = input("Enter level of difficulty (1-3), anything else to quit: ")
    if level == '1':
        player_vs_computer_easy()
    elif level == '2':
        player_vs_computer_medium()
    elif level == '3':
        player_vs_computer_hard()
    else:
        print("Invalid Input.")


if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X and Player 2 is O")
    play = input("Press p to play, anything else to quit: ").lower()
    while play == 'p':
        mode = input("Press 1 for Player vs Player, 2 for Player vs Computer: ")
        if mode == '1':
            player_vs_player()
            play = input("Press p to play again, q to quit: ").lower()

        elif mode == '2':
            player_vs_computer()
            play = input("Press p to play again, anything else to quit: ").lower()

        else:
            print("Invalid Input.")

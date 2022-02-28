# importing enum for enumerations
from enum import Enum
from typing import List


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


if __name__ == '__main__':
    M = [' '] * SIZE * SIZE

    winner = None
    player = ['X', 'O']
    while winner is None:
        print_grid(M)

        while not (
                inp := validate_input(M, input(
                    f'Player {player[0]}, take your turn (Enter coordinates separated by spaces): '))):
            print("Invalid Input. Try again:")

        winner = take_turn(M, player[0], inp)
        player.append(player.pop(0))

    print_grid(M)
    if winner.name == "DRAW":
        print("The game is a draw.")
    else:
        print(f"{winner.name} wins!!!")

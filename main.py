# importing enum for enumerations
import enum

SIZE = 3
solutions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


# creating enumerations using class
class Player(enum.Enum):
    DRAW = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2


def print_grid(M: list[str]):
    print(f"""
 {M[0]} | {M[1]} | {M[2]} 
-----------
 {M[3]} | {M[4]} | {M[5]} 
-----------
 {M[6]} | {M[7]} | {M[8]} 
""")


def check_winner(grid: list[str]):
    if any(all([grid[i] == 'x' for i in s]) for s in solutions):
        return Player.PLAYER_ONE
    elif any(all([grid[i] == 'o' for i in s]) for s in solutions):
        return Player.PLAYER_TWO
    elif ' ' not in grid:
        return Player.DRAW
    else:
        return None
    # if (
    # any([all([M[i][j] == 'x' for j in range(3)]) or all([M[j][i] == 'x' for j in range(3)]) for i in range(3)])) or (
    #         all([M[i][i] == 'x' for i in range(3)]) or all([M[i][2 - i] == 'x' for i in range(3)])):
    #     return Player.PLAYER_ONE
    # elif (
    # any([all([M[i][j] == 'y' for j in range(3)]) or all([M[j][i] == 'y' for j in range(3)]) for i in range(3)])) or (
    #         all([M[i][i] == 'y' for i in range(3)]) or all([M[i][2 - i] == 'y' for i in range(3)])):
    #     return Player.PLAYER_TWO
    # elif 0 == 0:
    #     return Player.DRAW
    # else:
    #     return None


def take_turn(M: list[str], player: Player):
    pass


M = [' '] * SIZE * SIZE
# M = ['x', 'y', 'x', 'y', 'x', 'x', 'x', 'y', 'y']
print_grid(M)
print(check_winner(M))

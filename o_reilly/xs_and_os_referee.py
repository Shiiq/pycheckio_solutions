# Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O)
# who take turns marking the spaces in a 3×3 grid. The player who succeeds in
# placing three respective marks in a horizontal, vertical,
# or diagonal rows (NW-SE and NE-SW) wins the game.
#
# But we will not be playing this game. You will be the referee for this games results.
# You are given a result of a game and you must determine if the game ends
# in a win or a draw as well as who will be the winner. Make sure to return "X"
# if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".


# works on custom 4x4 or more fields
def checkio(game_result: list[str]) -> str:
    row_size = len(game_result)
    col_size = len(game_result[0])
    if row_size != col_size:
        print("The field must a square")
    WIN_CASES = [row_size * "X",
                 row_size * "O"]
    to_rows = game_result
    to_cols = ["".join(game_result[i][j] for i in range(col_size)) for j in range(row_size)]
    diag_NW_SE = "".join(game_result[i][i] for i in range(row_size))
    diag_NE_SW = "".join(game_result[i][j] for i, j in zip(range(0, row_size, 1),
                                                       range(row_size-1, -1, -1)))

    for row in to_rows:
        if row in WIN_CASES:
            return row[0]
    for col in to_cols:
        if col in WIN_CASES:
            return col[0]
    if diag_NW_SE in WIN_CASES:
        return diag_NW_SE[0]
    if diag_NE_SW in WIN_CASES:
        return diag_NE_SW[0]
    return "D"


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
# 4x4
assert checkio(["X.O.", "XX..", "XOO.", "XX00"]) == "X"
# 5x5
assert checkio(["OO.OX", "XOX..", "XOXO.", ".OX..", "XO..."]) == "O"
# 3x3
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")

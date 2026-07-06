def verify_sudoku_board(board: list[list[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    sub_grids = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != 0 and element in row_sets[i]:
                return False
            if element != 0 and element in col_sets[j]:
                return False
            if element != 0 and element in sub_grids[i // 3][j // 3]:
                return False
            row_sets[i].add(element)
            col_sets[j].add(element)
            sub_grids[i // 3][j // 3].add(element)
    return True

    # Time complexity is O(1) as we have fix loop of 9, but if we had say n size bord this will be converted in O(n^2)
    # Space complexity is o(n^2) as well


def empty():
    return [[0 for _ in range(9)] for _ in range(9)]


# 1. Completely empty board -> valid (no conflicts possible)
empty_board = empty()  # expected: True

# 2. Fully solved, all 81 cells filled, no zeros -> valid
#    Confirms the checker returns True on a legitimately complete board.
solved = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]  # expected: True

# 3. Legal repeats: three 5s, but no shared row, column, or box -> valid
#    Guards against a checker that over-reports.
legal_repeats = empty()
legal_repeats[0][0] = 5
legal_repeats[1][3] = 5
legal_repeats[4][6] = 5  # expected: True

# 4. ROW conflict in the LAST row (row 8) -> catches row off-by-one errors
row_bad_last = empty()
row_bad_last[8][2] = 3
row_bad_last[8][7] = 3  # expected: False

# 5. COLUMN conflict in the LAST column (col 8) -> catches column off-by-one errors
col_bad_last = empty()
col_bad_last[1][8] = 4
col_bad_last[6][8] = 4  # expected: False

# 6. Multiple conflicts at once: a row dup AND a column dup
#    A correct checker only needs to find one to return False.
multi_bad = empty()
multi_bad[2][0] = 9
multi_bad[2][8] = 9  # row 2 duplicate
multi_bad[0][4] = 1
multi_bad[7][4] = 1  # column 4 duplicate  -> expected: False

# 7. SUBGRID conflict in the CENTER box (rows 3-5, cols 3-5)
#    Different row AND column, so row/col checks pass. Non-corner box
#    tests that your subgrid indexing isn't hardcoded to the top-left.
center_grid_bad = empty()
center_grid_bad[3][3] = 7
center_grid_bad[4][4] = 7  # expected: False (current code: True)

# 8. SUBGRID conflict in the BOTTOM-RIGHT box (rows 6-8, cols 6-8)
#    Boundary + subgrid combined.
br_grid_bad = empty()
br_grid_bad[7][7] = 2
br_grid_bad[8][8] = 2  # expected: False (current code: True)

print(verify_sudoku_board(empty_board))  # True
print(verify_sudoku_board(solved))  # True
print(verify_sudoku_board(legal_repeats))  # True
print(verify_sudoku_board(row_bad_last))  # False
print(verify_sudoku_board(col_bad_last))  # False
print(verify_sudoku_board(multi_bad))  # False
print(verify_sudoku_board(center_grid_bad))  # False
print(verify_sudoku_board(br_grid_bad))  # False

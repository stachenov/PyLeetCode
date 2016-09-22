import pytest

from problems import valid_sudoku
from problems.sudoku_solver import Solution


@pytest.mark.parametrize("board", [
    ([
         ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
     ]),
])
def test_solveSudoku(board):
    Solution().solveSudoku(board)
    assert all(all(map(lambda c: c != '.', r)) for r in board)
    assert valid_sudoku.Solution().isValidSudoku(board)

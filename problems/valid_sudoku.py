from itertools import product


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols, cells = [0] * 9, [0] * 9, [[0] * 3 for __ in xrange(3)]
        for i, j in product(xrange(9), xrange(9)):
            if board[i][j] != '.':
                m = 1 << int(board[i][j])
                if (rows[i] & m) != 0 or (cols[j] & m) != 0 or (cells[i / 3][j / 3] & m) != 0:
                    return False
                rows[i] |= m
                cols[j] |= m
                cells[i / 3][j / 3] |= m
        return True

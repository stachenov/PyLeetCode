from itertools import product


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # 7:47 - 8:56

        def clear_bit(x, c):
            return x & ~(1 << int(c))

        rows_avail = [reduce(clear_bit,
                             (c for c in r if c != '.'),
                             0b1111111110)
                      for r in board]
        cols_avail = [reduce(clear_bit,
                             (board[i][j] for i in xrange(9) if board[i][j] != '.'),
                             0b1111111110)
                      for j in xrange(9)]
        cells_avail = [[reduce(clear_bit,
                               (board[r * 3 + i][c * 3 + j]
                                for i, j in product(xrange(3), xrange(3))
                                if board[r * 3 + i][c * 3 + j] != '.'),
                               0b1111111110)
                        for c in xrange(3)]
                       for r in xrange(3)]

        def ntz(x):
            n = 1
            if (x & 0xFF) == 0: n += 8; x >>= 8
            if (x & 0x0F) == 0: n += 4; x >>= 4
            if (x & 0x03) == 0: n += 2; x >>= 2
            return n - (x & 1)

        def solve(row, col):
            i, j = row, col
            while i < 9:
                while j < 9:
                    if board[i][j] == '.':
                        m = rows_avail[i] & cols_avail[j] & cells_avail[i / 3][j / 3]
                        while m != 0:
                            board[i][j] = str(ntz(m))
                            rows_avail[i] &= ~(m & -m)
                            cols_avail[j] &= ~(m & -m)
                            cells_avail[i / 3][j / 3] &= ~(m & -m)
                            if solve(i, j + 1):
                                return True
                            board[i][j] = '.'  # backtrack
                            rows_avail[i] |= (m & -m)
                            cols_avail[j] |= (m & -m)
                            cells_avail[i / 3][j / 3] |= (m & -m)
                            m &= m - 1
                        return False
                    j += 1
                i += 1
                j = 0
            return True

        solve(0, 0)

from itertools import cycle


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        start, step1, step2 = 0, (numRows - 2) * 2 + 2, 0
        res = ""
        for row in xrange(numRows):
            i = start
            steps = cycle([step1]) if step2 == 0 \
                else cycle([step2]) if step1 == 0 \
                else cycle([step1, step2])
            while i < len(s):
                res += s[i]
                i += next(steps)
            step1 -= 2
            step2 += 2
            start += 1
        return res

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, prev = 0, 0
        for c in reversed(s.upper()):
            res += +values[c] if values[c] >= prev else -values[c]
            prev = values[c]
        return res

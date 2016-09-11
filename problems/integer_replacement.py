class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return [0, 0, 1, 2][n]
        elif (n & 0b01) == 0b00:
            return self.integerReplacement(n / 2) + 1
        elif (n & 0b11) == 0b01:
            return self.integerReplacement(n - 1) + 1
        else:
            return self.integerReplacement(n + 1) + 1

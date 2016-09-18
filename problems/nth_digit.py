class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits, start = 1, 1
        while n > 9 * start * digits:
            n -= 9 * start * digits
            digits += 1
            start *= 10
        number = (n - 1) / digits
        digit = (n - 1) % digits
        return int(str(start + number)[digit])

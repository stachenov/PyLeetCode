class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_int, max_int = -2 ** 31, 2 ** 31 - 1
        sign = -1 if x < 0 else +1
        rev = 0
        x = abs(x)
        while x > 0:
            rev *= 10
            rev += x % 10
            x /= 10
        rev *= sign
        return rev if min_int <= rev <= max_int else 0

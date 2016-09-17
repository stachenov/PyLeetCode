from itertools import dropwhile


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if not str:
            return 0
        sign = +1
        if str[0] == '-' or str[0] == '+':
            sign = -1 if str[0] == '-' else +1
            str = str[1:]
        if not str or not str[0].isdigit():
            return 0
        res = 0
        for c in str:
            if not c.isdigit():
                break
            res *= 10
            res += int(c)
        res *= sign
        min_int, max_int = -2 ** 31, 2 ** 31 - 1
        return min_int if res < min_int else max_int if res > max_int else res

from itertools import dropwhile


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        def mul(digit, magnitude):
            res, carry = [0] * (len(num1) + 1 + magnitude), 0
            for i in xrange(1, len(num1) + 1):
                m = int(num1[-i]) * digit + carry
                res[-i - magnitude] = m % 10
                carry = m / 10
            res[0] = carry
            return res
        def add(num):
            carry = 0
            def get(i): return num[-i] if 1 <= i <= len(num) else 0
            for i in xrange(1, len(res) + 1):
                s = res[-i] + get(i) + carry
                res[-i] = s % 10
                carry = s / 10
        for i2, d2 in enumerate(num2):
            add(mul(int(d2), len(num2) - 1 - i2))
        res = ''.join(map(str, dropwhile(lambda d: d == 0, res)))
        return res if res else "0"

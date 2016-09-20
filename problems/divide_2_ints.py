class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        udividend, udivisor, shift = abs(dividend), abs(divisor), 0
        while udividend >= udivisor:
            shift += 1
            udivisor <<= 1
        quot = 0
        while shift > 0:
            shift -= 1
            udivisor >>= 1
            if udividend >= udivisor:
                quot |= 1 << shift
                udividend -= udivisor
        if dividend >= 0 and divisor >= 0 or dividend < 0 and divisor < 0:
            return quot
        else:
            return -quot

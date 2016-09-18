class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        nd = 9
        d = 1
        s = 1
        # 9: 1-9
        # 90: 10-99
        # 900: 100-999
        # 9000: 1000-9999
        while n > nd * d:
            n -= nd * d
            nd *= 10
            d += 1
            s *= 10
        i = (n - 1) / d
        j = d - 1 - (n - 1) % d
        return (s + i) / 10 ** j % 10

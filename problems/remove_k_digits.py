from bisect import bisect_left


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        rem = len(num) - k
        if rem == 0:
            return "0"
        pos = [[] for __ in xrange(10)]
        for i, d in enumerate(map(int, num)):
            pos[d].append(i)
        res = ""
        i = 0
        while rem > 0:
            for d in xrange(10):
                j = bisect_left(pos[d], i)
                if j < len(pos[d]) and len(num) - pos[d][j] >= rem:
                    i = pos[d][j] + 1
                    if res or d > 0:
                        res += str(d)
                    break
            rem -= 1
        return res if res else "0"

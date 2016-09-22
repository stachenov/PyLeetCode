import re


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 9:04 - 9:12
        res = "1"
        p = re.compile(r"(?:1+|2+|3+|4+|5+|6+|7+|8+|9+)")
        for __ in xrange(n - 1):
            res = p.sub(lambda m: str(len(m.group(0))) + m.group(0)[0], res)
        return res

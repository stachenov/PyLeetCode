class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        for c in num:
            while k > 0 and res and res[-1] > c:
                res.pop()
                k -= 1
            res.append(c)
        if k > 0:
            res = res[:-k]
        return "".join(res).lstrip("0") or "0"

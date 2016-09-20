class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def generate(prefix, open, closed):
            if open + closed == 2 * n:
                res.append(prefix)
                return
            if open > closed:
                generate(prefix + ')', open, closed + 1)
            if open < n:
                generate(prefix + '(', open + 1, closed)
        generate("", 0, 0)
        return res

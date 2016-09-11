class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def get_money_amount(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j - i <= 1:
                return 0
            cache[(i, j)] = min(k + max(get_money_amount(i, k), get_money_amount(k + 1, j))
                                for k in xrange(i, j))
            return cache[(i, j)]

        return get_money_amount(1, n + 1)

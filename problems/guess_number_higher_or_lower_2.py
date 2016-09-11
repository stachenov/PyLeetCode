class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        money = [[0] * (n + 2) for __ in xrange(n + 2)]
        for hi in xrange(2, n + 1):
            for lo in xrange(hi - 1, 0, -1):
                money[lo][hi] = min(guess + max(money[lo][guess - 1],
                                                money[guess + 1][hi])
                                    for guess in xrange(lo, hi + 1))
        return money[1][n]

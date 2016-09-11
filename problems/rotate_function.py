class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        total = sum(A)
        s = [sum(i * a for i, a in enumerate(A))]
        for i in xrange(1, len(A)):
            s.append(s[-1] - len(A) * A[-i] + total)
        return max(s)

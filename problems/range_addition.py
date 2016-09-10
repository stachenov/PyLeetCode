from itertools import groupby


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        array = [0] * (length + 1)
        for u in updates:
            array[u[0]] += u[2]
            array[u[1] + 1] -= u[2]
        for i in xrange(1, length):
            array[i] += array[i - 1]
        return array[:length]

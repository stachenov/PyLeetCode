from itertools import groupby


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        key_points = [kp
                      for i, j, inc in updates
                      for kp in [(i, +inc), (j + 1, -inc)]]
        key_points.sort(key=lambda kp: kp[0])
        key_points = dict((i, sum(kp[1] for kp in g))
                          for i, g in groupby(key_points, key=lambda kp: kp[0]))
        array = [0] * length
        inc = 0
        for i in xrange(0, length):
            if i in key_points:
                inc += key_points[i]
            array[i] += inc
        return array

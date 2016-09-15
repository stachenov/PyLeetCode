from collections import defaultdict
from itertools import permutations


class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        quot_for = defaultdict(dict)
        for (x, y), quot in zip(equations, map(float, values)):
            quot_for[x][x] = quot_for[y][y] = 1
            quot_for[x][y] = quot
            if quot != 0:
                quot_for[y][x] = 1 / quot
        for x, y, z in permutations(quot_for, 3):
            if y in quot_for[x] and z in quot_for[y]:
                quot_for[x][z] = quot_for[x][y] * quot_for[y][z]
        return [quot_for[x].get(y, -1) for x, y in query]

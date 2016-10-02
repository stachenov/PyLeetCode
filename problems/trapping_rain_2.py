from itertools import product


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        # original idea by @ts, who won the contest with this problem
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        queue, level = set(), [[float('+inf')] * n for __ in xrange(m)]
        for i in xrange(m):
            queue |= {(i, 0), (i, n - 1)}
            level[i][0] = heightMap[i][0]
            level[i][n - 1] = heightMap[i][n - 1]
        for j in xrange(1, n - 1):
            queue |= {(0, j), (m - 1, j)}
            level[0][j] = heightMap[0][j]
            level[m - 1][j] = heightMap[m - 1][j]

        def within(i, j):
            return 0 <= i < m and 0 <= j < n

        nearby = ((0, -1), (0, +1), (-1, 0), (+1, 0))
        next_queue = set()
        while queue:
            for i, j in queue:
                for di, dj in nearby:
                    if within(i + di, j + dj):
                        new_level = max(level[i][j], heightMap[i + di][j + dj])
                        if new_level < level[i + di][j + dj]:
                            level[i + di][j + dj] = new_level
                            next_queue.add((i + di, j + dj))
            queue = next_queue
            next_queue = set()
        return sum(level[i][j] - heightMap[i][j]
                   for i, j in product(xrange(m), xrange(n)))

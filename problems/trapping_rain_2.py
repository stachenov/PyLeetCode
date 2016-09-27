from collections import defaultdict
from collections import deque
from itertools import product


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        nearby = ((0, -1), (0, +1), (-1, 0), (+1, 0))
        m, n = len(heightMap), len(heightMap[0])

        def within(i, j):
            return 0 <= i < m and 0 <= j < n

        class UnionFind:
            def __init__(self):
                self.root = {}
                self.rank = defaultdict(int)

            def __contains__(self, item):
                return item in self.root

            def __iter__(self):
                return iter(self.root)

            def add(self, row, col):
                if (row, col) in self:
                    return
                self.root[row, col] = row, col
                for di, dj in nearby:
                    if (row + di, col + dj) in self:
                        self.union(row, col, row + di, col + dj)

            def union(self, row1, col1, row2, col2):
                row1, col1 = self.find(row1, col1)
                row2, col2 = self.find(row2, col2)
                if (row1, col1) == (row2, col2):
                    return
                if self.rank[row1, col1] > self.rank[row2, col2]:
                    self.root[row2, col2] = row1, col1
                else:
                    self.root[row1, col1] = row2, col2
                if self.rank[row1, col1] + self.rank[row2, col2]:
                    self.rank[row1, col1] += 1

            def find(self, row, col):
                rootRow, rootCol = self.root[row, col]
                if (rootRow, rootCol) == (row, col):
                    return row, col
                self.root[row, col] = self.find(rootRow, rootCol)
                return self.root[row, col]

            def split(self):
                sets = defaultdict(set)
                for i, j in self:
                    sets[self.find(i, j)].add((i, j))
                return sets.values()

        filled = [[0] * n for __ in xrange(m)]
        wall = {(0, j) for j in xrange(n)}
        for i in xrange(1, m - 1):
            wall |= {(i, 0), (i, n - 1)}
        wall |= {(m - 1, j) for j in xrange(n)}
        walls = [wall]

        def next_starting(covered):
            starting = UnionFind()
            for i, j in covered:
                for di, dj in nearby:
                    if within(i + di, j + dj) and not filled[i + di][j + dj]:
                        starting.add(i + di, j + dj)
            return starting.split()

        while walls:
            for wall in walls:
                q = deque(wall)
                while q:
                    i, j = q.popleft()
                    filled[i][j] = heightMap[i][j]
                    for di, dj in nearby:
                        if within(i + di, j + dj) and not filled[i + di][j + dj] and heightMap[i + di][j + dj] >= heightMap[i][j]:
                            wall.add((i + di, j + dj))
                            q.append((i + di, j + dj))
            pools = []
            for wall in walls:
                more_walls = True
                while more_walls:
                    areas = next_starting(wall)
                    more_walls = False
                    for area in areas:
                        level = float('+inf')
                        for i, j in area:
                            for di, dj in nearby:
                                if (i + di, j + dj) in wall:
                                    level = min(level, heightMap[i + di][j + dj])
                        more_wall = {(i, j) for i, j in area if heightMap[i][j] >= level}
                        if more_wall:
                            for i, j in more_wall:
                                wall.add((i, j))
                                filled[i][j] = heightMap[i][j]
                            more_walls = True
                            pools = []
                            break
                        else:
                            pools.append((level, area))
            if not pools:
                break
            for level, pool in pools:
                q = deque(pool)
                while q:
                    i, j = q.popleft()
                    filled[i][j] = level
                    for di, dj in nearby:
                        if within(i + di, j + dj) and not (i + di, j + dj) in pool and heightMap[i + di][j + dj] < level:
                            pool.add((i + di, j + dj))
                            q.append((i + di, j + dj))
            walls = []
            for level, pool in pools:
                walls += next_starting(pool)
        return sum(filled[i][j] - heightMap[i][j] for i, j in product(xrange(m), xrange(n)))

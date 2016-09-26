from itertools import product


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        def bfs(row, col, level):
            minwall = float('+inf')
            visited = [[False] * len(r) for r in heightMap]
            q = [(row, col)]
            visited[row][col] = True
            while q:
                i, j = q.pop()
                if i == 0 or i == len(heightMap) - 1 or j == 0 or j == len(heightMap[i]) - 1:
                    return 0
                for di, dj in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                    if heightMap[i + di][j + dj] > level:
                        minwall = min(minwall, heightMap[i + di][j + dj])
                    elif not visited[i + di][j + dj]:
                        visited[i + di][j + dj] = True
                        q.append((i + di, j + dj))
            return minwall
        res = 0
        for i in xrange(len(heightMap)):
            for j, lev in enumerate(heightMap[i]):
                w = lev
                while True:
                    n = bfs(i, j, w)
                    if n > w:
                        res += n - w
                        w = n
                    else:
                        break
        return res

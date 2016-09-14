import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = min(len(matrix), k)
        rows = [(matrix[i][0], i, 0) for i in xrange(0, n)]
        heapq.heapify(rows)
        for __ in xrange(0, k):
            kth = heapq.heappop(rows)
            if kth[2] + 1 < n:
                heapq.heappush(rows, (matrix[kth[1]][kth[2] + 1], kth[1], kth[2] + 1))
        return kth[0]

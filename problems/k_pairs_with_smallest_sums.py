import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = [[nums1[0] + n2, 0, j] for j, n2 in enumerate(nums2)]
        heapq.heapify(heap)
        result = []
        for __ in xrange(0, k):
            smallest = heapq.heappop(heap)
            result.append([nums1[smallest[1]], nums2[smallest[2]]])
            smallest[1] += 1
            if smallest[1] < len(nums1):
                smallest[0] = nums1[smallest[1]] + nums2[smallest[2]]
                heapq.heappush(heap, smallest)
            if not heap:
                break
        return result

from heapq import heapify, heappop, heappush


class Solution(object):
    def __init__(self):
        self.maxArea = self.max_area_editorial

    def max_area_heap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        heap = [[-height[i], i] for i in xrange(len(height))]
        heapify(heap)
        while heap:
            top_left = top_right = heappop(heap)
            while heap and top_left[0] == heap[0][0]:
                top = heappop(heap)
                if top[1] < top_left[1]:
                    top_left = top
                if top[1] > top_right[1]:
                    top_right = top
            area = min(area, (top_right[1] - top_left[1]) * top_left[0])
            if not heap:
                break
            top_left[0] = top_right[0] = heap[0][0]
            heappush(heap, top_left)
            if top_left != top_right:
                heappush(heap, top_right)
        return -area

    def max_area_editorial(self, height):
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            area = max(area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area

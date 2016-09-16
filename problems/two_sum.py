from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in index:
                return [index[r], i]
            index[n] = i

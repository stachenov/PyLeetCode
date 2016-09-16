from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = defaultdict(list)
        for i, n in enumerate(nums):
            indices[n].append(i)
        for n in indices:
            r = target - n
            if r == n and len(indices[n]) >= 2:
                return indices[n][:2]
            elif r in indices:
                return [indices[n][0], indices[r][0]]

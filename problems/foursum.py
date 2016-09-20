from collections import defaultdict
from itertools import product


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sums_indexes = defaultdict(list)
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                sums_indexes[nums[i] + nums[j]].append((i, j))
        sums = sorted(sums_indexes.keys())
        res = set()
        i, j = 0, len(sums) - 1
        while i <= j:
            if sums[i] + sums[j] < target:
                i += 1
            elif sums[i] + sums[j] > target:
                j -= 1
            else:
                for (i1, j1), (i2, j2) in product(sums_indexes[sums[i]], sums_indexes[sums[j]]):
                    if i1 != i2 and i1 != j2 and j1 != i2 and j1 != j2:
                        res.add(tuple(sorted((nums[i1], nums[i2], nums[j1], nums[j2]))))
                i += 1
        return list(map(list, res))

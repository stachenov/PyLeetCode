from collections import Counter


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        num_set = Counter(nums)
        res = set()
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                r = 0 - nums[i] - nums[j]
                if r != nums[i] and r != nums[j] and r in num_set:
                    res.add(tuple(sorted((nums[i], nums[j], r))))
                elif r == nums[i] and r == nums[j] and num_set.get(r, 0) >= 3:
                    res.add((0, 0, 0))
                elif r == nums[i] and r != nums[j] and num_set.get(r, 0) >= 2:
                    res.add(tuple(sorted((nums[i], nums[j], r))))
                elif r != nums[i] and r == nums[j] and num_set.get(r, 0) >= 2:
                    res.add(tuple(sorted((nums[i], nums[j], r))))
        return list(map(list, res))

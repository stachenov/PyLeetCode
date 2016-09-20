from collections import Counter


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            r = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                while j < k and nums[j] + nums[k] < r:
                    j += 1
                while j < k and nums[j] + nums[k] > r:
                    k -= 1
                if j < k and nums[j] + nums[k] == r:
                    res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] + nums[k] == r:
                    j += 1
        return res

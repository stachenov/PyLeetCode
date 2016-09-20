from collections import Counter


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        while i <= len(nums) - 3:
            r = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < r:
                    j += 1
                elif nums[j] + nums[k] > r:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] + nums[k] == r:
                        j += 1
            while i <= len(nums) - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

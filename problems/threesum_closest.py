class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in xrange(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            if 3 * nums[i] - target > res - target > 0:
                return res
            while j < k:
                if nums[i] + 2 * nums[j] - target > res - target > 0:
                    return res
                if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                    res = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] < target:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    return res
        return res

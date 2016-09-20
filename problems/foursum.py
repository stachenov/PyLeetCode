class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, m, r = j + 1, len(nums) - 1, target - (nums[i] + nums[j])
                while k < m:
                    if nums[k] + nums[m] < r:
                        k += 1
                    elif nums[k] + nums[m] > r:
                        m -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        while k < m and nums[k] + nums[m] == r:
                            k += 1
        return res

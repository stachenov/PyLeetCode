class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 9:41 - 9:54
        i = 0
        while i < len(nums):
            if 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        return len(nums) + 1

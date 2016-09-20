class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while j < len(nums):
            nums[i] = nums[j]
            i += 1
            j += 1
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1
        return i

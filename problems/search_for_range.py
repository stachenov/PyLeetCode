class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if target <= nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        first = lo
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return [first, lo - 1]

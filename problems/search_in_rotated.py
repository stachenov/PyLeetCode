class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:  # the left part is not rotated
                if nums[0] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # the right part is not rotated
                if nums[mid] <= target <= nums[-1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

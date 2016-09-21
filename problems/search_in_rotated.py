from bisect import bisect_left


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            lo = 1
            while lo <= hi:
                mid = (lo + hi) / 2
                if nums[mid] < nums[mid - 1]:
                    r = mid
                    break
                elif nums[0] > nums[mid - 1]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            if nums[0] <= target <= nums[r - 1]:
                lo, hi = 0, r - 1
            else:
                lo, hi = r, len(nums) -1
        i = bisect_left(nums, target, lo, hi + 1)
        return i if i < len(nums) and nums[i] == target else -1

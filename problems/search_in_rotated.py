# coding=utf-8
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
            # Now that target != nums[mid], we have:
            # A: nums[0] <= nums[mid] (the left part is not rotated)
            # B: nums[0] <= target
            # C: target < nums[mid] (the same as target <= nums[mid])
            # D: target <= nums[-1]
            # Now, the check looks like this:
            # if A:
            #     if B and C (nums[0] <= target < nums[mid]):
            #         search the left part
            #     else (not B or not C):
            #         search the right part
            # else (not A, the right part is not rotated):
            #     if not C and D (nums[mid] < target <= nums[-1]):
            #         search the right part
            #     else (C or not D):
            #         search the left part
            # Karnaugh map (1 means search the left part):
            # AB \ CD 00 01 11 10
            #    00   1  0  1  1
            #    01   1  0  1  1
            #    11   0  0  1  1
            #    10   0  0  0  0
            # Which means:
            # !A & C | !A & !D | B & C = !A & (C | !D) | B & C
            # B & C is expressed elegantly in Python as nums[0] <= target < nums[mid]
            # C | !D is ugly, but its negative is: !C & D, nums[mid] <= target <= nums[-1]
            if nums[0] > nums[mid] and not (nums[mid] <= target <= nums[-1]) or nums[0] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

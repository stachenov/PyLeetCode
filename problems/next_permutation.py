from itertools import takewhile


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = reversed(nums[:])
        else:
            j = i + [(k, n) for k, n in takewhile(lambda t: t[1] > nums[i - 1],
                                                  enumerate(nums[i:]))][-1][0]
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            nums[i:] = reversed(nums[i:])

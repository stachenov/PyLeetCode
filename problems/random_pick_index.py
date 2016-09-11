import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        c = 0
        for i, n in enumerate(self.nums):
            if n == target:
                if random.randint(0, c) == 0:
                    pick = i
                c += 1
        return pick

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

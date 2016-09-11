import random
from bisect import bisect_left
from bisect import bisect_right


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        nums_index = sorted(((i, n) for i, n in enumerate(nums)),
                            key=lambda t: t[1])
        self.nums = [t[1] for t in nums_index]
        self.indices = [t[0] for t in nums_index]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        start = bisect_left(self.nums, target)
        end = bisect_right(self.nums, target)
        return self.indices[random.randint(start, end - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

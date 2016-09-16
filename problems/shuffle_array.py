import random


class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.nums = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # CLR, 3rd ed., p. 125
        copy = list(self.nums)
        for i in xrange(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            copy[i], copy[j] = copy[j], copy[i]
        return copy

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

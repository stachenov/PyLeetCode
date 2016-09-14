class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        combinations = [1] + [0] * target
        for t in xrange(1, target + 1):
            for n in nums:
                if t - n >= 0:
                    combinations[t] += combinations[t - n]
        return combinations[target]

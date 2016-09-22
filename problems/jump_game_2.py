class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reachable, next_reachable, jumps = 0, 0, 0
        for i, n in enumerate(nums):
            if i > reachable:
                jumps += 1
                reachable = next_reachable
            next_reachable = max(next_reachable, i + n)
        return jumps

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # one of the editorial solutions
        if not nums:
            return 0
        max_len_peak, max_len_valley = 1, 1
        for n1, n2 in zip(nums, nums[1:]):
            if n2 > n1:
                max_len_peak = max(max_len_peak, max_len_valley + 1)
            elif n2 < n1:
                max_len_valley = max(max_len_valley, max_len_peak + 1)
        return max(max_len_peak, max_len_valley)

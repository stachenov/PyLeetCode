class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        peak, valley, peak_len, valley_len = nums[0], nums[0], 1, 1
        for n in nums[1:]:
            valley = min(valley, n)
            peak = max(peak, n)
            if n > valley and valley_len + 1 > peak_len:
                peak = n
                peak_len = valley_len + 1
            if n < peak and peak_len + 1 > valley_len:
                valley = n
                valley_len = peak_len + 1
        return max(peak_len, valley_len)

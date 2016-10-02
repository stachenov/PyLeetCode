class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def achievable(result):
            s, c = 0, 1
            for n in nums:
                if n > result:
                    return False
                if s + n > result:
                    s = n
                    c += 1
                    if c > m:
                        return False
                else:
                    s += n
            return True
        lo, hi = min(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) / 2
            if achievable(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k > len(s):
            return 0
        counter = Counter(s)
        least_common = min(counter, key=counter.get)
        if counter[least_common] >= k:
            return len(s)
        else:
            return max(self.longestSubstring(t, k) for t in s.split(least_common))

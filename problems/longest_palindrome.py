from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        p, used_single = 0, False
        for c in counter.itervalues():
            p += c / 2 * 2
            if c % 2 != 0 and not used_single:
                p += 1
                used_single = True
        return p

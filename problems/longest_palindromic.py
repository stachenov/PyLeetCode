class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        modlen = 2 * len(s) + 1
        neginf = float('-inf')
        posinf = float('+inf')
        def get(i):
            if i % 2 == 0:
                return None # char boundary
            elif i < 0:
                return neginf
            elif i >= modlen:
                return posinf
            else:
                return s[i / 2]
        p = [0] * modlen
        for i in xrange(modlen):
            while get(i - p[i] - 1) == get(i + p[i] + 1):
                p[i] += 1
        r, c = max((p[i], i) for i in xrange(modlen))
        return s[(c - r) / 2: (c + r - 1) / 2 + 1]

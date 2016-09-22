class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = [[False] * (len(p) + 1) for __ in xrange(len(s) + 1)]
        for i in xrange(len(s) + 1):
            for j in xrange(len(p) + 1):
                if i > 0 and j > 0 and (p[j - 1] == '?' or p[j - 1] == s[i - 1]) and match[i - 1][j - 1] \
                        or i > 0 and j > 0 and p[j - 1] == '*' and match[i - 1][j] \
                        or j > 0 and p[j - 1] == '*' and match[i][j - 1] \
                        or i == 0 and j == 0:
                    match[i][j] = True
        return match[len(s)][len(p)]

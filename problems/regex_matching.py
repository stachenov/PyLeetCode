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
                extend_ij, extend_j, extend_i = False, False, False
                if i > 0 and j > 0 and match[i - 1][j - 1]:
                    extend_ij = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                if i > 0 and j > 1 and match[i - 1][j]:
                    extend_i = p[j - 1] == '*' and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                if j > 1 and match[i][j - 2]:
                    extend_j = p[j - 1] == '*'
                match[i][j] = extend_ij or extend_i or extend_j or i == 0 and j == 0
        return match[len(s)][len(p)]

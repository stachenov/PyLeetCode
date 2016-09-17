class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        for i in xrange(len(s) + 1):
            match = []
            for j in xrange(len(p) + 1):
                extend_ij, extend_j, extend_i = False, False, False
                if i > 0 and j > 0 and prev[j - 1]:
                    extend_ij = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                if i > 0 and j > 1 and prev[j]:
                    extend_i = p[j - 1] == '*' and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                if j > 1 and match[j - 2]:
                    extend_j = p[j - 1] == '*'
                match.append(extend_ij or extend_i or extend_j or i == 0 and j == 0)
            prev = match
        return match[len(p)]

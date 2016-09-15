class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = 0
        for cs in s:
            pos = t.find(cs, pos)
            if pos == -1:
                return False
            pos += 1
        return True

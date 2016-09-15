from bisect import bisect_left
from collections import defaultdict


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos_of = defaultdict(list)
        for it, ct in enumerate(t):
            pos_of[ct].append(it)
        pos = 0
        for cs in s:
            if cs not in pos_of:
                return False
            i = bisect_left(pos_of[cs], pos)
            if i == len(pos_of[cs]):
                return False
            pos = pos_of[cs][i] + 1
        return True
